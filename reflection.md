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

- **AI tools used**: I used Copilot  and Deepseek as my pair programmers throughout this project.
- **Correct AI Suggestion**: The AI correctly suggested that my `app.py` still contained redundant functions that were overriding the newly refactored functions in `logic_utils.py`. This "ghost code" was why the high/low hint bugs persisted even after I thought I fixed them. I verified this by deleting the old functions from `app.py`, restarting the Streamlit app, and confirming that the hints finally worked correctly.
- **AI Suggestion I Rejected**: The AI initially suggested adding complex `try-except TypeError` blocks inside the `check_guess` function to handle string inputs. I rejected this because it was over-engineered and mixed UI concerns with core game logic. Instead, I modified the approach to strictly validate inputs in the `parse_guess` function using `value.is_integer()`. I verified my version by writing a new `pytest` test case (`test_parse_guess_edge_cases`) to ensure that decimal inputs like `"22.3"` were correctly rejected before reaching the game logic.

---

## 3. Debugging and testing your fixes

- **How I decided a bug was fixed**: I decided a bug was fixed only if it passed both automated `pytest` tests and manual UI testing in the browser.
- **Test I ran**: For example, I ran a new test, `test_parse_guess_edge_cases`, to specifically check if the code correctly rejected decimal inputs like `"42.5"`. This test showed me that the AI's suggestion to use `value.is_integer()` successfully prevented the game from truncating decimals and falsely declaring a win.
- **How AI helped**: AI helped me design this test by pointing out the decimal truncation edge case in the first place, which prompted me to write a dedicated test to lock in that specific behavior.

---

## 4. What did you learn about Streamlit and state?

- Streamlit "reruns" means that every time a user interacts with a widget (like clicking a button), the entire Python script runs from top to bottom again. To prevent game variables (like the secret number and score) from resetting on every click, we use `st.session_state`. You can think of `st.session_state` as a persistent backpack; variables stored inside it are remembered across reruns. Understanding this was crucial for fixing the "New Game" freeze bug, as I needed to explicitly reset all session state variables to start a fresh game.

---

## 5. Looking ahead: your developer habits

- **Habit to reuse**: One habit I will definitely reuse is writing `pytest` test cases during debugging, rather than just relying on clicking around the UI. It forces me to define exactly what "correct" behavior looks like.
- **What I would do differently**: Next time I work with AI, I will ask the AI to show me explicit `diff` previews of its code changes before applying them. During this project, I learned that AI can leave behind redundant "ghost code" that silently overrides new logic.
- **How my thinking changed**: I learned that sometimes AI makes mistakes very confidently. It created a `check_guess` function that seemed completely logical at first glance, but was fundamentally backwards. 