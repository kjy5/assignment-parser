from collections import deque
from datetime import datetime

# CONFIGURATION
KEYWORDS = {"Page", "Discussion Topic", "Assignment", "Quiz"}
TAGS = ["dxarts200"]
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

    if line in KEYWORDS:
        # Check box
        current_line = deque("-[]")

        # Name
        current_line.append(input_lines[index + 1].strip())

        # Date
        current_line.append("@{")
        if line != "Page":
            line_split = input_lines[index+2].split()
            current_line.append(datetime.strptime(line_split[0], "%b").strftime("%B"))
            current_line.append(line_split[1])
            current_line.append(",")
        else:
            lecture_line = input_lines[index + 1].strip()
            if "1" in lecture_line:
                current_line.append("March 31 ,")
            elif "2" in lecture_line:
                current_line.append("April 7 ,")
            elif "3" in lecture_line:
                current_line.append("April 14 ,")
            elif "4" in lecture_line:
                current_line.append("April 21 ,")
            elif "5" in lecture_line:
                current_line.append("April 28 ,")
            elif "6" in lecture_line:
                current_line.append("May 5 ,")
            elif "7" in lecture_line:
                current_line.append("May 12 ,")
            elif "8" in lecture_line:
                current_line.append("May 19 ,")
            elif "9" in lecture_line:
                current_line.append("May 26 ,")
            elif "10" in lecture_line:
                current_line.append("June 2 ,")

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
