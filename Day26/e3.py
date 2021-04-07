with open('./Day26/file1.txt', mode='r') as file:
    fileA = file.readlines()

with open('./Day26/file2.txt', mode='r') as file:
    fileB = file.readlines()

result = [int(num) for num in fileA if num in fileB]

# Write your code above 👆

print(result)


