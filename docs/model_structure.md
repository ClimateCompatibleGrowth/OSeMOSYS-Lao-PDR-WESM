# 2. Model structure

## 2.1 The reference energy system

OSeMOSYS organises the energy system as a **reference energy system (RES)**: a
network in which *commodities* (fuels and energy services) flow through
*technologies* (conversion, transport and demand processes) from primary supply to
final service demand. Each technology is connected to commodities through three
ratios:

- an **input activity ratio (IAR)**: the commodities it consumes;
- an **output activity ratio (OAR)**: the commodities it produces; and
- an **emission activity ratio (EAR)**: the CO2 and PM2.5 released per unit of
  activity.

Service demands (electricity, mobility, useful cooking energy, industrial heat) are
specified exogenously and held identical across scenarios, so that scenario
differences reflect only how those demands are *met*, not how large they are.

## 2.2 Spatial structure

The **electricity sector** is resolved into three regions, **Northern (NOR),
Central (CEN) and Southern (SOU)**, connected by inter-regional interconnectors and
by cross-border links to China, Thailand, Vietnam and Cambodia (with a pilot link to
Singapore under the LTMS-PIP arrangement). Regional resolution matters for power
because hydrology, demand and interconnection differ markedly across the country.

All **other sectors** (transport, cooking, industry) are modelled at the **national
scale**, since sub-national activity data are not available. Where regional data did
exist (for example urban and rural population), they were aggregated to national
totals.

## 2.3 Temporal structure

The horizon runs annually from **2023 to 2055**, with results reported to **2050**;
the final five years are retained so that investment decisions late in the period are
not distorted by end-of-horizon effects. Within each year, **8 time slices** capture
seasonal and intra-day variation:

```{list-table}
:header-rows: 1
:widths: 20 25 30 25

* - Slice
  - Season
  - Intra-day block
  - Year fraction
* - S11
  - Dry
  - Night (22:00-06:00)
  - 0.218
* - S12
  - Dry
  - Morning interim (07:00-09:00)
  - 0.073
* - S13
  - Dry
  - Daytime interim (10:00-18:00)
  - 0.218
* - S14
  - Dry
  - Evening peak (19:00-21:00)
  - 0.073
* - S21
  - Wet
  - Night (22:00-06:00)
  - 0.157
* - S22
  - Wet
  - Morning interim (07:00-09:00)
  - 0.052
* - S23
  - Wet
  - Daytime interim (10:00-18:00)
  - 0.157
* - S24
  - Wet
  - Evening peak (19:00-21:00)
  - 0.052
```

The dry/wet split (roughly 212 dry days and 153 wet days) is the key driver of
hydropower availability, which is why individual power plants carry season-specific
capacity factors (see {doc}`parameterization`).

## 2.4 Naming conventions

Technology and commodity codes follow a positional convention that makes the RES
readable at a glance. Codes are generally built from a **region or scope prefix**, a
**sector/service segment**, a **fuel segment**, and a **variant suffix**.

```{list-table}
:header-rows: 1
:widths: 22 33 45

* - Segment
  - Example values
  - Meaning
* - Region / scope
  - `NOR`, `CEN`, `SOU`, `LAO`
  - Northern, Central, Southern region, or national (`LAO`)
* - Sector / service
  - `ELC`, `COK`, `HET`, `TRA`, `IND`, `COM`, `RES`
  - Electricity, cooking, heat, transport, industry, commercial, residential
* - Fuel / carrier
  - `FIR`, `CHC`, `PEL`, `LPG`, `BGS`, `COA`, `DSL`, `BIO`, `ELC`, `H2`
  - Firewood, charcoal, pellets, LPG, biogas, coal, diesel, biomass, electricity,
    hydrogen
* - Variant / role
  - `TCS`, `ICS`, `GAS`, `IDC`, `BOL`, `DUM`, `BKS`, `MIN`, `DEM`
  - Traditional stove, improved stove, gasifier, induction, boiler, dummy
    balancing, backstop, mining/production, demand-aggregation
```

### Worked examples

