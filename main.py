import os
output = []
for root, dirs, files in os.walk("."):
    for filename in files:
        if '.txt' in filename:
            output.append(open(filename, 'r', encoding='utf-8',
                          errors='ignore').read()+'\n')
with open('output.txt', 'w', encoding='utf-8', errors='ignore') as p:
    p.writelines(output)
