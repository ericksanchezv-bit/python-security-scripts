# 📡 TCP MD5 Tools

This folder contains Python scripts for **TCP communication with MD5 hashing**: a multi-threaded server and a client that sends messages and receives MD5 hashes.

---

## 🖥️ TCP Server (MD5 Echo)

The server:

- Listens for incoming client connections  
- Receives messages from clients  
- Computes the **MD5 hash** of each message  
- Sends the hash back to the client  
- Logs all activity to `server_log.txt`

### ✨ Features

- Multi-threaded: handles multiple clients concurrently  
- Logs messages and MD5 digests  
- Graceful shutdown with Ctrl+C  

### ⚙️ Requirements

- Python 3.x  
- Standard libraries only: `socket`, `threading`, `hashlib`, `datetime`  

### 🚀 Usage

1. Run the server:

```bash
python tcp_server.py