- `RESCOKUFIRTCS` = **RES**idential **COK**ing, **U**rban, **FIR**ewood,
  **T**raditional **C**ook**S**tove (an urban three-stone firewood fire).
- `RESCOKRFIRGAS` = residential cooking, **R**ural, firewood **GAS**ifier stove.
- `LAOCOABOLIND` = national (**LAO**) **COA**l **BOL**er for **IND**ustrial heat.
- `LAO0H2BOLIND` = national **H2** boiler for industrial heat.
- `DEMNORELCIND` = **DEM**and-aggregation technology for Northern-region industrial
  electricity.
- `MINCHC` = **MIN** (production) technology for **CHC** (charcoal) in kilns.

```{note}
Some technology and commodity codes were renamed between model versions. The
authoritative mapping of old to new names lives in the
`10.1 Technology_Commodity list` sheet of the input dataset shipped with the model.
```

## 2.5 Electricity

Power supply is represented plant-by-plant so that seasonal hydrology can be
captured. The build includes on the order of **70 existing hydropower plants** plus
around **80 committed or planned pipeline plants**, alongside individually
represented coal, solar and wind projects. Each plant carries dry-season and
wet-season capacity factors derived from multi-year monthly generation records, and
hydro plants are classified as run-of-river or reservoir.

### Two trade modalities

A distinctive feature of the Lao power sector is that its electricity is sold
through **two structurally different commercial channels**, and the model represents
each as a separate export technology so that the Trade lever can act on them
independently.

- **Channel 1: IPP direct export.** Large hydropower plants built under long-term
  build-operate-transfer concessions, financed largely with foreign equity alongside
  stakes held by the Lao Holding State Enterprise (LHSE). Their output is sold
  directly to neighbouring utilities, predominantly the Electricity Generating
  Authority of Thailand (EGAT), and also Vietnam and Cambodia, under US-dollar-
  denominated, take-or-pay power-purchase agreements (PPAs). Revenue from this
  channel largely bypasses the domestic system.
- **Channel 2: the EDL system.** EDL-Generation (75% owned by Électricité du Laos)
  and contracted IPPs sell power to EDL under PPAs; EDL-Transmission (a Lao-Chinese
  joint venture established in 2023) carries it and EDL distributes it to domestic
  consumers at low, kip-denominated tariffs (estimated at about half the
  cost-recovery level). Over the same regional interconnectors, EDL exports surplus
  electricity (`EXPE`) and imports power during the dry season (China, Thailand,
  Vietnam and Cambodia, with a pilot route to Singapore under the LTMS-PIP).

This split creates a structural currency mismatch: export PPAs and most sector debt
are in US dollars while domestic tariffs are in kip. In the model, the **trade lever
governs how much generating capacity is committed to export versus redirected to
domestic use**.

### Transmission

Cross-border and inter-regional flows are handled by dedicated transmission and
trade technologies:

- **Inter-regional interconnectors**: the North-Central and Central-South links.
- **Intra-regional transmission (`PWRTRN`)**: within-region network capacity, split
  Northern, Central and Southern.

## 2.6 Cooking

Cooking is the most technology-diverse part of the model, because it carries both
the household-air-quality (PM2.5) signal and the woodfuel-demand signal. It is built
household-by-household and then resolved into a ladder of stove technologies. The
base year combines the 2023 IEA energy balance with the 2021 national biomass survey,
because the IEA balance understates solid-fuel use; the survey-based reconstruction
puts firewood at about 1,950 kt (roughly 33 PJ) and charcoal at about 735 kt in 2023.
Households are split into urban and rural populations, about **1.35 million
households in 2023, 40% urban and 60% rural**, and per-household consumption
intensities anchor base-year demand. On this basis, roughly **97% of cooking energy
in 2023 is solid biomass**, dominated by firewood with significant charcoal use.

