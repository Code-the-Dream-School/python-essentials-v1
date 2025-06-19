# Assignment 12: Advanced Data Visualization

This assignment is to be created in the `assignment12` folder of your `python-assignment12` directory which is a separate repository. Continue to work in the ``assignment12`` branch.

---


## **Task 1: Plotting with Pandas**
1. Create a file called employee_results.py.
2. Load a DataFrame called employee_results using SQL.  Copy the `db/lesson.db` database from your `python_homework` folder to your `python-assignment12` folder.  Copy the `db` folder and the `lesson.db` file within it.  This can be done using the `cp -r` command.  In your `assignment12` folder, connect to `../db/lesson.db`. You use SQL to join the employees table with the orders table with the line_items table with the products table.  You then group by employee_id, and you SELECT the last_name and revenue, where revenue is the sum of price * quantity.  Ok, that's a lot of SQL to mess with, so here is the statement you need:
   ```SQL
   SELECT last_name, SUM(price * quantity) AS revenue FROM employees e JOIN orders o ON e.employee_id = o.employee_id JOIN line_items l ON o.order_id = l.order_id JOIN products p ON l.product_id = p.product_id GROUP BY e.employee_id;
   ```
3. Use the Pandas plotting functionality to create a bar chart where the x axis is the employee last name and the y axis is the revenue.
4. Give appropriate titles, labels, and colors.
5. Show the plot.

---

## **Task 2: A Line Plot with Pandas**
1. Create a file called cumulative.py.  The boss wants to see how money is rolling in.  You use SQL to access `../db/lesson.db` again.  You create a DataFrame with the order_id and the total_price for each order.  This requires joining several tables, GROUP BY, SUM, etc.
2. Add a "cumulative" column to the DataFrame.  This is an interesting use of apply():
   ```python
   def cumulative(row):
      totals_above = df['total_price'][0:row.name+1]
      return totals_above.sum()

   df['cumulative'] = df.apply(cumulative, axis=1)
   ```
   Because axis=1, apply() calls the cumulative function once per row.  Do you see why this gives cumulative revenue?  One can instead use cumsum() for the cumulative sum:
   ```python
   df['cumulative'] = df['total_price'].cumsum()
   ```
3. Use Pandas plotting to create a line plot of cumulative revenue vs. order_id.
4. Show the Plot.

---

## **Task 3: Interactive Visualizations with Plotly**

1. Load the Plotly wind dataset, via the following:
   ```python
   import plotly.express as px
   import plotly.data as pldata
   df = pldata.wind(return_type='pandas')
   ```
   Print the first and last 10 lines of the DataFrame.
2. Clean the data.  You need to convert the 'strength' column to a float.  Use of str.replace() with regex is one way to do this, followed by type conversion.
3. Create an interactive scatter plot of strength vs. frequency, with colors based on the direction.
4. Save and load the HTML file, as `wind.html`.  Verify that the plot works correctly.

---

## **Task 4: A Dashboard with Dash**

Ok, deep breath.  Start by copying `python-assignment12/assignment12/lesson11_c.py` to `python-assignment12/myapp.py`. We can reuse the template.  This is in the root of the project folder because you are going to deploy this to the cloud in Task 5.

1. The dataset to use is the Plotly built in `gapminder` dataset.  This has, among other things, the per capita GDP for various countries for each year.  For a given country, there will be one row per year.  This means that the 'countries' column has many duplicates.
2. You want a dropdown that has each unique country name. You create a Series called `countries` that is the list of countries with duplicates removed.  You use this Series to populate the dropdown.  Give the dropdown the initial value of 'Canada'.
3. You give the dropdown the id of 'country-dropdown' and also create a dcc.Graph with id 'gdp-growth'.
4. You create the decorator for the callback, associating the input with the dropdown and the output with the graph.
5. The decorator decorates an `update_graph()` function.  This is passed the country name as a parameter.  You need to filter the dataset to get only the rows where the country column matches this name.  Then you create a line plot for 'year' vs. 'gdpPercap`.  Give the plot a descriptive name that includes the country name.
6. The line to run the app doesn't need to change.
7. Run the program, and check it out in the browser.  Make bug fixes as needed.

---

## **Task 5: Deploying to Render.com**

1. Create a free account at Render.com.
2. Change `myapp.py` to add a line:
   ```python
   app = Dash(__name__)
   server = app.server # <-- This is the line you need to add
   ```
3. Add, commit, and push your changes to GitHub.  If you are using a branch, create a PR and merge that branch with main.
4. Go to your render.com dashboard and create a new web service.  Provide the public URL of your python-assignment12 repository.  You must specify a unique name.  The default name is the same as your GitHub repository, so that will likely conflict with another student.
5. The "Start Command" for the web service should be changed to read:
   ```
   gunicorn myapp:server
   ```
   The gunicorn package is a Python web server, which is used to run the Flask server for your Dash app.
6. Click the "Deploy Service" button.
7. Wait. Wait. Wait. The Render free plan is not fast.
8. Eventually, it will say that the service is running.  Wait.  Wait some more.
9. Click on the https link for your service in the upper part of your render.com dashboard.  Wait.  Wait.  Keep waiting.
10. After a while, you'll see the app!  Congratulations, you are live! 

---

## **Task 6: Reflection**
Create a file in the assignment12 folder called reflection.txt, and put in the following thoughts:

1. Reflect on the differences between static and interactive visualizations.
2. Write a short paragraph discussing the advantages of using dashboards for real-time data exploration.
3. Explain how interactive tools like Plotly and Dash can improve data communication in professional settings.

## **Task 7: Commit Your Work**

Add and commit all of the files created for the assignment to the `assignment12` branch.

---

#  Optional Assignment on Streamlit

