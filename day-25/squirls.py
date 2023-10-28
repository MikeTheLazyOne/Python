import pandas
import time
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# my idea
time_1 = time.time()
data_list = data["Primary Fur Color"].to_list()
gray_count = 0
Cinnamon_count = 0
blac_count = 0
nan_count = 0
for elem in data_list:
    if elem == "Gray":
        gray_count += 1
    elif elem == "Black":
        blac_count += 1
    elif elem == "Cinnamon":
        Cinnamon_count += 1
    else:
        nan_count += 1 
new_dict = {"colors":["Gray", "Black", "Cinnamon","Nan"], "number":[gray_count, blac_count, Cinnamon_count, nan_count]}
panda_data = pandas.DataFrame(new_dict)
time_2 = time.time()
print(panda_data)
print(f"time required = {time_2 - time_1}")
# course idea
time_3 = time.time()
gray_squriels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squriels_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squriels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
new_new_dict = {"colors":["Gray", "Black", "Cinnamon","Nan"], "number":[gray_squriels_count, black_squriels_count, cinnamon_squriels_count, nan_count]}

new_panda_data = pandas.DataFrame(new_new_dict)
time_4 = time.time()
print(new_panda_data)
print(f"time required = {time_4 - time_3}")