# Lesson 04: Introduction to Data Engineering — Assignment Answer Key

**Learning objective**: Students will learn to load, preview, and inspect datasets in Pandas by reading data from common formats and summarizing data structure to facilitate efficient data analysis.

You can mark the student's assignment as complete if they: 

- [ ] Have created the `assignment4` branch and submitted a pull request
- [ ] All pytest tests pass successfully
- [ ] Code follows proper Pandas conventions and best practices
- [ ] CSV and JSON files are properly formatted
- [ ] Data cleaning steps are applied in the correct order

## Sample Solution Code

```python
import pandas as pd
import numpy as np

# ========================================
# TASK 1: Introduction to Pandas - Creating and Manipulating DataFrames
# ========================================

# 1. Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame = pd.DataFrame(data)
print("Task 1 - Original DataFrame:")
print(task1_data_frame)

# 2. Add a new column
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print("\nTask 1 - DataFrame with Salary:")
print(task1_with_salary)

# 3. Modify an existing column
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1
print("\nTask 1 - DataFrame with incremented Age:")
print(task1_older)

# 4. Save the DataFrame as a CSV file
task1_older.to_csv('employees.csv', index=False)
print("\nTask 1 - Saved to employees.csv")

# ========================================
# TASK 2: Loading Data from CSV and JSON
# ========================================

# 1. Read data from a CSV file
task2_employees = pd.read_csv('employees.csv')
print("\nTask 2 - Employees from CSV:")
print(task2_employees)

# 2. Create JSON file (additional_employees.json)
# File contents:
"""
[
  {
    "Name": "Eve",
    "Age": 28,
    "City": "Miami",
    "Salary": 60000
  },
  {
    "Name": "Frank",
    "Age": 40,
    "City": "Seattle",
    "Salary": 95000
  }
]
"""

# Read data from JSON file
json_employees = pd.read_json('additional_employees.json')
print("\nTask 2 - Employees from JSON:")
print(json_employees)

# 3. Combine DataFrames
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("\nTask 2 - Combined DataFrame:")
print(more_employees)

# ========================================
# TASK 3: Data Inspection - Using Head, Tail, and Info Methods
# ========================================

# 1. Use head() method
first_three = more_employees.head(3)
print("\nTask 3 - First three rows:")
print(first_three)

# 2. Use tail() method
last_two = more_employees.tail(2)
print("\nTask 3 - Last two rows:")
print(last_two)

# 3. Get the shape of the DataFrame
employee_shape = more_employees.shape
print(f"\nTask 3 - DataFrame shape: {employee_shape}")

# 4. Use info() method
print("\nTask 3 - DataFrame info:")
more_employees.info()

# ========================================
# TASK 4: Data Cleaning
# ========================================

# 1. Create DataFrame from dirty_data.csv
dirty_data = pd.read_csv('dirty_data.csv')
print("\nTask 4 - Original dirty data:")
print(dirty_data)

# Create a copy for cleaning
clean_data = dirty_data.copy()

# 2. Remove duplicate rows
clean_data = clean_data.drop_duplicates()
print("\nTask 4 - After removing duplicates:")
print(clean_data)

# 3. Convert Age to numeric and handle missing values
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print("\nTask 4 - After converting Age to numeric:")
print(clean_data)

# 4. Convert Salary to numeric and replace placeholders with NaN
clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a'], pd.NA)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
print("\nTask 4 - After converting Salary to numeric:")
print(clean_data)

# 5. Fill missing numeric values
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())
print("\nTask 4 - After filling missing values:")
print(clean_data)

# 6. Convert Hire Date to datetime
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')
print("\nTask 4 - After converting Hire Date to datetime:")
print(clean_data)

# 7. Strip whitespace and standardize Name and Department as uppercase
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
print("\nTask 4 - After standardizing text:")
print(clean_data)

print("\n✓ All tasks completed!")
```

## Expected File Outputs

