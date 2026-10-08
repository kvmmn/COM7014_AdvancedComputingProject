# Working topic

Current path since 2026-09-28. Revised on 2026-10-08 after the dataset discovery, the related-work review and the article-to-dataset extraction. It is the plan to take into supervisor meetings. It is not an approved ARMS proposal, and it is not assessed writing.

## Working title

**When to Trust a Time-Series Foundation Model: A Per-Series Reliability Framework for Routing Between Foundation Models and Classical Forecasting Models**

This is the title held by the university ethics system. It is provisional until M1 closes (D-019). The supervisor confirmed the title may be modified and improved after M1. Intermittent demand stays in the research questions and method below. It is not repeated in the title.

## Problem

Current time-series foundation model benchmarks report accuracy at dataset level. They do not tell a practitioner which individual series a foundation model will forecast reliably, and which series should stay with a classical forecaster.

The published evidence is mixed. Foundation models often fail to beat smaller specialised models or strong simple baselines. On some domains and with some checkpoints, zero-shot foundation models are among the strongest available forecasts. The open question is how to make that choice before committing to an expensive model, and how to attach a confidence score that matches how often the choice is actually right.

Intermittent demand is part of that question. Sparse series are where classical methods such as Croston, SBA and TSB are the usual fallback, and where a foundation model is most likely to be the wrong default. A 2026 systematic review and meta-analysis of retail forecasting (Rubczynski 2026) finds an overall foundation-model advantage across 543 comparisons, but not on intermittent demand: on the M5 data, the reported foundation-model WRMSSE is 0.97 against 0.52 for a competition-grade LightGBM. The project does not re-establish that finding. It asks whether a router can detect the intermittent subset in advance and route it to the classical fallback.

## What is already done in this space

Routing between forecasting models is not a new idea, and the project does not claim it is. The related-work review and the article-to-dataset extraction on 2026-10-08 found three groups of prior work:

- **Feature-based selection among classical methods.** FFORMS, FFORMA and FFORMPP predict which classical method, or which combination, will perform best on a series from its features.
- **Routing within a foundation-model pool.** TimeRouter (Ning et al. 2026) routes between four frozen foundation models with one-vs-all XGBoost classifiers, a selective gate and an ensemble fallback, and reports a GIFT-Eval state of the art. TW3Cast, TSOrchestra, MoiraiAgent, TimeCopilot, Synapse and ZooCast also select or weight foundation models or their configurations.
- **Cross-family routing.** Zhang (2025) routes individual Favorita series among classical, machine-learning and deep-learning experts. CARFS (2023) learns a ranked model shortlist on M5 and applies it to Favorita. FAME (2026, preprint) performs cost-aware sparse expert routing on M5 and Favorita and calls Chronos for only 8.6% and 10.9% of series.

Per-series routing, cross-family routing, cost-aware routing and intermittent-demand routing therefore all exist. What none of these studies reports is whether the router's confidence is **calibrated**, whether a threshold on that confidence keeps error at a promised level, and whether the confidence still holds on a **field the router was not trained on**.

The calibration point is specific. Verma and Nalisnick (2022) show that one-vs-all classifiers produce calibrated probabilities of expert correctness, evaluated with reliability diagrams and expected calibration error. TimeRouter adopts the one-vs-all structure but uses the scores only as a threshold gate and does not report calibration.

## Aim

Design, implement and evaluate a reproducible per-series router that gives, for each series, a calibrated probability that trusting a time-series foundation model is the right choice, and that falls back to a classical forecaster when that probability is too low. On demand series, the fallback includes the classical intermittent-demand methods.

## Contribution

The project does not claim to be the first to route between forecasting models, or the first to route across model families. Its contribution is narrower:

1. **Calibrated trust.** A probability that the routing choice is correct, checked with reliability diagrams, expected calibration error and Brier score.
2. **Explicit deferral.** The router defers to the classical fallback whenever its probability falls below a threshold. The threshold is fixed on validation data to meet a target error rate, and the test is whether that target still holds on unseen data (risk–coverage curves). This is what separates the project from plain routing.
3. **Transfer.** Leave-one-dataset-out evaluation and a held-out field (Ausgrid energy data), so the trust probability is tested outside the data the router learned from.
4. **Regret and cost.** Per-series regret against an oracle selector and measured inference cost, not only aggregate accuracy.

