from collections import deque
from datetime import datetime

# Get input file
input_file = open("data/todo.txt", 'r')
input_lines = input_file.readlines()
input_file.close()

# Create output file
output_file = open("data/date_adjusted.md", 'w')

for index, line in enumerate(input_lines):
    if " @{" in line:
        date_start = line.index(" @{") + 3
        date_end = line.index("}")
        date_input = line[date_start:date_end].strip().split(' ')
        if ',' in date_input:
            date_input.remove(',')
        elif ',' in date_input[1]:
            date_input[1] = date_input[1].replace(',', '')
        month_number = datetime.strptime(date_input[0], "%B").month
        input_lines[index] = line[:date_start] + str(month_number) + "/" + date_input[
            1] + "/22" + line[date_end:]

output_file.writelines(input_lines)
output_file.close()
