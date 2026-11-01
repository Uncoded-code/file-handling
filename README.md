# Python File Handling

A beginner-friendly command-line project that demonstrates basic file operations in Python using `pathlib`.

## Features

- Check whether a file exists
- Read a file's contents
- Rewrite a file
- Append text to a file
- Create a file if it doesn't exist
- Delete a file

## Requirements

- Python 3

No external packages are required.

## Run

```bash
python filehandling.py
Follow the prompts to enter a file name and choose an operation. Relative file paths are resolved from the directory where you run the program.
Note
The append option needs a small code fix before it works. In filehandling.py, change:
f.append(data)
to:
f.write(data)
The file is already opened in append mode, so write() adds the text to the end.
Learning goals
This project practices Python input, conditional logic, exception handling, and file operations with pathlib and open().

The README describes appending as a feature once you apply the one-line fix above.

    
8:09 PM
