import csv
import pandas
# with open("weather_data.csv") as file:
#     lines = file.readlines()
    
#     print(lines)
#     for line in lines:
#         print(type(line))

## with csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = list()
#     for elem in data:
#         if elem[1] != "temp":
#             temperature.append(int(elem[1]))
        
        
#     print(temperature)
panda_data = pandas.read_csv("weather_data.csv")

data_dict = panda_data.to_dict()

data_av = panda_data['temp'].to_list()

average = sum(data_av)/len(data_av)

# print(average)
# print(panda_data['temp'].mean())
# print(panda_data['temp'].max())
monday_data = panda_data[panda_data.day == "Monday"]
monday_tempF = monday_data.temp[0]
monday_tempF = monday_tempF*9/5 + 32

print(monday_tempF)
