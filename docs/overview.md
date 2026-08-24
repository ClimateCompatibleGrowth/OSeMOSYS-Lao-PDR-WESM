# 1. Overview

## 1.1 What the model represents

The Lao PDR Whole Energy System Model (Lao-WESM) is a bottom-up, technology-rich
optimisation model of the Laotian energy system. It is built in
[OSeMOSYS](https://osemosys.org/) (the Open Source Energy Modelling System), a
linear-programming framework that chooses the least-cost mix of technologies and
fuels needed to meet a set of exogenous energy-service demands, subject to
resource, capacity and policy constraints.

Earlier OSeMOSYS studies of Laos concentrated on the power sector alone: notably
[Nakajima et al. (2025)](https://doi.org/10.1016/j.esr.2025.101865) on the
long-term risks of Laos' electricity trade, and
[Sridharan et al. (2025)](https://doi.org/10.1088/2515-7620/adfc2f) on green ammonia
as an alternative to electricity exports. This model, by contrast, is a
*whole-energy-system* representation. It brings four sectors into a single
optimisation so that trade-offs and co-benefits between them can be examined
together:

- **Electricity** generation, transmission, and cross-border trade;
- **Transport**, covering road, rail and aviation;
- **Industry**, split into process heat and electricity (including
  cryptocurrency-mining and data-centre load); and
- **Cooking**, covering residential (urban and rural) and commercial demand.

A separate health-accounting module translates household air-pollution exposure
from solid-fuel cooking into Disability-Adjusted Life Years (DALYs). This runs as a
post-processing step on the model output rather than inside the optimisation.

## 1.2 The question the model is built to answer

Laos occupies an unusual position: it exports large volumes of predominantly
hydroelectric power to its neighbours while, at home, importing essentially all of
its liquid fuels and meeting most of its cooking demand with solid biomass. The
model is designed to explore how the country can reconcile three objectives that
are usually considered in isolation:

- redirecting hydropower value toward domestic use (**Trade**);
- decarbonising the wider energy system (**Carbon**); and
- cleaning up household air quality (**Cooking / air quality**).

These three objectives become the three axes of the scenario design described in
{doc}`scenario_design`.

## 1.3 Scope and resolution

```{list-table}
:header-rows: 1
:widths: 30 70

* - Dimension
  - Coverage in the model
* - Base year
  - 2023
* - Model horizon
  - 2023 to 2055, in annual time steps
* - Reporting horizon
  - 2023 to 2050. The final five years are retained so that investment decisions
    late in the period are not distorted by end-of-horizon effects
* - Discount rate
  - 10%
* - Spatial resolution (power)
  - Three regions: Northern, Central, Southern, with inter-regional
    interconnectors and cross-border links
* - Spatial resolution (other sectors)
  - National, because sub-national activity data are not available for transport,
    cooking and industry
* - Time slices
  - 8 per year: two seasons (dry, wet) x four intra-day blocks
    (night, morning interim, daytime interim, evening peak)
* - Sectors
  - Power, transport, industry (heat and electricity), residential and commercial
    cooking
* - Emissions tracked
  - CO2 and primary PM2.5, as combustion by-products
* - Framework
  - OSeMOSYS (open-source, linear programming)
```

## 1.4 Relationship to the research article

The model is the quantitative engine behind the article *"Export clean, but live
dirty."* This documentation covers the model itself: its structure, data and how to
run it. The results, their interpretation, the policy discussion and the
cross-scenario statistical analysis all remain in the article and its Supplementary
Material, and are deliberately not reproduced here.
