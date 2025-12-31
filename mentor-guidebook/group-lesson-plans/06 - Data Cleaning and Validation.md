# Lesson Plan 06 – Data Cleaning and Validation

## About This Week
This week students learn essential data cleaning techniques—the unglamorous but critical work that precedes any meaningful data analysis. They'll handle missing values, remove duplicates, deal with outliers, and transform messy data into usable formats. The assignment uses real Kaggle datasets, reinforcing that real-world data is rarely clean. Students also learn pivot tables and the powerful `apply()` method for complex transformations.



## Explore Session (60 minutes)

**Purpose:** Introduce data cleaning concepts and techniques through practical examples before students tackle messy real-world datasets.  
**Materials:** Python environment with Pandas, sample datasets, Jupyter notebook or Python shell.

### Segment 1 – Warm-Up (5 min)
- Ask: "When you've worked with data so far, what problems have you encountered? Missing values? Weird formats? Duplicates?"
- Quick discussion: "Why do you think data is often 'dirty' or messy?"

*Mentor Tip: Share a quick real-world anecdote about data quality issues—helps students understand this is a universal problem, not unique to their experience.*



### Segment 2 – I Do: The Reality of Dirty Data (10 min)

**Explain the concept of "garbage in, garbage out":**

```python
import pandas as pd

# Example of dirty data
data = {
    'Name': ['Alice', 'bob', 'CHARLIE', ' David ', None],
    'Age': [25, -5, 150, 30, 28],
    'Email': ['alice@email.com', 'bob@', 'charlie@email.com', 
              'david@email.com', 'eve@email.com'],
    'Salary': ['$50,000', '60000', '$70,000', '80k', '55000']
}
df = pd.DataFrame(data)
print(df)
```

**Point out the problems:**
- Inconsistent name capitalization and spacing
- Invalid ages (negative, impossibly high)
- Malformed email address
- Inconsistent salary format

**Five main data cleaning tasks:**
1. **Standardization** - Making formats consistent
2. **Handling missing values** - Deciding what to do with gaps
3. **Removing duplicates** - Eliminating redundant records
4. **Addressing outliers** - Dealing with extreme/implausible values
5. **Validation** - Ensuring data meets requirements

**CFU Questions:**
- "What happens if we calculate average age with that -5 and 150 in there?"
- "Why might we have inconsistent formats in the first place?"
- "What's the risk of automatically 'fixing' data?"

*Mentor Tip: Emphasize that cleaning involves tradeoffs—always keep the original data!*



### Segment 3 – We Do: Pivot Tables (10 min)

**Start with a business scenario:**

```python
# Sales data
data = [
    {'Employee': 'Jones', 'Product': 'Widget', 'Region': 'West', 'Revenue': 9000},
    {'Employee': 'Jones', 'Product': 'Gizmo', 'Region': 'West', 'Revenue': 4000},
    {'Employee': 'Jones', 'Product': 'Widget', 'Region': 'East', 'Revenue': 4000},
    {'Employee': 'Smith', 'Product': 'Widget', 'Region': 'West', 'Revenue': 9007},
    {'Employee': 'Smith', 'Product': 'Gizmo', 'Region': 'West', 'Revenue': 40003},
]
sales = pd.DataFrame(data)
print(sales)
```

**Create pivot tables together:**

```python
# Pivot 1: Sales by product and region
pivot1 = pd.pivot_table(
    sales,
    index=['Product', 'Region'],
    values=['Revenue'],
    aggfunc='sum',
    fill_value=0
)
print(pivot1)

# Pivot 2: Sales by product, columns for region
pivot2 = pd.pivot_table(
    sales,
    index='Product',
    values='Revenue',
    columns='Region',
    aggfunc='sum',
    fill_value=0
)
print(pivot2)
```

**Explain the components:**
- `index` = rows
- `columns` = columns (optional)
- `values` = what to aggregate
- `aggfunc` = how to aggregate (sum, mean, count, etc.)
- `fill_value` = what to show if no data

