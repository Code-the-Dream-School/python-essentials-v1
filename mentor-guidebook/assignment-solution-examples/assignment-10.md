### **Lesson 10: Introduction to Web Scraping**
| Week | Topic | Learning Objective |
| ------ | ------ | ------ |
| 10 | Web Scraping | Students will use Selenium to scrape data from live sites, navigate the DOM with CSS selectors and XPath, and store results in CSV/JSON formats. |

#### **Assignment Rubric**
You can mark the student's assignment as complete if they:
*   [ ] Created an `assignment10` branch and included all required files (`get_books.py`, `owasp_top_10.py`, `ethical_scraping.txt`, etc.).
*   [ ] **Task 3:** Successfully extracted **Title**, **Author**, and **Format-Year** from the Durham Library site.
*   [ ] **Task 3:** Correctily joined multiple authors with a semicolon (`;`).
*   [ ] **Task 4:** Exported data to both `get_books.csv` and `get_books.json`.
*   [ ] **Task 5:** Provided reflections on `robots.txt` and ethical scraping.
*   [ ] **Task 6:** Used **XPath** to extract the OWASP Top 10 vulnerabilities into a CSV.
*   [ ] **Mindset:** Answered the three prompts regarding Information Literacy and AI.

#### **What to Look For**
*   **Incremental Progress:** In Task 3, look for the creation of a **DataFrame** from a list of dictionaries. 
*   **Robustness:** Check if they used a `try/finally` block to ensure `driver.quit()` is called even if an error occurs.
*   **XPath Logic:** In the OWASP task, ensure they didn't just hard-code the list but used XPath to locate titles and links dynamically.
*   **Ethical Considerations:** Ensure they acknowledge the importance of not overloading servers with rapid requests.

#### **Sample Code Reference**
*Handling Multiple Authors (Task 3):*
```python
# Expected logic for multiple authors
authors = [a.text for a in author_elements]
author_string = "; ".join(authors)
```

*XPath for Parent/Sibling (Concept):*
```python
# Moving from a known ID to a sibling container
parent = element.find_element(By.XPATH, '..')
target = parent.find_element(By.XPATH, 'following-sibling::div')
```
