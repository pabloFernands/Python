import csv
import pandas

#print(tempo_list)

# tempo_maximo = data["temp"].max()
# monday_day = data[data.day == "Monday"]
# monday_temp = monday_day["temp"]
#data_dict = data.to_dict()
#print(data)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_count, cinnamon_count, black_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv("squirrel_count.csv")