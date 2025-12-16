# Week 5: Data Wrangling and Aggregation - Assignment Review Guide

## Assignment Overview
This week students create a Jupyter notebook on Kaggle to practice Pandas data wrangling techniques. They work through 10 tasks covering selection, aggregation, merging, filtering, sorting, and real-world data analysis with an international football dataset. This is their first time using Kaggle notebooks, adding an extra layer of complexity to an already challenging assignment.

**Key Learning Objectives:**
- Master data selection with `.loc[]`, `.iloc[]`, and boolean filtering
- Aggregate data using `groupby()` and multiple aggregation functions
- Merge and join DataFrames with different strategies
- Transform data by adding, modifying, and deleting columns
- Work with real-world datasets and Kaggle environment



## Review Checklist

### Kaggle Setup
- [ ] Notebook is named "CTD_Assignment_5"
- [ ] Notebook is set to Public
- [ ] "Allow Comments" is enabled
- [ ] All cells have been run and show output
- [ ] Markdown cells describe each task
- [ ] International football dataset is properly loaded

### Task Completion
- [ ] **Task 1:** DataFrames created and selection operations performed
- [ ] **Task 2:** Aggregation with groupby showing mean, sum, count
- [ ] **Task 3:** Merge and join operations completed with NaN handling
- [ ] **Task 4:** Filtering rows based on conditions
- [ ] **Task 5:** Sorting by Salary in descending order
- [ ] **Task 6:** Columns renamed correctly
- [ ] **Task 7:** Salary transformation (10% increase)
- [ ] **Task 8:** DataFrames concatenated with index reset
- [ ] **Task 9:** Football data wrangled to show worst defensive teams
- [ ] **Task 10:** Tunisia's 10 most recent games displayed


## What to Look For: Task-by-Task

### Task 1: Data Selection

**Expected code:**
```python
import pandas as pd

data1 = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 30],
    'Salary': [50000, 60000, 70000, 80000, 55000]
}

data2 = {
    'Name': ['Frank', 'Grace', 'Helen', 'Ian', 'Jack'],
    'Age': [28, 33, 35, 29, 40],
    'Salary': [52000, 58000, 72000, 61000, 85000]
}

data3 = {
    'Name': ['Frank', 'Helen', 'Ian', 'Hima', 'Chaka'],
    'Age': [17, 93, 12, 57, 106],
    'Favorite Color': ['blue', 'pink', 'burgundy', 'red', 'turquoise']
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)

print(df1)
print(df2)
print(df3)

# Selection operations
print(df1['Name'])
print(df1[['Name', 'Salary']])
print(df1.iloc[:3])
```

**What to verify:**
- All three DataFrames created and printed
- 'Name' column selected correctly
- 'Name' and 'Salary' columns selected together
- First three rows sliced with `.iloc[:3]`

**Common mistakes:**
- Using `.loc[:3]` instead of `.iloc[:3]` (would give 4 rows, not 3)
- Not printing the results



### Task 2: Data Aggregation

**Expected code:**
```python
result = df1.groupby('Age').agg({'Salary': ['mean', 'sum', 'count']})
print(result)
```

**What to verify:**
- Groups created by 'Age'
- Three aggregations applied: mean, sum, count
- Result displayed correctly

**Expected output structure:**
```
            Salary                    
              mean    sum  count
Age                              
25         50000.0  50000      1
30         57500.0 115000      2
35         70000.0  70000      1
40         80000.0  80000      1
```

**Common mistakes:**
- Using `agg('mean')` instead of `agg(['mean', 'sum', 'count'])`
- Forgetting to specify the column: should be `agg({'Salary': [...]})`



### Task 3: Merging and Joining DataFrames

**This is the most complex task. Expected code:**

```python
import numpy as np

# Merge df1 and df3
df_1_3_merged = pd.merge(df1, df3, on='Name', how='outer', 
                         suffixes=['_left', '_right'])
print(df_1_3_merged)

# Fill NaN in Salary
df_1_3_merged['Salary'] = df_1_3_merged['Salary'].fillna(15000)

# Fill NaN in Favorite Color
df_1_3_merged['Favorite Color'] = df_1_3_merged['Favorite Color'].fillna('yellow')
print(df_1_3_merged)

# Create new Age column using np.where
df_1_3_merged['Age'] = np.where(
    df_1_3_merged['Age_left'].notna(),
    df_1_3_merged['Age_left'],
    df_1_3_merged['Age_right']
)
print(df_1_3_merged)

# Drop Age_left and Age_right
df_1_3_merged.drop(['Age_left', 'Age_right'], axis=1, inplace=True)
print(df_1_3_merged)

# Join method
df1_b = df1.set_index('Name')
df3_b = df3.set_index('Name')
joined = df1_b.join(df3_b, how='outer', lsuffix='_left', rsuffix='_right')
print(joined)
```

**What to verify:**
- Outer merge performed with correct suffixes
- NaN values in Salary replaced with 15000
- NaN values in Favorite Color replaced with 'yellow'
- Age column created using `np.where()`
- Age_left and Age_right dropped
- Join performed with 'Name' as index
- Join uses suffixes (note: `lsuffix` and `rsuffix` for join, not `suffixes`)

