from __future__ import print_function
"""
Project: File Processing Object
Description: FileProcessor class extracts file metadata and headers
             for forensic inspection.
"""

import os
import stat
import time
import getpass


class FileProcessor:
    def __init__(self, file_path):
        """Initialize with file path, verify existence, and collect metadata"""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File does not exist: {file_path}")

        self.file_path = file_path
        self.header = None

       
        file_stats = os.stat(file_path)
        self.file_size = file_stats.st_size

        
        try:
            self.owner = getpass.getuser()
        except Exception:
            self.owner = "Unknown"

        self.mode = stat.filemode(file_stats.st_mode)
        self.access_time = time.ctime(file_stats.st_atime)
        self.modify_time = time.ctime(file_stats.st_mtime)
        self.change_time = time.ctime(file_stats.st_ctime)

    def get_file_header(self, num_bytes=20):
        """Extract first N bytes of file and store in instance attribute"""
        with open(self.file_path, "rb") as f:
            self.header = f.read(num_bytes)

    def print_file_details(self):
        """Print metadata and header in hex"""
        print("=" * 60)
        print(f"File: {self.file_path}")
        print(f"Size: {self.file_size} bytes")
        print(f"Owner: {self.owner}")
        print(f"Permissions: {self.mode}")
        print(f"Access Time: {self.access_time}")
        print(f"Modify Time: {self.modify_time}")
        print(f"Change Time: {self.change_time}")

        if self.header:
            print("Header (Hex):", self.header.hex())
        else:
            print("Header not yet retrieved. Run get_file_header().")


def main():
    directory = input("Enter directory path: ").strip()

    if not os.path.isdir(directory):
        print("Invalid directory path.")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

       
        if os.path.isfile(file_path):
            try:
                processor = FileProcessor(file_path)
                processor.get_file_header()
                processor.print_file_details()
            except Exception as e:
                print(f"Error processing {filename}: {e}")


if __name__ == "__main__":
    main()
