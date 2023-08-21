# Define a function to convert 12-hour time to 24-hour time
def convert_to_24_hour_format(hour, minute, period):
# Check if the period is "am" and the hour is 12
    if period == "am" and hour == 12:
        hour = 0 # Set the hour to 0, representing midnight
# Check if the period is "pm" and the hour is not 12
    elif period == "pm" and hour != 12:
        hour += 12 # Add 12 to the hour to convert to 24-hour format

# Create a string with the hour and minute values, using two digits each
    time_24_hour = f"{hour:02d}{minute:02d}"
# Return the time in 24-hour format
    return time_24_hour

# Test cases
 # Output is "0830"
print(convert_to_24_hour_format(8, 30, "am")) 
# Output is "2030"
print(convert_to_24_hour_format(8, 30, "pm"))  
# Output is "0015"
print(convert_to_24_hour_format(12, 15, "am")) 
# Output is "1215" 
print(convert_to_24_hour_format(12, 15, "pm"))  