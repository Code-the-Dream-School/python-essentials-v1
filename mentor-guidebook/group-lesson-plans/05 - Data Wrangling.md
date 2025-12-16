# Lesson Plan 05 – Data Wrangling and Aggregation

## About This Week
This week students dive deep into Pandas data manipulation. They learn to select specific data subsets, aggregate data by groups, merge multiple datasets, and transform columns. The assignment introduces Jupyter notebooks on Kaggle and involves real-world data analysis with an international football dataset. This is a big technical leap—students are moving from basic Pandas to practical data analysis workflows.



## Explore Session (60 minutes)

**Purpose:** Introduce core data wrangling techniques through hands-on examples before students tackle the complex assignment.  
**Materials:** Python environment with Pandas installed, sample datasets, Jupyter notebook or Python shell.

### Segment 1 – Warm-Up (5 min)
- Ask: "What's been the most challenging part of working with Pandas so far?"
- Quick discussion: "When you look at a spreadsheet or table, how do you find specific information? What about combining information from two different tables?"

*Mentor Tip: Connect to real-world scenarios—finding all customers over age 30, calculating average sales by region, combining customer info with order history.*



### Segment 2 – I Do: Data Selection (15 min)

Demonstrate the four main selection methods:

```python
import pandas as pd

# Create sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'Score': [85, 92, 88, 76]
}
df = pd.DataFrame(data)
print(df)
```

**Show each selection method:**

```python
# 1. Select a column
print(df['Name'])

# 2. .loc[] - label-based
print(df.loc[0:2, ['Name', 'Age']])  # Rows 0-2, specific columns

# 3. .iloc[] - position-based  
print(df.iloc[:2])  # First 2 rows

# 4. Boolean filtering
print(df[df['Age'] > 24])

# 5. Multiple conditions (note the & and parentheses!)
print(df[(df['Age'] > 24) & (df['Score'] >= 88)])

# 6. String methods
print(df[df['Name'].str.contains('a')])
```

**Key differences to emphasize:**
- `.loc[0:2]` includes row 2 (unlike list slicing!)
- `.iloc[:2]` excludes row 2 (like list slicing)
- Use `&` for AND, `|` for OR (not `and`/`or`)
- String operations need `.str.` prefix

**CFU Questions:**
- "What's the difference between `.loc[]` and `.iloc[]`?"
- "Why do we need parentheses around each condition when using `&`?"
- "What happens if you forget `.str.` before `.contains()`?"

*Mentor Tip: Have students predict outputs before running code. Common mistake: forgetting `.str.` for string operations.*



### Segment 3 – We Do: Data Aggregation (15 min)

Build up from simple to complex aggregations:

```python
# Simple groupby
data = {
    'Category': ['A', 'B', 'A', 'B', 'C'],
    'Values': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)

# Group and sum
grouped = df.groupby('Category').sum()
print(grouped)

# Group and calculate mean
mean_values = df.groupby('Category')['Values'].mean()
print(mean_values)
```

Then show multiple aggregations:

```python
# Apply multiple functions at once
result = df.groupby('Category').agg({
    'Values': ['sum', 'mean', 'count']
})
print(result)
```

**Work through together:**
```python
# Real-world scenario: sales by region
sales_data = {
    'Region': ['North', 'South', 'North', 'South', 'North'],
    'Sales': [100, 150, 200, 175, 125]
}
sales_df = pd.DataFrame(sales_data)

# Calculate total and average sales per region
summary = sales_df.groupby('Region').agg({
    'Sales': ['sum', 'mean', 'count']
})
print(summary)
```

**CFU Questions:**
- "What does `groupby()` actually do to the data?"
- "What's the difference between passing `'sum'` vs `['sum', 'mean']` to `agg()`?"
- "How would you find the region with the highest total sales?"

*Mentor Tip: Emphasize that groupby creates groups, then applies functions to each group separately.*



### Segment 4 – I Do: Merging DataFrames (15 min)

Demonstrate the four join types:

```python
# Create two DataFrames
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 4],
    'Score': [85, 92, 88]
})

print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)
```

**Show each join type:**

