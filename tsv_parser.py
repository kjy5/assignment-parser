from collections import deque
from datetime import datetime

# CONFIGURATION
YEAR = datetime.now().year
TAGS = ["phys143"]
INPUT_FILEPATH = "data/Lecture_schedule.txt"
OUTPUT_FILEPATH = "data/lecture_schedule.md"

# Get input file
input_file = open(INPUT_FILEPATH, 'r')
input_lines = input_file.readlines()

# Create output file
output_file = open(OUTPUT_FILEPATH, 'w')

# Parse csv file
output_lines = deque()
current_line = deque()
for row in input_lines:
    # Remove extra characters
    row = row.replace('\ufeff', '')
    row = row.replace('"', '')

    # Split
    row = row.split("\t")

    # Check box
    current_line = deque("-[]")

    # Name
    # Lecture number
    current_line.append(row[1].strip())
    current_line.append(":")

    # Chapter numbers
    current_line.append(row[2].strip())
    if len(current_line[-1]) > 0:
        current_line.append("-")
    current_line.append(row[3].strip())
    if len(current_line[-1]) > 0 and current_line[-1][0] == "-":
        current_line[-1] = current_line[-1][1:]

    # Topic names
    current_line.append(":")
    current_line.append(row[4].strip())

    # Date
    current_line.append("@{")

    # Month
    current_line.append(datetime.strptime(row[0][-3:], "%b").strftime("%B"))

    # Day
    day = int(row[0][:2]) - 1
    if day < 1:
        day = 30

    current_line.append(str(day))
    current_line.append(",")
    current_line.append(str(YEAR))
    current_line.append("}")

    # Time
    current_line.append("@@{")
    current_line.append("9:00")
    current_line.append("PM")
    current_line.append("}")

    # Tags
    for tag in TAGS:
        current_line.append("#" + tag)

    # Add line to output
    current_line.append("\n")
    joined_line = " ".join(current_line)
    joined_line = joined_line.replace("  ", " ")
    joined_line = joined_line.replace(" : ", ": ")
    print(joined_line)
    output_lines.append(joined_line)

input_file.close()
output_file.writelines(list(output_lines))
output_file.close()
