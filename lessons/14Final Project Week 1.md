# Lesson 14 — Web Scraping and Dashboard Project

## **Lesson Overview**
In this lesson, students will scrape baseball history data from the **Major League Baseball History** website and display the results in an interactive dashboard. The project will demonstrate the student's ability to use **Selenium** for web scraping, clean and transform the data, and present it using **Streamlit** or **Dash** with interactive visualizations.

**Learning Objective:** 
By completing this project, students will:
- Use **Selenium** to scrape data from a website.
- Clean and transform the raw data into a structured format.
- Build an interactive dashboard using **Streamlit** or **Dash** to display the insights.
- Apply effective data visualization techniques to communicate their findings.
- Implement interactivity in visualizations to allow users to explore the data.

## **Project Description:**
You will scrape historical baseball data from the [Major League Baseball History](https://www.baseball-almanac.com/yearmenu.shtml) website and present it in a dashboard. The dashboard should include at least three visualizations, and these visualizations should respond to user input such as dropdowns or sliders.

### **Web Scraping:**
1. **Extracting Data:**
   - Use **Selenium** to scrape the data from the website: [Baseball Almanac Year Menu](https://www.baseball-almanac.com/yearmenu.shtml).
   - Extract the relevant information, such as the year, event names, and notable achievements or statistics for each year.
   - Save the raw data in a structured format, such as `.csv` or `.json`.

2. **Handling Challenges:**
   - Handle common scraping challenges such as:
     - Pagination: If the data is spread across multiple pages, ensure pagination is handled correctly.
     - Missing Tags: Some years might have missing data. Handle missing or malformed tags gracefully.
     - User-Agent Headers: Ensure the scraping script mimics a legitimate browser by using appropriate headers.
   - Avoid scraping duplication or making redundant requests to the website.

### **Data Cleaning & Transformation:**
1. **Cleaning Raw Data:**
   - Load the raw data into a **Pandas DataFrame**.
   - Clean the data by handling missing, malformed, or duplicate entries.
   - Document the cleaning process in Markdown or inline comments.
   - Example tasks:
     - Remove unnecessary columns or rows.
     - Standardize the year data format.
     - Remove duplicates or redundant data points.

2. **Data Transformation:**
   - Create new columns or perform aggregations to enable meaningful analysis.
   - For example, you can create new columns based on the event data, filter data based on year, or aggregate data to show year-over-year trends.

### **Data Visualization:**
1. **Creating Visualizations:**
   - Create at least three visualizations using **Plotly**, **Streamlit**, or **Dash**.
     - Examples include:
       - Visualizing trends in notable achievements over time.
       - Displaying distributions of event types across different years.
       - Comparing statistics or rankings based on player performance or events.
   - Ensure each visualization is relevant, well-labeled, and supports the data analysis.

2. **Interactive Components:**
   - Implement interactive elements such as:
     - Dropdowns for selecting different years or event categories.
     - Sliders to adjust the data view (e.g., filter by year or event type).
   - Ensure the visualizations dynamically update when the user interacts with these elements.

### **Dashboard / App Functionality:**
1. **Building the Dashboard:**
   - Build the dashboard using **Streamlit** or **Dash**.
   - Ensure the dashboard layout is clean, intuitive, and easy to navigate.
   - Allow users to explore different aspects of the data, such as filtering by year, player performance, or event type.

2. **User Instructions:**
   - Provide clear titles, instructions, and descriptions to guide users on how to interact with the dashboard.
   - Include tooltips or labels to help users understand the data and visualizations.

### **Code Quality & Documentation:**
1. **Organizing Code:**
   - Organize the code into logical sections or functions (e.g., scraping, cleaning, transformation, and visualization).
   - Ensure that the code is readable with inline comments explaining major steps or choices.
   
2. **Project Documentation:**
   - Include a **README.md** file with the following:
     - A summary of the project and its objectives.
     - Instructions for setting up and running the project.
     - A screenshot or demo of the dashboard.
   - Include a link to your GitHub repository for submission.

---

## **Rubric for Lesson 14 - Web Scraping and Dashboard Project**

### **Web Scraping (30 points)**

- [ ] **Appropriate Libraries**: Uses **Selenium** to retrieve data from the web or an equivalent scraping tool.
- [ ] **Handling Scraping Challenges**: Correctly handles common scraping challenges like missing tags, pagination, and user-agent headers.
- [ ] **Data Structure**: Saves raw data in a structured format such as `.csv` or `.json`.
- [ ] **Redundancy Prevention**: Ensures the scraper avoids scraping duplicate or redundant data.

### **Data Cleaning & Transformation (25 points)**

- [ ] **Data Loading**: Loads raw data into a **Pandas DataFrame** or equivalent structure.
- [ ] **Cleaning**: Effectively handles missing, duplicate, or malformed entries.
- [ ] **Transformation**: Applies appropriate transformations or filters to prepare the data for analysis.
- [ ] **Before/After Documentation**: Shows before/after stages of cleaning or reshaping data.

### **Data Visualization (25 points)**

- [ ] **Visualizations**: Includes at least three high-quality visualizations using **Plotly**, **Streamlit**, or **Dash**.
- [ ] **Relevance**: Visualizations are relevant, well-labeled, and support the data analysis.
- [ ] **Interactivity**: Implements user interactions such as dropdowns, sliders, or checkboxes to filter and explore the data.
- [ ] **Responsive Design**: Visualizations respond correctly to user input or filters.

### **Dashboard / App Functionality (10 points)**

- [ ] **Layout and Components**: The dashboard is clean, responsive, and allows users to explore the data easily.
- [ ] **Clear Instructions**: Includes clear titles, descriptions, and instructions for users.
- [ ] **Exploration Features**: Allows users to explore different aspects of the data (e.g., filter by year, event type, etc.).

### **Code Quality & Documentation (10 points)**

- [ ] **Code Organization**: Code is well-organized with logical sections and functions.
- [ ] **Inline Comments**: Major steps and logic are explained with inline comments.
- [ ] **README.md**: Includes a summary, setup instructions, and a screenshot of the dashboard.

---

## **Submission Instructions:**
1. **Submit the Link**: Submit the link to your GitHub repository with all code files, data files (if applicable), and the README.md.
2. **Final Project Presentation**: Provide a brief explanation of your dashboard functionality and insights during the presentation. Be ready to explain the rationale behind the visualizations and any conclusions drawn from the data.

---

## **Final Project Submission Deadline:**
- **Due**: [Date]
