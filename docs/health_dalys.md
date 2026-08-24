# 6. Health impacts: how DALYs are calculated

The model couples the energy system to a **household-air-pollution (HAP) health
module**. This chapter sets out, step by step, how the modelled cooking-stove fleet is
turned into a health burden expressed in **Disability-Adjusted Life Years (DALYs)**.

## 6.1 Where the calculation sits

The health burden is computed as a **post-processing step** on the model's cooking
output. It is *not* part of the cost-minimising optimisation. The exposure-response
function is non-linear, so it is applied after the optimisation rather than inside
it. The optimisation chooses the stove fleet; the health module then reads the
resulting stove shares and converts them into exposure and disease burden. Keeping it
outside the optimisation means the model is never "optimising for health" directly:
the health outcome is a consequence of the cooking transition driven by the
air-quality (C) lever.

```{important}
The health accounting is **narrower than the air-quality constraint it accompanies**.
Primary PM2.5 is tracked in the model for both cooking stoves and the transport
sector, so the C lever acts on cooking and transport alike. The DALYs reported here,
however, are derived from **household exposure to cooking smoke only**. The fraction
of transport emissions actually inhaled is far smaller than for smoke released inside
a kitchen, and ambient health effects from transport, industry and electricity
generation are outside the boundary of this calculation.
```

The calculation is carried out **separately for urban and rural populations** and for
**each year**, and summed over **five disease endpoints**:

- ischaemic heart disease (IHD),
- stroke,
- chronic obstructive pulmonary disease (COPD),
- lung cancer (LC), and
- acute lower-respiratory infection (ALRI).

Results are reported as **cumulative DALYs over 2023 to 2050**.

## 6.2 Step 1: Exposure

For each area $a$ (urban or rural) and year, the population-weighted indoor PM2.5
concentration is the stove-share-weighted average of the technology-specific indoor
concentrations in {ref}`Table 6.1 <daly-table-conc>`:

$$\bar{C}_a = \sum_s \theta_{s,a}\, C_{s,a}$$

where $\theta_{s,a}$ is the share of stove category $s$ (derived from the modelled
stove capacities) and $C_{s,a}$ its 24-hour indoor concentration.

Stove shares set **only the exposure concentration**. The exposed population $N_a$ is
the area population, obtained as the **household count multiplied by the mean
household size**. Counting exposure per person in this way, rather than per stove,
prevents fuel stacking, where one household owns several stoves, from inflating the
burden.

Personal exposure is then obtained with an indoor-to-personal adjustment
$\varepsilon = 0.71$:

$$z_a = \varepsilon\, \bar{C}_a$$

## 6.3 Step 2: Exposure-response (relative risk)

Relative risk for disease $d$ at personal exposure $z$ follows a **reduced form of the
integrated exposure-response (IER)** function, with the endpoint-specific parameters
in {ref}`Table 6.2 <daly-table-ier>`. The IER shape is used with the parameter
$\delta$ fixed at one, and **without age modification** of the IHD and stroke curves:

$$RR_d(z) = 1 + \alpha_d \left[1 - \exp\!\left(-\beta_d (z - z_{cf})^{\delta_d}\right)\right], \quad z > z_{cf}$$

and $RR_d = 1$ otherwise. The counterfactual is $z_{cf} = 7.5\ \mu g\,m^{-3}$, the WHO
theoretical-minimum-risk exposure level: below it, no excess risk is attributed.

The response is evaluated **separately for each stove category at its own personal
exposure** $\varepsilon C_{s,a}$, and then aggregated by the modelled cooking-capacity
share, giving the mean relative risk in area $a$:

$$\overline{RR}_{d,a} = \sum_s \theta_{s,a}\, RR_d(\varepsilon\, C_{s,a})$$

Clean-fuel categories sit at or below the counterfactual and enter at $RR = 1$,
contributing no excess risk.

```{note}
Evaluating the non-linear response per exposure category, rather than once at a
single population-mean concentration, avoids the bias of applying a non-linear
function to an average. It also removes the need for a separate solid-fuel-user
fraction, because the clean-versus-solid split is already carried by
$\theta_{s,a}$.
```

## 6.4 Step 3: Attributable fraction

