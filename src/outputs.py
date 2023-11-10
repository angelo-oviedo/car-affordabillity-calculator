# Libraries import
import termtables as tt

# Tables output that will be used shared to the user
vehicle_details_table = []
vehicle_financial_details_table = []
vehicle_monthly_ownership_costs_table = []

def listsGenerator(information_dict, list_to_generate):
    """
    This function will generate a list based on the information provided.
    
    Args:
        information_dict (dict): A dictionary with the information to be displayed.
        list_to_generate (list): The name of the list that will be generated.

    Returns:
        list: A list with the information provided.
    """
    # Extract the list of vehicles
    vehicles = information_dict.get("vehicle_details", [])

    # Initialize the table with headers based on list_to_generate
    if list_to_generate == "vehicle_details":
        table = [["Vehicle", "Make", "Model", "Year", "MPG", "Fuel Type"]]
    elif list_to_generate == "financial_details":
        table = [["Vehicle", "Yearly Maintenance Cost", "Yearly Insurance Cost", "Yearly Registration Cost", "Yearly Repair Cost", "Loan Amount", "Interest Rate", "Loan Term", "Down Payment"]]
    elif list_to_generate == "monthly_costs":
        table = [["Vehicle", "Monthly Loan Payment", "Yearly Maintenance and Repair Costs", "Total Monthly Cost of Ownership"]]
    else:
        raise ValueError("Invalid list name")

    # Populate the table rows with vehicle numbers
    for i, vehicle in enumerate(vehicles):
        vehicle_full_name = vehicle.get("make") + " " + vehicle.get("model")
        if list_to_generate == "vehicle_details":
            row = [vehicle_full_name, vehicle.get("make"), vehicle.get("model"), vehicle.get("year"), vehicle.get("MPG (miles per gallon)"), vehicle.get("fuel type")]
        elif list_to_generate == "financial_details":
            row = [vehicle_full_name, vehicle.get("Estimated yearly maintenance cost"), vehicle.get("Estimated yearly insurance cost"), vehicle.get("Estimated yearly registration cost"), vehicle.get("Estimated yearly repair cost"), vehicle.get("Car loan amount"), vehicle.get("Car loan interest rate"), vehicle.get("Car loan time"), vehicle.get("Car loan down payment")]
        elif list_to_generate == "monthly_costs":
            monthly_costs = vehicle.get("monthly_ownership_cost", {})
            row = [vehicle_full_name, monthly_costs.get("Monthly loan payment"), monthly_costs.get("Yearly maintenance and repair costs"), monthly_costs.get("Total monthly cost of ownership")]
        
        table.append(row)
    
    return table
