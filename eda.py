# ===============================================
# Quick Sunday Analysis: Airbnb Listings in Paris
# ===============================================

# -----------------------------
# 1) Import Libraries
# -----------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from ydata_profiling import ProfileReport

sns.set(style="whitegrid", palette="muted", font_scale=1.1)

# -----------------------------
# 2) Load Data
# -----------------------------
# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the CSV file
csv_path = os.path.join(current_dir, 'Listings.csv')

# Read CSV, parse host_since as datetime
df = pd.read_csv(csv_path, encoding='latin-1', parse_dates=['host_since']) # Adjust encoding if necessary, parsing dates for automatic datetime conversion

# -----------------------------
# 3) Basic Inspection
# -----------------------------
print(df.head())
print(df.info())
print(df.describe(include='all'))

# -----------------------------
# 4) Optional: EDA using ydata_profiling
# -----------------------------
# Generates a quick profiling report (uncomment to use)
# profile = ProfileReport(df, title="Data Profiling Report", explorative=True)
# profile.to_file("report.html")

# -----------------------------
# 4) Filter for Paris and select relevant columns
# -----------------------------
relevant_columns = ['host_since', 'neighbourhood', 'accommodates', 'city', 'price']
df = df[df['city'] == 'Paris'][relevant_columns]

print(df.info())
print(df.describe())
print(df.isnull().sum())

# -----------------------------
# 5) Handle Missing Values
# -----------------------------
# Fill missing host_since with median (optional: could drop or impute differently based on context and analysis needs e.ge mean, mode, etc.)   
df['host_since'] = df['host_since'].fillna(df['host_since'].median())

# -----------------------------
# 6) Optional: EDA using ydata_profiling
# -----------------------------
# Generates a quick profiling report (uncomment to use)
# profile = ProfileReport(df, title="Data Profiling Report", explorative=True)
# profile.to_file("report.html")


# -----------------------------
# 7) Analysis: Most Expensive Neighbourhood
# -----------------------------
# Average price by neighbourhood
paris_listings_neighbourhood = df.groupby('neighbourhood')['price'].mean().sort_values(ascending=True)
print(paris_listings_neighbourhood)

# Identify most expensive neighbourhood
most_expensive_neighbourhood = paris_listings_neighbourhood.idxmax()

# Filter data for the most expensive neighbourhood
df_most_expensive = df[df['neighbourhood'] == most_expensive_neighbourhood]

# Average price by number of accommodates in that neighbourhood
paris_listings_accommodations = (
    df_most_expensive.groupby('accommodates')['price']
    .mean()
    .sort_values(ascending=True)
)
print(paris_listings_accommodations)

# -----------------------------
# 8) Time Series Analysis: Listings Over Time
# -----------------------------
# Resample by year to get count of new hosts and average price
paris_listings_overtime = (
    df.set_index('host_since')
      .resample('Y')
      .agg({'neighbourhood': 'count', 'price': 'mean'})
)

# Replace full timestamp with just year as integer
paris_listings_overtime.index = paris_listings_overtime.index.year
paris_listings_overtime.index.name = 'year'
paris_listings_overtime.reset_index(inplace=True)
print(paris_listings_overtime)

# -----------------------------
# 9) Visualizations
# -----------------------------

# 9.1 Bar plot: Average price by neighbourhood
plt.figure(figsize=(12, 8))
sns.barplot(
    x=paris_listings_neighbourhood.values,
    y=paris_listings_neighbourhood.index,
    palette='viridis',
    hue=paris_listings_neighbourhood.values,
    legend=False
)
plt.title('Average Price by Neighbourhood in Paris')
plt.xlabel('Average Price (€)')
plt.ylabel('Neighbourhood')
plt.tight_layout()
plt.show()

# 9.2 Bar plot: Average price by number of accommodates in most expensive neighbourhood
sns.catplot(
    x=paris_listings_accommodations.index,
    y=paris_listings_accommodations.values,
    kind='bar',
    palette='summer',
    hue=paris_listings_accommodations.values,
    legend=False,
    height=8,
    aspect=1.5
)
plt.title(f'Average Price by Accommodates in {most_expensive_neighbourhood}, Paris')
plt.xlabel('Number of Accommodates')
plt.ylabel('Average Price (€)')
plt.tight_layout()
plt.show()

# 9.3 Dual-axis line plot: Count of new hosts & average price over time
fig, ax1 = plt.subplots(figsize=(14,6))
# plt.grid(axis='both', visible=False)
ax1.grid(False)

# Line 1: Count of new hosts
color1 = 'tab:blue'
sns.lineplot(
    data=paris_listings_overtime,
    x='year',
    y='neighbourhood',
    marker='o',
    ax=ax1,
    color=color1,
    label='Number of Listings',
)
ax1.set_ylabel('Number of Listings', color=color1)
ax1.set_ylim(0)
ax1.tick_params(axis='y', labelcolor=color1)

# Line 2: Average price
ax2 = ax1.twinx()
ax2.grid(False)
color2 = 'tab:orange'
sns.lineplot(
    data=paris_listings_overtime,
    x='year',
    y='price',
    marker='*',
    ax=ax2,
    color=color2,
    label='Average Price (€)'
)
ax2.set_ylabel('Average Price (€)', color=color2)
ax2.set_ylim(0)
ax2.tick_params(axis='y', labelcolor=color2)

# Combine legends from both axes
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

plt.title('Number of Listings and Average Price Over Time in Paris')
fig.tight_layout()
plt.show()
