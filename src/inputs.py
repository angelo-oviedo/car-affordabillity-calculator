# import the validation logic
from validation import validated_input, regex_expressions

input_dict = {
    "user_inputs": {
        "name": ("What is your name?: ", "string")    
    },
    "vehicles_inputs": {
        "make": ("What is the make of the vehicle?:", "string"),
        "model": ("What is the model of the vehicle?:","string"),
        "year": ("What is the year of the vehicle?:", "int"),
        "MPG (miles per gallon)": ("What is the MPG of the vehicle?:", "float"),
        "fuel type": ("What is the fuel type of the vehicle? (gasoline, diesel):", "fuel"),
        "Average distance driven per weekday": ("What is the average distance driven per weekday (M-F)? (miles):", "float"),
        "Average distance driven per weekend": ("What is the average distance driven per weekend? (miles):", "float"),
        "Estimated yearly maintenance cost": ("What is the estimated yearly maintenance cost? ($):", "float"),
        "Estimated yearly insurance cost": ("What is the estimated yearly insurance cost? ($):", "float"),
        "Estimated yearly registration cost": ("What is the estimated yearly registration cost? ($):", "float"),
        "Estimated yearly repair cost": ("What is the estimated yearly repair cost? ($):", "float"),
        "Car loan ammount": ("What is the car loan ammount? ($):", "float"),
        "Car loan interest rate": ("What is the car loan annual interest rate? (%):", "float"),
        "Car loan time": ("What is the car length of the loan term in years? (ex: 2):", "float"),
        "Car loan down payment": ("What is the car loan down payment? ($):", "float"),
    },
}

def get_input(input_key, input_type, input_dict, expected_type):
    """
    Prompts the user for the specified input based on the dictionary.

    Args:
        input_key (str): The key for the input to get from the user.
        input_type (str): The type of input to get from the user ('user_inputs' or 'vehicles_inputs').
        input_dict (dict): The dictionary containing the input information.
        expected_type (str): The type of the input expected ('string', 'int', 'float').

    Returns:
        str or int or float: The user's response to the prompt, cast to the appropriate type.
    """
    prompt_text = input_dict[input_type][input_key][0]

    while True:
        user_response = input(prompt_text + " ")
        if validated_input(regex_expressions, expected_type, user_response):
            if expected_type == 'int':
                return int(user_response)
            elif expected_type == 'float':
                return float(user_response)
            else:
                return user_response
        else:
            print("Invalid input, please try again.")

def gather_imputs(input_dict):
    """
    Gathers all the inputs from the user.

    Args:
        input_dict (dict): The dictionary containing the input information.

    Returns:
        dict: The dictionary containing all the user's inputs.
    """
    
    # This dictionary will hold all the user's inputs
    user_inputs = {}
    
    # Get the user information
    user_inputs["user_details"] = {}
    for input_key, (prompt, expected_type) in input_dict["user_inputs"].items():
        user_inputs["user_details"][input_key] = get_input(input_key, "user_inputs", input_dict, expected_type)
     
    # Get the vehicle information
    n_vehicles = int(input("How many vehicles do you want to introduce?: "))
    
    # Build the correct dictionary for each vehicle the user inputs
    user_inputs['vehicle_details'] = []
    for number in range(n_vehicles):
        print(f"Enter the information of the vehicle number " + str(number+1))
        
        # Dictionary for each vehicle stored
        vehicle_info = {}
        for input_key, (prompt, expected_type) in input_dict["vehicles_inputs"].items():
            vehicle_info[input_key] = get_input(input_key, "vehicles_inputs", input_dict, expected_type)
        
        # This line will append the filled dictionary to the vehicle details list
        user_inputs['vehicle_details'].append(vehicle_info)
    
    return user_inputs