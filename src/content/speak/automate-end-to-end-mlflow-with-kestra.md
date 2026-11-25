---
title: 'Automate end to end MLflow with Kestra and MLflow'
date: '2024-11-09'
kind: workshop
event: 'PyDay BCN 2024'
location: 'Barcelona, Spain'
eventUrl: 'https://pybcn.org/talks/pyday_bcn_2024/automate-end-to-end-mlflow-with-kestra-and-mlflow/'
image: '/images/automate-end-to-end-mlflow-with-kestra/pyday-bcn-2024-workshop.webp'
tags:
  - MLOps
  - Orchestration
  - Kestra
  - MLflow
  - Python
related:
  - writing/orchestration-without-the-bloat
description: 'A 75-minute hands-on workshop building an end-to-end machine learning pipeline with Kestra for orchestration and MLflow for experiment tracking, using a Kaggle competition as the use case.'
---

A hands-on workshop at [PyDay BCN 2024](https://pybcn.org/events/pyday_bcn/pyday_bcn_2024/), run in English as part of the data engineering track.

![Manuel presenting the workshop notebook on a projector while attendees follow along on their laptops](/images/automate-end-to-end-mlflow-with-kestra/pyday-bcn-2024-workshop.webp)
_Photo: [PyBCN](https://pybcn.org/events/pyday_bcn/pyday_bcn_2024/)_

## What we built

An end-to-end machine learning pipeline around a Kaggle competition, covering the whole loop:

1. Download the competition dataset from Kaggle.
2. Explore and process the data.
3. Train several models with different algorithms.
4. Run inference on the submission samples.
5. Upload the results back to Kaggle automatically.

## Tools

- **[Kestra](https://kestra.io)**: an orchestration platform, used to chain the pipeline steps together.
- **[MLflow](https://mlflow.org)**: tracks experiments, parameters, and models across the ML lifecycle.

The workshop introduced the basics of both.