**CFU Questions:**
- "How is this different from `groupby()`?"
- "When would you use a pivot table vs groupby?"
- "What does `fill_value=0` do?"

*Mentor Tip: Pivot tables are like Excel pivot tables—students may already know the concept!*



### Segment 4 – I Do: The `apply()` Method (10 min)

**Explain the problem `apply()` solves:**

"Sometimes you need to create a new column based on complex logic from multiple columns. Simple operators won't cut it."

```python
# Commission based on complex rules
per_employee = sales.groupby('Employee').agg({'Revenue': 'sum'})
per_employee['Commission Plan'] = ['A', 'B']

# Plan A: $1000 base + 5% over $10k
# Plan B: $1400 base + 4% over $10k
# Nothing if under $10k

def calculate_commission(row):
    if row['Revenue'] < 10000:
        return 0
    if row['Commission Plan'] == 'A':
        return 1000 + 0.05 * (row['Revenue'] - 10000)
    else:
        return 1400 + 0.04 * (row['Revenue'] - 10000)

per_employee['Commission'] = per_employee.apply(
    calculate_commission, 
    axis=1  # Process by row, not column
)
print(per_employee)
```

**Key points:**
- `apply()` calls a function once per row (when `axis=1`)
- The function receives the entire row
- Returns a value for the new column
- More flexible than `.map()` or operators

**CFU Questions:**
- "What does `axis=1` mean?"
- "Why can't we just use `*` or `+` operators here?"
- "What parameter does our function receive?"



### Segment 5 – We Do: Handling Missing Data (15 min)

**Work through the common approaches:**

```python
# Create data with missing values
data = {
    'Name': ['Alice', 'Bob', None, 'David'],
    'Age': [24, 27, 22, None],
    'Score': [85, None, 88, 76]
}
df = pd.DataFrame(data)
print(df)
```

**Approach 1: Find missing data**
```python
# Find rows with any missing data
missing = df[df.isnull().any(axis=1)]
print(missing)
```

**Approach 2: Drop missing data**
```python
# Remove rows with any missing values
df_dropped = df.dropna()
print(df_dropped)
print(f"Lost {len(df) - len(df_dropped)} rows")
```

**Approach 3: Fill missing data**
```python
# Fill with different strategies
df_filled = df.fillna({
    'Name': 'Unknown',
    'Age': df['Age'].mean(),  # Average age
    'Score': df['Score'].median()  # Median score
})
print(df_filled)
```

**Discuss tradeoffs:**
- `dropna()`: Loses data, but keeps quality high
- `fillna()`: Keeps data, but introduces assumptions
- No perfect answer—depends on context

**CFU Questions:**
- "When would you drop vs fill missing data?"
- "Why use median instead of mean for some columns?"
- "What's the risk of filling missing values?"

*Mentor Tip: Emphasize that these are judgment calls. There's no single "right" approach.*



### Segment 6 – Quick Coverage of Other Techniques (10 min)

**Removing Duplicates:**
```python
data = {
    'Name': ['Alice', 'Bob', 'Alice', 'David'],
    'Age': [24, 27, 24, 32]
}
df = pd.DataFrame(data)

# Remove exact duplicates
df_unique = df.drop_duplicates()
print(df_unique)

# Remove based on specific column
df_unique_names = df.drop_duplicates(subset='Name')
print(df_unique_names)
```

**Handling Outliers:**
```python
# Replace impossible ages
df['Age'] = df['Age'].apply(
    lambda x: df['Age'].median() if x > 100 or x < 0 else x
)
```

**Standardizing Data:**
```python
# Fix inconsistent formatting
df['Name'] = df['Name'].str.lower().str.strip()
df['City'] = df['City'].replace({'NYC': 'New York', 'LA': 'Los Angeles'})
```

**Don't go too deep—just preview these concepts.**



### Segment 7 – Wrap-Up (5 min)

**Key takeaways:**
- Real data is messy—cleaning is a huge part of data work
- Pivot tables reorganize data for easier analysis
- `apply()` handles complex row-by-row logic
- Missing data: drop it or fill it (both have tradeoffs)
- Always keep original data—cleaning can introduce errors

