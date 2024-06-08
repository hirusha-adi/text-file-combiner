import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="Concatenate files with a given extension into a single output file.")
    parser.add_argument('-e', '--extension', type=str, required=True, help="File extension to search for.")
    parser.add_argument('-o', '--output', type=str, default='output.txt', help="Output file name. Default is 'output.txt'.")
    
    args = parser.parse_args()
    file_extension = args.extension
    output_file_name = args.output

    output = []
    for root, dirs, files in os.walk("."):
        for filename in [f for f in files if f.endswith(file_extension)]:
            filepath = os.path.join(root, filename)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                output.append(file.read() + '\n')

    with open(output_file_name, 'w', encoding='utf-8', errors='ignore') as output_file:
        output_file.writelines(output)


if __name__ == "__main__":
    main()
