---
title: 'TemporalSeries'
date: '2026-11-25'
category: engineering
tags:
  - Rust
  - Time Series
  - Quantitative Analysis
description: 'A high-performance Rust library for quantitative time-series analysis: returns, moving averages, volatility, autocorrelation, and statistical tests.'
repoUrl: 'https://github.com/MGijon/TemporalSeries'
liveUrl: 'https://docs.rs/temporalseries'
related:
  - writing/building-a-time-series-engine-in-rust
# Set to true to hide this project everywhere on the site (lists, pages, related links, sitemap).
draft: false
---

TemporalSeries is a Rust library for quantitative time-series analysis. It is published as the [`temporalseries`](https://docs.rs/temporalseries) crate under the MIT license.

## Data structures

- **`TimeSeries`**: an `i64` timestamp index paired with `f64` values.
- **`TemporalSeries<T, B>`**: a generic series over a pluggable storage backend: columnar, row-based, or chunked.
- **`Panel`**: several named series on a shared index, with analytics applied column by column.

## Analytics

- **Statistics**: mean, standard deviation, quantiles, IQR, skewness, excess kurtosis.
- **Returns**: simple, log, and cumulative returns; `diff`, `pct_change`, `shift`.
- **Moving averages**: simple and exponential moving averages, crossover signals.
- **Volatility**: rolling standard deviation, true range, average true range, Bollinger bands.
- **Autocorrelation**: ACF and PACF (Levinson–Durbin).
- **Statistical tests**: augmented Dickey–Fuller (stationarity) and Jarque–Bera (normality).

## Design notes

Fallible operations return a `Result` with a typed error instead of panicking. Positions that can't produce a value are filled with `NaN` rather than truncated, so the output keeps the input's length and stays aligned with the index. Timestamps are always stored as `i64`, and an optional `chrono` feature converts to and from `DateTime` values with a configurable time unit.

The library is benchmarked with Criterion, and its tests and coverage run in CI.
