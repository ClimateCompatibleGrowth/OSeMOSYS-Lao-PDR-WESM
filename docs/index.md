# OSeMOSYS Lao PDR Whole Energy System Model (WESM)

This site is the online documentation for the **Lao PDR Whole Energy System Model
(Lao-WESM)**, an open-source energy-system optimisation model built in
[OSeMOSYS](https://osemosys.org/). The model represents the entire Laotian energy
system, spanning electricity generation and trade, transport, industrial heat,
and residential and commercial cooking, over the period **2023 to 2055**, with
results reported to **2050**.

The model was developed within the
[Climate Compatible Growth (CCG)](https://climatecompatiblegrowth.com/) programme,
and underpins the research article *"Export clean, but live dirty: reconciling
power exports, decarbonisation and clean cooking in Lao PDR."* This documentation
describes the **data, structure, assumptions, scenario design, and reproduction
workflow** of the model. It is deliberately not a results paper: the headline
findings, figures and policy discussion live in the article and its Supplementary
Material, not here.

```{note}
This is **version 2** of the documentation, regenerated from the latest model run.
The model files, full input dataset, and the version history (with Zenodo DOIs) are
listed in the [repository README](https://github.com/ClimateCompatibleGrowth/OSeMOSYS-Lao-PDR-WESM).
```

## How to read this documentation

The chapters follow the natural workflow of building and running the model:

1. {doc}`overview`: what the model is, its scope, and the questions it answers.
2. {doc}`model_structure`: the reference energy system, covering regions, sectors,
   technologies, commodities, modes and time slices.
3. {doc}`parameterization`: data sources, base-year calibration to the 2023 energy
   balance, demand projections, and techno-economic assumptions.
4. {doc}`scenario_design`: the 3x3x3 Trade x Carbon x Cooking scenario matrix.
5. {doc}`execution_guide`: how to obtain the files, run the scenarios, and
   post-process results.
6. {doc}`health_dalys`: how the household-air-pollution health burden (DALYs) is
   calculated.
7. {doc}`references`: data sources and further reading.

```{toctree}
:maxdepth: 2
:caption: Contents
:hidden:

overview
model_structure
parameterization
scenario_design
execution_guide
health_dalys
references
```

## Acknowledgements

This material has been produced with support from the Climate Compatible Growth
(CCG) programme, which is funded by UK aid from the UK government. The views
expressed do not necessarily reflect the UK government's official policies.
