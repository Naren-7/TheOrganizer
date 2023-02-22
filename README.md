# 

# File Organizer

The `FileOrganizer` class allows you to organize files in a folder according to their type.

## Installation

You do not need to install anything to use this class, as it depends on Python's standard library.

## Usage

### Create an instance

```python
from file_organizer import FileOrganizer

organizer = FileOrganizer()

```

### Run the script

```bash
python3 TheOrganizer.py ~/path

```

### Set the source directory

You can set the source directory using the `set_dir_path()` method:

```python
organizer.set_dir_path('/directory/path')

```

By default, the source directory is the current directory where the Python file containing the `FileOrganizer` class is located.

### Organize files

To organize files in a folder according to their type, call the `organize()` method:

```python
organizer.organize()

```

This method creates a folder for each file type in the source folder and moves the corresponding files to the appropriate folder.

### File types

By default, `FileOrganizer` organizes the following file types:

- Documents: .pdf, .doc, .docx, .txt
- Images: .jpg, .jpeg, .png, .gif
- Music: .mp3, .wav
- Videos: .mp4, .avi, .mov

You can modify or add file types using the `file_types` dictionary:

```python
organizer.file_types = {
    'Text files': ['.txt', '.md'],
    'Data files': ['.csv', '.json', '.xml'],
    'Code files': ['.py', '.html', '.css', '.js']
}

```

### Full example

```python
from file_organizer import FileOrganizer

# Create an instance of FileOrganizer
organizer = FileOrganizer()

# Organize files in the current directory
organizer.organize()

```

## Add to PATH

Here is a summary of the steps to easily run the `TheOrganizer.py` file from any location:

1. Open a terminal or command prompt.
2. Run the following command in the terminal to check the location of the `FileOrganizer.py` file:

```bash
pwd

```

This command will give you the current path where you are. Make sure you are in the correct path where the `FileOrganizer.py` file is located.

1. Now, copy the directory path that contains the `FileOrganizer.py` file.
2. Add the path to the system PATH by running the following command in the terminal:

**On Windows:**

```bash
setx path "%path%;directory_path"

```

**On Linux/MacOS:**

```bash
export PATH=$PATH:directory_path

```

Make sure to replace `directory_path` with the path you copied earlier.

1. You can now run the algorithm from any location by typing the following command in the terminal:

```bash
python FileOrganizer.py

```

Make sure to replace `custom_path` with the path you want to use.

## With Alias

1. Open the `~/.bashrc` or `~/.zshrc` file in your favorite text editor. For example, you can use the nano command:

```bash
nano ~/.bashrc
code ~/.bashrc
vim ~/.bashrc

```

or

```bash
nano ~/.zshrc
code ~/.zshrc
vim ~/.zshrc

```

1. Add the following line at the end of the file to create an alias called `organize` that runs the script:

```bash
alias organize='python /file_path'

```

1. Save and close the file.
2. To make the changes take effect, load the `~/.bashrc` or `~/.zshrc` file with the following command:

```bash
source ~/.bashrc
source ~/.zshrc

```

1. You can now run the script from any location using the `organize` alias. For example:

```bash
organize

```
