import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    date = d.strftime("%A %d %B %Y")
    return date

    #2020-06-19T07:00:00+08:00
    #Friday 02 July 2021.


def convert_f_to_c(temp_in_farenheit):
    celsius = round(((float(temp_in_farenheit) - 32)/1.8),1)
    return celsius


def calculate_mean(weather_data):
    total = 0
    for item in weather_data:
        total = total+(float(item))
    mean = (total/len(weather_data))
    return float(mean)

def load_data_from_csv(csv_file):
    data = []
    with open (csv_file, encoding= "utf-8") as csv_doc:
        reader = csv.reader(csv_doc)
        header = next(csv_doc)
        for line in reader:
            if len(line) != 0:
                data.append([line[0], int(line[1]), int(line[2])]) 
    return data


def find_min(weather_data):
    if len(weather_data) == 0:
        return()
    for i in range(0, len(weather_data)):
        mini = round(float(min(weather_data)),1)
        minpos = weather_data.reverse()
        minpos = len(weather_data) - weather_data.index(min(weather_data)) -1
        return(mini, minpos)


def find_max(weather_data):
    if len(weather_data) == 0:
        return()
    for i in range(0, len(weather_data)):
        maxi = round(float(max(weather_data)),1)
        maxpos = weather_data.reverse()
        maxpos = len(weather_data) - weather_data.index(max(weather_data)) -1
        return(maxi, maxpos)


def generate_summary(weather_data):
    celsmintemp = []
    for item in weather_data:
        celsmintemp.append(item[1])
    mini, miniposition = find_min(celsmintemp)
    celsmin = convert_f_to_c(mini)

    celsmaxtemp = []
    for item in weather_data:
        celsmaxtemp.append(item[2])
    maxi, maxiposition = find_max(celsmaxtemp)
    celsmax = convert_f_to_c(maxi)

    mindate = convert_date(weather_data[miniposition][0])
    maxdate = convert_date(weather_data[maxiposition][0])

    
    summary = ""
    summary += (f"{len(celsmintemp)} Day Overview\n")
    summary += (f"  The lowest temperature will be {format_temperature(celsmin)}, and will occur on {mindate}.\n")
    summary += (f"  The highest temperature will be {format_temperature(celsmax)}, and will occur on {maxdate}.\n")
    summary += (f"  The average low this week is {format_temperature(convert_f_to_c(calculate_mean(celsmintemp)))}.\n")
    summary += (f"  The average high this week is {format_temperature(convert_f_to_c(calculate_mean(celsmaxtemp)))}.\n")
    return summary

    #The lowest temperature will be 9.4°C, and will occur on Friday 02 July 2021.
    #The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.
    #The average low this week is 12.2°C.
    #The average high this week is 17.8°C.



def generate_daily_summary(weather_data):
    
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = ""
    for item in weather_data:
        summary += (f"---- {convert_date(item[0])} ----\n")
        summary += (f"  Minimum Temperature: {format_temperature(convert_f_to_c(item[1]))}\n")  
        summary += (f"  Maximum Temperature: {format_temperature(convert_f_to_c(item[2]))}\n\n")  
    return summary
