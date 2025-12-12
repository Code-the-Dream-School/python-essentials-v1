# Lesson 04: Introduction to Data Engineering — Group Mentor Guide

Welcome to Lesson 4 of the Python 100 course! This week, students are learning:

- Introduction to Pandas: Creating and manipulating DataFrames
- Loading Data: Reading data from CSV, JSON, and dictionaries
- Data Inspection: Using `head()`, `tail()`, `info()` to inspect datasets
- Data Cleaning: Handling missing values, converting data types, text standardization

Students are working in the `assignment4` folder with `assignment4.py` and running tests with `pytest -v -x assignment4-test.py`.

## Warm-Up (5–10 minutes)

Choose one:

**Relationship-Building**  
- What's a dataset or topic you've been curious to analyze or explore with data?
- If you could collect data on anything in your daily life, what would it be?

**Check for Understanding (from last week)**  
- What's the difference between a list and a dictionary in Python?
- How do you access a value in a dictionary?
- What's a method, and how is it different from a function?

## Explore vs. Apply — Session Formats

**Explore Sessions** → Walk through Pandas basics: Series, DataFrames, reading CSVs, using inspection methods  
**Apply Sessions** → Debug student code, work through data cleaning challenges, troubleshoot test failures

## Sample Timing for 1-Hour Session

| Time      | Activity                                 |
|-----------|------------------------------------------|
| 0:00–0:10 | Warm-up + review last week               |
| 0:10–0:30 | Explore: walk through Pandas fundamentals |
| 0:30–0:50 | Apply: live code + assignment help       |
| 0:50–1:00 | Wrap-up + final questions                |

## Check for Understanding (Ask 2–3)

- What's the difference between a Pandas Series and a DataFrame?
- How do you read a CSV file into a DataFrame?
- What does `df.head()` show you? What about `df.info()`?
- Why would you use `pd.to_numeric()` with `errors='coerce'`?
- What's the difference between `df['column']` and `df.loc[row, column]`?

## Explore Prompts

Use these to demonstrate key concepts live:

- Let's create a simple DataFrame from a dictionary together
- How do we read a CSV file? What parameters can we use?
- What's the difference between accessing data with `.loc[]` vs `.iloc[]`?
- Why do we need to handle missing data? What are some strategies?

*Mini-Demo Ideas:*

```python
import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'LA', 'Chicago']
}
df = pd.DataFrame(data)
print(df)

# Reading a CSV file
df = pd.read_csv('employees.csv')
print(df.head(3))

# Data inspection
print(df.info())
print(df.shape)

# Accessing data
print(df['Name'])  # Get a column
print(df.loc[0, 'Name'])  # Get specific cell
print(df.iloc[0, 0])  # Get by position

# Handling missing data
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Age'] = df['Age'].fillna(df['Age'].mean())
```

---

## Apply Prompts (Live Coding & Troubleshooting)

### Assignment Hotspots
* **Task 1**: Forgetting to use `copy()` when creating modified DataFrames
* **Task 1**: Setting `index=False` when saving to CSV (tests will fail if index is included!)
* **Task 2**: JSON file formatting - must be valid JSON with proper structure
* **Task 2**: Using `pd.concat()` with `ignore_index=True` to combine DataFrames
* **Task 3**: Understanding difference between `head()` (returns DataFrame) and just viewing data
* **Task 4**: Chain of data cleaning operations - order matters!
* **Task 4**: `pd.to_numeric()` vs `pd.to_datetime()` - using the right converter
* **Task 4**: `.str.strip()` and `.str.upper()` only work on string columns
* **Task 4**: Calculating mean/median before filling NaN values

### Try This Live

**Let's walk through Task 4 data cleaning together:**

```python
# Read dirty data
dirty_data = pd.read_csv('dirty_data.csv')
clean_data = dirty_data.copy()

# Remove duplicates
clean_data = clean_data.drop_duplicates()

# Convert Age to numeric
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')

# Convert Salary to numeric (replace placeholders first)
clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a'], pd.NA)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')

# Fill missing values
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())

# Convert dates
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')

# Standardize text
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
```

**Ask:**
* Why do we need `copy()` instead of just assigning the variable?
* What happens if we try to calculate mean() before converting to numeric?
* Why use `errors='coerce'` instead of letting it fail?

## Common Pitfalls & Solutions

| Issue | Solution |
|-------|----------|
| "SettingWithCopyWarning" | Use `.copy()` to create true copies, not views |
| Tests fail on CSV export | Check `index=False` parameter in `to_csv()` |
| JSON file won't read | Validate JSON syntax (commas, quotes, brackets) |
| Can't calculate mean/median | Ensure column is numeric type first |
| `.str` methods don't work | Check if column is object/string dtype |
| Wrong data selected | Review `.loc[]` vs `.iloc[]` syntax |

## Engagement Strategies (for quiet groups)

* **Live Debug**: "Let's run this code together and see what error we get"
* **Comparison Challenge**: "What's the difference between these two approaches?"
* **Predict the Output**: "Before we run this, what do you think will happen?"
* **Pair Review**: "Compare your Task 2 JSON files - are they structured the same way?"

## Optional Challenges

- Add error handling to check if CSV file exists before reading
- Create a function that takes a DataFrame and returns a cleaned version
- Export only certain columns to a new CSV file
- Create a DataFrame with intentional missing values and practice different `fillna()` strategies
- Use `.describe()` to get statistical summaries of numeric columns

## Python Environment Reminders

**Common Setup Issues:**
- Make sure you're working in the `assignment4` branch
- Run pytest from the correct directory: `pytest -v -x assignment4-test.py`
- If pandas isn't recognized, check that requirements.txt was installed
- Use `python` command in terminal to test code interactively

**VSCode Tips:**
- Use "Run Python File" button to execute entire script
- Terminal should show test results clearly
- Check the OUTPUT panel for print statements

## Mentor To-Do
- [ ] Run a session using this guide  
- [ ] Help students understand DataFrame fundamentals
- [ ] Guide through data cleaning process step-by-step
- [ ] Submit your [Mentor Session Report](https://airtable.com/appoSRJMlXH9KvE6w/shrp0jjRtoMyTXRzh)
