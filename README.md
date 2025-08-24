# Airbnb Listings in Paris - Quick EDA

This repository contains a quick exploratory analysis of Airbnb listings in Paris.

## Overview
- **Dataset:** `listings.csv`
- **Analysis:** Filtering for Paris, calculating average prices, most expensive neighbourhood, and trends over time.
- **Tools:** Python, Pandas, Seaborn, Matplotlib, ydata_profiling

## Contents
- `eda.py` — Python script performing data loading, cleaning, EDA, and visualizations.
- `report.html` — ydata_profiling report for quick EDA.
- `visuals/` — PNGs of charts:
  - Average price by neighbourhood
  - Average price by accommodates in the most expensive neighbourhood
  - Count of new hosts & average price over time

## Usage
1. Clone the repo
2. Run `eda.py` (requires Python 3.x, Pandas, Matplotlib, Seaborn, ydata_profiling)
3. Explore `report.html` for a detailed profiling summary
