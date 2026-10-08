# Dataset Discovery V2: Scholarly Article-to-Dataset Extraction

**Project:** COM7014 Advanced Computing Project

**Record date:** 8 October 2026

**Scope:** scholarly discovery and full-text dataset extraction

**Status:** working research record; no dataset downloaded and no model executed

## Executive finding

The literature search materially changed the dataset strategy. M5 and Corporación Favorita remain useful because they are large, public, covariate-rich demand benchmarks with extensive published comparators. They cannot, however, be treated as evidence that per-series model routing is novel. Multiple studies already use them for feature-based model selection, ranked shortlisting, or sparse expert routing.

The strongest directly competing studies found were:

- Zhang's *Intelligent Routing for Sparse Demand Forecasting*, which routes individual Favorita series among classical, machine-learning and deep-learning experts;
- FAME, which performs cost-aware sparse expert routing on M5, Favorita and confidential industrial vending-machine data, with Chronos as an optional high-cost expert;
- CARFS, which learns a ranked forecast-model shortlist on M5 and applies it to Favorita;
- AutoForecast and FFORMPP, which establish broader meta-learning and forecast-performance-prediction precedents.

The defensible contribution therefore moves from “build a per-series router” to a narrower question: **can a router produce a calibrated probability that trusting a foundation model is the right decision, generalise to a held-out dataset family or field, and defer to a classical/intermittent-demand fallback at an explicit accuracy–cost operating point?**

## 1. Search and verification method

### 1.1 Discovery sources

The discovery pass used:

- Google Scholar for broad title and phrase discovery;
- ACM Digital Library and an author manuscript for AutoForecast;
- ScienceDirect and DOI records for International Journal of Forecasting and Machine Learning with Applications papers;
- SpringerLink for the open-access energy model-selection study;
- Taylor & Francis Online for the 2026 supply-chain study and its data-availability statement;
- PubMed and PubMed Central for clinical adaptive-selection work;
- arXiv and OpenReview for recent routing manuscripts;
- official repositories only to confirm an access route, not to download data.

The principal Google Scholar query was:

```text
"forecast model selection" time series dataset
```

Google Scholar reported approximately 358 results at the time of the search. Follow-up searches combined these concepts:

```text
forecast model selection
algorithm selection
model routing
meta-learning forecasting
sparse demand forecasting
intermittent demand
energy / healthcare / transport / cloud workload
dataset / benchmark / corpus
```

Each paper is described by its actual accessible version: journal article, conference paper, author manuscript, preprint, or workshop manuscript.

### 1.2 Screening and extraction fields

Titles and abstracts were screened for an explicit connection to forecasting-model selection, routing, meta-learning, forecast combination, or cross-model benchmarking. Full text was then used to extract:

1. dataset and authoritative access route;
2. forecasting unit;
3. number of series or entities;
4. observation frequency and history length;
5. forecast horizon and split design;
6. sparsity/intermittency information;
7. exogenous variables or metadata;
8. public, restricted, confidential, or unclear availability;
9. how the article used the dataset;
10. implications for dataset selection and project originality.

### 1.3 Evidence-status labels

- **Peer-reviewed article/conference paper:** stable publisher or proceedings record.
- **Author manuscript:** full article supplied by an author or institution, checked against publication metadata.
- **Preprint/workshop manuscript:** technically informative but not treated as equivalent to a peer-reviewed final article.
- **Public candidate:** an access route exists; licence and redistribution still require authoritative verification.
- **Evidence only:** useful to establish a real problem or method, but unavailable or unsuitable for reproducible experiments.

## 2. Detailed article-to-dataset extraction

### A2D-001 — Intelligent Routing for Sparse Demand Forecasting

**Source:** Qiwen Zhang (2025), arXiv:2506.14810 and OpenReview workshop manuscript.

**Dataset:** Corporación Favorita Grocery Sales Forecasting.

