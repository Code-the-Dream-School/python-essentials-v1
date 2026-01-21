### **Python 100: Advanced SQL and Database Integration — Group Mentor Guide**

Welcome to Lesson 9! This week, students are moving beyond basic data retrieval to perform complex data analysis using **subqueries**, **aggregation**, and **multi-table joins**. They will also learn to integrate these database operations safely into Python scripts using **parameterized queries** to prevent SQL injection.

#### **Warm-Up (5–10 minutes)**
Choose one:
**Relationship-Building (Mindset: Peer Collaboration)**
* The "lone coder" is a myth; most tech companies use collaborative workspaces. Can you think of a time when asking a peer for help or a screenshare helped you get a project over the finish line?
* What is one challenge you personally encounter when collaborating with others, and how do you try to overcome it?

**Check for Understanding (SQL Basics)**
* What is the difference between an `INNER JOIN` and a `LEFT JOIN`?
* Why should you test your SQL queries in a database interface (like `sqlcommand.py`) before putting them into your Python code?

#### **Explore vs. Apply — Session Formats**
* **Explore Sessions** → Demonstrate **subqueries** and **aggregation** (GROUP BY/HAVING) live using the `sqlcommand.py` tool.
* **Apply Sessions** → Help students set up their **two VSCode terminal sessions** and debug Python integration using `sqlite3`.

#### **Sample Timing for 1-Hour Session**
| Time | Activity |
| ------ | ------ |
| 0:00–0:10 | Warm-up + Review Peer Collaboration mindset |
| 0:10–0:30 | Explore: Subqueries, Joins, and Aggregation functions |
| 0:30–0:50 | Apply: Implementing transactions and parameterized queries in Python |
| 0:50–1:00 | Wrap-up: Window functions and final questions |

#### **Check for Understanding (Ask 2–3)**
* Why do we use the `HAVING` clause instead of `WHERE` for filtering aggregated results?
* What is a **parameterized query**, and why is it safer than using f-strings for SQL statements?
* What happens to a database if an error occurs during a **transaction** but before it is committed?
* What does `PRAGMA foreign_keys = 1` do for a database connection?

#### **Explore Prompts**
* **Subquery Demo:** Let's find the highest-paid employee in each department using a nested `SELECT`. 
* **Aggregation & Filtering:** Let’s group employees by department and only show those where the average salary is over 70,000 using `HAVING`.
* **SQL Injection Simulation:** Let's look at why `cursor.execute(f"SELECT... {id}")` is dangerous and how to fix it with a placeholder `?`.

#### **Apply Prompts (Assignment Hotspots)**
* **The Two-Terminal Setup:** Students must ensure one terminal is in the `assignment9` folder while the other runs `sqlcommand.py` to correctly locate the database file.
* **Transaction Blocks:** Ensure students are using `try-except` blocks with `conn.commit()` and `conn.rollback()` when creating new orders.
* **The RETURNING Clause:** When inserting a new order, remind students to use `RETURNING order_id` so they can use that ID for the subsequent `line_item` inserts.
* **Complex JOINs:** Task 1 requires joining three tables: `orders`, `line_items`, and `products`. Practice identifying the common keys (IDs) between these tables.

#### **Optional Challenges**
* **Window Functions:** Use `RANK() OVER (PARTITION BY ...)` to rank employees by salary within their own departments.
* **Date Manipulation:** Use `JULIANDAY('now')` to calculate the age of employees based on their birth dates.
* **Performance:** Discuss when to create an **Index** to speed up frequent queries on large tables.

#### **Mentor To-Do**
* [ ] Demonstrate how to use `sqlcommand.py` for rapid SQL testing.
* [ ] Review the importance of closing the database connection with `conn.close()`.
* [ ] Submit your Mentor Session Report.
