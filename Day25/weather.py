#with open('./Day25/weather_data.csv') as data_file:
#    data = data_file.readlines()


# import csv

# with open('./Day25/weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)


import pandas

data = pandas.read_csv('./Day25/weather_data.csv')
print(data['temp'])

data_ditc = data.to_dict()

temp_list = data['temp'].to_list()

total = 0
for temp in temp_list:
    total += temp

avg =(data['temp'].max())

print(avg)

monday = data[data.day == 'Monday']

print(data[data.temp == avg])
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)


## Create a data frame from scratch

data_dict = {
    'students': ['amy', 'james', 'john'],
    'scores': [76,50,78]
}

data = pandas.DataFrame(data_dict)
data.to_csv('./Day25/mydata.csv')