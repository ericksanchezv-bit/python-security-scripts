# 🧾 File Processing Object

## 📘 Project Overview
The **File Processing Object** is a simple Python-based tool that extracts and displays file metadata and binary headers for forensic inspection.  
It’s designed to help cybersecurity students and analysts understand file attributes such as permissions, timestamps, and ownership information.

---

## 🧠 Features
- Extracts detailed file metadata:
  - Size, owner, permissions, and timestamps
- Retrieves and displays the first N bytes (default: 20) of each file in hexadecimal
- Iterates through all files in a specified directory
- Provides clear console output for forensic review

---

## 🧩 Technologies Used
- **Language:** Python 3  
- **Libraries:** `os`, `stat`, `time`, `getpass` (all from Python standard library)
