import re

def validate_credit_card(card_number):
    # Remove any hyphens from the card number
    card_number = card_number.replace("-", "")
    
    # Define the regular expression pattern
    pattern = r'^[4-6]\d{15}$'
    
    # Check if the card number matches the pattern
    if re.match(pattern, card_number):
        # Check for consecutive repeated digits
        if not has_consecutive_repeated_digits(card_number, 4):
            return True
    
    return False

def has_consecutive_repeated_digits(number, min_consecutive):
    for i in range(len(number) - min_consecutive + 1):
        if len(set(number[i:i+min_consecutive])) == 1:
            return True
    return False
