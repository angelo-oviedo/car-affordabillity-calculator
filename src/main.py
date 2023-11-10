# import the inputs logic
from inputs import gather_imputs, input_dict

# import the calculation logic
from calculator import calculateMonthlyOwnershipCosts, getRecommendation

# import the outputs logic
from outputs import listsGenerator

# Libraries import
import termtables as tt

def main():
    print("Welcome to the Car Affordability Calculator! \n" + "Please kindly enter the following requested information: ")
    while True:
        # Get the inputs from the user
        user_inputs = gather_imputs(input_dict)
        print("\n Thank you " + user_inputs["user_details"]["name"]+ ".\n")
        #Calculate based on the inputs and the number of cars to evaluate
        # Initialize the URL for fetching fuel prices
        fuel_price_url = "https://gasprices.aaa.com/"
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
        
        # Print the results
        vehicle_details_table = listsGenerator(user_inputs, "vehicle_details")
        vehicle_financial_details_table = listsGenerator(user_inputs, "financial_details")
        vehicle_monthly_ownership_costs_table = listsGenerator(user_inputs, "monthly_costs")
        
        print("The following are the details of the vehicles you entered: \n")
        tt.print(vehicle_details_table, style=tt.styles.thin_thick)
        print("\n")
        print("The following are the financial details of the vehicles you entered: \n")
        tt.print(vehicle_financial_details_table, style=tt.styles.thin_thick)
        print("\n")
        print("The following are the monthly ownership costs of the vehicles you entered: \n")
        tt.print(vehicle_monthly_ownership_costs_table, style=tt.styles.thin_thick)
        print("\n")
        
        # Recommend the best car based on the monthly ownership costs
        recommendation, table = getRecommendation(user_inputs)
        print(recommendation)
        print("\nDetailed Comparison:")
        print(table)
        if input("Do you want to try again? (Y/N): ").lower() != "y":
            print("Thank you for using the Car Affordability Calculator!")
            break
        else:
            print("Kindly enter the following requested information: ")
    
main()