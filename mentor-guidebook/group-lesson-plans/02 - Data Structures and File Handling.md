# Week 2: Data Structures & File Handling — Group Mentor Guide

In Week 2, students practiced:

- Using and manipulating Python lists, tuples, sets, and dictionaries
- Writing and reading `.txt` and `.csv` files
- Looping through nested data structures
- Importing libraries like `csv` and `json`

They’re working in Jupyter notebooks this week and using real-world data formats for the first time.

## 🧊 Warm-Up (5–10 minutes)

Choose one:

**👋 Relationship-Building**
- What’s one piece of data you’d want to track about your daily life?
- Have you ever worked with a spreadsheet or CSV before?

**💡 Check for Understanding (from Week 1)**
- What’s the difference between a `print()` and a `return`?
- What types of problems is Python especially good for?

## 🧭 Explore vs. Apply — Session Formats

**Explore Sessions** → Talk through use cases, review the difference between data types, practice code snippets  
**Apply Sessions** → Live coding, error debugging, writing/parsing files together

## ⏱️ Sample Timing for 1-Hour Session

| Time      | Activity                             |
|-----------|--------------------------------------|
| 0:00–0:10 | Warm-up + check understanding        |
| 0:10–0:30 | Explore data structures or file I/O  |
| 0:30–0:50 | Try This Live or troubleshoot tasks  |
| 0:50–1:00 | Recap + Q&A                          |

## ❓ Check for Understanding

Ask 2–3 before moving on:

- What’s the difference between a list and a set?
- When would you use a dictionary instead of a list?
- What’s the difference between `append()` and `extend()`?
- What are the steps to write to a file in Python?

## 🧑‍🏫 Explore Prompts

- Let’s draw or describe a real-life situation where we’d use a dictionary.
- What happens if you try to add a duplicate item to a set?
- What does the `open()` function actually do? Why do we use `with`?

🧑‍💻 *Mini-Demo Ideas:*
```python
# Tuple vs. List mutability
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

my_list[0] = 10     # ✅ Works
# my_tuple[0] = 10  # ❌ Error!

# Writing to a file
with open("test.txt", "w") as f:
    f.write("Hello, Code the Dream!")
```

## 🛠️ Apply Prompts (Live Coding & Troubleshooting)

### 
🔧 Common Struggles
* Forgetting `.items()` when looping through a dictionary
* Syntax errors using with `open(...)` block
* Confusing sets and dictionaries (both use {})
* Appending rows to CSVs vs overwriting files

## ✅ Try This Live

“Let’s write a program that loops through a list of dictionaries and prints something useful.”

```python
students = [
    {"name": "Luis", "completed": True},
    {"name": "Jazmine", "completed": False},
    {"name": "Asha", "completed": True}
]

for student in students:
    if student["completed"]:
        print(f"{student['name']} finished the assignment!")
```

Ask:
* How would we turn this into a CSV?
* Could we filter this list instead of printing?

## 💬 Engagement Strategies
* Compare Types: “Which data structure would you use for a recipe? A phone book?”
* Chat First: “Write one dictionary in the chat with three keys.”
* Break & Fix: Show broken file handling code and debug it together
* Whiteboard Model: Visualize how `.append()` changes a list step-by-step

## 💡 Optional Challenges
* Count word frequencies in a .txt file
* Store user profiles in a list of dictionaries and write to CSV
* Loop through a nested dictionary to summarize results

✅ Mentor To-Do
* Run a session using this guide
* Help students debug or extend their data structure work
* Submit your [Mentor Session Report](https://airtable.com/appoSRJMlXH9KvE6w/shrp0jjRtoMyTXRzh)
