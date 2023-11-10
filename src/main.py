# import the inputs logic
from inputs import gather_imputs, input_dict

# import the calculation logic
from calculator import calculateMonthlyOwnershipCosts

def main():
    print("Welcome to the Car Affordability Calculator! \n" + "Please kindly enter the following requested information: ")
    # Get the inputs from the user
    # user_inputs = gather_imputs(input_dict)
    user_inputs = {
        'user_details': {
            'name': 'Angelo'
        }, 
        'vehicle_details': [
            {
                'make': 'Toyota',
                'model': 'Corolla',
                'year': 1992,
                'MPG (miles per gallon)': 200.0,
                'fuel type': 'gasoline',
                'Average distance driven per weekday': 20.0,
                'Average distance driven per weekend': 40.0,
                'Estimated yearly maintenance cost': 1000.0,
                'Estimated yearly insurance cost': 1000.0,
                'Estimated yearly registration cost': 1000.0,
                'Estimated yearly repair cost': 1000.0,
                'Car loan amount': 1000.0,
                'Car loan interest rate': 1000.0,
                'Car loan time': 5.0,
                'Car loan down payment': 1000.0
            },
            {
                'make': 'Suzuki',
                'model': 'Bravo',
                'year': 1990,
                'MPG (miles per gallon)': 200.0,
                'fuel type': 'diesel',
                'Average distance driven per weekday': 20.0,
                'Average distance driven per weekend': 40.0,
                'Estimated yearly maintenance cost': 2000.0,
                'Estimated yearly insurance cost': 2000.0,
                'Estimated yearly registration cost': 2000.0,
                'Estimated yearly repair cost': 2000.0,
                'Car loan amount': 20000.0,
                'Car loan interest rate': 2.0,
                'Car loan time': 2.0,
                'Car loan down payment': 2000.0
            }
        ]
    }
    print("Thank you " + user_inputs["user_details"]["name"]+ ".")
    #Calculate based on the inputs and the number of cars to evaluate
    
    # Initialize the URL for fetching fuel prices
    fuel_price_url = "https://www.eia.gov/petroleum/gasdiesel/"
     # Calculate based on the inputs and the number of cars to evaluate
    for i, vehicle in enumerate(user_inputs['vehicle_details']):
        # Extracting details for each vehicle
        v_details = user_inputs['vehicle_details'][i]
        # Calculating the monthly ownership costs for each vehicle
        all_ownership_costs = calculateMonthlyOwnershipCosts(
            yearly_maintenance_cost=v_details['Estimated yearly maintenance cost'],
            yearly_insurance_cost=v_details['Estimated yearly insurance cost'],
            yearly_registration_cost=v_details['Estimated yearly registration cost'],
            yearly_repair_cost=v_details['Estimated yearly repair cost'],
            fuel_type=v_details['fuel type'],
            MPG=v_details['MPG (miles per gallon)'],
            avg_dist_per_weekday=v_details['Average distance driven per weekday'],
            avg_dist_per_weekend=v_details['Average distance driven per weekend'],
            URL=fuel_price_url,
            loan_amount=v_details['Car loan amount'],
            down_payment=v_details['Car loan down payment'],
            annual_interest_rate=v_details['Car loan interest rate'],
            loan_term_years=v_details['Car loan time']
        )
        # Adding the monthly ownership cost to the user_inputs dictionary for each vehicle
        user_inputs['vehicle_details'][i]['monthly_ownership_cost'] = all_ownership_costs
    print(user_inputs)    
        
    
    
    
    
main()

    
    
