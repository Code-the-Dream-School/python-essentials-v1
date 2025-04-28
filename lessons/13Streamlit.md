# Building Interactive Apps with Streamlit

## Lesson Overview

**Learning objective:** Learn to create interactive web applications for data visualization and analysis using Streamlit.

Topics: 
  * Introduction to Streamlit and its benefits
  * Basic Streamlit components and layout
  * Interactive data visualization with Streamlit
  * Deploying Streamlit applications

## What is Streamlit?

Streamlit is a Python library that makes it easy to create custom web apps for machine learning and data science. It turns data scripts into shareable web apps in minutes, not weeks.

### Key Features
* Simple Python-first syntax
* Rich set of UI components
* Easy integration with data science libraries
* Quick deployment options

### Installation and Setup

First, let's set up a virtual environment and install Streamlit:
Create a project folder named streamlit_project.
Open the project folder in VSCode or any IDE of your choice.

In the terminal:

#  Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# For Windows (Git Bash):
source .venv/Scripts/activate
# For macOS/Linux:
source .venv/bin/activate

# Verify installation
streamlit --version

# create requirements.txt file
streamlit==1.24.0
pandas==1.5.3
plotly==5.15.0
numpy==1.24.3

# install dependencies
pip install -r requirements.txt


Note: Make sure you see `(.venv)` in your terminal prompt, indicating that the virtual environment is active, before installing Streamlit. You'll need to activate the virtual environment each time you open a new terminal session.


## Basic Streamlit Components
### Text and Data Display

In this section, you will learn to display basic text, markdown, and data elements using Streamlit.
#### Exercise 1: Text and Data Display
- Create a python script app.py

import streamlit as st

# Basic text elements
st.title("My First Streamlit App")
st.header("Section 1")
st.subheader("Header")
st.subheader("Subheader")
st.text("Simple text")
st.markdown("**Bold** and *italic* text")

# Display data
st.write("Automatic data display")
st.code("print('Hello World')", language='python')
st.latex("\int_{a}^{b} x^2 dx")

- at this point you can execute app.py by running 'streamlit run app.py' in your terminal and in your browser paste 'http://localhost:8501'. You will be seeing the components you just typed.

- You can refresh your browser tab (http://localhost:8501) or use the 'Always rerun' option on the Streamlit page for automatic updates.

#### Exercise - 2
### Data Input Components

# Text input
st.header("Section 2")
name = st.text_input("Enter your name", "John Doe")
description = st.text_area("Description", "Write something...")

# Numeric input
age = st.number_input("Age", min_value=0, max_value=120, value=25)
score = st.slider("Score", 0, 100, 50)

# Selection widgets
option = st.selectbox("Choose an option", ["A", "B", "C"])
options = st.multiselect("Multiple options", ["X", "Y", "Z"])

# Date and time
date = st.date_input("Select date")
time = st.time_input("Select time")

# File uploader
uploaded_file = st.file_uploader("Choose a file")

# Buttons and checkbox
if st.button("Click me"):
    st.write("Button clicked!")
    
if st.checkbox("Show/Hide"):
    st.write("Visible content")

- you can again now refresh your tab in browser to see the updated output.


## Exercise 3: Layout and Containers
st.header("Section 3")
# Columns
col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
    st.write("Content for column 1")
with col2:
    st.header("Column 2")
    st.write("Content for column 2")

# Expandable sections
with st.expander("Click to expand"):
    st.write("Expanded content here")

# Sidebar
st.sidebar.title("Sidebar")
sidebar_option = st.sidebar.selectbox("Select option", ["A", "B", "C"])


## Exercise 4: Building a Simple Dashboard
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Create sample data
np.random.seed(42)
sample_data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
    'Sales': np.random.randint(100, 500, size=4),
    'Profit': np.random.randint(20, 100, size=4)
}
df = pd.DataFrame(sample_data)

# Sidebar filters
st.sidebar.header('Filter Options')
selected_product = st.sidebar.selectbox('Select Product', df['Product'])

# Filter data
filtered_df = df[df['Product'] == selected_product]

# Main content
st.title('Simple Product Dashboard')

# Metrics
col1, col2 = st.columns(2)
with col1:
    st.metric('Sales', f"${filtered_df['Sales'].values[0]:,}")
with col2:
    st.metric('Profit', f"${filtered_df['Profit'].values[0]:,}")

# Bar chart
st.subheader('Sales and Profit Comparison')
bar_chart = px.bar(df, x='Product', y=['Sales', 'Profit'], barmode='group')
st.plotly_chart(bar_chart)

## Conclusion
 You now know how to:
- Create basic Streamlit apps
- Add input forms, layouts, and sidebars
- Build simple dashboards with metrics and charts