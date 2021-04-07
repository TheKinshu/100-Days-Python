#
# file = open('./Day24/my_file.txt')
# content = file.read()
# print(content)
# file.close()

# Mode = r - read, w - write, a - append
with open('./Day24/new_file.txt', mode='w') as file:
    file.write("\nNew text.")

