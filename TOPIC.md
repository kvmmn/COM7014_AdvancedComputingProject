# Working topic

Current path since 2026-09-28. This follows the initial proposal draft. It is the plan to take into supervisor meetings. It is not an approved ARMS proposal, and it is not assessed writing.

## Working title

**When to Trust a Time-Series Foundation Model: A Per-Series Reliability Framework for Routing Between Foundation Models and Classical Forecasting Models**

This is the title held by the university ethics system. Intermittent demand stays in the research questions and method below. It is not repeated in the title.

## Problem

Current time-series foundation model benchmarks report accuracy at dataset level. They do not tell a practitioner which individual series a foundation model will forecast reliably, and which series should stay with a classical forecaster.

The published evidence is mixed. Foundation models often fail to beat smaller specialised models or strong simple baselines. On some domains and with some checkpoints, zero-shot foundation models are among the strongest available forecasts. The open question is how to make that choice before committing to an expensive model, and how to attach a confidence score that matches how often the choice is actually right.

Intermittent demand is part of that question. Sparse series are where classical methods such as Croston, SBA, and TSB are the usual fallback, and where a foundation model is most likely to be the wrong default.

## Aim

Design, implement, and evaluate a reproducible per-series reliability router. Given a time series, the router decides whether a time-series foundation model or a classical fallback should produce the forecast, and it reports a calibrated confidence for that decision. On intermittent series, the fallback includes the classical intermittent-demand methods.

## Research questions

1. Which measurable series characteristics predict whether a time-series foundation model outperforms a classical baseline on that series? The characteristics include seasonality strength, intermittency, length, non-stationarity, trend curvature, spectral entropy, and the presence of exogenous variables.
2. Can a lightweight meta-learner, using those characteristics, route between a foundation model and a classical fallback so that routed accuracy matches or exceeds the best single model at a lower inference cost?
3. Can the router emit a calibrated reliability score, so that when it says to trust the foundation model, the foundation model wins at the promised rate?
4. On intermittent series, do Croston, SBA, and TSB remain the appropriate fallback when the pool also contains strong zero-shot foundation models, and can the router identify that subset in advance?

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

- Foundation models: two or three open checkpoints, chosen from Chronos, TimesFM, MOIRAI, and TinyTimeMixer after a local smoke test.
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

Calibrate the router's confidence. Report reliability diagrams and coverage. Report inference cost so any claim of the form "use the foundation model only when reliability exceeds a threshold" is tied to a measured cost, not only to accuracy.

### Intermittent demand

Stratify the results by intermittency class. Test whether the router sends intermittent series to Croston, SBA, or TSB, and whether that choice is more reliable than sending them to a foundation model. This uses the Stage 1 corpus. It does not add a second project.

## Evaluation

- Point accuracy: MASE and sMAPE per series.
- Routing quality: routing accuracy and regret against an oracle selector that already knows the winner.
- Calibration: calibration error of the reliability score.
- Cost: cost per forecast.
- Intermittency: results split by intermittency class, including whether the classical intermittent methods remain the better fallback.
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

## Decisions still open

These stay open for the supervisor. They do not reopen the choice of topic.

- The exact checkpoint list, frozen only after a smoke test on the available machine.
- Which public intermittent collections join the main benchmark.
- The module brief, the marking rubric, the word budget, and the deadline.

## Hard stops

Do not download a research dataset, run model experiments, or start artefact development until the proposal and ethics gates required by the module are recorded. Do not draft assessed report sections until the deliverables, structure, and word budget are confirmed.
