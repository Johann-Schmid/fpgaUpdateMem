# Function to invert hexadecimal values
def invert_hex(line):
    # Remove any trailing newline or comma for processing
    line_body = line.rstrip(',\n')
    inverted_line = ''
    # Process every two characters as a hex value, excluding the last two bytes
    for i in range(0, len(line_body), 2):
        hex_value = line_body[i:i+2]
        # Invert the hex value by XOR with FF (hex)
        inverted_value = format(int(hex_value, 16) ^ 0xFF, '02X')
        inverted_line += inverted_value
    # Reattach the last two characters unchanged
    return inverted_line + line[-2:]

# Load the file
input_file_path = 'memPattern.coe'  # Replace with your actual file path
output_file_path = 'memPatternChanged.coe'  # Replace with your desired output file path

# Read the content of the file
with open(input_file_path, 'r') as file:
    content = file.readlines()

# Invert bits from line 2 onward
inverted_content = content[:2]  # Keep the first two lines unchanged
inverted_content += [invert_hex(line) for line in content[2:]]

# Save the modified content to a new file
with open(output_file_path, 'w') as file:
    file.writelines(inverted_content)

print(f"Inverted file saved as {output_file_path}")

