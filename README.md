# File Combiner

This script concatenates files with a specified extension into a single output file. It offers options to search only in the current working directory or recursively through all subdirectories.

## Requirements

- Python 3.x

## Setup Guide

### Windows

1. **Clone the repository or download the script:**

    ```sh
    git clone https://github.com/hirusha-adi/file-combiner
    cd ./file-combiner
    ```

    Alternatively, you can directly download the `file-combiner.py` script and place it in your desired directory.

2. **Ensure you have Python 3 installed:**

    You can download Python 3 from the official [Python website](https://www.python.org/).

3. **Run the script using Python:**

    ```sh
    python file-combiner.py [options]
    ```

### Ubuntu

```bash
# install dependecies
sudo apt install python3

# run the script
python file-combiner.py [options]
```

You can also install it

```bash
# move to user bin directory
sudo mv file-combiner.py /usr/bin/file-combiner

# give executable permissions
sudo chmod +x /usr/bin/file-combiner

# run it from anywhere
file-combiner [options]
```

Or, you can move it elsewhere and add this directory to the system PATH.

## Usage

The script uses command-line arguments to specify the file extension, output file name, and whether to search recursively.

### Command Line Arguments

- `-e, --extension` (required): The file extension to search for.
- `-o, --output` (optional): The output file name. Defaults to `output.txt`.
- `-r, --recursive` (optional): Recursively search through all subdirectories. If not specified, the script will only look in the current working directory.

### Help

To see the help message with all options, run:

```sh
> python .\file-combiner.py --help
usage: file-combiner.py [-h] -e EXTENSION [-o OUTPUT] [-r]
Concatenate files with a given extension into a single output file.

options:
  -h, --help            show this help message and exit
  -e EXTENSION, --extension EXTENSION
                        File extension to search for.
  -o OUTPUT, --output OUTPUT
                        Output file name. Default is 'output.txt'.
  -r, --recursive       Recursively search through all subdirectories.
```

### Examples

#### 1. Recursively search for `.txt` files and concatenate them into `combined_output.txt`:

```sh
python file-combiner.py -e .txt -o combined_output.txt -r
```

#### 2. Search for `.log` files only in the current working directory and concatenate them into `output.txt`:

```sh
python file-combiner.py -e .log
```

#### 3. Recursively search for `.md` files and concatenate them into `documentation.md`:

```sh
python file-combiner.py -e .md -o documentation.md -r
```

#### 4. Search for `.csv` files only in the current working directory and concatenate them into `data_output.txt`:

```sh
python file-combiner.py -e .csv -o data_output.txt
```

#### 5. Search for `.py` files only in the current working directory and concatenate them into `scripts_output.txt`:

```sh
python file-combiner.py -e .py -o scripts_output.txt
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

This file was generated with the help of ChatGPT on `6/8/2024`
