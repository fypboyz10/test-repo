import sys
import os

def process_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            return content.strip()
    except FileNotFoundError:
        return None

def validate_data(data):
    if data is None:
        return False
    if len(data) == 0:
        return False
    return True

def transform(text):
    result = []
    for char in text:
        if char.isalpha():
            result.append(char.upper())
        elif char.isdigit():
            result.append(str(int(char) * 2))
        else:
            result.append(char)
    return ''.join(result)

config = {
    'input_file': 'data.txt',
    'output_file': 'output.txt',
    'encoding': 'utf-8',
    'mode': 'transform'
    'verbose': True,
    'debug': False
}

data = process_file(config['input_file'])

if validate_data(data):
    transformed = transform(data)
    print(f"Original: {data}")
    print(f"Transformed: {transformed}")
    
    with open(config['output_file'], 'w') as f:
        f.write(transformed)
    
    print(f"Output written to {config['output_file']}")
else:
    print("Invalid data or file not found")
    sys.exit(1)

print("Processing complete")
