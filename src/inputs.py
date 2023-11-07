input_dict = {
    "user_inputs": {
        "name": "What is your name?"    
    },
    "vehicles_inputs": {
        "make": "What is the make of the vehicle?",
        "model": "What is the model of the vehicle?",
        "year": "What is the year of the vehicle?",
        "MPG (miles per gallon)": "What is the MPG of the vehicle?",
        "fuel type": "What is the fuel type of the vehicle? (gasoline, diesel, electric)",
        "Average distance driven per day": "What is the average distance driven per day? (miles)",
        "Estimated yearly maintenance cost": "What is the estimated yearly maintenance cost? ($)",
        "Estimated yearly insurance cost": "What is the estimated yearly insurance cost? ($)",
        "Estimated yearly registration cost": "What is the estimated yearly registration cost? ($)",
        "Estimated yearly repair cost": "What is the estimated yearly repair cost? ($)",
        "Car loan ammount": "What is the car loan ammount? ($)",
        "Car loan interest rate": "What is the car loan interest rate? (%)",
        "Car loan down payment": "What is the car loan down payment? ($)",
    },
}

def get_input(input_key, input_type, input_dict):
    """
    Prompts the user for the specified input based on the dictionary.

    Args:
        input_key (str): The key for the input to get from the user.
        input_type (str): The type of input to get from the user ('user_inputs' or 'vehicles_inputs').
        input_dict (dict): The dictionary containing the input information.

    Returns:
        str: The user's response to the prompt.
    """
    # Get the prompt text from the dictionary
    prompt_text = input_dict[input_type][input_key]
    
    # Prompt the user and return their input
    return input(prompt_text + " ")

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
    for input_key in input_dict["user_inputs"]:
        user_inputs["user_details"][input_key] = get_input(input_key, "user_inputs", input_dict)
     
    # Get the vehicle information
    n_vehicles = int(input("How many vehicles do you want to introduce?: "))
    
    # Build the correct dictionary for each vehicle the user inputs
    user_inputs['vehicle_details'] = []
    for number in range(n_vehicles):
        print(f"Enter the information of the vehicle number " + str(number+1))
        
        # Dictionary for each vehicle stored
        vehicle_info = {}
        for input_key in input_dict["vehicles_inputs"]:
            vehicle_info[input_key] = get_input(input_key, "vehicles_inputs", input_dict)
        
        # Append the filled dictionary to the vehicle details list
        user_inputs['vehicle_details'].append(vehicle_info)
    
    return user_inputs

    
    