The project does not claim to beat TimeRouter, FAME or other routing systems on aggregate accuracy. The contribution is the reliability, deferral and transfer dimension.

## Research questions

**Main question.** Can a per-series router give a calibrated probability that trusting a time-series foundation model is the right choice, and does that probability still hold on datasets and fields it was not trained on?

1. **Signals.** Which measurable series characteristics predict whether a foundation model outperforms a classical baseline on that series? Candidates include seasonal strength, trend, intermittency, length, non-stationarity, spectral entropy and the presence of exogenous variables. *Refuted if* feature-based prediction does no better than always predicting the majority outcome under held-out-dataset evaluation.
2. **Value.** Can routing match or beat the best single model at lower inference cost? *Refuted if* always-FM or always-classical matches or beats the router on error at equal or lower measured cost.
3. **Trust (central).** Is the router's trust probability calibrated, including on a held-out field? *Refuted if* held-out calibration error exceeds a pre-declared bound, or if error does not fall as coverage is reduced.
4. **Sparse demand.** Can the router identify intermittent series in advance and send them to the classical fallback? The premise that classical and tree baselines beat foundation models on intermittent demand is already established (Rubczynski 2026). *Refuted if* the learned router does no better than the fixed Syntetos–Boylan rule, evaluated on demand series only.

## Artefact

A small, testable forecasting toolkit:

- a fixed model pool with one shared forecasting interface;
- a per-series feature table;
- a router that selects a foundation model or a classical fallback;
- a separate intermittent-demand baseline family for sparse series;
- a calibration report for the router's confidence, with the deferral threshold and risk–coverage curves;
- a cost record in wall-clock time and a stated compute measure;
- tests, a command-line entry point, and a reproducibility note.

The artefact is the router and the evaluation protocol around it. Training a new foundation model is outside the project.

## Method

Three stages, plus the intermittent-demand analysis on the same corpus. Each stage must be able to stand as a result even if the next stage is weaker than hoped.

### Corpus

Each dataset has one job. The design is provisional until licence, provenance, overlap and feasibility checks pass. Details are in [`research/dataset-discovery-v2-scholar-article-extraction.md`](research/dataset-discovery-v2-scholar-article-extraction.md).

| Layer | Datasets | Job |
|---|---|---|
| 1 · Breadth | GIFT-Eval | Comparability with the benchmark literature; main router training data |
| 2 · Sparse demand | M5, Favorita, Car Parts, NN5 | Direct comparison with published routing studies (FAME, Zhang, CARFS, Barak) |
| 3 · Held-out field | Ausgrid | Energy field never seen in router training; entity-level split as in Werling et al. (2023) |
| Reserve | Alibaba, public epidemiological archives | Used only if access, duration and transformation gates pass |

Proposed common ground: every series is forecast as a univariate series at its native frequency; the router sees only scale-free features of the history; errors are scaled (MASE) so they can be pooled; horizons follow each dataset's published protocol. Covariates are outside the core comparison.

### Stage 1. Characterisation corpus

Run a frozen model pool in zero-shot or pretrained mode across the corpus.

- Foundation models: Chronos-2, TimesFM-2.5 and MOIRAI, provisionally. They carry no leakage flag on GIFT-Eval, but that flag does not cover other datasets, so every model–dataset pair needs its own overlap check. Chronos T5, TimesFM 1.0 and 2.0, and TinyTimeMixer R1 and R2 are excluded because they are flagged as leaking GIFT-Eval test data. The final list is frozen after a local smoke test.
- Classical fallback: Seasonal Naive, ETS, ARIMA and Theta, plus Croston, SBA and TSB on demand series.
- Record per-series error and a small set of static series features.

Inference only. No fine-tuning on the critical path.

### Stage 2. Router

Train a lightweight meta-learner on the tabular series features. The routing label is fixed before evaluation: a pre-declared primary metric and tie margin, with near-ties assigned to the cheaper model.

