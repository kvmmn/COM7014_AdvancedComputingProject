# Working topic

Current path since 2026-09-28. Revised on 2026-10-08 after the dataset discovery and the related-work review. It is the plan to take into supervisor meetings. It is not an approved ARMS proposal, and it is not assessed writing.

## Working title

**When to Trust a Time-Series Foundation Model: A Per-Series Reliability Framework for Routing Between Foundation Models and Classical Forecasting Models**

This is the title held by the university ethics system. It is provisional until M1 closes (D-019). The supervisor confirmed the title may be modified and improved after M1. Intermittent demand stays in the research questions and method below. It is not repeated in the title.

## Problem

Current time-series foundation model benchmarks report accuracy at dataset level. They do not tell a practitioner which individual series a foundation model will forecast reliably, and which series should stay with a classical forecaster.

The published evidence is mixed. Foundation models often fail to beat smaller specialised models or strong simple baselines. On some domains and with some checkpoints, zero-shot foundation models are among the strongest available forecasts. The open question is how to make that choice before committing to an expensive model, and how to attach a confidence score that matches how often the choice is actually right.

Intermittent demand is part of that question. Sparse series are where classical methods such as Croston, SBA, and TSB are the usual fallback, and where a foundation model is most likely to be the wrong default. A 2026 systematic review (Rubczynski 2026) already establishes that foundation models lose badly on intermittent retail demand: on the M5 competition data, a foundation model posts 0.97 wrmsse against a competition-grade LightGBM at 0.52. The project does not re-establish that finding. It asks whether a router can detect the intermittent subset in advance and route it to the classical fallback.

## What is already done in this space

Routing between forecasting models is not a new idea, and the project does not claim it is. The related-work review on 2026-10-08 found that several systems already route or select among foundation models on the GIFT-Eval benchmark:

- **TimeRouter** (Ning et al. 2026) routes between four frozen foundation models with one-vs-all XGBoost classifiers, a selective gate, and an ensemble fallback. It reports LB MASE 0.6765, a GIFT-Eval state of the art.
- **TSOrchestra**, **MoiraiAgent**, and **TimeCopilot** use fine-tuned or prompted language models to select or weight foundation models.
- **Synapse** and **ZooCast** arbitrate or match among foundation models without a language model.

Every one of these systems routes **within a pool of foundation models**. None of them includes a classical statistical fallback, an intermittent-demand method, a calibrated probability of the routing decision being correct, per-series regret against an oracle, or full cost accounting.

The calibration point is specific. Verma and Nalisnick (2022) show that one-vs-all classifiers produce **calibrated probabilities of expert correctness**, evaluated with reliability diagrams and expected calibration error. TimeRouter adopts the one-vs-all structure but uses the scores only as a threshold gate, and does not report calibration. The property the structure was designed to provide is left unused.

## Aim

Design, implement, and evaluate a reproducible per-series reliability router. Given a time series, the router decides whether a time-series foundation model or a classical fallback should produce the forecast, and it reports a calibrated confidence for that decision. On intermittent series, the fallback includes the classical intermittent-demand methods.

## Contribution

The project does not claim to be the first to route between forecasting models. Its contribution is narrower:

1. **Cross-family routing.** Route between a foundation-model pool and a classical fallback family, including intermittent-demand methods, rather than within a foundation-model pool.
2. **Calibrated reliability.** Deliver the calibrated probability of routing correctness that the one-vs-all structure was designed for, with reliability diagrams, expected calibration error, and coverage.
3. **Intermittent demand.** Test whether Croston, SBA, and TSB remain the better fallback on sparse series, and whether the router identifies that subset in advance.
4. **Regret and cost.** Report per-series regret against an oracle selector and a full cost accounting, not only aggregate accuracy.

The project does not claim to beat TimeRouter on aggregate MASE. The contribution is the reliability and fallback dimension.

## Research questions

