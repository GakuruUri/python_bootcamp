import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# DataFrames
data_dict = data.to_dict()
print(data_dict)

# Series
temp_list = data["temp"].to_list()
print(temp_list)
size_temp = len(temp_list)
sum_temp = sum(temp_list)
avg_temp = sum_temp/size_temp
print(avg_temp)


average = sum(temp_list) / len(temp_list)
print(average)

print(data["temp"].mean())

print(data["temp"].max())
# Get data in columns
print(data["temp"])
print(data.temp)

# Get data in rows

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a dataFrame from scratch





