Compare it with these reference baselines, which are not part of the routing pool:

- always using the foundation model;
- always using the classical fallback;
- a pre-foundation-model selector in the FFORMS line;
- the fixed Syntetos–Boylan rule on demand series;
- a global LightGBM forecaster, the strongest reported M5 baseline.

### Stage 3. Calibration, deferral and cost

Calibrate the router's confidence with the one-vs-all approach of Verma and Nalisnick (2022); post-hoc calibration (Platt or isotonic) is an ablation. Set the deferral threshold on validation data and report risk–coverage curves on held-out data. Report inference cost so any claim of the form "use the foundation model only when confidence exceeds a threshold" is tied to measured cost.

### Intermittent demand

Stratify the demand-series results by Syntetos–Boylan class. Test whether the router detects intermittent series in advance and sends them to Croston, SBA or TSB, and whether that recovers the accuracy a single foundation model loses. This uses the same corpus. It does not add a second project.

## Evaluation

- Point accuracy: MASE per series. sMAPE only on strictly positive series.
- Distributional accuracy: CRPS or weighted quantile loss where models produce quantiles.
- Routing quality: routing accuracy and regret against an oracle selector.
- Calibration and deferral: expected calibration error, Brier score, reliability diagrams and risk–coverage curves.
- Cost: wall-clock inference per forecast on declared hardware.
- Validation: rolling-origin evaluation for forecasts; leave-one-dataset-out evaluation for the router. When Ausgrid is the test field, GIFT-Eval's energy datasets are removed from router training. Model–dataset pairs with uncertain overlap are excluded from headline results and reported separately.
- Feasibility: a smoke test on the project laptop sets a stratified subsample if the full corpus does not fit.
- Ablations: feature groups; foundation-model pool size of one, two and three; results by field.
- Sanity check: a simple context-parroting baseline, so a foundation model is not credited for a pattern a trivial rule already captures.

## What is in scope

- Public benchmarks and open model checkpoints.
- Intermittent-demand series and the Croston, SBA, and TSB baselines.
- CPU or single-machine inference.
- A router whose failure is informative: if the foundation model wins on most series and loses badly on a minority, detecting that minority is a valid result.

## What is out of scope until a later, separate decision

- Training a new foundation model.
- Parameter-efficient fine-tuning as a required stage.
- Inventory-cost simulation as a required result. The current question is whether the router chooses the better forecast, including on intermittent series.
- Federated learning, quantum machine learning, and construction-domain text analytics.
- Any claim that a foundation model is generally better, or that a router is useful, before the comparisons above are run.
- Any claim to beat TimeRouter or the other routing systems on aggregate benchmark accuracy.

## Decisions still open

These stay open for the supervisor. They do not reopen the choice of topic.

- The contribution: calibrated trust-or-defer, tested for transfer, as the distinction from FAME, Zhang, CARFS, TimeRouter and TW3Cast.
- The corpus layers and the univariate common ground above.
- The validation rules, including the energy-free router training set for the Ausgrid test.
- LightGBM as a required reference baseline outside the routing pool.
- Model licences, Kaggle terms and the upstream conditions of each added dataset.
- The exact checkpoint list, frozen only after a smoke test.
- A proposed title after M1: *When to Trust a Time-Series Foundation Model: Calibrated Per-Series Routing Between Foundation Models and Classical Forecasters*. Any change must also be made in the ethics system.
- The module brief, the marking rubric, the word budget and the deadline.

## Project staging

The supervisor set the phase model (D-018):

| Stage | Content |
|---|---|
| M1 | Topic field and quality, leading to the proposal. Includes scientific dataset discovery. |
| M2 | Models and evaluations, plus implementation. |
| M3 | Writing the project and the thesis. |

The proposal is rebuilt problem-first under M1 (D-016). The current draft is a starting reference only.

## Hard stops

Do not download a research dataset, run model experiments, or start artefact development until the proposal and ethics gates required by the module are recorded. Do not draft assessed report sections until the deliverables, structure, and word budget are confirmed.
