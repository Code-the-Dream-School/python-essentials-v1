## **Week 10: Intro to Web Scraping — Group Mentor Guide**
Welcome to Week 10! This week, students are learning to harvest data from live websites using **Selenium** and **WebDriver Manager**. They are moving from structured database queries to extracting information from the **Document Object Model (DOM)** while navigating the ethical boundaries of web traffic.

#### **Warm-Up (5–10 minutes)**
Choose one:
**Relationship-Building (Mindset: Information Literacy/AI)**
*   Have you ever received coding advice from AI or a forum that turned out to be completely wrong or outdated? How did you figure it out?
*   When looking at a technical tutorial, what "clues" do you use to decide if it is trustworthy?

**Check for Understanding (from Previous Lessons)**
*   What is the difference between an HTML **tag**, **attribute**, and **content**?
*   Why might we need to use Python to turn a website's information into a "structured format" like a CSV?

#### **Explore vs. Apply — Session Formats**
*   **Explore Sessions** → Walk through the hierarchical tree structure of the **DOM** using browser developer tools and demonstrate basic **Selenium** initialization.
*   **Apply Sessions** → Debugging **CSS Selectors**, troubleshooting **WebDriver** installations, or refining **XPath** logic for complex sections like "See also" or search results.

#### **Sample Timing for 1-Hour Session**
| Time | Activity |
| ------ | ------ |
| 0:00–0:10 | Warm-up + Reviewing "Information Literacy" mindset |
| 0:10–0:30 | Explore: Live DOM inspection + Selenium "Headless" mode |
| 0:30–0:50 | Apply: Building a loop to extract book titles and authors |
| 0:50–1:00 | Wrap-up: Ethical scraping and `robots.txt` discussion |

#### **Check for Understanding (Ask 2–3)**
*   What is the role of **WebDriver Manager** in a Selenium script? (Answer: It automates the installation of the browser driver required for operations).
*   Why do we often need to include `sleep()` or delays when scraping multiple pages? (Answer: To avoid overloading the server and being an "abuse of privilege").
*   What is **headless mode**, and why would you use it?
*   What is a `robots.txt` file?

#### **Explore Prompts**
*   **Live Inspection:** Open the Wikipedia "Web Scraping" page and use `Shift-Ctrl-J`. Let’s find the `href` of the first link together.
*   **Selector Practice:** How would we select *all* images that have a `src` attribute? Let's try `img[src]`.
*   **Handling Errors:** Let's write a `try/except` block for a `driver.get()` request. Why is the `finally: driver.quit()` part so important?

#### **Apply Prompts (Assignment Hotspots)**
*   **Dynamic Content:** Remind students that many pages use JavaScript to load data, which is why we use Selenium instead of basic request libraries.
*   **The Semicolon Challenge:** In Task 3, students must join multiple authors with a semicolon (`;`). Practice the `.join()` method if they are stuck.
*   **XPath vs. CSS:** If a `div` has no ID or Class, how can we use **XPath axes** like `following-sibling` to find it?
*   **Environment Setup:** Ensure students have run `pip install selenium webdriver-manager` inside their `python_homework` directory.

---

### **Resource 2: Assignment Review Guide**
