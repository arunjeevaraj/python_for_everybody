#!/usr/bin/env python3
# this tells the os how the script is run, and who runs it.

import re

print("running python   ..... exiting !!")

file1 = 'regex_sum_1038960.txt'
file2 = 'regex_sum_42.txt'

numbers_list = []
handle_f1 = open(file1)
for lines in handle_f1:
    numbers = re.findall('[0-9]+', lines)
    if len(numbers) > 0:
        numbers_list.append(numbers)

sum = 0
list_of_numbers = []
for inside_list in numbers_list:
    for numbers in inside_list:
        sum += int(numbers)
        list_of_numbers.append(int(numbers))

print("sum of the numbers in the text : "+ str(sum))