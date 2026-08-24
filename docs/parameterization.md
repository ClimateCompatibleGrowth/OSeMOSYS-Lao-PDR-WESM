# 3. Parameterization

This chapter describes how the model is populated with numbers: the base-year energy
balance it is calibrated to, the drivers behind the demand projections, and the
techno-economic assumptions attached to each technology. The complete, machine-
readable parameter set ships with the model dataset (see {doc}`execution_guide`);
this chapter documents the sources and logic behind it.

## 3.1 Base-year energy balance (2023)

The model is calibrated to a reconstructed **2023 energy balance** for Laos. This was
built by combining the IEA World Energy Balances with the Ministry of Energy and
Mines (MEM) statistical yearbooks and a national biomass survey, because standard
international statistics substantially understate solid-fuel and charcoal use in the
country. The reconstruction puts firewood consumption at roughly 1,950 kt (about 33
PJ) and charcoal at about 735 kt in 2023.

Key calibration anchors for the base year:

```{list-table}
:header-rows: 1
:widths: 35 65

* - Quantity
  - 2023 value
* - Electricity generated
  - ~38.7 TWh (~139 PJ), ~72% hydro and ~26% coal
* - Share of electricity exported
  - ~67% on a net basis (~25.9 TWh)
* - Imported electricity
  - ~14 PJ, drawn mainly in the dry season
* - Liquid fuels
  - ~47.8 PJ, ~100% imported (diesel ~38.2, gasoline ~6.9 PJ, plus jet and LPG)
* - Cooking energy
  - ~69 PJ delivered to stoves, ~97% solid biomass (firewood ~65%, charcoal ~32%)
* - Woodfuel
  - ~95 PJ, being direct firewood plus the wood fed to charcoal kilns
* - Households
  - ~1.35 million (40% urban, 60% rural)
* - Industrial heat
  - ~29 PJ (coal ~15, biomass ~11, diesel ~2.5 PJ)
* - Industrial electricity
  - ~13 PJ, including ~3.5 TWh of crypto-mining / data-centre load
* - Motorcycle fleet
  - ~2.4 million
```

## 3.2 Demand projections

Service demands are projected exogenously and held fixed across scenarios. The
drivers come from published regional outlooks rather than being estimated inside the
model:

- **Sector GDP growth, clean-cooking access and demand elasticities** from the ASEAN
  Energy Outlook and an ADB Energy Outlook for Asia and the Pacific;
- **Urbanisation** from the UN Population Division; and
- **Transport activity** (passenger- and tonne-kilometres) from the Lao Statistics
  Bureau.

Because demands are identical in every scenario, differences in cost, emissions and
health outcomes across the scenario matrix are attributable solely to differences in
the supply-side technology mix.

## 3.3 Techno-economic assumptions

Each technology carries capital cost, fixed and variable operating cost, efficiency,
operational life and (where relevant) capacity factor. The main sources are:

- **Renewables**: regional resource potential from government estimates and an NREL
  assessment; costs from standard technology catalogues.
- **Transport**: vehicle costs and fuel economy from a regional technology catalogue
  supplemented by a Vietnamese vehicle-cost study where Lao-specific data were
  missing.
- **Cooking**: stove techno-economics modified from the published Zambia
  clean-cooking modelling files (Cronin et al., 2026) and refined with Lao
  stakeholder input.
- **Industry**: boiler efficiencies derived from the 2023 balance and an EU
  reference scenario.

### Cook-stove techno-economics

```{list-table}
:header-rows: 1
:widths: 30 15 13 15 12 15

* - Stove
  - Fuel
  - Life (yr)
  - Capex (USD)
  - O&M (%/yr)
  - Efficiency
* - Three-stone fire
  - Firewood
  - 15
  - 0
  - 0
  - 10%
* - Improved firewood
  - Firewood
  - 6
  - 4
  - 2
  - 22%
* - Gasifier
  - Firewood
  - 5
  - 48
  - 2
  - 51%
* - Pellet gasifier
  - Pellet
  - 5
  - 48
  - 2
  - 51%
* - Traditional charcoal
  - Charcoal
  - 6
  - 4
  - 2
  - 21%
* - Improved charcoal
  - Charcoal
  - 5
  - 6
  - 2
  - 30%
* - LPG
  - LPG
  - 7
  - 43
  - 2
  - 66%
* - Biogas
  - Biogas
  - 10
  - 676
  - 2
  - 55%
* - Ethanol
  - Ethanol
  - 10
  - 12
  - 2
  - 58%
* - Kerosene
  - Kerosene
  - 5
  - 19
  - 2
  - 42%
* - Electric induction
  - Electricity
  - 15
  - 76
  - 4
  - 76%
```

Electric cooking is represented by the induction stove only. Charcoal is not a
primary fuel: it is produced from wood in kilns, an inefficient conversion (roughly
43%) tracked explicitly, so moving households off charcoal cuts total woodfuel demand
by more than the charcoal energy it replaces.

### Industrial boiler efficiencies

```{list-table}
:header-rows: 1
:widths: 40 30 30

* - Boiler fuel
  - Existing fleet
  - Improved / new
* - Coal
  - 40%
  - 82%
* - Diesel
  - 40%
  - 86%
* - Biomass (firewood / pellet)
  - 25%
  - 82%
* - Electric
  - 100%
  - 100%
```

## 3.4 Health (DALY) accounting

Household-air-pollution health impacts are computed as a **post-processing step** on
the model's cooking output and reported as cumulative DALYs over 2023-2050. Because
this is a self-contained methodology, it has its own chapter. See
{doc}`health_dalys` for the full calculation, covering the exposure,
exposure-response, attributable-fraction and DALY equations, plus the parameter
tables (indoor PM2.5 by stove, IER coefficients and GBD background rates).

## 3.5 Run-configuration settings

A few global settings are properties of the OSeMOSYS run configuration rather than of
individual technologies:

- **Discount rate: 10%**, applied throughout the analysis.
- **Currency and cost year**, together with solver settings, are set in the scenario
  data files distributed with each release (`data/data_files_S1_S29.zip`). Consult
  those files and the supporting dataset for the exact figures used in the latest
  run; see {doc}`execution_guide`.

System cost is reported as the **total discounted cost over the model horizon**.

## 3.6 Supporting-data workbook

For readers who want to go deeper, a curated workbook collects the underlying source
worksheets behind this chapter, being the 2023 IEA energy balance and the model input
data (fuel prices, solar profiles, load curves, power cost assumptions, operational
lives, the NPDP power-plant list, and hydrogen supply and cost data), renumbered and
renamed, with a `00 Contents` map. It reproduces the Northern, Central and Southern
regional structure only. The complete dataset for each release is archived on Zenodo.

{download}`Download the supporting-data workbook (.xlsx) <../data/Lao_WESM_supporting_data.xlsx>`
