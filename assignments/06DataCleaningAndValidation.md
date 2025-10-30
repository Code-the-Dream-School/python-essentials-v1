## Lesson 6 Assignment — Data Cleaning and Validation I
### Data Cleaning and Validation with Pandas

### **Objective:**
This assignment gives you practice in several data manipulation techniques. In subsequent sections, the focus is on exploring fundamental data cleaning and validation techniques using the Pandas library in Python. You will learn how to handle missing data, transform data types, remove duplicates, manage outliers, standardize data, encode categorical variables, and validate data ranges.

This assignment is to be created in a Kaggle notebook, as you did for Assignment 5.  This time, create a notebook called CTD_Assignment_6 for code as described below.

### **Tasks:**

### **Task 1: Practice Pivot Tables**

1. In the upper right of your notebook page click on "Add Input" and then "Datasets".  Search on "Ecommerce Consumer Behavior".  You should find a dataset from Salahuddin Ahmed.  Click on the plus button to add this one to your notebook.

2. Resolve the file you need to read, by running the first cell in your notebook. Then read the file into a DataFrame called `ecommerce`.  Print out the first 5 rows, so that you know what the data looks like.

3. In the following step, you will want to sum the Purchase_Amount values.  Unfortunately, this column is stored as a string.  Replace the column with one that converts the string to a float.  You will need to take the dollar sign off before conversion.

4. Create a "buying_patterns" pivot table from the data.  The index should be the 'Purchase_Category'.  The columns should be 'Gender' and 'Income_Level'.  The value you sum should be 'Purchase_Amount'.  Print out the resulting DataFrame.

5. Create a "demographics" pivot table from the ecommerce DataFrame.  You want two levels of index, on 'Income_Level' and 'Education_Level'.  For columns you want 'Marital_Status'.  You want to count the 'Customer_ID' values.  Print out the resulting DataFrame.

### **Task 2: Practice apply()**

1. Add another input.  This time, you search for "AI-Powered Job Recommendations".  You should find a dataset from Samay Ashar.  

2. Create a new code cell.  Add code to resolve the name of the file you need to read.  For this part, you use the job recommendations file.  Read it into a DataFrame called "jobs".  Print out the first 10 lines, so that you know what the column names are.

3. Use the `apply()` method to create an additional column in the jobs DataFrame called 'Check These Out'.  Give that a value of "Yes" if the job is entry level, has a salary greater than or equal to 70000, and requires both SQL and Python.  Give the column a value of "No" otherwise.

4. Create a DataFrame called "my_jobs".  Select the rows from "jobs" that have a 'Check These Out' column value of 'Yes'.  Print out the first 10 lines.

### **Task 3: Handling Missing Data**

1. **Create a DataFrame using the provided data:**

   - Add another input dataset.  This time, search on "code the dream lesson 5"
   - Create another code block.
   - Resolve the name of the file as usual.
   - Read it into a DataFrame called df.
   - The DataFrame contains columns for 'Name', 'Age', 'Salary', 'Join Date', and 'City', with some missing values.
   - Print the original DataFrame.
  
Here's a summary of what the DataFrame looks like to help you get started (but don't use this code):

```python
data = {
    'Name': ['Alice', 'Bob', None, 'David', 'Eva'],
    'Age': [25, None, 35, 40, 30],
    'Salary': [50000, 60000, None, 80000, 55000],
    'Join Date': ['2020-01-01', None, '2020-03-15', '2020-04-20', None],
    'City': ['New York', 'Los Angeles', 'Chicago', None, 'Miami']
}
df = pd.DataFrame(data)
```

