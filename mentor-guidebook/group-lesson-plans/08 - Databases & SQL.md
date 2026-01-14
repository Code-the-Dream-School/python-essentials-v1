# Python: Introduction to Databases and SQL — Group Mentor Guide

Welcome to Lesson 8 of the Python course! This week, students are learning:

- What relational databases are and why they're used
- How to create and connect to SQLite databases
- How to define tables with proper schema (primary keys, foreign keys, constraints)
- How to write basic SQL queries (SELECT, INSERT, UPDATE, DELETE)
- How to handle one-to-many and many-to-many relationships
- How to use JOIN statements to combine tables
- How to integrate SQL with Pandas using `pd.read_sql_query()`

Students are building a magazine subscription database with publishers, magazines, subscribers, and subscriptions.

## Warm-Up (5–10 minutes)

Choose one:

**Relationship-Building**  
- What subscriptions do you have? (magazines, streaming services, apps)
- Have you ever wondered how a company tracks who's subscribed to what?

**Check for Understanding (from last week)**  
- How do you handle missing data in a DataFrame?
- What's a regular expression used for?
- How do you validate data before processing it?

## Explore vs. Apply — Session Formats

**Explore Sessions** → Walk through database concepts, table relationships, and SQL syntax  
**Apply Sessions** → Debug SQL queries, troubleshoot foreign key issues, practice JOIN statements

## Sample Timing for 1-Hour Session

| Time      | Activity                                        |
|-----------|-------------------------------------------------|
| 0:00–0:10 | Warm-up + review database concepts              |
| 0:10–0:30 | Explore: tables, relationships, basic queries   |
| 0:30–0:50 | Apply: write queries, debug joins, test in VSCode|
| 0:50–1:00 | Wrap-up + final questions                       |

## Check for Understanding (Ask 2–3)

- What's the difference between a primary key and a foreign key?
- What are the three types of table relationships? (one-to-one, one-to-many, many-to-many)
- Why use a join table for many-to-many relationships?
- What's the difference between `JOIN` and `LEFT JOIN`?
- Why do we use constraints like `NOT NULL` and `UNIQUE`?
- What does `PRAGMA foreign_keys = 1` do?
- How do you prevent duplicate insertions?

## Explore Prompts

Use these to demonstrate key concepts live:

- Let's map out the magazine database — what tables do we need?
- Where should foreign keys go in a one-to-many relationship?
- How do we handle many-to-many? Let's draw it on a whiteboard.
- What happens when we try to insert invalid data with constraints on?

*Mini-Demo Ideas:*  

```python
# Connecting to SQLite
import sqlite3

with sqlite3.connect("../db/example.db") as conn:
    cursor = conn.cursor()
    # Your SQL here
    conn.commit()  # Don't forget to commit writes!

# Creating a table with constraints
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        age INTEGER
    )
""")

# Inserting with parameterized queries (safe from SQL injection!)
cursor.execute(
    "INSERT INTO students (name, age) VALUES (?, ?)", 
    ("Alice", 20)
)

# Querying data
cursor.execute("SELECT * FROM students WHERE age > ?", (18,))
results = cursor.fetchall()
for row in results:
    print(row)  # Each row is a tuple

# Simple JOIN example
cursor.execute("""
    SELECT students.name, courses.course_name 
    FROM enrollments
    JOIN students ON enrollments.student_id = students.student_id
    JOIN courses ON enrollments.course_id = courses.course_id
""")
```

---

## Apply Prompts (Live Coding & Troubleshooting)

### Assignment Hotspots
* Forgetting `PRAGMA foreign_keys = 1` — foreign key constraints won't work!
* Not committing transactions — changes disappear when connection closes
* Missing `IF NOT EXISTS` in CREATE TABLE — program crashes on second run
* Foreign key points to wrong table or wrong column
* Trying to insert foreign keys that don't exist (violates constraint)
* Not handling `sqlite3.IntegrityError` exceptions for duplicate entries
* Confusing which table should have the foreign key in one-to-many relationships
* JOIN table missing both foreign keys in many-to-many relationships
* Forgetting the comma in single-element tuples: `(value,)` not `(value)`
* Not checking for existing records before inserting (creates duplicates)

### Try This Live

**Let's figure out the magazine database structure together:**

Ask:
* Publishers → Magazines: Is this one-to-many? Which table gets the foreign key?
* Subscribers → Magazines: Is this many-to-many? Do we need a join table?
* What columns does the subscriptions table need?

**Let's write a query to find all magazines for a publisher:**

```python
# First, let's think about what we need:
# - Publisher name from publishers table
# - Magazine names from magazines table
# - How are they connected? magazines.publisher_id!

cursor.execute("""
    SELECT publishers.name, magazines.name 
    FROM magazines
    JOIN publishers ON magazines.publisher_id = publishers.publisher_id
    WHERE publishers.name = ?
""", ("National Geographic",))

results = cursor.fetchall()
for row in results:
    print(f"Publisher: {row[0]}, Magazine: {row[1]}")
```

Ask:
* Why do we need the JOIN?
* What if a publisher has no magazines? Would `LEFT JOIN` help?
* Could we write this without a JOIN? (Yes, but less efficient!)

## Engagement Strategies (for quiet groups)

* Whiteboard It: "Let's draw the table relationships — circles for tables, arrows for foreign keys."
* SQL Detective: "Here's a query that's not working — can you spot the error?"
* Query Challenge: "Can you write a query to find all subscribers to 'Time' magazine?"
* Relationship Quiz: "I say a scenario, you tell me: one-to-one, one-to-many, or many-to-many?"

## Optional Challenges

- Add a `renewal_date` to subscriptions and write a query to find expiring subscriptions
- Write a query to count how many subscribers each magazine has
- Add an `active` boolean to subscriptions and write UPDATE queries to mark them inactive
- Create a function that displays all of a subscriber's magazines in a formatted way
- Try the SQLBolt tutorial (highly recommended!)

## Integration with Pandas (Task 5)

Students will use `pd.read_sql_query()` to load SQL results into DataFrames:

```python
import pandas as pd
import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    sql = """
        SELECT li.line_item_id, li.quantity, p.product_id, 
               p.product_name, p.price
        FROM line_items li
        JOIN products p ON li.product_id = p.product_id
    """
    df = pd.read_sql_query(sql, conn)
    
# Now use Pandas to analyze
df['total'] = df['quantity'] * df['price']
summary = df.groupby('product_id').agg({
    'line_item_id': 'count',
    'total': 'sum',
    'product_name': 'first'
})
```

This connects SQL (for querying structured data) with Pandas (for analysis)!

## Mentor To-Do
- [ ] Run a session using this guide  
- [ ] Help students visualize table relationships (draw diagrams!)
- [ ] Verify students understand primary vs foreign keys
- [ ] Check that students installed SQLite Viewer extension
- [ ] Submit your [Mentor Session Report](https://airtable.com/appoSRJMlXH9KvE6w/shrp0jjRtoMyTXRzh)
