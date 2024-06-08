import os

output = []
for root, dirs, files in os.walk("."):
    for filename in [f for f in files if f.endswith('.txt')]: # txt files only
        filepath = os.path.join(root, filename)
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
            output.append(file.read() + '\n')

with open('output.txt', 'w', encoding='utf-8', errors='ignore') as output_file:
    output_file.writelines(output)
