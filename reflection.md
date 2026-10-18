# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. *Reversed High/Low Logic*: The game gives the completely opposite hint. For example, guessing the minimum value (1) returns "Go LOWER!", and guessing a higher value (e.g., 35 when the target is 2) returns "Go HIGHER!". This makes it impossible to narrow down the correct number using logic.
  2. *Incorrect Score Calculation*: After making only two guesses (35, then 2) and winning the game, the final score was inexplicably 65. It seems the score is derived from the guessed number itself rather than the number of attempts or logic.
  3. *New Game State Issue*: After winning a game and clicking the "New Game" button, entering a new number and clicking "Submit" does nothing. The page requires a manual browser refresh to reset the game state properly.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input Used | Expected Behavior | Actual Behavior | Console Error / Output | Suspected Code Location |
| :--- | :--- | :--- | :--- | :--- |
| `1` (Target > 1) | "Go HIGHER!" | "Go LOWER!" | none | `logic_utils.py` -> `check_guess()` |
| `35` (Target is 2) | "Go LOWER!" | "Go HIGHER!" | none | `logic_utils.py` -> `check_guess()` |
| `35`, then `2` | High score (e.g., 90+) | Final score: 65 | none | `app.py` (score update logic) |
| Click "New Game" after win | Reset game, allow new guesses | Page doesn't respond; requires refresh | none | `app.py` (session state reset logic) |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
