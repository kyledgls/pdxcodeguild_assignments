"""
This lab calculates rain data
"""
import datetime



new_list = []
with open("opb.rain.txt", "r") as file:
    contents = file.read()
    contents = contents.replace('-', '0')
    contents = contents.split()
    new_list.append(contents)
    date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')
    print(date.month, date.day, date.year)


print(contents)