# WESM: model files

> **The model file and the scenario data files now ship in [`../data/`](../data/):**
> `data/model.v.5.4.txt` (the OSeMOSYS MathProg formulation) and
> `data/data_files_S1_S29.zip` (the 29 scenario data files, `data_file_S1.txt` to
> `data_file_S29.txt`). Start there to run the model.

This folder holds any **additional run material for the latest run** that is not part
of that pair.

Expected contents (adjust names to match your toolchain):

- Any run configuration (discount rate, currency, cost year, solver settings) used
  to produce the latest results.
- Any toolchain-specific variant of the model, for example an `otoole` configuration.
  The **MUIO-compatible version of the model file** is not distributed here; it is
  available from the authors on request.

For the scenario definitions behind each data file, see the
[Scenario design](https://osemosys-lao-pdr-wesm.readthedocs.io/en/latest/scenario_design.html)
chapter of the documentation.

> Large files and full result dumps are distributed via **Zenodo** rather than
> committed here. See the version table in the top-level `README.md` for the DOI.

## Placeholder

```
WESM/
├── README.md   ← this file
└── config/     ← add: run configuration
```
