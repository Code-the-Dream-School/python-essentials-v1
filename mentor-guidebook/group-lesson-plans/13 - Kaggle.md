## **Lesson 13: Capstone Project: Kaggle Dataset — Group Mentor Guide**

Welcome to Week 13! This week marks the beginning of the students' final capstone phase. Students will be transitioning from structured lessons to an open-ended **data pipeline project**, where they must demonstrate their ability to load, clean, analyze, and visualize real-world data using Python and Pandas.

### **Warm-Up (5–10 minutes)**
**Mindset: Managing Imposter Syndrome**
*   The tech industry can often trigger feelings of self-doubt. Mike Cannon-Brookes suggests that even CEOs of major tech companies experience this. 
*   **Discussion:** Have you ever felt like you didn't "belong" or were worried someone would find out you didn't know everything? How do you handle those feelings of self-doubt while working on a complex project like this capstone?

### **Check for Understanding (Theory)**
*   What is the primary goal of a **data pipeline**? (Answer: To demonstrate the full lifecycle of data: loading, cleaning, aggregation, and visualization).
*   Why is it important to document data cleaning in **Markdown blocks** rather than just code comments? (Answer: It makes the analysis reproducible and helps non-technical stakeholders understand the "why" behind data changes).
*   What is the difference between a simple aggregation and **feature engineering**? (Answer: Aggregation groups existing data to find trends; feature engineering creates new columns/data points to derive deeper insights).

### **Explore vs. Apply — Session Formats**
*   **Explore Sessions** → Review the four provided datasets (Global Superstore, TMDB Movies, WHO Life Expectancy, Seattle Airbnb) to help students choose the one that matches their interests.
*   **Apply Sessions** → Live-code a "mini-pipeline" using a sample CSV to demonstrate how to use `info()` to find null values and `groupby()` to create a meaningful aggregation.

### **Sample Timing for 1-Hour Session**
| Time | Activity |
| :--- | :--- |
| 0:00–0:10 | Warm-up: Discussing Imposter Syndrome and project anxiety |
| 0:10–0:25 | Explore: Comparing the four datasets and their unique cleaning challenges |
| 0:25–0:50 | Apply: Troubleshooting initial Pandas `read_csv()` calls and identifying "dirty" data |
| 0:50–1:00 | Wrap-up: Setting a goal for the first 3 insights to be found in the data |

### **Check for Understanding (Ask 2–3)**
*   What Pandas functions are best for a first "preview" of the data? (Answer: `head()`, `tail()`, and `info()`).
*   How do you decide whether to use `dropna()` or `fillna()` for missing values? (Answer: Depends on whether the missing data is significant or if it can be replaced by a mean/median without biasing the results).
*   When creating a visualization, what are three essential "accessibility" features it should have? (Answer: Titles, labels, and legends).

### **Apply Prompts**
*   **Dataset Approval:** If a student wants to use an alternative dataset, remind them they must get **CIL approval** by the end of week 13.
*   **Feature Engineering:** Encourage students to think beyond date extraction; suggest deriving "Gross Margin" or "Customer Lifetime Value" for more complex analysis.
*   **Visualization Variety:** Ensure students aren't just making three bar charts; they should use a range of types like scatter plots, histograms, or heatmaps.