**Assignment preview:**
- Work with real Kaggle datasets (ecommerce, jobs, eclipses)
- Practice all these cleaning techniques
- 8 tasks covering everything we discussed
- Start early—debugging real data takes time!

*Mentor Tip: Remind students that this week's work is practical and directly applicable to any data analysis job.*



## Apply Session (60 minutes)

**Purpose:** Support students through the challenging data cleaning assignment with real datasets.  
**Materials:** Kaggle notebooks, assignment instructions, real datasets.

### Segment 1 – Dataset Overview (10 min)

**Walk through the three datasets:**

1. **Ecommerce Consumer Behavior**
   - Customer purchases, demographics
   - Used for pivot table practice
   - Issue: Purchase_Amount stored as string with "$"

2. **AI-Powered Job Recommendations**
   - Job listings with requirements, salaries
   - Used for `apply()` practice
   - Need to check multiple conditions

3. **Code The Dream Lesson 5 / Eclipses**
   - Employee/customer data with missing values
   - Eclipse observations in Arkansas
   - Has missing data, duplicates, invalid dates

**Show how to add datasets in Kaggle:**
- Click "Add Input" → "Datasets"
- Search for dataset name
- Click "+" to add
- Run first cell to see file paths



### Segment 2 – Walkthrough Task 1 & 2 (15 min)

**Task 1: Pivot Tables**

Common issue: Purchase_Amount is a string
```python
# Load the data
ecommerce = pd.read_csv('/kaggle/input/...')

# Fix the Purchase_Amount column
ecommerce['Purchase_Amount'] = ecommerce['Purchase_Amount'].str.replace('$', '').astype(float)

# Create pivot table
buying_patterns = pd.pivot_table(
    ecommerce,
    index='Purchase_Category',
    columns=['Gender', 'Income_Level'],
    values='Purchase_Amount',
    aggfunc='sum'
)
print(buying_patterns)
```

**Task 2: apply() Method**

```python
# Load jobs data
jobs = pd.read_csv('/kaggle/input/...')

# Create function for complex logic
def check_job(row):
    if (row['Experience_Level'] == 'Entry Level' and 
        row['Salary'] >= 70000 and
        'SQL' in row['Required_Skills'] and 
        'Python' in row['Required_Skills']):
        return 'Yes'
    return 'No'

# Apply the function
jobs['Check These Out'] = jobs.apply(check_job, axis=1)

# Filter to jobs of interest
my_jobs = jobs[jobs['Check These Out'] == 'Yes']
print(my_jobs.head(10))
```

**CFU Questions:**
- "Why do we need `.str.replace()` before `.astype(float)`?"
- "What would happen if we forgot `axis=1` in apply()?"



### Segment 3 – Guided Work on Tasks 3-5 (20 min)

**Task 3: Missing Data Strategy**

Key steps to emphasize:
```python
# 1. Load and examine
df = pd.read_csv('/kaggle/input/...')
print(df.info())  # See which columns have missing data

# 2. Drop rows with ANY missing data
df1 = df.dropna()
print(df.info())
print(df1.info())  # Compare

# 3. Fill strategically
df = df.fillna({
    'Name': 'Unknown',
    'Age': df['Age'].mean(),
    'Salary': df['Salary'].median(),
    'Join Date': '2020-01-01'
})

# 4. Drop remaining (only City should have NaN now)
df2 = df.dropna()
df2 = df2.reset_index(drop=True)

# 5. Convert types
df2['Age'] = df2['Age'].astype(int)
```

**Task 4: Data Transformation**

Watch for the CSV separator issue:
```python
# Note the separator!
df3 = pd.read_csv('/kaggle/input/...', sep='|')

# Converting dates with errors
df3['Date'] = pd.to_datetime(df3['Date'], errors='coerce')
# 'coerce' turns invalid dates to NaT (Not a Time)
```

**Task 5: Duplicates**

```python
# Find duplicates
duplicate_series = df3.duplicated()
print(duplicate_series[duplicate_series == True].head(10))
print(duplicate_series.value_counts())

# Remove duplicates
df3 = df3.drop_duplicates()
print(df3.info())
```

