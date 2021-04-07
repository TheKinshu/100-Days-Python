'''
#Fuke not found
#with open("afile", 'r') as file:
#    file.read()

#Key Error
a_dictonary = {'ley': 'value'}
value = a_dictonary['non_existent_key']

#index error
fruitlist = ['apple', 'bannab', 'pear']
fruitlist = fruitlist[3]

#Type error
text =  'a'
print(text + 5)

try:
    file = open('./Day30/a_file.txt')
    dict = {'key': 'valye'}
    print(dict['something'])
except FileNotFoundError:
    file = open('./Day30/a_file.txt', 'w')
    file.write('Something')
except KeyError as message:
    print(f'{message} does not exist')
else:
    content = file.read()
    print(content)
finally:
    file.close()
    raise TypeError('Tis is an error that I made up')
'''

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height **2
print(bmi)