# Libraries import
import re
from bs4 import BeautifulSoup
import requests
import statistics

# - Calculate monthly gas costs based on:
#     - MPG/gas efficiency.
#     - Driving frequency on weekdays and weekends.

def getFuelData(url, fuel_type):
    
    try:
        # Start a session for efficient network calls
        with requests.Session() as session:
            response = session.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the table by caption depending on the fuel type
            if fuel_type.lower() == "gasoline":
                caption = "U.S. Regular Gasoline Prices*(dollars per gallon)"
            elif fuel_type.lower() == "diesel":
                caption = "U.S. On-Highway Diesel Fuel Prices*(dollars per gallon)"
            else:
                raise ValueError(f"Invalid fuel type: {fuel_type}")

            # Find the table with the correct caption
            table = soup.find('caption', text=re.compile(caption, re.IGNORECASE)).find_parent('table')
            
            # Extract the entire row referring to the US row of the table
            fuel_row = table.find('a', href="/dnav/pet/pet_pri_gnd_dcus_nus_w.htm").find_parent('tr')
            values = [float(td.get_text()) for td in fuel_row.find_all('td')[1:4]]

            # Check if values list is not empty before calculating mean
            if values:
                average_price = round(statistics.fmean(values), 3)
            else:
                raise ValueError(f"No data found for {fuel_type} fuel type.")

            return average_price
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except ValueError as e:
        print(e)

def calculateMonthlyFuelCost(fuel_type, MPG, avg_dist_per_weekday, avg_dist_per_weekend, URL):
    avg_fuel_price = getFuelData(URL, fuel_type)
    if avg_fuel_price is not None:
        total_avg_miles_per_week = avg_dist_per_weekday * 5 + avg_dist_per_weekend * 2
        avg_fuel_consuption = total_avg_miles_per_week / MPG
        approx_monthly_fuel_cost = round((avg_fuel_price * avg_fuel_consuption) * 4, 2)
        return approx_monthly_fuel_cost
    else:
        return "Could not calculate fuel cost due to missing data."

# Car loan and interest rate calculations:
#     - Monthly cost calculation including down payment consideration.

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