# 4. Scenario design

## 4.1 Three independent levers

The scenario design is organised around three policy levers, each representing a
distinct decision that Lao PDR faces and each set at three ambition levels (1 = least
ambitious, 3 = most ambitious):

```{list-table}
:header-rows: 1
:widths: 12 22 66

* - Lever
  - Theme
  - What it controls
* - **T: Trade**
  - Who controls the hydro
  - How much exported hydropower is redirected to domestic use rather than sold
    abroad under existing contracts. This is fundamentally about money and energy
    sovereignty.
* - **M: Carbon**
  - Grid and system decarbonisation
  - A national CO2 cap that tightens over time, representing the country's climate
    commitments.
* - **C: Cooking / air quality**
  - Household air quality
  - A national PM2.5 cap. Because cooking is the dominant source of household PM2.5,
    this lever drives the cooking transition, but at its strictest level it also
    reaches into transport.
```

### Trade (T)

- **T1** (business as usual): existing independent-power-producer (IPP) export
  contracts are retained.
- **T2** (gradual reversion): contracts are allowed to lapse as they expire, giving
  partial domestic priority.
- **T3** (domestic priority): exported power is redirected to domestic use. This is
  treated as an upper bound, since much of the fleet is contractually locked to
  foreign off-takers.

### Carbon (M)

A cap on national CO2 emissions.

- **M1**: no carbon cap.
- **M2**: annual CO2 held **72% below** the level reached without a cap in 2050.
- **M3**: CO2 brought to **zero in 2050**.

### Cooking / air quality (C)

A cap on national **primary PM2.5** emissions. Cooking supplies 95% of modelled
primary PM2.5 in 2023 and 97% in 2050, which is why C is referred to as the cooking
lever even though it is implemented as a national constraint.

- **C1**: no PM2.5 cap.
- **C2**: emissions held **67% below** the uncapped level in 2050. The difference
  between C1 and C2 arises predominantly through changes in cooking, as efficient
  gasifier, pellet and LPG stoves displace traditional firewood.
- **C3**: emissions brought to **zero in 2050**. Because the model applies a
  primary-PM2.5 factor to transport as well as cooking, a national zero-emission
  requirement also reaches road transport and removes tailpipe primary PM2.5, so C3
  electrifies the fleet and yields a CO2 co-benefit even with no carbon policy in
  force.

```{admonition} Cap trajectories
:class: note
Both the carbon and the air-quality caps are **specified from 2027** and **decline
linearly from 2035** to their 2050 value.
```

## 4.2 The full 3x3x3 matrix

Combining three levers at three levels each gives a **full factorial of 27
scenarios (S1-S27)**. A factorial design (rather than moving one lever at a time) is
what lets the analysis separate each lever's main effect from the interactions
between levers.

```{list-table}
:header-rows: 1
:widths: 12 22 12 22 12 20

* - ID
  - T / M / C
  - ID
  - T / M / C
  - ID
  - T / M / C
* - **S1**
  - T1 M1 C1 *(baseline)*
  - S10
  - T1 M2 C2
  - S19
  - T2 M3 C1
* - S2
  - T1 M3 C3
  - S11
  - T1 M2 C3
  - S20
  - T2 M3 C2
* - S3
  - T3 M1 C1
  - S12
  - T1 M3 C1
  - S21
  - T2 M3 C3
* - **S4**
  - T2 M2 C2 *(achievable)*
  - S13
  - T1 M3 C2
  - S22
  - T3 M1 C2
* - **S5**
  - T3 M3 C3 *(most ambitious)*
  - S14
  - T2 M1 C1
  - S23
  - T3 M1 C3
* - S6
  - T3 M2 C1
  - S15
  - T2 M1 C2
  - S24
  - T3 M2 C2
* - S7
  - T1 M1 C2
  - S16
  - T2 M1 C3
  - S25
  - T3 M2 C3
* - S8
  - T1 M1 C3
  - S17
  - T2 M2 C1
  - S26
  - T3 M3 C1
* - S9
  - T1 M2 C1
  - S18
  - T2 M2 C3
  - S27
  - T3 M3 C2
```

## 4.3 Anchor scenarios

Three scenarios anchor most of the narrative:

- **S1 (T1 M1 C1)**, the **baseline**: today's trajectory with no new policy.
- **S4 (T2 M2 C2)**, the **achievable midpoint**: moderate ambition on all three
  levers, and the pathway argued to capture most of the benefit at feasible cost.
- **S5 (T3 M3 C3)**, the **most ambitious** transition: full ambition on every lever.

## 4.4 Sensitivity runs

Two additional runs test the sensitivity of the achievable pathway to hydrology by
re-running **S4 (T2 M2 C2)** under dry and wet conditions:

- **S28**: S4 under a dry-hydrology year.
- **S29**: S4 under a wet-hydrology year.

## 4.5 Implementation

Each lever is implemented as a constraint on the optimisation. The carbon and PM2.5
levers enter as declining emission caps; the trade lever governs how much generating
capacity is committed to export versus made available domestically. Demands are held
constant across all runs, so the objective, minimising total discounted system cost
over the horizon, isolates the cost of each combination of ambition levels.

```{note}
Carbon-capture (CCS) technologies are excluded from all 27 core scenarios by
default. The CCS boiler variants exist in the technology set (see
{doc}`model_structure`) but are reserved for optional sensitivity analysis. No CCS
is therefore deployed anywhere in the matrix, but that absence is a **design
assumption about what the matrix explores**, not a finding that the model rejected
CCS on cost grounds.
```
