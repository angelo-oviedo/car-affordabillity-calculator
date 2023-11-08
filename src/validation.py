# Libraries import
import re

# Regex patterns used to validate the correct data type
regex_expressions = {
    "string": "^[A-Za-z ]+$",  # Matches one or more letters and spaces
    "int": "^\d+$",            # Matches one or more digits
    "float": "^\d*(\.\d+)?$",  # Matches any number of digits, an optional decimal point, and more digits, but no negative sign
    "fuel": "^(gasoline|diesel|Gasoline|Diesel)$" # Matches to only the words "gasoline" and "fuel" for a special validation
}

def validated_input(regex_expressions, expression_type, user_input):
    """
    Validates the user input based on a regular expression.
    It is used to ensure that the input conforms to the expected data type (e.g., string, integer, float).

    Args:
        regex_expressions (dict): A dictionary containing regular expression patterns for different input types.
        expression_type (str): The key for the type of expression to match (e.g., 'string', 'int', 'float').
        user_input (str): The input provided by the user that needs to be validated.

    Returns:
        bool: True if the input matches the regular expression, False otherwise.
    """

    if not re.match(regex_expressions[expression_type], user_input):
        print(f"Error! Make sure you are entering a valid {expression_type}.")
        return False
    else:
        return True