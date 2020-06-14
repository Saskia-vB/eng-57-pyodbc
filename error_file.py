# Reading a text file
# f = open ('text_file.txt', 'r')
#
# print(f.name)
#
# f.close()

# to use a text within a block of code without worrying about closing it:

# read and print out contents of txt file
# with open('text_file.txt', 'r') as f:
#     f_contents = f.read()
#     print(f_contents)

# reading a txt file and print each line using a loop
# with open('text_file.txt', 'r') as f:
#     for line in f:
#         print(line, end='')

# I can write to a file
# if the file does exist it will override it so if you want to write to an existing file you write with a for appending
# with open('test_file.txt', 'w') as f:
#     f.write('Test')

# append
# with open('text_file.txt', 'a') as f:
#     f.write('it worked again!')

# write on a new line
# with open('text_file.txt', 'a') as f:
#     f.write('this time on a new line!\n')

# created a function that can open any txt file and print out each line
# def read_text(text_file):
#     with open(text_file, 'r') as f:
#         for line in f:
#             print(line, end = '')
#
# print(read_text('test_file.txt'))

# create a function that writes a new line in a file
# user_input = str(input("Enter your new line: "))
# def new_line(user_input):
#     with open('test_file.txt', 'a') as f:
#         f.write("'" + user_input + "'" + '\n')
#
# print(new_line(user_input))
