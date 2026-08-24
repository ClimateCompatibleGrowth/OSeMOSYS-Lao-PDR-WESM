# 5. Execution and reproduction guide

This chapter explains how to obtain the model, run the scenarios, and post-process
the results. It is written to be followed by someone new to the model but familiar
with the basics of OSeMOSYS.

## 5.1 What ships with a release

Each release of the model consists of four things:

1. the **OSeMOSYS model file** `data/model.v.5.4.txt` — the GNU MathProg formulation
   (sets, parameters, variables, objective and constraints) used for every run;
2. the **scenario data files** `data/data_files_S1_S29.zip` — one MathProg data file
   per scenario, `data_file_S1.txt` to `data_file_S29.txt`;
3. the **supporting dataset** under `data/` (`Lao_WESM_supporting_data.xlsx`, the
   curated workbook from which the model parameters are derived, including the
   reconstructed 2023 energy balance); and
4. this **documentation** (`docs/`).

The complete, citable archive of model files and data for a given version is
deposited on **Zenodo** (see the version table in the repository README for the DOI).

```{note}
Result dumps (`results.txt`) and solver artefacts (`.lp`, `.sol`) are **not**
committed to git — they run to hundreds of megabytes per scenario. They are
distributed through Zenodo. The model file and the scenario data files needed to
regenerate them are in `data/`.
```

## 5.2 The files you need to run the model

Everything required to reproduce a scenario is in the `data/` folder of the
repository:

```{list-table}
:header-rows: 1
:widths: 34 66

* - File
  - What it is
* - `data/model.v.5.4.txt`
  - The OSeMOSYS formulation in GNU MathProg. Version 5.4 of the Lao-WESM
    formulation: standard OSeMOSYS with storage, user-defined constraints (UDC),
    input-to-capacity ratios and the inter-year emission-change accounting used for
    the DALY calculation. Identical for all 29 runs.
* - `data/data_files_S1_S29.zip`
  - The 29 scenario data files. Unzip to get `data_file_S1.txt` ...
    `data_file_S29.txt`, one per scenario.
* - `data/Lao_WESM_supporting_data.xlsx`
  - The supporting data behind the parameter values (not read by the solver). See
    {doc}`parameterization`.
```

{download}`Download the model file (model.v.5.4.txt) <../data/model.v.5.4.txt>`

{download}`Download the 29 scenario data files (.zip) <../data/data_files_S1_S29.zip>`

The scenario numbering follows {doc}`scenario_design` exactly: `data_file_S1.txt` is
S1 (T1 M1 C1, the baseline), `data_file_S4.txt` is S4 (T2 M2 C2, the achievable
midpoint), `data_file_S5.txt` is S5 (T3 M3 C3, the most ambitious), and
`data_file_S28.txt` / `data_file_S29.txt` are the dry- and wet-hydrology
sensitivities on S4. The full S-number to T/M/C mapping is the 27-scenario table in
{doc}`scenario_design`.

The scenario data files differ **only** in their trade, carbon and PM2.5 constraint
parameters; demands, technology sets, costs and resource potentials are identical
across the matrix. Diffing two data files is therefore a quick way to see exactly
what a lever changes.

## 5.3 Software prerequisites

The model is built in open-source **OSeMOSYS** and is written in **GNU MathProg**. To
run it you will need:

- a **MathProg-capable OSeMOSYS toolchain**. `model.v.5.4.txt` has been checked
  against **GLPK** (`glpsol`, v4.65), which both translates the model and can solve
  it;
- a linear-programming **solver**. GLPK's own simplex will solve the model, but the
  problem is large — roughly **530,000 rows, 440,000 columns and 4 million non-zeros**
  per scenario — so a higher-performance solver (CPLEX, Gurobi or CBC) reading an
  exported `.lp` file is considerably faster; and
- **Python**, for the post-processing scripts (result extraction, DALY calculation
  and figure generation).

