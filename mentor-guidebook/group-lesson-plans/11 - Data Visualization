### **Group Mentor Guide: Introduction to Data Visualization**

#### **About This Week**
This week, students transition from data manipulation to **data visualization** using two primary Python libraries: **Matplotlib** and **Seaborn**. The goal is for students to effectively "tell stories" with data by creating line plots, bar charts, histograms, heatmaps, and pair plots. By the end of this lesson, students will be able to customize these visualizations with labels, titles, and color palettes to enhance their ability to communicate data insights.

#### **Explore Session (60 minutes)**
**Purpose:** Reinforce the foundational concepts of data visualization and build comfort with basic syntax before moving to the assignment.
**Materials:** Mentor slides, Python environment (local shell or Kaggle notebook), and chat for participation.

##### **Segment 1 – Warm-Up (5 min)**
*   **Ask:** “Why do we use visualizations instead of just looking at raw data tables?”
*   **Quick poll:** “Which library is built on top of the other: Matplotlib or Seaborn?” (Answer: Seaborn is built on Matplotlib).

##### **Segment 2 – I Do (10 min)**
**Mentor demonstrates Matplotlib basics:**
*   **Explain:** The different roles of **Line Plots** (trends), **Bar Plots** (categorical comparisons), and **Histograms** (distributions).
*   **Demonstrate:** Creating a basic Line Plot with `plt.plot()`, adding a title with `plt.title()`, and labeling axes with `plt.xlabel()` and `plt.ylabel()`.
*   **CFU Questions:** 
    *   “What happens if you run your code but forget to include `plt.show()`?”
    *   “Why is it important to use markers or different line styles in a line plot?”

##### **Segment 3 – We Do (20 min)**
**Collaborative example: Statistical Visualizations with Seaborn.**
*   **Discuss:** **Correlations** and how they are represented in a **Heatmap** (values between -1.0 and 1.0).
*   **Walkthrough:** Look at the Titanic dataset examples and discuss why a **Pair Plot** is useful for multivariate analysis.
*   **CFU Questions:**
    *   “In a Heatmap, what would a strong negative correlation look like visually?”
    *   “When would you choose Seaborn over basic Matplotlib?”

##### **Segment 4 – You Do (20 min)**
**Short Task: Data Interpretation.**
*   Show the **Titanic Correlation Heatmap** and ask students: “Based on this visual, which factors most strongly affected who survived?”
*   Have students suggest a specific color palette from the documentation to use for a bar plot.

##### **Segment 5 – Wrap-Up (5 min)**
*   Summarize key takeaways: Basic plots (Matplotlib) vs. Statistical plots (Seaborn).
*   **Remind:** The assignment requires a **Kaggle notebook** and uses the "Diabetes Health Indicators Dataset".
*   **Deadline:** Assignments are due **Feb 10, 2026**.

#### **Apply Session (60 minutes)**
**Purpose:** Support students as they work through the assignment tasks, specifically focusing on data understanding and complex plot customization.

##### **Segment 1 – Quick Recap (5 min)**
*   **Ask:** “What was the most surprising thing you found when looking at the 22 columns of the Diabetes dataset?”
*   Address any initial hurdles with **Kaggle** setup.

##### **Segment 2 – Guided Coding (25 min)**
**Mentor demonstrates Task 4 (General Health over Time):**
*   Show how to use `groupby()` on "Age" and aggregate using `mean()`.
*   **Logic Check:** Explain the step of subtracting `GenHlth` from 5 so that higher values represent better health.
*   **CFU Questions:**
    *   “Why do we need to use `sort_index()` before plotting the line chart?”
    *   “What story does the resulting line plot tell about health and age?”

##### **Segment 3 – Peer or Solo Debugging (20 min)**
*   **Common Bug:** Help students who find the **Task 5 Heatmap** "hard to read" by demonstrating how to **subset** the correlation matrix as required in Task 6.
*   **Advanced Task:** Discuss using `qcut()` to divide "BMI" into 10 quantiles for a more readable pair plot.
*   **Mentor Tip:** Remind students they can ignore deprecation warnings when creating the Seaborn heatmap.

##### **Segment 4 – Wrap-Up and Reflection (10 min)**
*   **Mindset Discussion:** “Problem solving is a learned skill. How did you handle it today when you felt like you had 'no idea how to get started'?”
*   **Final Reminder:** Ensure they save their Kaggle version and set the sharing permissions to **Public** before submitting the URL.