Useful cooking-energy demand is split three ways: **urban residential
(`LAOCOKURB`), rural residential (`LAOCOKRUR`) and commercial (`LAOCOKCOM`)**.
Commercial cooking is calibrated to IEA 2023 commercial energy use (LPG, firewood,
charcoal and electricity) and grown with service-sector activity. Each service is met
by a ladder of competing stoves, each with its own efficiency, capital cost, fixed
cost and lifetime (see {doc}`parameterization`):

```{list-table}
:header-rows: 1
:widths: 40 30 30

* - Stove family
  - Fuel
  - Example codes
* - Three-stone / traditional
  - Firewood, charcoal
  - `RESCOK*FIRTCS`, `RESCOK*CHCTCS`
* - Improved combustion
  - Firewood, charcoal
  - `RESCOK*FIRICS`, `RESCOK*CHCICS`
* - Gasifier
  - Firewood, pellets
  - `RESCOK*FIRGAS`
* - Clean gaseous / liquid
  - LPG, biogas, ethanol
  - `RESCOK*LPGICS`, `RESCOK*BGSICS`
* - Electric
  - Electricity (induction)
  - `RESCOK*ELIDC`
```

Charcoal is not a primary fuel: it is carbonised from wood in kilns via the
`MINCHC` technology at roughly 43% efficiency, so switching households away from
charcoal reduces woodfuel demand by more than the charcoal energy it replaces.
Pellets are produced through `MINPEL` and biogas through `MINBGS`. Region-specific
"dummy" electricity technologies (for example `NORCOKURBDUM`) route grid
electricity to national cooking demand, and backstop technologies (`RESCOKURBBKS`,
`RESCOKRURBKS`) guarantee feasibility.

## 2.7 Industry

Industrial energy use falls almost entirely into two end-use vectors, **process
heat (`LAOHETIND`)** and **electricity (`LAOELCIND`)**, with no significant
petrochemical feedstock reported in the energy balance. In 2023, process heat
accounts for about **29 PJ** (coal ~15 PJ, solid biomass/firewood ~11 PJ, diesel
~2.5 PJ) and electricity for about **13 PJ**, so heat is roughly 70% and electricity
30% of industrial final energy.

Heat is met by a single national heat-service demand served by competing boilers.
Each boiler type carries an efficiency, so the model captures the large gap between
the inefficient existing fleet (coal and diesel around 40%, biomass around 25%) and
improved, best-practice or electric boilers (around 82-100%; see
{doc}`parameterization`). The same useful heat can therefore be met either by
replacing inefficient boilers or by switching fuels:

```{list-table}
:header-rows: 1
:widths: 45 25 30

* - Boiler
  - Fuel
  - Code
* - Coal boiler
  - Coal
  - `LAOCOABOLIND`
* - Diesel boiler
  - Diesel
  - `LAODSLBOLIND`
* - Biomass boiler
  - Firewood / pellets
  - `LAOBIOBOLIND`
* - Electric boiler
  - Electricity
  - `LAOELCBOLIND`
* - Hydrogen boiler
  - Hydrogen
  - `LAO0H2BOLIND`
* - Coal boiler with CCS
  - Coal
  - `LAOCOACCSBOLIND`
* - Biomass boiler with CCS
  - Biomass
  - `LAOBIOCCSBOLIND`
```

The hydrogen boiler becomes available in the mid-2030s but is typically
out-competed by direct electrification. The two carbon-capture (CCS) boiler variants
exist in the technology set but are **excluded from the default scenarios**, so no
CCS is deployed anywhere in the 27-scenario matrix. This is a design assumption
about what the core matrix explores, not a result the model produced; see
{doc}`scenario_design`.

Industrial electricity is split into conventional process and motor-drive demand and
the electricity consumed by **cryptocurrency mining and data centres**. The latter is
large but volatile: it reached on the order of **3.5 TWh in 2023** (around an eighth
of national electricity demand) before falling sharply in subsequent years, and it is
carried as a distinct, separately projected load so that it does not distort the
underlying industrial trend.

## 2.8 Transport

Transport is built from the ground up on national activity and vehicle-stock
statistics and then resolved into competing drivetrains, so the model can choose how
each mobility service is provided.