```python
# Inner join (only matching rows)
inner = pd.merge(df1, df2, on='ID', how='inner')
print("\nInner join:")
print(inner)  # Only IDs 1 and 2

# Left join (all from left, matching from right)
left = pd.merge(df1, df2, on='ID', how='left')
print("\nLeft join:")
print(left)  # All from df1, NaN for Charlie's score

# Right join (all from right, matching from left)
right = pd.merge(df1, df2, on='ID', how='right')
print("\nRight join:")
print(right)  # All from df2, NaN for ID 4's name

# Outer join (all from both)
outer = pd.merge(df1, df2, on='ID', how='outer')
print("\nOuter join:")
print(outer)  # All rows, NaN where no match
```

**Visual analogy:** Draw Venn diagrams showing what each join type includes.

**CFU Questions:**
- "When would you use an inner join vs an outer join?"
- "What does `NaN` mean and when does it appear?"
- "If both DataFrames have an 'Age' column, what happens?"

*Mentor Tip: Join types are confusing at first. Use real-world examples: "You have a customer list and an orders list. Inner join = customers who placed orders. Left join = all customers, showing who ordered what."*



### Segment 5 – We Do: Data Transformation (10 min)

Practice common transformations together:

```python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Salary': [50000, 60000, 55000]
})

# 1. Add a column
df['Bonus'] = df['Salary'] * 0.1
print(df)

# 2. Transform with operator
df['Salary'] = df['Salary'] * 1.05  # 5% raise
print(df)

# 3. Transform with map()
df['Level'] = df['Salary'].map(
    lambda x: 'Senior' if x > 55000 else 'Junior'
)
print(df)

# 4. Drop a column
df.drop('Bonus', axis=1, inplace=True)
print(df)
```

**CFU Questions:**
- "Why can't we write `df['Name'] = df['Name'].upper()`?"
- "When would you use `map()` vs just an operator like `*`?"
- "What does `axis=1` mean in the `drop()` method?"



### Segment 6 – Wrap-Up (5 min)

**Key takeaways:**
- Selection: `.loc[]` for labels, `.iloc[]` for positions, boolean masks for filtering
- Aggregation: `groupby()` + aggregation functions to summarize data
- Merging: `merge()` combines on columns, `join()` combines on indices
- Transformation: Create/modify columns using operators, `.map()`, or NumPy functions

**Assignment preview:**
- "This week you'll work in Kaggle notebooks—a new environment!"
- "You'll analyze real international football data"
- "Break it into small steps and test each one"

*Mentor Tip: Reassure students that Kaggle notebooks are just like Jupyter—Python is Python regardless of where you run it.*



## Apply Session (60 minutes)

**Purpose:** Help students navigate Kaggle setup and work through challenging parts of the assignment.  
**Materials:** Kaggle accounts, assignment instructions, screen sharing capability.

### Segment 1 – Kaggle Setup Walkthrough (10 min)

**Live demo:**
1. Navigate to kaggle.com and sign in
2. Click "+" in upper left → "New Notebook"
3. Show markdown cells vs code cells
4. Demonstrate running a cell
5. Show "Add Input" → "Datasets" for adding data
6. Explain session timeouts and "Run All"

**CFU Questions:**
- "What's the difference between a markdown cell and a code cell?"
- "What happens if your session times out?"
- "How do you add a dataset to your notebook?"

*Mentor Tip: Have students do this setup live during the session if possible.*



### Segment 2 – Walkthrough Tasks 1-3 (20 min)

**Task 1: Data Selection**

Key points to emphasize:
```python
# Selecting columns
df1['Name']  # Single column
df1[['Name', 'Salary']]  # Multiple columns

# Slicing with iloc
df1.iloc[:3]  # First 3 rows
```

**Task 2: Aggregation**

Common mistake to watch for:
```python
# Group by Age and aggregate Salary
df1.groupby('Age').agg({'Salary': ['mean', 'sum', 'count']})
```

**Task 3: Merging**

Walk through the merge step-by-step:
```python
# Outer merge with suffixes
merged = pd.merge(df1, df3, on='Name', how='outer', 
                  suffixes=['_left', '_right'])

# Fill NaN values
merged['Salary'] = merged['Salary'].fillna(15000)

# Use np.where to combine Age columns
import numpy as np
merged['Age'] = np.where(
    merged['Age_left'].notna(),
    merged['Age_left'],
    merged['Age_right']
)

# Drop unwanted columns
merged.drop(['Age_left', 'Age_right'], axis=1, inplace=True)
```

**CFU Questions:**
- "Why do we need suffixes when merging?"
- "What does `fillna()` do?"
- "How does `np.where()` work like a ternary expression?"

*Mentor Tip: Task 3 is complex. Break it into small steps and check each output.*



