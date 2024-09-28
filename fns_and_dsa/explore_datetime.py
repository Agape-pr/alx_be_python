from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format as required
    print(f"Current date: {formatted_date}")
display_current_datetime()
number_of_days = int(input("Enter numbe of days: "))
def calculate_future_date(number_of_days):
    days = datetime.timedelta(days=number_of_days)
    future_date = datetime.datetime.now() + days
    print(f"Future date: {future_date}")
calculate_future_date(number_of_days)
    
