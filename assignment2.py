##
#  Student Name:  William Zhao
#  Course: CIS 502 Applied Python Programming
#  Lab # 2
#  Application: Validating User Input of Monetary Amounts, Generating Measures of Central Tendency 
#  Description: Prompt and obtain revenue values from the user.  Validate that the user input provided 
#               is valid for monetary amounts.  Use the type Decimal to ensure precise monetary 
#               calculations.
#               
#  Development Environment:  Anaconda
#  Version: Python 3.8
#  Solution File:  WilliamZhaoLab2.py
#  Date: 02/01/23

# Program Source
from decimal import Decimal
import statistics as st
from collections import Counter

def check_modal(lst):
    """
    checks if data is modal
    if it is returns the mode
    """

    count = Counter(lst)
    if len(count) == len(lst):
        return "is not modal"
    else:
        return max(count, key=count.get)

def get_revenue(NUM_RUNS):
    """
    validates and returns revenues
    """
    idx = 0
    Revenues = []
    while idx < NUM_RUNS:
        user_input = input("Enter a revenue value ( >=0 ): ")
        try:
            revenue_value = Decimal(user_input).quantize(Decimal(".01"))
            if revenue_value >= 0:
                Revenues.append(revenue_value)
                idx += 1
        except:
            user_input = input("Enter value ( >=0 ): ")

    return Revenues

def descriptive_statistics(Revenues):
    """
    returns the mean, median, mode, and standard 
    deviation of given  list of values
    """
    mode = check_modal(Revenues) # Note I couldnt use st.mode since if Revenues
                                 # was all unique it would return the first value
    mean = st.mean(Revenues)
    median = st.median(Revenues)
    standard_deviation = st.stdev(Revenues)

    return round(mean,2), round(median,2), mode, round(standard_deviation,2)

def main():
    values = get_revenue(7)
    mean, median, mode, standard_deviation = descriptive_statistics(values)
    print(f"Revenues: {[float(i) for i in values]}")
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Standard Deviation: {standard_deviation}")

if __name__ == "__main__":
    main()

'''
Test Run 1
Enter a revenue value ( >=0 ): hello, world 
Enter value ( >=0 ): -1
Enter a revenue value ( >=0 ): 239.5
Enter a revenue value ( >=0 ): 53.9
Enter a revenue value ( >=0 ): 211.5
Enter a revenue value ( >=0 ): 11.98
Enter a revenue value ( >=0 ): 5.98
Enter a revenue value ( >=0 ): 23.95
Enter a revenue value ( >=0 ): 115.2
Revenues: [239.5, 53.9, 211.5, 11.98, 5.98, 23.95, 115.2]
Mean: 94.57
Median: 53.90
Mode: is not modal
Standard Deviation: 96.97
'''

'''
Test Run 2
Enter a revenue value ( >=0 ): 3430000
Enter a revenue value ( >=0 ): 130000
Enter a revenue value ( >=0 ): 3060000
Enter a revenue value ( >=0 ): 2130000
Enter a revenue value ( >=0 ): 2040000
Enter a revenue value ( >=0 ): 780000
Enter a revenue value ( >=0 ): 450000
Revenues: [3430000.0, 130000.0, 3060000.0, 2130000.0, 2040000.0, 780000.0, 450000.0]
Mean: 1717142.86
Median: 2040000.00
Mode: is not modal
Standard Deviation: 1291945.75

'''