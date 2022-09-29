import tkinter as tk
from collections import deque
from datetime import datetime
from tkinter import filedialog

# CONFIGURATION
KEYWORDS = {"Assignment", "Quiz"}
TAGS = ["phys141"]
YEAR = datetime.now().year

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

# 0 = seeking keyword, 1 = seeking assignment name, 2 = seeking due date
assignment_state = 0

# Parse input file
output_lines = deque()
current_line = deque()
add_quiz_tag = False
for line in input_lines:
    line = line[:-1]
    if line in KEYWORDS:
        current_line = deque("-[]")
        assignment_state = 1
        add_quiz_tag = line == "Quiz"
    elif assignment_state == 1:
        current_line.append(line.strip())
        assignment_state = 2
    elif assignment_state == 2 and line.startswith("Due"):
        line_split = line.split()

        current_line.append("@{")
        current_line.append(datetime.strptime(line_split[1], "%b").strftime("%B"))
        current_line.append(line_split[2])
        current_line.append(",")
        current_line.append(str(YEAR))
        current_line.append("}")

        # Add due time
        current_line.append("@@{")
        current_line.append(line_split[4][:-2])
        current_line.append(line_split[4][-2:].upper())
        current_line.append("}")

        # Add tags
        for tag in TAGS:
            current_line.append("#" + tag)
        if add_quiz_tag:
            current_line.append("#quiz")

        # Add line to output
        current_line.append("\n")
        output_lines.append(" ".join(current_line))
        assignment_state = 0

input_file.close()
output_file.writelines(list(output_lines))
output_file.close()
