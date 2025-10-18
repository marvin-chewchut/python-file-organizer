# python-file-organizer
A Python script that automatically sorts and moves files in a directory into organized folders based on their file types (e.g., images, documents, videos, etc.).

## 🧩 Project Overview
A File Organizer is a Python script that automatically sorts and moves files in a directory into organized folders based on their file types (e.g., images, documents, videos, etc.).

Instead of manually cleaning your messy “Downloads” folder, this script can:

1. Detect each file type (e.g., .pdf, .jpg, .mp3)
2. Create folders like “Images,” “Documents,” “Audio,” etc.
3. Move the files into those folders automatically.

## ▶ How to run file_organizer.py

### Prerequisites
- Python 3.8 or newer installed.

### Command
  `python file_organizer.py {target path} {target file extension}`

### Common usage examples
- Organize a specific folder (Windows):
    - `python file_organizer.py "C:\Users\Marvin\Downloads" .bmp .txt`
- Organize a specific folder (macOS / Linux):
    - `python3 file_organizer.py  ~/Downloads .bmp .txt`