2. **Perform the following operations on new DataFrames:**
     - Create df1 by using `dropna()` on the df DataFrame created above.  Print the `info()` for df and df1 to see how many lines have missing values.
     - **Replace missing values** in df using the `fillna()` method:
     - Replace missing 'Name' values with `'Unknown'`.
     - Replace missing 'Age' values with the **mean** of the 'Age' column.
     - Replace missing 'Salary' values with the **median** of the 'Salary' column.
     - Replace missing 'Join Date' values with `'2020-01-01'`.
     - **Remove rows with missing values** using the `dropna()` method and save the result in df2.  Only the 'City' column should have missing values at this point.  Reset the index.
     - Convert the 'Age' column in df2 to **integer** type using `astype(int)`.
     - Print the updated df2 DataFrame.

### **Task 4: Data Transformation**
1. **Convert Data Types:**
   - Add another input.  This time search for "Code The Dream Eclipses".  This is a list of eclipses that were or will be observed in Arkansas.
   - Load the CSV file into a DataFrame called df3.  **Note:** The separator is "|" for this CSV file.
   - Print df3.info() and the first 5 rows of df3.
   - Attempt to convert the 'Date' column to **datetime** format using `pd.to_datetime()`.  You will see that an error is thrown for an invalid date.
   - Add `errors='coerce` to your `pd.to_datetime()` statement and try the conversion again.
   - Print the first 20 lines of the revised df3.  Examine what is stored for the dates that could not be converted.

### **Task 5: Removing Duplicates**
1. **Identify and remove duplicate records:**
   - Print `df3.info()`.
   - Use the `duplicated()` method to identify duplicate rows in the DataFrame, and save the result in duplicate_series.  This Series has `True` for each duplicate entry.
   - Print `duplicate_series[duplicate_series == True].head(10)` to see the first 10 duplicated entries.
   - Print `duplicate_series.value_counts()` to see how many duplicates you have.
   - Use the `drop_duplicates()` method to remove duplicate rows.
   - Print `info()` for the updated DataFrame.
  
By default, `drop_duplicates()` keeps the first occurrence of each duplicate row. You could use the `keep` parameter to change this behavior, but the default is ok for now.

### **Task 6: Handling Outliers**
1. **Identify and replace outliers in the 'Age' column:**
   - For this and the following tasks, use df2 again.
   - Consider outliers as values greater than 100 or less than 0.
   - Replace outliers with the **median** of the 'Age' column.
   - Print the updated DataFrame after handling outliers.

Outliers can also be identified using statistical methods like the Interquartile Range (IQR) or Z-scores -- but we'll just keep it simple for now

### **Task 7: Standardizing Data**
1. **Standardize the 'Name' column:**
   - Convert all names to lowercase and trim any leading or trailing whitespace using `str.lower()` and `str.strip()`.
   - Print the updated DataFrame.

2. **Standardize inconsistent entries in the 'City' column:**
   - Find variations in the City name:
   ```python
   print(df.groupby('City').agg({'Name': 'count'})) # This will show all city names, so you can see variations
   ```
   - Replace variations like 'NYC' with 'New York' and 'LA' with 'Los Angeles'.
   - Print the updated DataFrame.

### **Task 8: Validating Data Ranges**
1. **Ensure the 'Age' column contains values within the valid range (18 to 65):**
   - Replace invalid ages (less than 18 or greater than 65) with a NaN value.  (NaN is actually part of numpy: `np.nan` is the value you should use.  Don't use the string 'NaN'!)
   - Print the updated Dataframe.
   - Fill the NaN values with the **median** of the 'Age' column.
   - Print the updated DataFrame.

**Explanation:** Validating data ranges ensures that your data is consistent and suitable for analysis or modeling.

### **Submit the Notebook for Your Assignment**  

📌 **Follow these steps to submit your work:**  

#### **1️⃣ Get a Sharing Link for Your Assignment**  
- On the upper right of the Kaggle page, click on Save Version and save, accepting all defaults.  You can just do a quick save.
- On the upper right, click on Share.  Choose Public, make sure that Allow Comments is on, and copy the public URL to your clipboard.

#### **2️⃣ Submit Your Kaggle Link**  
- Paste the URL into the **assignment submission form**.  

---
