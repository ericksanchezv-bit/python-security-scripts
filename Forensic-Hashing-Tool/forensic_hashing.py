from __future__ import print_function
"""
Forensic Hashing Tool

This script recursively scans files in a directory and computes MD5 hashes
for each file. It displays the hash along with the file path for forensic
analysis and file integrity verification.

"""
import os
import hashlib

directory = "."

fileList   = []
fileHashes = {}

for root, dirs, files in os.walk(directory):

    # Walk the path from top to bottom.
    # For each file obtain the filename 
    
    for fileName in files:
        path = os.path.join(root, fileName)
        fullPath = os.path.abspath(path)
        fileList.append(fullPath)
        
        try:
            with open(fullPath, "rb") as f:
                fileBytes = f.read()
                md5Hash = hashlib.md5(fileBytes).hexdigest()

                fileHashes[md5Hash] = fullPath

        except Exception as e:
            print(f"Could not read {fullPath}: {e}")


print("\nFile Hashes:")
for hashValue, filePath in fileHashes.items():
    print(f"{hashValue} : {filePath}")
        
