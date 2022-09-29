from collections import deque
from datetime import datetime
import tkinter as tk
from tkinter import filedialog

# CONFIGURATION
YEAR = datetime.now().year
TAGS = ["phys141"]

# Get input file
# noinspection DuplicatedCode
root = tk.Tk()
root.withdraw()
input_filepath = filedialog.askopenfilename()
input_file = open(input_filepath, 'r')
input_lines = input_file.readlines()

# Create output file
output_filepath = filedialog.asksaveasfile(mode='w', defaultextension=".md").name
output_file = open(output_filepath, 'w')

# Parse csv file
output_lines = deque()
current_line = deque()
for row in input_lines:
    row = row.replace('\ufeff', '')
    row = row.split(",")
    print(row)
    # Start + name
    current_line = deque("-[]")
    current_line.append(row[1].strip())

    # Date
    current_line.append("@{")

    # Month
    current_line.append(datetime.strptime(row[0][-3:], "%b").strftime("%B"))

    # Day
    day = int(row[0][:2])
    if "Midterm" not in row[1]:
        day -= 1

    current_line.append(str(day))
    current_line.append(",")
    current_line.append(str(YEAR))
    current_line.append("}")

    # Time
    if "Midterm" not in row[1]:
        current_line.append("@@{")
        current_line.append("9:00")
        current_line.append("PM")
        current_line.append("}")

    # Tags
    for tag in TAGS:
        current_line.append("#" + tag)
    if "Midterm" in row[1]:
        current_line.append("#exam")

    # Add line to output
    current_line.append("\n")
    output_lines.append(" ".join(current_line))

input_file.close()
output_file.writelines(list(output_lines))
output_file.close()

