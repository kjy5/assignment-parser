import tkinter as tk
from collections import deque
from datetime import datetime
from tkinter import filedialog

# CONFIGURATION
KEYWORDS = {"Jan", "Feb", "Mar"}
TAGS = ["phys142"]
YEAR = datetime.now().year
INPUT_FILEPATH = "data/assignments.txt"
OUTPUT_FILEPATH = "data/assignments.md"

# Get input file
input_file = open(INPUT_FILEPATH, 'r')
input_lines = input_file.readlines()

# Create output file
output_file = open(OUTPUT_FILEPATH, 'w')

# Parse input file
output_lines = deque()
current_line = deque()
for index, line in enumerate(input_lines):
    line = line.strip()
    print(line)

    if line[:3] in KEYWORDS:
        # Check box
        current_line = deque("-[]")

        # Name
        current_line.append(input_lines[index - 1].strip())

        # Date
        line_split = line.split()
        current_line.append("@{")
        current_line.append(datetime.strptime(line_split[0], "%b").strftime("%B"))
        current_line.append(line_split[1])
        current_line.append(",")
        current_line.append(str(YEAR))
        current_line.append("}")

        # Add due time
        current_line.append("@@{")
        current_line.append("11:59")
        current_line.append("PM")
        current_line.append("}")

        # Add tags
        for tag in TAGS:
            current_line.append("#" + tag)

        # Add to output
        current_line.append("\n")
        output_lines.append(" ".join(current_line))

input_file.close()
output_file.writelines(list(output_lines))
output_file.close()