The population attributable fraction follows directly from the mean relative risk:

$$PAF_{d,a} = \frac{\overline{RR}_{d,a} - 1}{\overline{RR}_{d,a}}$$

## 6.5 Step 4: DALYs

DALYs are the attributable fraction applied to the exposed population $N_a$ and the
area-specific background disease rate $I_{d,a}$ from
{ref}`Table 6.3 <daly-table-bg>`, expressed **per 100,000 people** and summed over
areas and endpoints:

$$DALY = \sum_a \sum_d PAF_{d,a}\, N_a\, \frac{I_{d,a}}{100{,}000}$$

## 6.6 Key assumptions

- Background disease rates are from **GBD 2019** for Lao PDR. **Urban rates are set 15%
  below** and **rural rates 20% above** the national average, to reflect health-access
  disparities. The two multipliers are **normalised each year** so that their
  population-weighted mean reproduces the national rate.
- Indoor concentrations are **literature-derived values**. **Rural concentrations are
  set 25% above urban** (capped at 1500 µg m⁻³) to reflect smaller, less-ventilated
  kitchens.
- The 15%, 20% and 25% adjustments above are assumptions, and are examined in the
  sensitivity analysis.
- Because firewood is priced at essentially zero in the model, the modelled economic
  case for cleaner cooking is a **conservative** one.

```{warning}
**How to read the numbers.** The coefficients $\alpha_d$ and $\beta_d$ are a
reduced-form approximation, and the shares $\theta_{s,a}$ are modelled
cooking-capacity shares, which under fuel stacking are an imperfect proxy for the
share of people actually cooking on each stove type. The health findings are
therefore most robust as **relative differences across scenarios**; absolute burdens
should be read as indicative.
```

## 6.7 Parameter tables

(daly-table-conc)=
### Table 6.1: Indoor 24-hour PM2.5 concentrations by stove category (µg m⁻³)

Rural values are 25% above urban.

```{list-table}
:header-rows: 1
:widths: 50 25 25

* - Stove category
  - Urban
  - Rural
* - Traditional firewood
  - 852
  - 1065
* - Improved firewood
  - 314
  - 393
* - Firewood gasifier
  - 87
  - 109
* - Traditional charcoal
  - 541
  - 676
* - Improved charcoal
  - 162
  - 203
* - Pellet gasifier
  - 87
  - 109
* - LPG
  - 79
  - 99
* - Biogas
  - 20
  - 25
* - Ethanol
  - 15
  - 19
* - Electric induction
  - 10
  - 13
```

(daly-table-ier)=
### Table 6.2: Reduced-form exposure-response coefficients by endpoint

The shape parameter δ is fixed at one; functional form after Burnett et al. (2014).

```{list-table}
:header-rows: 1
:widths: 55 15 15 15

* - Disease
  - α
  - β
  - δ
* - Ischaemic heart disease (IHD)
  - 0.4991
  - 0.0010
  - 1.0
* - Stroke
  - 0.4462
  - 0.0010
  - 1.0
* - Chronic obstructive pulmonary disease (COPD)
  - 0.2848
  - 0.0006
  - 1.0
* - Lung cancer (LC)
  - 0.2776
  - 0.0011
  - 1.0
* - Acute lower-respiratory infection (ALRI)
  - 0.8726
  - 0.0013
  - 1.0
```

(daly-table-bg)=
### Table 6.3: Background disease burden, Lao PDR (DALYs per 100,000; GBD 2019)

Urban and rural values apply factors of 0.85 and 1.20 to the national rate. In the
calculation these factors are normalised each year so that their population-weighted
mean equals the national rate.

```{list-table}
:header-rows: 1
:widths: 40 20 20 20

* - Disease
  - National
  - Urban
  - Rural
* - IHD
  - 2800
  - 2380
  - 3360
* - Stroke
  - 3100
  - 2635
  - 3720
* - COPD
  - 1200
  - 1020
  - 1440
* - Lung cancer
  - 420
  - 357
  - 504
* - ALRI
  - 1800
  - 1530
  - 2160
```

```{note}
The DALY method summarised here is applied to every scenario in the matrix. The
cross-scenario health results are reported in the research article, not in this
documentation.
```
