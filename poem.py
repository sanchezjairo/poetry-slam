import random

def get_file_lines(filename):
    f = open(filename, 'r')
    # print(f.read().splitlines())
    return f.read().splitlines()
lines_list = get_file_lines("poem.txt")
# print(lines_list)

