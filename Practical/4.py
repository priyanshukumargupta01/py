#Write a python script to print the current date in the following format “Sun May 29 02:26:23 IST 2017” 

import time

# Get the current time formatted with day, month, date, time, timezone, and year
formatted_date = time.strftime("%a %b %d %H:%M:%S %Z %Y")

print(formatted_date)