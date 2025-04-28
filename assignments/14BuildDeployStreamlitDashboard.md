# CTD_Assignment_14: Build and Deploy a Streamlit Dashboard

This assignment is to be implemented using **Streamlit**.  
You will **import a dataset**, **build a dashboard**, **visualize insights**, **showcase data cleaning**, and **deploy your app** to **Streamlit Community Cloud**.

---

## **Task 1: Import a Dataset**
- Choose a public dataset (CSV, Excel, or through an API).
- Import the dataset into your Python script using Pandas.
- Display the first few rows (`.head()`) to give an overview of the data.

**Tips**: You can find datasets on Kaggle, UCI Machine Learning Repository, or other open sources.

---

## **Task 2: Data Cleaning**
- Identify any missing or inconsistent values.
- Handle missing data by either:
  - Filling (e.g., with mean/median/mode) or
  - Dropping missing values.
- Rename columns if necessary for clarity.
- Display a brief before/after summary of your cleaning process in your app.

**Tip**: Use Streamlit components like `st.write()` and `st.dataframe()` to show the changes.

---

## **Task 3: Build a Streamlit Dashboard**
1. Add a **title** and **description** of the dashboard.
2. Add a **sidebar** with:
   - Filters like dropdowns (`st.selectbox()`), sliders (`st.slider()`), or multiselect (`st.multiselect()`).
3. Create the following sections:
   - **Dataset Overview**: Show a table or key summary statistics.
   - **Data Cleaning Summary**: Explain what cleaning steps were taken.
   - **Visualizations**: (See next task)

---

## **Task 4: Create Visualizations**
- Create at least **two different types** of visualizations:
  - Example: Bar chart, line chart, pie chart, scatter plot, or a histogram.
- Make visualizations **interactive** using either:
  - Streamlit’s built-in plotting (`st.line_chart()`, `st.bar_chart()`)  
  - or integrate external libraries like **Plotly** or **Matplotlib**.
- Visualizations should update based on user selections in the sidebar.

📌 **Tip**: Use `st.plotly_chart()` for Plotly charts, `st.pyplot()` for Matplotlib.

---

## **Task 5: Get Creative **
- Add **at least one extra feature**. Some ideas:
  - Use `st.map()` to plot geographic data if available.
  - Add a `st.checkbox()` to hide/show parts of the dashboard.
  - Create tabs using `st.tabs()` to organize sections.
  - Allow file downloads (like a cleaned CSV) using `st.download_button()`.

---

## **Task 6: Deploy Your App**
1. Create a **GitHub repository** and push your Streamlit app code.
2. Deploy your app to **Streamlit Community Cloud**:
   - Go to [Streamlit Cloud](https://streamlit.io/cloud).
   - Connect your GitHub repository.
   - Set up and deploy the app.
3. Make sure your app **loads successfully** and is publicly accessible.

---

## **Task 7: Submit Your Assignment**

✅ **What to submit:**
- Paste your **Streamlit Community Cloud app URL** (deployment link).
- Paste your **GitHub repository URL** where your code is stored.

you can see this for streamit cheatsheet:
https://cheat-sheet.streamlit.app/


🔗 Example Submission:
https://canada.streamlit.app/
https://github.com/parker84/canada-dashboard

https://dash-board.streamlit.app/
https://github.com/dataprofessor/dashboard-v2