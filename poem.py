import random

def get_file_lines(filename):
    f = open(filename, 'r')
    # print(f.read().splitlines())
    return f.read().splitlines()
lines_list = get_file_lines("poem.txt")
# print(lines_list)

def lines_printed_backwards(lines_list):
    for i in range(len(lines_list)):
        print(i, lines_list[-(i + 1)])
lines_printed_backwards(lines_list)