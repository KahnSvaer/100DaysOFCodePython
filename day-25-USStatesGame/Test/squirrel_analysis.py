import pandas
import pandas as pd

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
unique_colors = set(squirrel_data["Primary Fur Color"].to_list())

color_list = list(unique_colors)  # To preserve the index
clean_color_list = [x for x in color_list if x == x]  # Cleaning to remove null value as null != null
count_list = []

for color in clean_color_list:
    counter = len(squirrel_data[squirrel_data["Primary Fur Color"] == color])
    count_list.append(counter)

color_count_dic = {
    "Fur Color": clean_color_list,
    "Count": count_list
}

data_csv = pd.DataFrame(color_count_dic)
data_csv.to_csv("squirrel_count.csv")
