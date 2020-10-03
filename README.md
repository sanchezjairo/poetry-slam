import random
# function gets txt file and opens it in a list as a string
def get_file_lines(filename):
    f = open(filename, 'r')
    # print(f.read().splitlines())
    return f.read().splitlines()
lines_list = get_file_lines("poem.txt")
#print(lines_list)

# function get the txt file and prints it backwards
def lines_printed_backwards(lines_list):
     for i in range(len(lines_list)):
         print(i, lines_list[-(i + 1)])
#lines_printed_backwards(lines_list)

# function gets the txt file lines and each line randomly chooses a different lines every time its called
def lines_printed_random(lines_list):
    for i in range(len(lines_list)):
         print(i, lines_list[random.randint(0, 13)])
#lines_printed_random(lines_list)

# function calls the txt file lines and starts in the middle of then poem and goes back wards until evry line is called 
def lines_printed_customs(lines_list):
    for i in range(len(lines_list)):
         print(i, lines_list[-(i - 7)])
lines_printed_customs(lines_list)

lines_printed_random(lines_list)

lines_printed_backwards(lines_list)

print(lines_list)
         