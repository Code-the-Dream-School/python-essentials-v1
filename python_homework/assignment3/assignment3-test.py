import assignment3 as a3
import numpy as np
import pandas as pd
import os

test1_df = pd.DataFrame({   'Name': ['Alice', 'Bob', 'charlie'], 
                            'Age': [25, 30, 35], 
                            'City': ['New York', 'Los Angeles', 'Chicago']})

# Task 1
def test_data_frame_from_dictionary():
    assert test1_df.equals(a3.task1_data_frame)

def test_added_column():
    assert a3.task1_with_salary['Salary'].equals(pd.Series([70000, 80000, 90000]))

def test_increment_column():
    assert a3.task1_older["Age"].equals(pd.Series([26, 31, 36]))

def test_write_csv():
    assert os.access("./employees.csv", os.F_OK) == True
    # make sure there is no index
    assert pd.read_csv('employees.csv').shape == (3, 4)
    


# Task 2
def test_read_data_frame_from_csv():
    assert a3.task1_older.equals(a3.task2_employees)

test2_json_df = pd.DataFrame({ 'Name': ['Eve', 'Frank'],
                                'Age': [28, 40],
                                'City': ['Miami', 'Seattle'],
                                'Salary': [60000, 95000]})

def test_read_data_frame_from_json():
    assert os.access("./additional_employees.json", os.F_OK) == True
    assert a3.json_employees.equals(test2_json_df)

def test_concat_json_employees():
    assert a3.more_employees.equals(pd.concat([a3.task2_employees, a3.json_employees], ignore_index=True))
    assert a3.more_employees.shape == (5, 4)


# Task 3
def test_head():
    assert a3.first_three.equals(a3.more_employees.head(3))

def test_tail():
    assert a3.last_two.equals(a3.more_employees.tail(2))

def test_shape():
    assert a3.employee_shape == (5, 4)


# Task 4
from io import StringIO
sample_data = """Name,Age,Salary,Hire Date,Department
Alice, 29,50000,2021/01/15, Sales 
Bob, 32, unknown,2020-03-18,MARKETING
 charlie, NaN, 70000,3/25/2019,marketinG
Dana, 41, n/a,2020/12/01, HR
Eve, 24,65000,2021/06/07,  hr
Frank, 32,75000, 2019-07-11,Sales
Bob, 32, unknown,2020-03-18,MARKETING
"""
# Read into DataFrame
ddf = pd.read_csv(StringIO(sample_data))
tdf = ddf.copy()

# Perform the same cleaning steps
tdf.drop_duplicates(inplace=True)
tdf['Age'] = pd.to_numeric(tdf['Age'], errors='coerce')
tdf['Salary'] = tdf['Salary'].replace(['unknown', 'n/a'], pd.NA)
tdf['Salary'] = pd.to_numeric(tdf['Salary'], errors='coerce')
tdf['Hire Date'] = pd.to_datetime(tdf['Hire Date'], errors='coerce')
tdf['Name'] = tdf['Name'].str.strip()
tdf['Department'] = tdf['Department'].str.strip().str.upper()

def test_dirty_data_read():
    assert a3.dirty_data.equals(ddf)

def test_no_duplicate_rows():
    assert len(a3.clean_data) == 6

def test_age_numeric():
    assert pd.api.types.is_numeric_dtype(a3.clean_data['Age'])
    assert a3.clean_data['Age'].dropna().between(1, 100).all()

def test_salary_numeric():
    assert pd.api.types.is_numeric_dtype(a3.clean_data['Salary'])

def test_no_missing_age_or_salary():
    assert not a3.clean_data['Age'].isnull().any() 
    assert not a3.clean_data['Salary'].isnull().any()

def test_hire_date_datetime():
    assert pd.api.types.is_datetime64_any_dtype(a3.clean_data['Hire Date'])

def test_department_uppercase():
    all_upper = True
    for dept in a3.clean_data['Department']:
        if not dept.isupper():
            all_upper = False
    assert all_upper

# If dates are not converted properly with form="mixed" will end up with NaTs
def test_hire_date_notNAT():
    nat_count = a3.clean_data['Hire Date'].isna().sum()
    assert nat_count == 0


