You can use either Dash or Streamlit for your capstone project.

## Overview
This assignment is to be implemented using **Streamlit**.  
You will **import a dataset**, **build a dashboard**, **visualize insights**, **showcase data cleaning**, and **deploy your app** to **Streamlit Community Cloud**.

### Requirements
- Import a dataset that has already been cleaned and prepared
- Explain what cleaning and preparation was done
- Visualize key insights through interactive dashboards
- Deploy your app using Streamlit Community Cloud

## Task 1: Project Setup

1. Create a new folder called ``streamlit-assignment`` for your project on your local machine.  It will be initialized as a git repository, so make sure it is outside of any other git repository.  

2. Initialize a Git repository inside this folder:
```bash
git init
```

3. Create a .gitignore file and make sure it includes:
```bash
.venv/
__pycache__/
*.pyc
.DS_Store
```

4. Set up a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # on macOS/Linux
.venv\Scripts\activate     # on Windows
```

5. Create requirements.txt file.  You can use the same requirements.txt file which you used for the Streamlit lesson.
```bash
streamlit
pandas
plotly
numpy
matplotlib
```
6. Install the dependencies. Run following command in your vs code terminal.
```bash
pip install -r requirements.txt
```
7. Create a Python file named `streamlit_app.py` in your project folder.
   This is the main script Streamlit will run when deploying your app.

## Task 2: Build Your Streamlit Dashboard

### Required Components

1. **Title and Description**
   - Use `st.title()` and `st.markdown()` to introduce your dashboard

2. **Dataset Overview**
   - Import your cleaned dataset using Pandas.
   - Display the dataset using `st.dataframe()` or `st.write()`
   - Optionally, summarize with `.describe()` or key statistics

3. **Data Cleaning Summary**
   - Briefly describe what cleaning steps you performed
   - Optional: Show comparison table (raw vs cleaned)

4. **Visualizations**
   - Include at least two interactive charts
   - Examples: bar chart, pie chart, line chart, scatter plot, histogram
   - Use Streamlit's built-in charts or libraries like Plotly/Matplotlib


## Task 3: Deploy Your App
1. Create a **GitHub repository** and push your code:
   - Log in to your GitHub account and create a new repository.(https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)
   - Copy the repository URL.
   - Link your local project folder to the GitHub repository:
     ```bash
     git remote add origin <repository-url>
     ```
   - Add and commit your changes:
     ```bash
     git add .
     git commit -m "Initial commit"
     ```
   - Push your code to the GitHub repository:
     ```bash
     git branch -M main
     git push -u origin main
     ```
2. Deploy to **Streamlit Community Cloud**:
   - Visit [Streamlit Cloud](https://streamlit.io/cloud) and log in with your Streamlit account. If you don't have an account, create one using your email or GitHub credentials.

   - Click on the **"New App"** button to start the deployment process.

   - In the **"Select a repository"** section:
      - Connect your GitHub account if you haven't already.
      - Choose the repository where your Streamlit app code is stored.

   - In the **"Branch"** dropdown, select the branch containing your code (usually `main`).

   - In the **"Main file path"** field, specify the path to your Streamlit app file (e.g., `streamlit_app.py`).

   - Click **"Deploy"** to start the deployment process.

   - Wait for the deployment to complete. Once done, you will see a URL where your app is hosted.

   - Test your app by visiting the provided URL to ensure everything works as expected.

   - If you need to make updates to your app, push the changes to your GitHub repository. Streamlit Cloud will automatically redeploy your app with the latest changes.
3. Verify your app loads successfully and is publicly accessible

## Task 4: Submit Your Assignment

### Required Submissions
- Your **Streamlit Community Cloud app URL** (deployment link), this link is added to the ``service_urls.txt`` in the ``assignment12` folder in the `python-assignment12` repo.
- Your **GitHub repository URL** link is also added to the `service_urls.txt`
- Add and commit the `service_urls.txt` file in the `assignment12` branch.

### Resources
- [Streamlit Cheat Sheet](https://cheat-sheet.streamlit.app/)

### Example Submissions
1. Canada Dashboard:
   - App: https://canada.streamlit.app/
   - Code: https://github.com/parker84/canada-dashboard

2. Dashboard v2:
   - App: https://dash-board.streamlit.app/
   - Code: https://github.com/dataprofessor/dashboard-v2

---

### **Submit Your Assignment on GitHub**  

📌 **Follow these steps to submit your work:**  

#### **1️⃣ Add, Commit, and Push Your Changes** 
- Create a file called `service_urls.txt` in the assignment12 folder.  In it, paste the URL for your Render.com service.  If you did the Streamlit assignment, make sure the Streamlit github repository url and streamlit.io service url are added to the `service_urls.txt` file as well.
- Within your `python-assignment12` folder, do a git add and a git commit for the files you have created, so that they are added to the `assignment12` branch.
- Push that branch to GitHub. 

#### **2️⃣ Create a Pull Request**  
- Log on to your GitHub account.
- Open your `python-assignment12` repository.
- Select your `assignment12` branch.  It should be one or several commits ahead of your main branch.
- Create a pull request.

#### **3️⃣ Submit Your GitHub Link**  
- Your browser now has the link to your pull request.  Copy that link. 
- Paste the URL into the **assignment submission form**.
- if you did the optional Streamlit assignment, make sure that repository link and the url for the streamlit.io service are included in the `service_urls.txt` file. 

To summarize, a pull request for the `assignment12` branch in your new `python-assignment12` repository is pasted into the link submission field in the **assignment submission form**.  The `render.com` Dash service is published in `service_urls.txt` file. If you do the streamlit assignment, the link for the `streamlit-assignment` repository and the url for the `streamlit.io` service are included in the `service_urls.txt` file.

---
