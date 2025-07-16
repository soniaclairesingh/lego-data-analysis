# -*- coding: utf-8 -*-
"""
LEGO Data Analysis Project
Created on Tue Jul 15 12:47:55 2025
@author: Sonia Singh
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
sets = pd.read_csv(r"C:\Users\Sonia Singh\sql\raw_data\lego\sets.csv")
themes = pd.read_csv(r"C:\Users\Sonia Singh\sql\raw_data\lego\themes.csv")

# -----------------------------
# Top Themes by Set Count
# -----------------------------

# Count sets per theme_id
theme_counts = sets['theme_id'].value_counts().reset_index()
theme_counts.columns = ['theme_id', 'set_count']

# Merge with theme names
merged_df = pd.merge(theme_counts, themes, left_on='theme_id', right_on='id')
clean_themes = merged_df[['name', 'set_count']].sort_values('set_count', ascending=False)

# Plot Top 10 Themes by Set Count
top_10 = clean_themes.head(10)

plt.figure(figsize=(12, 6))
sns.barplot(data=top_10, x='name', y='set_count', palette='viridis', ci=None)
plt.xticks(rotation=45, ha='right')
plt.xlabel('Theme Name', fontsize=14)
plt.ylabel('Number of Sets', fontsize=14)
plt.title('Top 10 LEGO Themes by Set Count', fontsize=18)
plt.tight_layout()
plt.savefig("top_lego_themes.png", dpi=300, bbox_inches='tight')
plt.show()

# -----------------------------
# Average Parts per Theme
# -----------------------------

# Calculate average number of parts per theme_id
avg_parts = sets.groupby('theme_id')['num_parts'].mean().reset_index()
avg_parts.columns = ['theme_id', 'avg_num_parts']

# Merge with theme names
avg_parts_df = pd.merge(avg_parts, themes, left_on='theme_id', right_on='id')
avg_parts_df['avg_num_parts'] = avg_parts_df['avg_num_parts'].round(2)

# Select Top 10 Themes by Average Parts
top_10_avg_parts = avg_parts_df.sort_values(by='avg_num_parts', ascending=False).head(10)

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(data=top_10_avg_parts, x='avg_num_parts', y='name', palette='viridis', ci=None)
plt.xlabel('Average Number of Parts', fontsize=14)
plt.ylabel('Theme Name', fontsize=14)
plt.title('Top 10 LEGO Themes by Average Parts', fontsize=18)
plt.tight_layout()
plt.savefig("top_lego_parts.png", dpi=300, bbox_inches='tight')
plt.show()

# -----------------------------
# Yearly Trends of Set Size
# -----------------------------

# Average number of parts per year
yearly_parts = sets.groupby('year')['num_parts'].mean().reset_index()
yearly_parts['num_parts'] = yearly_parts['num_parts'].round(2)

# Plot
plt.figure(figsize=(10, 6))
sns.lineplot(data=yearly_parts, x='year', y='num_parts')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Average Number of Parts', fontsize=14)
plt.title('Average LEGO Set Size Over Years', fontsize=18)
plt.tight_layout()
plt.savefig("yearly_trends_parts.png", dpi=300, bbox_inches='tight')
plt.show()