| Property | Extracted detail |
|---|---|
| Unit | Daily item–store demand series |
| Scale | 19,646 router-training series and 5,000 disjoint holdout series; 24,646 total |
| Horizons | 14 and 30 days |
| Feature representation | 34 features: tsfresh statistics plus demand frequency, mean inter-demand interval, coefficient of variation and mean demand |
| Sparsity | Mean zero-sales share 57.2%; median 62.2% |
| Demand regimes | 30% smooth, 18% erratic, 24% lumpy and 28% intermittent under the reported ADI/CV² categorisation |
| Expert pool | ETS, Croston, naive, moving average, LightGBM, DeepAR and PatchTST |
| Routers | Rule-based, LightGBM and InceptionTime |
| Metric | NWRMSLE |
| Access | Public Kaggle competition route; competition terms still apply |

**Implication:** this is a direct per-series, cross-family routing precedent. Favorita alone cannot demonstrate novelty. The manuscript reports up to 11.8% improvement and 4.67× faster inference, but the stable proceedings status should be checked because the available PDF contains placeholder DOI text.

Primary source: [arXiv record](https://arxiv.org/abs/2506.14810).

### A2D-002 — FAME: Forecastability-Aware Mixture of Experts

**Source:** Qianyang Li et al. (2026), arXiv:2606.08896, preprint with public code.

**Datasets:** confidential SNBC vending-machine transactions, M5 and Favorita.

| Property | Extracted detail |
|---|---|
| Industrial scale | More than 5,000 vending machines and more than 60 million transactions |
| Public benchmarks | M5 item–store demand and Favorita active store–item demand |
| Split | Chronological 28-day validation and 28-day test horizons for both public benchmarks |
| Filtering | Favorita histories shorter than 60 days are removed |
| M5 covariates | Calendar events, SNAP indicators, prices and hierarchy |
| Favorita covariates | Holidays, oil price and item/store metadata |
| Fingerprint | Lifecycle, zero ratio, ADI, CV², volatility, trend, seasonality, spectral, metadata and contextual features |
| Expert families | Statistical, machine-learning and deep forecasting models; optional foundation-model extension |
| Foundation-model result | Optional Chronos invoked for 8.6% of M5 series and 10.9% of Favorita series |
| Availability | M5 and Favorita public through competition routes; SNBC confidential |

**Implication:** FAME is the closest technical overlap found. It already combines sparse routing, intermittent-demand features, a heterogeneous expert pool, oracle regret and inference cost. Its use of “calibrated” refers to operating-point/softmax choices; the paper does not report a calibrated probability of routing correctness through reliability diagrams, expected calibration error or risk–coverage behaviour. As a preprint, it is strong novelty-warning evidence rather than settled peer-reviewed authority.

Primary source: [arXiv record](https://arxiv.org/abs/2606.08896).

### A2D-003 — CARFS ranked forecast-model selection

**Source:** Reinard C. Ganzevoort and Jan H. van Vuuren (2023), *Machine Learning with Applications*, 13, 100482. DOI: 10.1016/j.mlwa.2023.100482.

**Datasets:** M5 and Corporación Favorita.

| Phase | Dataset use |
|---|---|
| Benchmarking | M5: 3,049 products across 10 stores, or 30,490 bottom-level item–store series |
| Implementation | A 1,000-series subset of Favorita for ranked model recommendations |
| Method | Feature-based clustering and a ranked shortlist of forecast models |

**Implication:** transfer from an M5 benchmark database to new Favorita series is already demonstrated. A new evaluation needs a stricter reliability target and preferably a held-out field rather than another random retail split.

Primary source: [DOI](https://doi.org/10.1016/j.mlwa.2023.100482).

### A2D-004 — FFORMPP

**Source:** Thiyanga S. Talagala, Feng Li and Yanfei Kang (2022), *International Journal of Forecasting*. DOI: 10.1016/j.ijforecast.2021.07.002.

**Datasets:** M1, M3, synthetic GRATIS series and M4.

| Role | Dataset design |
|---|---|
| Observed reference data | M1 and M3 yearly, quarterly and monthly series |
| Synthetic augmentation | 10,000 GRATIS series for each frequency category |
| Frequencies | Yearly, quarterly, monthly, weekly, daily and hourly |
| External test | M4, 100,000 series |
| M4 horizons | 6 yearly, 8 quarterly, 18 monthly, 13 weekly, 14 daily and 48 hourly steps |
| Label/target | Predicted MASE for candidate forecast models |

The paper also warns that M4 daily series contain duplication/leakage-like construction issues, including shifted segments and constant-value transformations.

**Implication:** FFORMPP is a methodological anchor for feature-based performance prediction and for checking whether the meta-training feature space covers the test series. M1/M3/M4 are useful comparators and frequency controls, but not sufficient as intermittent-demand evaluation.

Primary source: [arXiv full text](https://arxiv.org/abs/1908.11500).

### A2D-005 — AutoForecast

**Source:** Mustafa Abdallah et al., *Evaluation-Free Time-Series Forecasting Model Selection via Meta-Learning*, ACM TKDD author manuscript.

**Datasets:** a released multi-domain corpus and Adobe production traces.

| Property | Extracted detail |
|---|---|
| Corpus | 348 datasets containing 625 time series |
| Structure | 308 univariate datasets and 40 multivariate datasets |
| Model space | 322 forecasting-model/hyperparameter configurations |
| Domains | IoT, finance, sales, cloud computing, energy, quality control, storage, environment, employment and other |
| Adobe trace | CPU and memory for 50 production services over 15 days, 1–15 May 2021 |
| Release | Dataset corpus, meta-features, model performances and source code released by the authors |

The application distribution reported by the paper is: IoT 26 datasets, finance 34, sales 18, cloud 12, energy 25, quality control 13, fast storage 24, environment 38, employment 7 and other 151.

**Implication:** the corpus is a valuable source of cross-domain candidates and precomputed model-performance metadata. It should not be adopted wholesale: many entries contain one or a few series, and each upstream dataset needs an individual provenance and licence check.

Primary source: [author manuscript](https://engineering.purdue.edu/dcsl/wp-content/uploads/2025/02/AutoForecast_ACM_TKDD.pdf).

### A2D-006 — Automatic demand forecast model selection in supply chains

**Source:** Wassim Garred, Raphaël Oger and Matthieu Lauras (2026), *International Journal of Production Research*. DOI: 10.1080/00207543.2026.2623194.

**Datasets:** M3 monthly and an industrial supply-chain dataset.

- M3 monthly is openly available and supplies the reproducible benchmark.
- The industrial participants did not consent to public data sharing.
- Other supporting data may be requested from the corresponding author, but this is not an assured reproducible access route.

**Decision:** retain M3 as a comparator; reject the industrial dataset from the experimental corpus while using the paper as evidence of a live supply-chain model-selection problem.

Primary source: [publisher article](https://www.tandfonline.com/doi/full/10.1080/00207543.2026.2623194).

### A2D-007 — M5 competition data

**Source:** M5 competition papers and official data route.

| Level | Series count |
|---|---:|
| Bottom-level item–store | 30,490 |
| All hierarchical aggregation levels | 42,840 |

The data cover 3,049 products sold in 10 stores across three US states, with daily unit sales, a 28-day official horizon, calendar events, SNAP information and prices.

**Decision:** retain as a major comparability and intermittency candidate. It is heavily reused and appears in known model-training corpora, so every checkpoint needs dataset-specific overlap handling.

Primary source: [M5 competition article](https://www.sciencedirect.com/science/article/pii/S0169207021001187).

### A2D-008 — Car Parts

**Source:** intermittent-demand forecasting literature and the Monash/GIFT-Eval representations.

- 2,674 monthly series;
- length 51 observations;
- 2,509 complete series in the published setup;
- final six months used as holdout in the referenced design;
- explicit spare-parts intermittent-demand domain.

**Decision:** retain as a compact intermittency anchor. The short histories and likely presence in foundation-model training corpora limit unqualified zero-shot claims.

Primary source: [journal article](https://www.sciencedirect.com/science/article/pii/S0169207011000781).

### A2D-009 — On forecast stability

**Source:** 2025 *International Journal of Forecasting* article.

**Datasets:** M4 monthly, M3 monthly, the first 1,000 Favorita series, and an aggregated M5-items dataset.

The article defines each Favorita series as daily unit sales for one item at one store and replaces missing observations with zeros. Its public experimental repository makes the 1,000-series Favorita subset a potentially reproducible local-compute protocol.

Primary source: [article page](https://www.sciencedirect.com/science/article/abs/pii/S0169207025000068).

### A2D-010 — Ausgrid value-oriented forecast selection

**Source:** Dorina Werling et al. (2023), *Automating Value-Oriented Forecast Model Selection by Meta-learning: Application on a Dispatchable Feeder*, LNCS 14467.

**Dataset:** Ausgrid Solar Home Electricity.

| Property | Extracted detail |
|---|---|
| Entities | 300 Australian residential buildings |
| Signals | Electricity load and photovoltaic generation |
| Period | 1 July 2010 to 30 June 2013 |
| Native frequency | 30 minutes |
| Paper frequency | Resampled hourly |
| Forecast split | First two years train; final year test |
| Selector split | First 200 buildings train; final 100 buildings test |
| Derived target | Prosumption = load minus PV generation |
| Selection objective | Highest downstream value in a PV-battery dispatch problem |

**Decision:** strongest article-derived held-out energy candidate. It is public, entity-level, and already supports a clean cross-building model-selection split. Authoritative upstream terms still need to be recorded before use.

Primary source: [Springer open-access chapter](https://link.springer.com/chapter/10.1007/978-3-031-48649-4_6).

### A2D-011 — NN5 meta-learning model selection

**Source:** Sasan Barak, Mahdi Nasiri and Mehrdad Rostamzadeh (2019).

**Dataset:** NN5 cash-withdrawal competition.

- 111 daily ATM cash-demand series from the United Kingdom;
- 791 observations per series in the study;
- 56-day forecast horizon;
- three rolling origins;
- series contain multiple seasonalities, trends, structural breaks, zeros and missing values;
- six classifier families are used as meta-learners for forecasting-model selection.

**Decision:** retain as a compact non-retail demand candidate with direct model-selection precedent. Missingness and genuine zero demand must be kept distinct during intermittency classification.

Primary source: [arXiv record](https://arxiv.org/abs/1908.08489).

### A2D-012 — Los Angeles transport-network forecasting

**Source:** Julien Monteil et al. (2019), *On model selection for scalable time series forecasting in transport networks*.

**Dataset:** traffic-speed observations supplied by The Weather Company.

| Property | Extracted detail |
|---|---|
| Initial road segments | 1,220 |
| Retained segments | 1,098 after removing series with at least 20% missingness |
| Period | 14 weeks in 2018 |
| Frequency | 15 minutes |
| Split | 12 training weeks, 1 validation week, 1 test week |
| Horizon | Up to 3 hours, or 12 steps |
| Context | Road graph, time of day and day of week; weather and road type were also tested |

The authors explicitly state that they do not have permission to share the dataset.

**Decision:** evidence only; reject as project data because the reported corpus cannot support reproducible evaluation.

Primary source: [arXiv record](https://arxiv.org/abs/1911.13042).

### A2D-013 — Clinical adaptive model selection

**Source:** Zitao Liu and Milos Hauskrecht (2017), CIKM. DOI: 10.1145/3132847.3132859.

**Dataset:** electronic health records for 500 post-surgical cardiac patients.

Each patient contributes six Complete Blood Count laboratory time series: MCHC, MCH, MCV, MPV, RBC and RDW. The framework adaptively switches between population, patient-specific and short-term individualised models, using dynamic linear and Gaussian-process variants.

**Decision:** strong evidence that instance-level adaptive model selection matters in healthcare, but no public release route was established. Do not include in the reproducible corpus.

Primary source: [PubMed record](https://pubmed.ncbi.nlm.nih.gov/29296289/).

### A2D-014 — FluSight and COVID-19 Forecast Hub data

**Source:** *Mind the Baseline: The Hidden Impact of Reference Model Selection on Forecast Assessment* and its public processing artefact.

**Datasets:** weekly US influenza and COVID-19 hospitalisation forecasts and ground truth.

The influenza component covers:

- 86 unique forecast models;
- 110 forecast dates;
- all 50 US states, Washington DC and national targets;
- complete seasons 2021/22–2023/24 and an incomplete 2024/25 season;
- quantile forecasts across locations and horizons.

**Decision:** promising for calibration methodology and baseline-sensitivity analysis. It is a forecast archive rather than a ready-made target-series benchmark, so a reproducible transformation specification is required before selection.

Primary sources: [study](https://www.medrxiv.org/content/10.1101/2025.08.01.25332807v1.full) and [data artefact](https://datacompass.lshtm.ac.uk/id/eprint/4747/).

### A2D-015 — Alibaba Cluster Trace and vmCloud

**Source:** *SpectraNet: a lightweight hybrid time–frequency deep learning framework for sustainable cloud workload forecasting* (2025), *Journal of Cloud Computing*. DOI: 10.1186/s13677-025-00815-z.

| Dataset | Extracted detail |
|---|---|
| Alibaba Cluster Trace 2018 v2 | More than 4,000 machines over eight days; CPU, memory, network and disk activity plus container/job metadata |
| vmCloud | Approximately two million timestamped VM observations; CPU, memory, network traffic, execution time, instruction count, power, energy efficiency and task metadata |

**Decision:** Alibaba is a credible reserve cloud-domain source with an official public repository, but its size requires a prespecified subset. vmCloud remains provisional until its authoritative provenance and licence are verified.

Primary source: [DOI](https://doi.org/10.1186/s13677-025-00815-z).

## 3. Consolidated dataset decision matrix

| Dataset | Domain | Direct selection/routing precedent | Public/reproducible status | Primary role now | Main unresolved risk |
|---|---|---:|---|---|---|
| GIFT-Eval | Seven domains | Yes, TSFM routing systems | Public benchmark | Primary comparability benchmark | Per-checkpoint leakage applies only to the declared benchmark setup |
| M5 | Retail demand | Yes: CARFS and FAME | Public competition route | Retail/intermittency comparator | Saturated prior use; model-training overlap; competition terms |
| Favorita | Grocery demand | Yes: Zhang, CARFS, FAME | Public competition route | Sparse-demand comparator | Cannot support routing novelty by itself |
| Car Parts | Spare parts | Classical intermittent-demand studies | Public archive representations | Compact intermittency anchor | Short histories; training overlap |
| NN5 | ATM cash demand | Yes: meta-learning selector | Public competition/archive | Compact non-retail demand candidate | Zeros versus missing observations |
| Ausgrid | Energy/prosumption | Yes: per-building value-oriented selector | Public upstream source | Preferred held-out energy candidate | Upstream licence and checkpoint overlap |
| AutoForecast corpus | Multi-domain | Yes | Released by authors | Candidate generator/meta-feature source | Mixed upstream provenance and small per-dataset counts |
| M1/M3/M4 | Multiple/economic | Yes: FFORMPP and related work | Public competition archives | Frequency/control comparators | M4 daily construction quality; extensive pretraining exposure |
| Alibaba 2018 | Cloud operations | Model benchmarking rather than per-series routing | Official public repository | Reserve held-out cloud candidate | Size, preprocessing, possible TSFM training overlap |
| CDC FluSight / COVID hubs | Healthcare | Baseline/ensemble evaluation | Public repositories | Calibration-method reserve | Requires transformation into router-ready instances |
| SNBC | Vending-machine demand | Yes: FAME | Confidential | Evidence only | Not shareable |
| LA traffic speed | Transport | Yes: model selection/comparison | Not shareable by cited authors | Evidence only | Reproducibility failure |
| Cardiac CBC EHR | Healthcare | Yes: adaptive switching | No public release established | Evidence only | Privacy and access |

## 4. Consequences for the experimental design

### 4.1 What can still be claimed

The evidence supports investigation of:

- a calibrated probability of **routing correctness**, not merely a softmax routing weight;
- explicit reliability diagrams, expected calibration error, Brier score and risk–coverage curves;
- routing between foundation models and classical/intermittent-demand fallbacks;
- near-tie handling that prefers the cheaper model;
- per-series regret relative to an oracle;
- leave-one-dataset-out and leave-one-domain-out evaluation;
- model–dataset leakage matrices rather than a model-only “clean” label;
- measured inference cost on declared hardware.

### 4.2 What should not be claimed

The public evidence does not support claims that:

- per-series forecasting-model routing is new;
- combining classical, machine-learning and deep experts is new;
- M5 or Favorita provides a novel routing testbed;
- a benchmark-level “no leakage” flag proves cleanliness on external datasets;
- a wrapper repository licence automatically covers every upstream dataset;
- confidential industrial data can be reproduced or redistributed.

### 4.3 Proposed corpus architecture after this pass

The current evidence supports a three-part structure, still subject to licence, overlap, compute and approval gates:

1. **Comparability layer:** GIFT-Eval configurations with checkpoint-specific leakage declarations.
2. **Intermittency layer:** Car Parts plus carefully specified M5/Favorita/NN5 subsets.
3. **Held-out-field layer:** Ausgrid as the leading energy candidate; Alibaba or public epidemiological data as reserves.

M5 and Favorita are retained because they allow comparison with current routing literature, not because they establish originality. Ausgrid is especially valuable because the article supplies an entity-level 200-building/100-building selector split, supporting a genuine held-out-instance design outside retail.

## 5. Quality controls and remaining gates

Before any candidate enters the experimental corpus, the following must be recorded:

1. authoritative upstream source and version;
2. licence, attribution and redistribution conditions;
3. exact series/entity definition;
4. temporal split and forecast horizon;
5. missing-value and zero-demand treatment;
6. exogenous-variable availability;
7. checkpoint-specific training-overlap status;
8. memory, storage and runtime estimate on the project hardware;
9. published baseline and metric compatibility;
10. proposal and ethics approval status.

No dataset download or model execution is authorised by this research record.

## 6. Current priority order

1. Verify Ausgrid's authoritative release terms and model-training overlap.
2. Freeze a reproducible NN5 version and distinguish missing observations from zero withdrawals.
3. Audit the exact M5 and Favorita subsets used by the three direct routing studies.
4. Inspect the AutoForecast corpus manifest for public, multi-series, licence-clear candidates.
5. Verify Alibaba preprocessing and select a bounded machine-level subset only if the energy candidate is insufficient.
6. Keep private clinical, transport and industrial datasets as problem evidence only.

## 7. References and access links

- Zhang, Q. (2025). [*Intelligent Routing for Sparse Demand Forecasting*](https://arxiv.org/abs/2506.14810).
- Li, Q. et al. (2026). [*FAME: Forecastability-Aware Mixture of Experts for Heterogeneous Time Series Forecasting*](https://arxiv.org/abs/2606.08896).
- Ganzevoort, R. C. and van Vuuren, J. H. (2023). [*A two-phased cluster-based approach towards ranked forecast-model selection*](https://doi.org/10.1016/j.mlwa.2023.100482).
- Talagala, T. S., Li, F. and Kang, Y. (2022). [*FFORMPP: Feature-based forecast model performance prediction*](https://doi.org/10.1016/j.ijforecast.2021.07.002).
- Abdallah, M. et al. [*Evaluation-Free Time-Series Forecasting Model Selection via Meta-Learning*](https://engineering.purdue.edu/dcsl/wp-content/uploads/2025/02/AutoForecast_ACM_TKDD.pdf).
- Garred, W., Oger, R. and Lauras, M. (2026). [*Automatic demand forecast model selection in supply chains*](https://www.tandfonline.com/doi/full/10.1080/00207543.2026.2623194).
- Werling, D. et al. (2023). [*Automating Value-Oriented Forecast Model Selection by Meta-learning*](https://link.springer.com/chapter/10.1007/978-3-031-48649-4_6).
- Barak, S., Nasiri, M. and Rostamzadeh, M. (2019). [*Time series model selection with a meta-learning approach*](https://arxiv.org/abs/1908.08489).
- Monteil, J. et al. (2019). [*On model selection for scalable time series forecasting in transport networks*](https://arxiv.org/abs/1911.13042).
- Liu, Z. and Hauskrecht, M. (2017). [*A Personalized Predictive Framework for Multivariate Clinical Time Series via Adaptive Model Selection*](https://pubmed.ncbi.nlm.nih.gov/29296289/).
- Stapper, M. et al. [*Mind the Baseline*](https://www.medrxiv.org/content/10.1101/2025.08.01.25332807v1.full).
- [M5 competition article](https://www.sciencedirect.com/science/article/pii/S0169207021001187).
- [Car Parts intermittent-demand article](https://www.sciencedirect.com/science/article/pii/S0169207011000781).
- [SpectraNet / Alibaba and vmCloud evaluation](https://doi.org/10.1186/s13677-025-00815-z).
