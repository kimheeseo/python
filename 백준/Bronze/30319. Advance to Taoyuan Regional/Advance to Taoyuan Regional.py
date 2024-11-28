from datetime import datetime, timedelta

def is_too_late(date_str):
    # Parse the input date
    topc_date = datetime.strptime(date_str, "%Y-%m-%d")
    
    # Set the ICPC Taoyuan Regional Contest date
    icpc_date = datetime(2023, 10, 21)
    
    # Calculate the deadline (35 days before ICPC date)
    deadline = icpc_date - timedelta(days=35)
    
    # Compare the TOPC date with the deadline
    return "TOO LATE" if topc_date > deadline else "GOOD"

# Read input
input_date = input().strip()

# Print result
print(is_too_late(input_date))