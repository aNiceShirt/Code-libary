# with open("day-25_csv_data/weather_data.csv", "r") as data_file:
#     weather_data = data_file.readlines()
# print(weather_data)


# import csv

# with open("day-25_csv_data/weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
# print(temperatures)


# import pandas

# data = pandas.read_csv("day-25_csv_data/weather_data.csv")

# print(data["temp"])

# data_dict = data.to_dict()

# data_list = data["temp"].to_list()

# print(data_list)

# average = 0
# for data in data_list:
#     average += data
# average = average/len(data_list)
# print(average)

# average = sum(data_list) / len(data_list)

# print(data["temp"].mean())

# print(data["temp"].max())

## Get data in column
# print(data.condition)

## Get data in row
# print(data[data.day == "Monday"])

# data.temp.max()

## Get the row where max temp
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
# monday_temp_F = monday_temp * 9/5 +32
# print(monday_temp_F)

## Create dataframe from dictionary
# data_dict = {
#     "students": ["Amy", "Lars", "Søren"],
#     "scores": [12,13,14]
# }
# data_DF = pandas.DataFrame(data_dict)
# data_DF.to_csv("day-25_csv_data/data_df.csv")


## Squirrel data: Fur color count

import pandas

data = pandas.read_csv("day-25_csv_data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Counts of each value
fur_color_count = data["Primary Fur Color"].value_counts()

fur_color_count.to_csv("day-25_csv_data/data_fur_colors.csv")

