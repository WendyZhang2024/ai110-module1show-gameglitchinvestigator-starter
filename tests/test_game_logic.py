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
    # Test valid string inputs (integer and float format)
    assert parse_guess("50") == (True, 50, None)
    assert parse_guess("50.0") == (True, 50, None)

def test_parse_guess_invalid():
    # Test invalid string input
    assert parse_guess("abc")[0] == False

def test_update_score():
    # Test score calculation: winning on the first attempt gives 100 points
    assert update_score(0, "Win", 1) == 100
    # Test score deduction: wrong guess deducts 5 points
    assert update_score(50, "Too High", 2) == 45