Have students work through Tasks 6-8 independently or in breakout rooms.



### Segment 4 – Common Issues & Debugging (10 min)

**Frequent problems to address:**

1. **String operations on non-strings**
   ```python
   # Error: AttributeError: 'float' object has no attribute 'str'
   # Solution: Convert to string first
   df['Phone'] = df['Phone'].astype(str)
   ```

2. **CSV separator issues**
   ```python
   # If data looks weird, check separator
   df = pd.read_csv(file, sep='|')  # Not always comma!
   ```

3. **Chaining string operations**
   ```python
   # Works:
   df['Name'] = df['Name'].str.lower().str.strip()
   
   # Doesn't work:
   df['Name'] = df['Name'].lower().strip()
   ```

4. **apply() axis confusion**
   ```python
   # axis=1 means row-wise (what we usually want)
   # axis=0 means column-wise
   ```

5. **NaN vs 'NaN' string**
   ```python
   import numpy as np
   df['Age'] = np.nan  # Correct
   df['Age'] = 'NaN'   # Wrong! This is a string
   ```



### Segment 5 – Wrap-Up (5 min)

**Submission checklist:**
- [ ] All 8 tasks completed
- [ ] Output visible for each task
- [ ] Markdown cells explain each task
- [ ] Notebook saved and set to Public
- [ ] Public URL submitted

**Debugging tips:**
- Print DataFrames at each step
- Use `.info()` to check data types
- Check for hidden spaces in column names
- Test on small samples first

**Reminders:**
- This assignment is substantial—start early
- Real data is messy—that's normal
- Use print statements liberally
- Ask questions when stuck!



## Key Teaching Points

### Data Cleaning Concepts
- **Garbage in, garbage out** - Bad data = bad analysis
- **Tradeoffs** - Every cleaning choice has pros/cons
- **Keep originals** - Always preserve raw data
- **Real data is messy** - This is normal, not a sign you're doing it wrong

### Pivot Tables
- Reorganize data for better presentation
- Like groupby but with different output structure
- `index` = rows, `columns` = columns, `values` = what to aggregate
- Multiple aggregation functions possible

### apply() Method
- For complex row-wise logic
- Receives entire row as parameter
- More flexible than operators or `.map()`
- `axis=1` for row-wise, `axis=0` for column-wise

### Missing Data
- `dropna()` = remove rows with missing data
- `fillna()` = replace missing data with values
- Choose based on context and how much data you'd lose
- Mean vs median matters (outliers affect mean)

### Other Cleaning Tasks
- `drop_duplicates()` removes redundant records
- Outliers replaced with median/mean
- Standardization via `.str.` methods
- Type conversion with `astype()` and `pd.to_datetime()`



## Common Student Struggles

1. **Pivot table parameter confusion**
   - index vs columns vs values
   - When to use aggfunc
   - Multi-level indices

2. **apply() axis parameter**
   - Forgetting axis=1
   - Understanding row vs column operations

3. **Missing data strategy**
   - When to drop vs fill
   - Mean vs median choice
   - Cascading effects of filling

4. **String operations**
   - Forgetting `.str.` prefix
   - Type conversion before string operations

5. **Real dataset challenges**
   - Unexpected formats
   - Hidden characters/spaces
   - CSV separator issues

6. **NaN handling**
   - Using string 'NaN' instead of np.nan
   - Understanding NaT (Not a Time)



## Questions to Assess Understanding

**Pivot Tables:**
- "What's the difference between index and columns parameters?"
- "When would you use pivot_table vs groupby?"

**apply():**
- "What does axis=1 mean in apply()?"
- "What's the difference between apply() and map()?"

**Missing Data:**
- "When would you use dropna() vs fillna()?"
- "Why might you use median instead of mean to fill missing values?"

**Data Cleaning:**
- "Why is it important to keep the original data?"
- "What are the risks of automatically 'fixing' data?"
- "How do you decide whether to drop or fix outliers?"
