# Requirements gathered from the project statement/client

## Overall Requirements

- Build a calculator:
    1. Runs in the terminal.
    2. Asks the user for information relevant to their upcoming car purchase.
    3. User should input two vehicles and related information.
    4. Avoid unnecessary questions but ensure core aspects are covered.

## Specific Functional Requirements

- Calculate monthly gas costs based on:
    - MPG/gas efficiency.
    - Driving frequency on weekdays and weekends.
- Consider 1 year of car maintenance and repairs based on user feedback.
- Car loan and interest rate calculations:
    - Monthly cost calculation including down payment consideration.
- Final output:
    - Concise printout of all user-submitted information.
    - Recommendation on which car to buy with clear reasons.

## Technical Requirements

- Programming Language: Python.
- Structure: Use functions and built-in Python data structures (lists, tuples, dictionaries, strings, input, etc.).
- Code Standards: Follow PEP-8 standards.
- Paradigm: Choose either functional programming or object-oriented programming (OOP), not both.

## Calculator Details

### Inputs:
- Number of vehicles to compare (minimum 2).
- For each vehicle:
    - Make and model.
    - Purchase price.
    - MPG (miles per gallon) or gas efficiency.
    - Average distance driven on weekdays and weekends.
    - Estimated yearly maintenance and repair costs.
    - Car loan amount (minus any down payment).
    - Interest rate on the car loan.
    - Duration of the car loan.
    - Down payment amount (if any).

### Outputs:
- Monthly gas cost for each vehicle.
- Yearly maintenance and repair costs for each vehicle.
- Monthly loan payment for each vehicle.
- Total monthly cost of ownership for each vehicle (including loan payment, gas, maintenance, and repairs).
- Summary of input information for comparison.
- Recommendation on which vehicle to buy with justification based on:
    - Total monthly cost.
    - Long-term cost-effectiveness.