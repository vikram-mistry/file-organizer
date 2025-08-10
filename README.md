# File Organizer

A Python script to automatically organize files in a specified folder into categorized subfolders based on file types.

## Features

- Automatically moves files into folders like **Documents**, **Images**, **Videos**, **Audio**, **Archives**, **Apps**, and **Others**.
- Supports organizing any folder by providing the path as a CLI argument or via interactive prompt.
- Non-destructive: existing folders and files not matched by categories remain unaffected.
- Easy to use and extend with more file type categories.
- Installable from PyPI for easy setup.

## Installation

Install the latest release from PyPI:

~~~bash
pip install file-organizer-advanced
~~~

For more details, visit the PyPI page:
https://pypi.org/project/file-organizer-advanced/

## Usage

Run the CLI command to organize your files:
~~~bash
file-organizer-advanced
~~~

By default, it organizes your Downloads folder. To specify a different folder:

Example:

~~~bash
file-organizer-advanced /Users/username/Downloads
~~~

## Development and Testing (Optional)

If you want to contribute or test the package locally, follow these steps:

1. **Create and activate a Python virtual environment:**

~~~bash
python3 -m venv env
source env/bin/activate   # On Windows use `env\Scripts\activate`
~~~
2. **Install the package from PyPI or Locally:**
~~~bash
pip install --upgrade pip
pip install file-organizer-advanced
# Or for local development:
pip install -e .
~~~
3. **Run the CLI tool to organize a folder:**
~~~bash
file-organizer-advanced /path/to/folder
~~~
4.	**When done, deactivate the environment:**
~~~bash
deactivate
~~~

## How it works

- Scans the target folder.
- Detects file types based on extensions.
- Moves files into corresponding folders.
- Creates folders if they don’t exist.

## Notes

- Running the CLI multiple times will not affect already organized files.
- The CLI does not modify files inside existing subfolders.
- Files without known extensions are moved to the **Others** folder.

# Sample Output:
✅ Moved: example.pdf → Documents
✅ Moved: vacation.jpg → Images
✅ Moved: project.zip → Archives
✅ Moved: app.dmg → Apps

📂 Folder '/Users/username/Downloads' organized successfully!

# Screenshot
![Script Output Screenshot](File_Organizer_Screenshot.PNG)