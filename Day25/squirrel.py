import pandas
from pandas.core.frame import DataFrame


data = pandas.read_csv('.\Day25\Squirrel_Data.csv')

Gray = len(data[data['Primary Fur Color'] == 'Gray'])
Cinnamon = len(data[data['Primary Fur Color'] == 'Cinnamon'])
Black = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {
    "Fur Colour": ['Gray', 'Cinnamon', 'Black'],
    "Count": [Gray, Cinnamon, Black]
}

df = pandas.DataFrame(data_dict)

df.to_csv("./Day25/Squirrel_Count.csv")