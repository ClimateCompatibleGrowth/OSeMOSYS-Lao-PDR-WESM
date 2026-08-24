# data: model file, scenario data files and input dataset

This folder holds everything needed to **run** the model, plus the curated supporting
data behind its parameter values.

## `model.v.5.4.txt` - the OSeMOSYS model file

The Lao-WESM formulation in **GNU MathProg**: sets, parameters, variables, the
cost-minimising objective and all constraints. Version 5.4 is standard OSeMOSYS
extended with storage, user-defined constraints (UDC), input-to-capacity ratios and
the inter-year emission-change accounting used for the DALY calculation. The **same**
model file is used for all 29 runs; only the data file changes.

## `data_files_S1_S29.zip` - the scenario data files

The 29 MathProg data files, one per scenario: `data_file_S1.txt` to
`data_file_S29.txt`. Numbering follows the
[Scenario design](https://osemosys-lao-pdr-wesm.readthedocs.io/en/latest/scenario_design.html)
chapter - S1 (T1 M1 C1) is the baseline, S4 (T2 M2 C2) the achievable midpoint, S5
(T3 M3 C3) the most ambitious, and S28 / S29 the dry- and wet-hydrology
sensitivities on S4. The 27 core files differ only in their trade, carbon and PM2.5
constraint parameters.

To run one scenario:

```bash
unzip data_files_S1_S29.zip -d scenario_data
glpsol -m model.v.5.4.txt -d scenario_data/data_file_S4.txt -o results_S4.txt
```

Each scenario builds a problem of roughly 530,000 rows and 440,000 columns, so expect
a ~230 MB LP and a ~115 MB result file per run. The model can also be run through the
**MUIO** interface; the MUIO-compatible version of the model file is available **from
the authors on request**. See the
[Execution and reproduction guide](https://osemosys-lao-pdr-wesm.readthedocs.io/en/latest/execution_guide.html)
for the full workflow.

## `Lao_WESM_supporting_data.xlsx` - supporting data

A single, cleaned workbook of the source worksheets that underpin the documentation,
renumbered and renamed for clarity. Open the **`00 Contents`** sheet for the full map
of each sheet to its original source. The sheets are grouped in two parts:

**Part A: base-year energy balance** (from the 2023 IEA extended balance):
`A01` IEA 2023 balance, `A02` MEM yearbook, `A03` LSB population, `A04` ASEAN Energy
Outlook (8th ed.), `A05` cooking tech, `A06` residential cook calc, `A07` residential
demand, `A08` commercial, `A09` industrial, `A10` agricultural, `A11` crypto.

**Part B: model input data** (from the OSeMOSYS model dataset):
`B01` transport naming, `B02` vehicle stock, `B03` fuel prices, `B04-B06` solar
profiles (Northern / Central / Southern), `B07` RE potential (NREL), `B08-B11`
timeslices / load curves (national / N / C / S), `B12-B20` power cost assumptions
(biomass, onshore wind, rooftop and utility solar PV, small and large hydro, coal,
coal-CCS, operational life), `B21` power-plant list (NPDP), `B22` hydrogen supply
chain, `B23` hydrogen cost.

```{note}
Only Northern, Central and Southern regions are represented in the model. Any
"Vientiane" regional tabs from the source workbooks are intentionally excluded, along
with internal working/figure sheets, to keep the supporting data clean.
```

```{warning}
Sheet `B21 Power Plant Info` is reproduced to **column M only**. The source worksheet
also carries a per-plant domestic/export capacity split and the exporting country;
these are withheld as confidential electricity-export commitments, consistent with the
data-availability statement of the associated article. Do not restore those columns
when regenerating the workbook.
```

## What is not here

- **Result dumps and solver artefacts** (`results.txt`, `.lp`, `.sol`) are far too
  large for git; regenerate them from the model and data files above, or download
  them from Zenodo.
- The **full, citable dataset** for each release, including items not reproduced in
  the curated workbook above, is archived on **Zenodo**; add the DOI to the version
  table in the top-level `README.md`. Confidential data (for example
  electricity-export contract commitments) are excluded from the public archive.

See the
[Parameterization](https://osemosys-lao-pdr-wesm.readthedocs.io/en/latest/parameterization.html)
chapter of the documentation for the sources behind each dataset.
