"""
Core logic for the Game Glitch Investigator.
"""

def get_range_for_difficulty(difficulty: str) -> tuple[int, int]:
    """
    Returns the minimum and maximum range for a given difficulty level.
    
    Args:
        difficulty (str): The selected difficulty ("Easy", "Normal", "Hard").
        
    Returns:
        tuple[int, int]: A tuple containing (min_value, max_value).
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100

def parse_guess(raw: str) -> tuple[bool, int | None, str | None]:
    """
    Parses and validates the user's raw input string.
    
    Args:
        raw (str): The raw string input from the user.
        
    Returns:
        tuple[bool, int | None, str | None]: A tuple of (is_valid, parsed_integer, error_message).
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."
    try:
        value = float(raw)
        if not value.is_integer():
            return False, None, "Please enter a valid integer."
        value = int(value)
    except ValueError:
        return False, None, "That is not a number."
    return True, value, None

def check_guess(guess: int, secret: int) -> tuple[str, str]:
    """
    Compares the guess to the secret number and returns the outcome and hint.
    
    Args:
        guess (int): The user's guessed number.
        secret (int): The target secret number.
        
    Returns:
        tuple[str, str]: A tuple of (outcome, hint_message).
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"  
    return "Too Low", "📈 Go HIGHER!"      

def update_score(current_score: int, outcome: str, attempt_number: int) -> int:
    """
    Calculates the updated score based on the game outcome.
    
    Args:
        current_score (int): The score before this guess.
        outcome (str): The result of the guess ("Win", "Too High", "Too Low").
        attempt_number (int): The current attempt count.
        
    Returns:
        int: The new calculated score.
    """
    if outcome == "Win":
        points = max(10, 100 - (attempt_number - 1) * 10)
        return current_score + points
    if outcome in ["Too High", "Too Low"]:
        return max(0, current_score - 5)
    return current_score