**Base year and calibration.** The starting point is the Lao Statistics Bureau, which
reports the registered fleet by category (motorcycles and motorcycle taxis,
three-wheelers, sedans, taxis, pick-ups, jeeps, vans and trucks) and annual passenger
and freight movement by land, water, rail and air. These series are extended to the
2023 base year with Ministry of Energy and Mines yearbooks and the latest official
stock release. The fleet is overwhelmingly two- and three-wheeled: **motorcycles
alone number about 2.4 million in 2023**, dwarfing the roughly 0.1 million sedans.
Historical pkm and tkm by mode (available from 2000) calibrate the base year, and the
vehicle stock is translated into service activity using category-specific assumptions
on annual mileage, occupancy (passengers per vehicle) and load factor (tonnes per
vehicle).

**Modes.** The many registration categories are consolidated into a compact set of
representative modes: motorcycles and three-wheelers, cars (sedans, jeeps and
pick-ups), buses, light-duty vehicles (vans and light trucks) and heavy-duty trucks,
alongside rail and aviation, each split into passenger and freight service where
relevant. Inland-water and maritime transport is excluded: it accounts for a very
small share of activity and lacks consistent data. Demand is expressed in the natural
service units of **passenger-kilometres (pkm)** and **tonne-kilometres (tkm)**, so
the same service can be met by any eligible drivetrain, and it is projected from
population, urbanisation and sector GDP growth with long-run elasticities, held
identical across scenarios.

**Drivetrains.** Each mode is represented by a menu of vehicle technologies
distinguished by drivetrain: internal-combustion (diesel or gasoline),
battery-electric, and hydrogen fuel-cell; aviation is served by conventional jet,
bio-jet and synthetic e-fuel, and rail by electric or diesel traction. Every
technology carries its own techno-economic parameterisation: energy intensity
(litres/100 km and MJ/km, converted to useful energy per pkm or tkm), capital and
operating costs, lifetime, and occupancy or load factor. Fuel economy and costs for
conventional and electric vehicles draw on a regional technology catalogue and a
Vietnamese vehicle-cost study (used as a proxy where Lao-specific data are missing),
and electric mobility additionally carries charging-infrastructure cost.

**Fuel supply.** Liquid fuels enter through explicit blending steps (diesel with
biodiesel, gasoline with ethanol, and jet fuel with aviation biofuel), while
electricity reaches vehicles through a charging technology and hydrogen is produced
by electrolysis (and converted to e-fuel for aviation). Rail and aviation use
dedicated calculations that convert reported traffic into energy service, so that
long-distance and freight movements that cannot easily electrify (notably aviation)
are represented realistically and can take up hydrogen-derived e-fuel where it is
cost-effective. Because mobility demand is fixed, the transport results isolate the
drivetrain transition: how far, how fast and at what cost each mode electrifies.

## 2.9 Emissions

Two pollutants are tracked as combustion by-products through emission activity
ratios: **CO2** (the target of the Carbon lever) and **primary PM2.5** (the target of
the Cooking / air-quality lever).

The two have different coverage across the model, and the difference matters for how
the levers behave:

- **CO2** arises wherever fossil fuel is burned, which couples the power sector,
  industrial boilers and transport to the national carbon cap. Under the national
  carbon-accounting convention used here, **biomass CO2 is treated as biogenic**, so
  the carbon cap does not directly constrain firewood or charcoal cooking.
- **Primary PM2.5** is applied to **cooking stoves and the transport sector only**.
  Power generation, charcoal kilns and industrial heat carry no primary-PM2.5
  emission factor, so the air-quality cap acts on cooking and transport alone.
  Cooking supplies about **95% of modelled primary PM2.5 in 2023 and 97% in 2050**,
  which is why the C lever is described as the cooking lever even though it is
  implemented as a national primary-PM2.5 constraint.

PM2.5 emitted by solid-fuel stoves feeds the post-processing health module that
converts household exposure into DALYs, described in {doc}`health_dalys`. Note that
the health module is narrower than the constraint: it covers cooking exposure only.
