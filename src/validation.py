# Libraries import
import re

# Regex patterns used to validate the correct data type
regex_expressions = {
    "string": "^[A-Za-z ]+$",  # Matches one or more letters and spaces
    "int": "^\d+$",            # Matches one or more digits
    "float": "^-?\d*(\.\d+)?$", # Matches an optional leading sign, any number of digits, an optional decimal point, and more digits
    "fuel": "^(gasoline|diesel|Gasoline|Diesel)$" # Matches to only the words "gasoline" and "fuel" for a special validation
}

def validated_input(regex_expressions, expression_type, user_input):
    if not re.match(regex_expressions[expression_type], user_input):
        print(f"Error! Make sure you are entering a valid {expression_type}.")
        return False
    else:
        return True