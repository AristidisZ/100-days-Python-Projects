import pandas
import pandas as pd

data = pd.read_csv("Squirels.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur color": ["Grey", "Red", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}


data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")


# import csv
#
# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
#     print(temperature)


import pandas as pd

# data = pd.read_csv("weather-data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data[data["day"] == "Monday"])
# print(data[data["temp"] == data["temp"].max()])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print((monday.temp * 9/5) + 32)
