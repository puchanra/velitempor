import re

# Example response string
response = "Example text 1:some text here 1.another part"

# Split the response based on the pattern '1' followed by '.' or ':'
split_response = re.split(r'1(?:\.|:)', response)

# Ensure there are enough parts in the split response to avoid IndexError
if len(split_response) > 1:
    # Get the desired part, strip leading/trailing whitespace
    result = split_response[1].strip()
    print(result)
else:
    print("Pattern not found or insufficient split parts.")
