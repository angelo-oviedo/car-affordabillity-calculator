# Libraries import
import re
from bs4 import BeautifulSoup
import requests
import statistics

# - Calculate monthly gas costs based on:
#     - MPG/gas efficiency.
#     - Driving frequency on weekdays and weekends.

def getFuelData(url, fuel_type):
    
    # Get the html content of the webpage and parse it
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')

    # Get the specific fuel average price depending of the type
    if (fuel_type in ["gasoline", "Gasoline"]):
        # Extract the entire row refering to the US row of the table regarding gasoline
        gas_row = soup.find('a', href="/dnav/pet/pet_pri_gnd_dcus_nus_w.htm").parent.parent
        # Extract the numeric values from the 'td' elements with the 3 last data points
        values = [float(td.get_text()) for td in gas_row.find_all('td')[1:4]]
        # Get the average price, since we have the value for the last 3 weeks
        average_gasoline_price = round(statistics.fmean(values), 3)
        return average_gasoline_price
    else:
        # Extract the entire row refering to the US row of the table regarding diesel
        diesel_row = soup.find('a', href="/dnav/pet/pet_pri_gnd_dcus_nus_w.htm").parent.parent
        values = [float(td.get_text()) for td in diesel_row.find_all('td')[1:4]]
        average_diesel_price = round(statistics.fmean(values), 3)
        return average_diesel_price
