# Libraries import
import requests
import termtables as tt
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def getFuelData(url, fuel_type):
    """
    Fetches the average fuel price from a given web page.

    Args:
        url (str): The URL of the web page to scrape the fuel data from.
        fuel_type (str): The type of fuel to fetch the data for. Valid options are 'gasoline' or 'diesel'.

    Returns:
        float: The average fuel price for the specified fuel type.

    Raises:
        ValueError: If an invalid fuel type is specified or if no data could be found.
        requests.RequestException: If there is an issue with the network call.
    """
    try:
        ua = UserAgent()
        
        
        # Create a fake user agent to avoid being blocked by the website
        headers = {
            'User-Agent': ua.chrome
        }

        # Fetch the page and create a session to keep the connection open
        with requests.Session() as session:
            response = session.get(url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the table
            table = soup.find('table', class_='table-mob')
            if not table:
                raise ValueError("Table not found.")

            # Extract the headers (fuel types)
            headers = [th.get_text().strip() for th in table.find_all('th')]
            if 'Regular' not in headers or 'Diesel' not in headers:
                raise ValueError("Regular or Diesel headers not found.")

            # Find the index for Regular and Diesel
            regular_index = headers.index('Regular')
            diesel_index = headers.index('Diesel')

            # Find the row for current average prices
            current_avg_row = table.find('td', string='Current Avg.').find_parent('tr')
            if not current_avg_row:
                raise ValueError("Current average prices row not found.")

            # Extract the prices
            prices = [td.get_text() for td in current_avg_row.find_all('td')]
            if(fuel_type == 'gasoline'):
                gasoline_price = prices[regular_index].split('$')[1]
                return float(gasoline_price)
            elif(fuel_type == 'diesel'):
                diesel_price = prices[diesel_index].split('$')[1]
                return float(diesel_price)
            else:
                raise ValueError("Invalid fuel type specified.")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except ValueError as e:
        print(e)
                

def calculateMonthlyFuelCost(fuel_type, MPG, avg_dist_per_weekday, avg_dist_per_weekend, URL):
    """
    Calculates the estimated monthly fuel cost based on vehicle efficiency and driving frequency.

    Args:
        fuel_type (str): The type of fuel used by the vehicle ('gasoline' or 'diesel').
        MPG (float): The fuel efficiency of the vehicle in miles per gallon.
        avg_dist_per_weekday (float): The average distance driven per weekday.
        avg_dist_per_weekend (float): The average distance driven per weekend day.
        URL (str): The URL to fetch current fuel prices from.

    Returns:
        float: The estimated monthly fuel cost.
    """
    avg_fuel_price = getFuelData(URL, fuel_type)
    if avg_fuel_price is not None:
        total_avg_miles_per_week = avg_dist_per_weekday * 5 + avg_dist_per_weekend * 2
        avg_fuel_consuption = total_avg_miles_per_week / MPG
        approx_monthly_fuel_cost = round((avg_fuel_price * avg_fuel_consuption) * 4, 2)
        return approx_monthly_fuel_cost
    else:
        return "Could not calculate fuel cost due to missing data."

def calculateMonthlyLoanPayments(loan_amount, down_payment, annual_interest_rate, loan_term_years):
    """
    Calculate the monthly payment of a loan.

    Args:
        loan_amount (float): Total amount of the loan.
        down_payment (float): Down payment subtracted from the loan amount.
        annual_interest_rate (float): The annual interest rate (as a decimal, so 5% should be input as 0.05).
        loan_term_years (int): The length of the loan term in years.

    Returns:
        float: The monthly payment amount.
    """
    principal = loan_amount - down_payment
    monthly_interest_rate = annual_interest_rate / 12
    number_of_payments = loan_term_years * 12
    
    # If the interest rate is 0, return the principal divided by the number of payments
    if annual_interest_rate == 0:
        return principal / number_of_payments
    
    # Monthly payment calculation using the formula: https://www.calculatorsoup.com/calculators/financial/compound-interest-calculator.php
    monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / ((1 + monthly_interest_rate) ** number_of_payments - 1)
    
    return monthly_payment

def calculateMonthlyOwnershipCosts(yearly_maintenance_cost, yearly_insurance_cost, yearly_registration_cost, yearly_repair_cost, fuel_type, MPG, avg_dist_per_weekday, avg_dist_per_weekend, URL, loan_amount, down_payment, annual_interest_rate, loan_term_years):
    """
    Calculates the estimated total monthly cost of owning a vehicle.

    This includes all recurring costs such as maintenance, insurance, registration, and repair costs, 
    as well as the monthly fuel cost and loan payment.

    Args:
        yearly_maintenance_cost (float): The estimated yearly cost for maintenance.
        yearly_insurance_cost (float): The estimated yearly cost for insurance.
        yearly_registration_cost (float): The estimated yearly cost for registration.
        yearly_repair_cost (float): The estimated yearly cost for repairs.
        fuel_type (str): The type of fuel used by the vehicle ('gasoline' or 'diesel').
        MPG (float): The fuel efficiency of the vehicle in miles per gallon.
        avg_dist_per_weekday (float): The average distance driven per weekday.
        avg_dist_per_weekend (float): The average distance driven per weekend day.
        URL (str): The URL to fetch current fuel prices from.
        loan_amount (float): Total amount of the car loan.
        down_payment (float): The down payment made on the car loan.
        annual_interest_rate (float): The annual interest rate for the car loan.
        loan_term_years (int): The term of the car loan in years.

    Returns:
        dict: The estimated costs of all costs and other specifics.
    """
    
    yearly_estimations = (yearly_maintenance_cost + yearly_insurance_cost + yearly_registration_cost + yearly_repair_cost)
    monthly_estimations = (yearly_estimations / 12)
    monthly_fuel_cost = calculateMonthlyFuelCost(fuel_type, MPG, avg_dist_per_weekday, avg_dist_per_weekend, URL)
    monthly_loan_payment = calculateMonthlyLoanPayments(loan_amount, down_payment, annual_interest_rate, loan_term_years)
    monthly_ownership_cost = monthly_estimations + monthly_fuel_cost + monthly_loan_payment
    
    user_facing_costs = {
        "Yearly maintenance and repair costs": round(yearly_estimations, 2),
        "Monthly loan payment": round(monthly_loan_payment, 2),
        "Total monthly cost of ownership": round(monthly_ownership_cost, 2),
    }
    
    return user_facing_costs

def getRecommendation(information_dict):
    """
    This function makes a recommendation based on the information provided.
    
    Args:
        information_dict (dict): A dictionary with the information to be displayed.
        
    Returns:
        str: A string with the recommendation.
        table: A table with the winning categories.
    """
    
    # Extract the list of vehicles
    vehicles = information_dict.get("vehicle_details", [])

    # Give every vehicle a score variable
    for vehicle in vehicles:
        vehicle["score"] = 0

    # Define categories for comparison and their sorting order (True for ascending, False for descending)
    comparison_categories = {
        "Total monthly cost of ownership": (True, lambda v: v["monthly_ownership_cost"]["Total monthly cost of ownership"]),
        "Car loan interest rate": (True, lambda v: v["Car loan interest rate"]),
        "Estimated yearly maintenance cost": (True, lambda v: v["Estimated yearly maintenance cost"]),
        "MPG (miles per gallon)": (False, lambda v: v["MPG (miles per gallon)"]),
        "Year": (False, lambda v: v["year"])
    }

    # Rank and score vehicles for each category
    category_winners = {}
    for category, (asc, key_func) in comparison_categories.items():
        sorted_vehicles = sorted(vehicles, key=key_func, reverse=not asc)
        for rank, vehicle in enumerate(sorted_vehicles, start=1):
            # Higher rank means more points (better)
            vehicle["score"] += (len(vehicles) + 1) - rank
            if rank == 1:  # Record the winner for each category
                category_winners[category] = vehicle['make'] + ' ' + vehicle['model']

    # Find the vehicle with the highest score
    recommended_vehicle = max(vehicles, key=lambda v: v["score"])
    
    # Prepare the recommendation string
    recommendation = f"The recommended vehicle is the {recommended_vehicle['make']} {recommended_vehicle['model']} ({recommended_vehicle['year']}), with a total score of {recommended_vehicle['score']}. This vehicle excels in the following categories:"

    # Add the winning categories for the recommended vehicle
    for category, winner in category_winners.items():
        if winner == recommended_vehicle['make'] + ' ' + recommended_vehicle['model']:
            recommendation += f"\n- {category}"

    # Generate and print the termtables for additional details
    headers = ["Category", "Winner"]
    data = [[category, winner] for category, winner in category_winners.items()]
    table = tt.to_string(data, header=headers)

    return recommendation, table