**Common mistakes:**
- Using inner merge instead of outer
- Forgetting suffixes on merge
- Not using `.notna()` in np.where condition
- Using wrong suffix parameter names for join (should be `lsuffix`/`rsuffix`)
- Not setting index before joining



### Task 4: Filtering Rows

**Expected code:**
```python
filtered = df1[df1['Age'] > 30]
print(filtered)
```

**What to verify:**
- Filter condition is `Age > 30` (not `>=`)
- Result shows only Bob, David (ages 35, 40, 30 would not be included)
- Actually, if Eva is 30, only Charlie (35) and David (40) should appear

**Common mistakes:**
- Using `>=` instead of `>`
- Forgetting parentheses around condition



### Task 5: Sorting Data

**Expected code:**
```python
sorted_df = df1.sort_values(by='Salary', ascending=False)
print(sorted_df)
```

**What to verify:**
- Sorted by 'Salary' column
- Descending order (`ascending=False`)
- Highest salary (David: 80000) appears first

**Common mistakes:**
- Using `ascending=True` (would be lowest first)
- Forgetting `by=` parameter name



### Task 6: Renaming Columns

**Expected code:**
```python
renamed_df = df1.rename(columns={
    'Age': 'Employee Age',
    'Salary': 'Employee Salary'
})
print(renamed_df)
```

**What to verify:**
- 'Age' renamed to 'Employee Age'
- 'Salary' renamed to 'Employee Salary'
- Not using `inplace=True` (per instructions)
- New DataFrame stored in variable

**Common mistakes:**
- Using `inplace=True` (instructions say not to)
- Wrong syntax for rename dictionary



### Task 7: Data Transformation

**Expected code:**
```python
df1['Salary'] = df1['Salary'] * 1.10
print(df1)
```

**What to verify:**
- All salaries increased by 10% (multiplied by 1.10)
- Alice: 50000 → 55000
- Bob: 60000 → 66000
- etc.

**Common mistakes:**
- Multiplying by 0.10 instead of 1.10 (that would make salaries 10% of original!)
- Adding 10 instead of multiplying



### Task 8: Concatenating DataFrames

**Expected code:**
```python
concatenated = pd.concat([df1, df2], ignore_index=True)
print(concatenated)
```

**What to verify:**
- df1 and df2 combined vertically (rows added)
- Index reset (0, 1, 2, ... 9, not 0, 1, 2, 3, 4, 0, 1, 2, 3, 4)
- Total of 10 rows (5 from df1 + 5 from df2)

**Common mistakes:**
- Forgetting `ignore_index=True`
- Using `merge()` instead of `concat()`



### Task 9: Football Data Wrangling

**This is the most challenging task. Expected logic:**

```python
# Read dataset
football_results = pd.read_csv(
    '/kaggle/input/international-football-results-from-1872-to-2017/results.csv'
)
print(football_results.head())

# Select columns
results_1 = football_results[[
    'home_team', 'away_team', 'home_score', 'away_score', 'date'
]]
print(results_1.head())

# Rename for home teams perspective
results_2 = results_1.rename(columns={
    'home_team': 'team',
    'away_team': 'opponent',
    'home_score': 'points_for',
    'away_score': 'points_against'
})
print(results_2.head())

# Rename for away teams perspective
results_3 = results_1.rename(columns={
    'away_team': 'team',
    'home_team': 'opponent',
    'away_score': 'points_for',
    'home_score': 'points_against'
})
print(results_3.head())

# Concatenate
football_results = pd.concat([results_2, results_3], ignore_index=True)
print(football_results.head())

# Group by team and get mean points against
points_against = football_results.groupby('team')['points_against'].mean()

# Sort descending and show top 10
points_against_sorted = points_against.sort_values(ascending=False)
print(points_against_sorted.head(10))
```

**What to verify:**
- Dataset loaded correctly
- Columns selected from original data
- Two separate rename operations (home perspective and away perspective)
- Concatenation combines both perspectives
- Groupby calculates mean points_against per team
- Sorted in descending order (worst defense first)
- Top 10 displayed

**Expected top teams (approximately):**
Teams with historically weak defenses should appear (exact order may vary based on dataset version)

**Common mistakes:**
- Not understanding the home/away reorganization logic
- Forgetting to reset index in concatenation
- Sorting ascending instead of descending
- Not selecting the 'points_against' column before aggregating



### Task 10: Tunisia's Recent Games

**Expected approach:**

```python
# Filter for Tunisia
tunisia_games = football_results[football_results['team'] == 'Tunisia']

# Sort by date descending
tunisia_sorted = tunisia_games.sort_values(by='date', ascending=False)

# Get first 10 rows
tunisia_recent = tunisia_sorted.head(10)

print(tunisia_recent)
```

**What to verify:**
- Filtered to only Tunisia games
- Sorted by date in descending order (most recent first)
- First 10 games shown
- Includes all relevant columns (team, opponent, points_for, points_against, date)

**Common mistakes:**
- Forgetting to sort by date
- Sorting ascending instead of descending (would show oldest games)
- Filtering on wrong column name
- Case sensitivity issues with 'Tunisia'
