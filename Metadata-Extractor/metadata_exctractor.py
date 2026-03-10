"""
Metadata/Image exctractor script

This script scans a directory for image files and displays their
metadata in a table including filename, extension, format, dimensions, and mode.

"""

import os
from PIL import Image
from prettytable import PrettyTable

def main():
    # 1) Prompt the user for a directory path
    directory = input("Enter the directory path to search: ").strip()

    # 2) Verify that the path exists and is a directory
    if not os.path.exists(directory):
        print("Error: Path does not exist.")
        return
    if not os.path.isdir(directory):
        print("Error: Provided path is not a directory.")
        return

    # 3) Iterate through files and examine 
    table = PrettyTable(["File", "Ext", "Format", "Width", "Height", "Mode"])
    table.align = "l"

    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            ext = os.path.splitext(file)[1]

            try:
                with Image.open(filepath) as img:
                    table.add_row([
                        filepath,
                        ext,
                        img.format,
                        img.width,
                        img.height,
                        img.mode
                    ])
            except Exception:
                # Skip files that are not valid images
                continue

    # 4) Print table
    print(table)

if __name__ == "__main__":
    main()
