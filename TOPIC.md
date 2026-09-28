# Working topic

Selected: 2026-09-28. This is the working centre of the project. It is not yet an approved ARMS proposal, and it is not assessed writing.

## Working title

**When to Trust a Time-Series Foundation Model: A Per-Series Reliability Framework for Routing Between TSFMs and Classical Forecasters**

## Problem

Current time-series foundation model benchmarks report accuracy at dataset level. They do not tell a practitioner which individual series a foundation model will forecast reliably, and which series should stay with a classical forecaster.

The published evidence is mixed. Foundation models often fail to beat smaller specialised models or strong simple baselines. On some domains and with some checkpoints, zero-shot foundation models are among the strongest available forecasts. The open question is how to make that choice before committing to an expensive model, and how to attach a confidence score that matches how often the choice is actually right.

## Aim

Design, implement, and evaluate a reproducible per-series reliability router. Given a time series, the router decides whether a time-series foundation model or a classical fallback should produce the forecast, and it reports a calibrated confidence for that decision.

## Research questions

1. Which measurable series characteristics predict whether a time-series foundation model outperforms a classical baseline on that series?
2. Can a lightweight meta-learner, using those characteristics, route between a foundation model and a classical fallback so that routed accuracy matches or exceeds the best single model at a lower inference cost?
3. Can the router emit a calibrated reliability score, so that when it says to trust the foundation model, the foundation model wins at the promised rate?

## Artefact

A small, testable forecasting toolkit:

- a fixed model pool with one shared forecasting interface;
- a per-series feature table;
- a router that selects foundation model, classical fallback, or a stated ensemble rule;
- a calibration report for the router's confidence;
- a cost record in wall-clock time and a stated compute measure;
- tests, a command-line entry point, and a reproducibility note.

The artefact is the router and the evaluation protocol around it. Training a new foundation model is outside the project.

## Method

Three stages. Each stage must be able to stand as a result even if the next stage is weaker than hoped.

### Stage 1. Characterisation corpus

Run a frozen model pool in zero-shot or pretrained mode across a public general forecasting benchmark, with one or two intermittency-heavy collections only if that scope is confirmed before the pool is frozen.

- Foundation models: two or three open checkpoints, chosen from Chronos, TimesFM, MOIRAI, and TinyTimeMixer after a local smoke test.
- Classical baselines: Seasonal Naive, ETS, ARIMA, and Theta.
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

## Evaluation

- Point accuracy: MASE and sMAPE per series.
- Routing quality: routing accuracy and regret against an oracle selector that already knows the winner.
- Calibration: calibration error of the reliability score.
- Cost: cost per forecast.
- Validation: rolling-origin evaluation only, with an explicit check for training-data overlap and test leakage.
- Ablations: feature groups; foundation-model pool size of one, two, and three; results stratified by domain.
- Sanity check: a simple context-parroting baseline as an extra arm, so a foundation model is not credited for a pattern a trivial rule already captures.

## What is in scope

- Public benchmarks and open model checkpoints.
- CPU or single-machine inference.
- A router whose failure is informative: if the foundation model wins on most series and loses badly on a minority, detecting that minority is a valid result.

## What is out of scope until a later, separate decision

- Training a new foundation model.
- Parameter-efficient fine-tuning as a required stage.
- Federated learning, quantum machine learning, and construction-domain text analytics.
- Any claim that a foundation model is generally better, or that a router is useful, before the comparisons above are run.

## Decisions still open

- Whether intermittent-demand series stay in the Stage 1 corpus.
- The exact checkpoint list, frozen only after a smoke test on the available machine.
- Supervisor assignment, the module brief, the marking rubric, the word budget, and the deadline.

## Hard stops

Do not download a research dataset, run model experiments, or start artefact development until the proposal and ethics gates required by the module are recorded. Do not draft assessed report sections until the deliverables, structure, and word budget are confirmed.
