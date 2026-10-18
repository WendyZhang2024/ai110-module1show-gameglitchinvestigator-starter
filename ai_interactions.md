# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I asked Deepseek to help me implement a "Guess History" feature in the Streamlit sidebar to track all previous guesses, including both valid integers and invalid string inputs, and to ensure it resets when a new game starts.

**What did the agent do?**

It added a `st.sidebar.divider()` and a subheader, then inserted a `for` loop that iterates over `st.session_state.history`. It also modified the submission logic to append raw strings to the history if the user input fails validation.

**What did you have to verify or fix manually?**

The agent initially tried to use a non-existent Streamlit UI function `st.sidebar.list()` to display the history items. I reviewed the diff, caught the error, and manually corrected it by using `st.sidebar.text()` inside a standard `for` loop. I also manually verified that the history array clears correctly when clicking "New Game".

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Non-numeric string | "How to test if parse_guess rejects 'abc'?" | `assert parse_guess("abc")[0] == False` | Yes | Prevents the app from crashing with a `ValueError` when users type letters. |
| Decimal input | "Generate a test to ensure decimals are rejected." | `assert parse_guess("42.5")[0] == False` | Yes | Prevents the logic bypass where `int(float("42.5"))` truncates to 42 and falsely triggers a win. |
| Negative integer | "Test negative integer input parsing." | `assert parse_guess("-10") == (True, -10, None)` | Yes | Ensures the parser correctly identifies valid integers, even if they are outside the game's bounds (handled later by game logic). |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
"Please review the code style and type hints in `logic_utils.py` to see if there is an error causing the decimal truncation."
```

**Linting output before:**

```
Warning: Missing type hints for function arguments and return types.
Warning: Implicit conversion from float to int might cause unexpected truncation (e.g., int(float("46.4")) -> 46).
```

**Changes applied:**

```
The AI's static analysis pointed out two major issues:
1. **Missing Type Hints**: Functions lacked clear type definitions, making it hard to catch bugs. The AI suggested adding professional type hints like `def check_guess(guess: int, secret: int) -> tuple[str, str]:`.
2. **Implicit Truncation Risk**: The AI noticed that if the input isn't properly handled, decimals could be truncated. However, because our updated `parse_guess` function already had `value.is_integer()`, the AI realized the source code was correct but the **running instance was stale**. It instructed me to kill all running Streamlit processes (which were still using old cached code) and restart on a fresh port using `python -m streamlit run app.py --server.port 8503`.

By applying the type hints and restarting the server instance, the bug was completely resolved.
```

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

| | Model A | Model B |
|-|---------|---------|
| **Model name** | GitHub Copilot | Deepseek |
| **Response summary** | Suggested modifying the return strings inside the existing `app.py` file (e.g., changing "Go HIGHER" to "Go LOWER"). However, it failed to notice that these old functions were overriding the newly imported ones, causing the bug to persist. | Identified the structural flaw: redundant functions in `app.py` were shadowing `logic_utils.py`. Suggested completely removing the old code, strictly separating UI from logic, and enforcing `value.is_integer()` to prevent decimal truncation. |
| **More Pythonic?** | No | Yes |
| **Clearer explanation?** | No | Yes |

**Which did you prefer and why?**

I strongly preferred Deepseek. GitHub Copilot tried to patch the symptoms by modifying the surface-level strings, but it missed the architectural issue—specifically, the "ghost code" in `app.py` that was still running. Deepseek diagnosed the root cause, forced a clean refactor, and provided strict edge-case handling (rejecting decimals like `22.3`), which made the final code much more robust and testable.
