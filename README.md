# OSeMOSYS Lao PDR Whole Energy System Model (WESM)

This repository contains the **Lao PDR Whole Energy System Model (Lao-WESM)**, an
open-source [OSeMOSYS](https://osemosys.org/) model of the entire Laotian energy
system, developed within the [Climate Compatible Growth
(CCG)](https://climatecompatiblegrowth.com/) programme. The model covers electricity
generation and trade, transport, industrial heat, and residential and commercial
cooking over **2023-2050**, and underpins the research article *"Export clean, but
live dirty: reconciling power exports, decarbonisation and clean cooking in Lao
PDR."*

📖 **Documentation:** <https://osemosys-lao-pdr-wesm.readthedocs.io/> *(update to your
Read the Docs URL once published)*

## Repository layout

```
OSeMOSYS-Lao-PDR-WESM/
├── docs/     Documentation source (Sphinx + Read the Docs, MyST Markdown)
├── WESM/     OSeMOSYS model files (baseline + scenario runs)
├── data/     Model file, the 29 scenario data files, and the input dataset
├── README.md
├── LICENSE
├── .readthedocs.yaml
└── .gitignore
```

## Versions

| Version | Date    | DOI | Description |
| ------- | ------- | --- | ----------- |
| 0.1.0   | 12/2023 | [10.5281/zenodo.11103010](https://doi.org/10.5281/zenodo.11103010) | First release, based on the PBFL Southern Partners Fund project. |
| **2.0.0** | **TBD 2026** | **`TBD`: mint on Zenodo and paste the DOI badge here** | Whole-energy-system model regenerated from the latest run; adds transport, industrial heat and cooking, the 3x3x3 Trade x Carbon x Cooking scenario matrix, and household-air-pollution (DALY) accounting. Supports the ERL article. |

<!--
To add the version-2 DOI badge after minting on Zenodo, replace the TBD cell above
with, e.g.:
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
-->

## Data and model files

Everything needed to run the model is in [`data/`](data/):

| File | What it is |
| ---- | ---------- |
| `data/model.v.5.4.txt` | The OSeMOSYS model file (GNU MathProg). The same file is used for all 29 runs. |
| `data/data_files_S1_S29.zip` | The 29 scenario data files, `data_file_S1.txt` to `data_file_S29.txt` (S1-S27 factorial plus the S28 dry / S29 wet hydrology sensitivities). |
| `data/Lao_WESM_supporting_data.xlsx` | The curated supporting dataset behind the parameter values. |

```bash
unzip data/data_files_S1_S29.zip -d data/scenario_data
glpsol -m data/model.v.5.4.txt -d data/scenario_data/data_file_S4.txt -o results_S4.txt
```

The model can also be run through the **MUIO** interface; the MUIO-compatible version
of the model file is available **from the authors on request**. See the
[Execution and reproduction guide](https://osemosys-lao-pdr-wesm.readthedocs.io/en/latest/execution_guide.html)
for the full workflow.

Result dumps and solver artefacts are too large for git and are archived on
**Zenodo** for citability - see the version table above for the DOI.

## Building the documentation locally

```bash
pip install -r docs/requirements.txt
sphinx-build -b html docs docs/_build/html
# then open docs/_build/html/index.html
```

## Citation

Please cite both the Zenodo model archive and the associated article. See the
[References](https://osemosys-lao-pdr-wesm.readthedocs.io/en/latest/references.html)
page of the documentation for the full citation.

## Acknowledgements

This material has been produced with support from the Climate Compatible Growth
(CCG) programme, which is funded by UK aid from the UK government. The views
expressed do not necessarily reflect the UK government's official policies.

## License

Released under the [Apache License 2.0](LICENSE).
