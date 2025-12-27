import re

# Input and output file names
input_file = "input.txt"
output_file = "emails.txt"

# Read content from input file
with open(input_file, "r") as file:
    text = file.read()

# Regular expression to find email addresses
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

# Write extracted emails to output file
with open(output_file, "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Email addresses extracted and saved successfully!")