```{admonition} Running the model through the MUIO interface
:class: tip
The runs behind this study were produced through the **MUIO** graphical interface,
and the model can be built and run that way. The same formulation is also committed
as `WESM/OSeMOSYS_Model_MUIO_Ver5.4.txt` under the name it carries in MUIO; it is
identical to `data/model.v.5.4.txt` apart from blank lines. What is *not* in the
repository is the MUIO **project workspace** itself (the interface's own database of
sets, parameters and scenarios) - that is available from the authors on request (see
the author list in {doc}`references`). Running `model.v.5.4.txt` with GLPK as
described below is the equivalent command-line route and needs no MUIO
installation.
```

## 5.4 Running a scenario

Unzip the scenario data files first:

```bash
cd data
unzip data_files_S1_S29.zip -d scenario_data
```

Then build and solve one scenario. Everything is driven by the pair *(model file,
scenario data file)*; nothing else changes between runs:

```bash
# Solve S4 (T2 M2 C2, the achievable midpoint) directly with GLPK
glpsol -m data/model.v.5.4.txt \
       -d data/scenario_data/data_file_S4.txt \
       -o results_S4.txt
```

To use a different solver, export the problem instead of solving it and hand the
`.lp` file to CPLEX, Gurobi or CBC:

```bash
glpsol -m data/model.v.5.4.txt \
       -d data/scenario_data/data_file_S4.txt \
       --wlp S4.lp --check
```

```{admonition} Expect large intermediate files
:class: warning
Translating one scenario produces an LP of roughly **230 MB** and a result file of
roughly **115 MB**. Allow several GB of free disk and memory per run, and do not
commit these artefacts to git (`.lp`, `.sol` and `.mps` files are already covered by
`.gitignore`).
```

Conceptually the run has four steps:

1. **Pick the scenario data file.** The 27 core scenarios differ only in their trade,
   carbon and PM2.5 constraints; S28 and S29 additionally change hydrology (see
   {doc}`scenario_design`).
2. **Build the model.** Combine the data file with `model.v.5.4.txt` to produce a
   solver-ready problem.
3. **Solve.** Optimise total discounted system cost over the full 2023-2055 horizon.
   Results are reported to 2050; the final five years exist only to keep
   late-horizon investment decisions undistorted.
4. **Extract results.** Read the solution into result variables (for example
   `ProductionByTechnology`, `TotalTechnologyAnnualActivity`,
   `AnnualTechnologyEmission`, `TotalCapacityAnnual`) for plotting and analysis.

## 5.5 Reading results: conventions

When post-processing, follow these conventions so that quantities are consistent
across users:

- **Generation** should be read from `ProductionByTechnology` (or
  `ProductionByTechnologyByMode` where the toolchain reports by mode).
- **Fuel or energy use** should be read from the corresponding use-by-technology
  variable rather than from an aggregate.
- Always verify a headline number against the raw result variable before quoting or
  plotting it, rather than relying on an intermediate aggregate.

## 5.6 Post-processing and figures

A set of Python scripts turns the raw result variables into the figures used in the
article and its Supplementary Material. To keep the scripts portable, they read the
results directory from an environment variable (for example `RESULTS_DIR`) rather
than a hard-coded path, so the same scripts run against a local solve or a downloaded
result archive.

## 5.7 Reproducing the full study

To reproduce the whole analysis rather than a single scenario, run all **27
scenarios** (S1-S27) plus the two hydrology sensitivities (S28, S29) — that is, all
29 data files in `data_files_S1_S29.zip` against the same `model.v.5.4.txt`:

```bash
for i in $(seq 1 29); do
  glpsol -m data/model.v.5.4.txt \
         -d data/scenario_data/data_file_S${i}.txt \
         -o results_S${i}.txt
done
```

Then collect the result variables for each run and perform the cross-scenario
analysis. The main-effects and interaction analysis in the article requires the
**complete factorial**, because it decomposes cost and emission outcomes by lever: a
partial set of runs cannot reproduce those numbers.
