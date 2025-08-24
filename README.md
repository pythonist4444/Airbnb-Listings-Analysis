# Airbnb Listings in Paris - Quick EDA

This repository contains a quick exploratory analysis of Airbnb listings in Paris.

## Overview
- **Dataset:** `listings.csv`
- **Analysis:** Filtering for Paris, calculating average prices, most expensive neighbourhood, and trends over time.
- ## ⚙️ Tech Stack

| Tool |  |
|------|------|
| Python | ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white) |
| Pandas | ![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat&logo=pandas&logoColor=white) |
| Matplotlib | ![Matplotlib](https://img.shields.io/badge/-Matplotlib-11557C?style=flat&logo=matplotlib&logoColor=white) |
| Seaborn | ![Seaborn](https://img.shields.io/badge/-Seaborn-8CAAE6?style=flat&logo=seaborn&logoColor=white) |
| ydata_profiling | ![ydata_profiling](https://img.shields.io/badge/-ydata_profiling-FF7F50?style=flat) |

---

## Contents
- `eda.py` — Python script performing data loading, cleaning, EDA, and visualizations.
- `report.html` — ydata_profiling report for quick EDA.
- `visuals/` — PNGs of charts:
  - Average price by neighbourhood
  - Average price by accommodates in the most expensive neighbourhood
  - Count of new hosts & average price over time

## 🖥️ Visuals

**Average Price by Neighbourhood**  
![avg_price_by_neighbourhood](https://github.com/pythonist4444/Airbnb-Listings-Analysis/blob/f617272e3ad57e145c217d348feb71ac197b04ea/Avg%20Price%20by%20Neighbourhoods.png)  

**Average Price by Accommodates (Most Expensive Neighbourhood)**  
![avg_price_by_accommodates](https://github.com/pythonist4444/Airbnb-Listings-Analysis/blob/f617272e3ad57e145c217d348feb71ac197b04ea/Avg%20Price%20by%20no%20of%20Accommodates.png)  

**Listings Over Time: Count of New Hosts & Average Price**  
![listings_over_time](https://github.com/pythonist4444/Airbnb-Listings-Analysis/blob/f617272e3ad57e145c217d348feb71ac197b04ea/Listings%20overtime.png)  


## Usage
1. Clone the repo
2. Run `eda.py` (requires Python 3.x, Pandas, Matplotlib, Seaborn, ydata_profiling)
3. Explore `report.html` for a detailed profiling summary





