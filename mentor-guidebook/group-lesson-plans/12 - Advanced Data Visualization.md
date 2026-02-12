### **Python 100: Advanced Data Visualization Techniques — Group Mentor Guide**

Welcome to Lesson 12! This week, students move from static charts to **interactive visualizations** and **web-based dashboards**. They will learn to use **Plotly** and **Dash** to create dynamic user experiences and will practice professional deployment workflows by hosting their apps on **Render.com**.

#### **Warm-Up (5–10 minutes)**
Choose one:
**Relationship-Building (Mindset: Design and Accessibility)**
*   Think of a time you were in a new physical location or on a website and couldn't find your way around (like looking for a bathroom or an "exit"). How did that frustrating experience make you feel?
*   What is your favorite design feature as a user? What makes it "pleasant" to use?

**Check for Understanding (Visualization Basics)**
*   When should you use a **Line Plot** versus a **Bar Plot**? (Answer: Line plots show trends over time; Bar plots compare quantities between categories).
*   What is the main advantage of an **interactive visualization** over a **static** one? (Answer: Users can zoom, filter, and hover for tooltips to explore data deeply).

#### **Explore vs. Apply — Session Formats**
*   **Explore Sessions** → Demonstrate how a **Dash callback** works (the "Inputs" and "Outputs") and how to test a local web server at `http://localhost:8050`.
*   **Apply Sessions** → Help students debug their **SQL joins** for Task 1 or troubleshoot the **Render.com** deployment process.

#### **Sample Timing for 1-Hour Session**
| Time | Activity |
| ------ | ------ |
| 0:00–0:10 | Warm-up + Verifying `python-assignment12` repository setup |
| 0:10–0:30 | Explore: Plotly interactivity and Dash's `@app.callback` decorators |
| 0:30–0:50 | Apply: Troubleshooting Task 1 (SQL Revenue) or Task 5 (Deployment) |
| 0:50–1:00 | Wrap-up: Discussion on A11y (color contrast) + Final questions |

#### **Check for Understanding (Ask 2–3)**
*   What does the `app = Dash(__name__)` statement do? (Answer: It creates the application object that hosts the layout and callbacks).
*   How do you verify your **virtual environment** is active in the terminal? (Answer: Run `which python` and ensure it points to the `.venv` folder).
*   In a Dash dashboard, what happens when a user changes a value in a **Dropdown**? (Answer: It triggers the callback function to update the graph).
*   What is the "Start Command" needed to run a Dash app on Render? (Answer: `gunicorn myapp:server`).

#### **Explore Prompts**
*   **Dash Callbacks:** Let's look at `@app.callback`. If we had two dropdowns, how would we pass both values into our `update_graph` function?
*   **Plotly Interactivity:** Let's run the Iris dataset example (`lesson12_b.py`). How many different ways can we interact with this chart in the browser?
*   **Pandas Plotting:** Let's take a simple dictionary and see how quickly we can turn it into a bar chart using `df.plot()`.

#### **Apply Prompts (Assignment Hotspots)**
*   **The SQL Join:** Task 1 requires joining **four tables** (employees, orders, line_items, and products). Remind students they can use the provided SQL statement if they get stuck.
*   **Repository Location:** Ensure students created `python-assignment12` **outside** of the usual `python_homework` folder.
*   **Render Deployment:** Remind students that Render is slow on the free plan. They should expect to "Wait. Wait. Wait." for the service to go live.
*   **Environment Variables:** If they are deploying, remind them to add `server = app.server` to their code so `gunicorn` can find it.

#### **Optional Challenges**
*   **Streamlit vs. Dash:** If students are curious, discuss the pros and cons. Streamlit is easier to learn but Dash offers more control for complex projects.
*   **Advanced A11y:** Use the **A11y color contrast tool** to check if their "Monthly Sales" bar chart colors meet accessibility guidelines.

#### **Mentor To-Do**
* [ ] Confirm students have successfully pushed their first commit to their new repository.
* [ ] Help students troubleshoot any "port conflict" errors when running Dash locally.
* [ ] Submit your Mentor Session Report.