1. Which measurable series characteristics predict whether a time-series foundation model outperforms a classical baseline on that series? The characteristics include seasonality strength, intermittency, length, non-stationarity, trend curvature, spectral entropy, and the presence of exogenous variables.
2. Can a lightweight meta-learner, using those characteristics, route between a foundation model and a classical fallback so that routed accuracy matches or exceeds the best single model at a lower inference cost?
3. Can the router emit a calibrated reliability score, so that when it says to trust the foundation model, the foundation model wins at the promised rate?
4. Can a per-series router identify the intermittent subset in advance and route it to the classical fallback, and does that routing recover the accuracy that a single foundation model loses on intermittent series? The premise that classical and tree baselines beat foundation models on intermittent demand is already established (Rubczynski 2026). The open question is whether the router can detect and act on it per series.

## Artefact

A small, testable forecasting toolkit:

- a fixed model pool with one shared forecasting interface;
- a per-series feature table;
- a router that selects a foundation model or a classical fallback;
- a separate intermittent-demand baseline family for sparse series;
- a calibration report for the router's confidence;
- a cost record in wall-clock time and a stated compute measure;
- tests, a command-line entry point, and a reproducibility note.

The artefact is the router and the evaluation protocol around it. Training a new foundation model is outside the project.

## Method

Three stages, plus the intermittent-demand analysis on the same corpus. Each stage must be able to stand as a result even if the next stage is weaker than hoped.

### Stage 1. Characterisation corpus

Run a frozen model pool in zero-shot or pretrained mode across a public general forecasting benchmark and one or two intermittency-heavy collections.

- Foundation models: two or three open checkpoints from the leakage-clean set. The dataset discovery on 2026-10-07 and 2026-10-08 found that Chronos T5, TimesFM 1.0 and 2.0, and TinyTimeMixer R1 and R2 are flagged as leaking test data on GIFT-Eval. The clean checkpoints are Chronos-2, TimesFM-2.5, and the MOIRAI family. The final list is frozen after a local smoke test.
- General classical baselines: Seasonal Naive, ETS, ARIMA, and Theta.
- Intermittent-demand baselines: Croston, SBA, and TSB.
- Record per-series error and a small set of static series features, including seasonality strength, intermittency, length, and non-stationarity.

Inference only. No full fine-tuning on the critical path.

### Stage 2. Router

Train a lightweight meta-learner on the tabular series features to predict the per-series winner.

Compare it with:

- a pre-foundation-model meta-learning selector in the FFORMS line;
- always using the foundation model;
- always using the classical fallback;
- a naive rule such as selection by series length.

### Stage 3. Calibration and cost

Calibrate the router's confidence using the one-vs-all approach of Verma and Nalisnick (2022). Report reliability diagrams, expected calibration error, and coverage. Report inference cost so any claim of the form "use the foundation model only when reliability exceeds a threshold" is tied to a measured cost, not only to accuracy.

### Intermittent demand

Stratify the results by intermittency class. Test whether the router detects intermittent series in advance and sends them to Croston, SBA, or TSB, and whether that routing recovers the accuracy a single foundation model loses on those series. The premise that classical and tree baselines beat foundation models on intermittent demand is already established (Rubczynski 2026). This uses the Stage 1 corpus. It does not add a second project.

## Evaluation

- Point accuracy: MASE and sMAPE per series.
- Routing quality: routing accuracy and regret against an oracle selector that already knows the winner.
- Calibration: expected calibration error, reliability diagrams, and coverage of the reliability score.
- Cost: cost per forecast, including foundation-model forward passes.
- Intermittency: results split by intermittency class, including whether the router detects and routes the intermittent subset, and whether that routing recovers the accuracy a single foundation model loses.
- Validation: rolling-origin evaluation only, with an explicit check for training-data overlap and test leakage.
- Ablations: feature groups; foundation-model pool size of one, two, and three; results stratified by domain.
- Sanity check: a simple context-parroting baseline as an extra arm, so a foundation model is not credited for a pattern a trivial rule already captures.

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

- The exact checkpoint list, frozen only after a smoke test on the available machine. The clean set is Chronos-2, TimesFM-2.5, and MOIRAI.
- Which public intermittent collections join the main benchmark. Dataset selection follows the scientific protocol in `PROJECT_BRAIN/PRIVATE/DATASET_DISCOVERY_PROTOCOL.md` (D-017).
- The module brief, the marking rubric, the word budget, and the deadline. The supervisor required the student to check the deadline and official constraints and report back (S-002).

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
