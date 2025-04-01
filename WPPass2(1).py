
input_str = "rhinoceros"
output_str = ""



for i, char in enumerate(input_str):
    # Check if the index is odd
    
    if i % 2 != 0:
        input_str += char.upper()
    else:
        input_str += char
    output_str = (input_str)
print(f"output_string={output_str}",end="")