### employees.csv
```csv
Name,Age,City,Salary
Alice,26,New York,70000
Bob,31,Los Angeles,80000
Charlie,36,Chicago,90000
```

### additional_employees.json
```json
[
  {
    "Name": "Eve",
    "Age": 28,
    "City": "Miami",
    "Salary": 60000
  },
  {
    "Name": "Frank",
    "Age": 40,
    "City": "Seattle",
    "Salary": 95000
  }
]
```

## Expected Test Results

When running `pytest -v -x assignment4-test.py`, all tests should pass:

```
test_task1_data_frame PASSED
test_task1_with_salary PASSED
test_task1_older PASSED
test_task1_csv_file PASSED
test_task2_employees PASSED
test_task2_json_employees PASSED
test_task2_more_employees PASSED
test_task3_first_three PASSED
test_task3_last_two PASSED
test_task3_employee_shape PASSED
test_task4_dirty_data PASSED
test_task4_remove_duplicates PASSED
test_task4_age_numeric PASSED
test_task4_salary_numeric PASSED
test_task4_fill_missing PASSED
test_task4_convert_dates PASSED
test_task4_standardize_text PASSED
```

## Common Student Errors & Solutions

### Task 1 Issues

**Error**: "SettingWithCopyWarning"
```python
# WRONG:
task1_with_salary = task1_data_frame
task1_with_salary['Salary'] = [70000, 80000, 90000]

# CORRECT:
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
```

**Error**: Index included in CSV file
```python
# WRONG:
task1_older.to_csv('employees.csv')

# CORRECT:
task1_older.to_csv('employees.csv', index=False)
```

**Error**: Modifying Age incorrectly
```python
# WRONG - This modifies a view, not the DataFrame:
task1_older['Age'][0] = task1_older['Age'][0] + 1

# CORRECT - This modifies the entire column:
task1_older['Age'] = task1_older['Age'] + 1
```

### Task 2 Issues

**Error**: Invalid JSON syntax
```json
// WRONG - Missing comma, trailing comma, or using single quotes:
[
  {
    "Name": "Eve"
    "Age": 28
  },
  {
    'Name': 'Frank',
    'Age': 40,
  }
]

// CORRECT:
[
  {
    "Name": "Eve",
    "Age": 28,
    "City": "Miami",
    "Salary": 60000
  },
  {
    "Name": "Frank",
    "Age": 40,
    "City": "Seattle",
    "Salary": 95000
  }
]
```

**Error**: Combining DataFrames without ignoring index
```python
# WRONG - Index values will be preserved and cause issues:
more_employees = pd.concat([task2_employees, json_employees])

# CORRECT:
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
```

### Task 3 Issues

**Error**: Forgetting head()/tail() return DataFrames
```python
# WRONG - This just prints, doesn't save:
print(more_employees.head(3))

# CORRECT:
first_three = more_employees.head(3)
```

**Error**: Using wrong method for shape
```python
# WRONG:
employee_shape = more_employees.shape()

# CORRECT - shape is an attribute, not a method:
employee_shape = more_employees.shape
```

### Task 4 Issues

**Error**: Wrong order of operations
```python
# WRONG - Trying to calculate mean before converting to numeric:
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')

# CORRECT - Convert first, then calculate mean:
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
```

**Error**: Forgetting to replace placeholders before converting
```python
# WRONG - 'unknown' will become NaN but wasn't explicitly handled:
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')

# CORRECT:
clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a'], pd.NA)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
```

**Error**: Using .str methods on non-string columns
```python
# WRONG - If Age is numeric, this will fail:
clean_data['Age'] = clean_data['Age'].str.strip()

# CORRECT - Only use .str on string columns:
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
```

**Error**: Not chaining string methods properly
```python
# WRONG - strip() doesn't modify in place:
clean_data['Name'].str.strip()
clean_data['Name'].str.upper()

# CORRECT - Assign result and chain methods:
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
```
