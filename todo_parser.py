import tkinter as tk
from collections import deque
from tkinter import filedialog

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

output_lines = deque()

for line in input_lines:
    if "psych210" in line:
        output_lines.append(line)

input_file.close()
output_file.writelines(list(output_lines))
output_file.close()