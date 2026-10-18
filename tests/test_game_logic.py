from logic_utils import check_guess, parse_guess, update_score

def test_winning_guess():
    # Check if a correct guess returns the Win tuple
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # Check if a high guess returns the correct hint and message
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    # Check if a low guess returns the correct hint and message
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")

def test_parse_guess_valid():
    # Only integer-formatted input is valid.
    assert parse_guess("50") == (True, 50, None)

def test_parse_guess_invalid():
    # Test invalid string and fractional numeric inputs.
    assert parse_guess("abc")[0] == False
    assert parse_guess("22.3") == (
        False,
        None,
        "Please enter a valid integer.",
    )
    assert parse_guess("22.0") == (
        False,
        None,
        "Please enter a valid integer.",
    )

def test_update_score():
    # Test score calculation: winning on the first attempt gives 100 points
    assert update_score(0, "Win", 1) == 100
    # Test score deduction: wrong guess deducts 5 points
    assert update_score(50, "Too High", 2) == 45