### Segment 3 – Guided Work: Football Dataset (20 min)

**Task 9 is the most challenging—walk through strategy:**

```python
# 1. Read the dataset
football_results = pd.read_csv('/kaggle/input/...')
print(football_results.head())

# 2. Select columns for home teams
results_1 = football_results[[
    'home_team', 'away_team', 'home_score', 'away_score', 'date'
]]

# 3. Rename for home perspective
results_2 = results_1.rename(columns={
    'home_team': 'team',
    'away_team': 'opponent',
    'home_score': 'points_for',
    'away_score': 'points_against'
})

# 4. Rename for away perspective
results_3 = results_1.rename(columns={
    'away_team': 'team',
    'home_team': 'opponent',
    'away_score': 'points_for',
    'home_score': 'points_against'
})

# 5. Concatenate and reset index
football_results = pd.concat(
    [results_2, results_3], 
    ignore_index=True
)

# 6. Group by team and get mean points against
points_against = football_results.groupby('team')['points_against'].mean()

# 7. Sort descending and show top 10
points_against.sort_values(ascending=False).head(10)
```

**Strategy tips:**
- Print after each step to verify
- Understand the logic: we're reorganizing data so each row represents one team's perspective
- Concatenation combines home and away games into one dataset

Have students work through Task 10 (Tunisia games) in breakout rooms or independently.



### Segment 4 – Common Issues & Debugging (10 min)

**Address frequent problems:**

1. **Session timeout errors**
   - Solution: Click "Run All" to re-run all cells

2. **Path not found for dataset**
   - Solution: Run the first cell to see available paths

3. **KeyError on merge**
   - Solution: Check that key columns exist and are spelled correctly

4. **SettingWithCopyWarning**
   - Explain this is a warning, not an error
   - Solution: Use `.copy()` or assign to new DataFrame

5. **Forgetting `.str.` for string operations**
   - Solution: Always use `.str.` prefix for string methods on Series



### Segment 5 – Wrap-Up & Submission (5 min)

**Submission checklist:**
- [ ] All tasks complete with output visible
- [ ] Markdown cells explain each task
- [ ] Notebook saved with "Save Version"
- [ ] Sharing set to "Public" with "Allow Comments" on
- [ ] Public URL copied and submitted

**Reminders:**
- Test your code by clicking "Run All"
- Make sure output is visible for each task
- Your reviewer needs to see results, not just code



## Key Teaching Points

### Data Selection
- `.loc[]` = label-based (includes endpoint in slice)
- `.iloc[]` = position-based (excludes endpoint like lists)
- Boolean filtering requires `&`/`|` not `and`/`or`
- String operations need `.str.` prefix

### Data Aggregation  
- `groupby()` splits data into groups
- Aggregation functions apply to each group separately
- `.agg()` can apply multiple functions at once
- Result structure depends on single function vs list of functions

### Merging
- `how='inner'` = only matching rows
- `how='left'` = all left, matching right
- `how='right'` = all right, matching left
- `how='outer'` = all rows from both
- `NaN` appears where no match exists

### Data Transformation
- Use operators for math: `df['col'] = df['col'] * 2`
- Use `.map()` for custom logic with lambda
- Use NumPy functions for advanced operations
- Always create new column when transforming



## Common Student Struggles

1. **Confusion between .loc and .iloc**
   - Emphasize: labels vs positions, inclusive vs exclusive

2. **Boolean filtering syntax**
   - Must use `&` and `|`, not `and` and `or`
   - Must wrap each condition in parentheses

3. **Understanding groupby logic**
   - Show visual: data split into groups, function applied to each

4. **Join type selection**
   - Use Venn diagrams and real-world analogies

5. **Kaggle environment**
   - Session timeouts, finding dataset paths, running cells in order

6. **Task 9 complexity**
   - Breaking down the home/away reorganization logic



## Questions to Assess Understanding

**Data Selection:**
- "How would you select all rows where Age > 30 AND Score > 80?"
- "What's returned when you do `df['Name']`?"

**Aggregation:**
- "If you groupby 'Category', what does `.mean()` calculate?"
- "What's the difference between `agg('sum')` and `agg(['sum', 'mean'])`?"

**Merging:**
- "Which join type would you use to keep all customers even if they haven't ordered?"
- "When do you get NaN values in a merge result?"

**Transformation:**
- "How do you add 10% to all values in the 'Price' column?"
- "When would you use `.map()` vs a simple operator?"
