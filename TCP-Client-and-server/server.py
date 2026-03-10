"""
 TCP Server (MD5 Echo)

Multi-threaded TCP server that:
- Receives messages from clients
- Computes MD5 hash of each message
- Sends hash back to client
- Logs all activity with timestamps

"""
import socket
import threading
import hashlib
from datetime import datetime

# Server host and port
HOST = ''
PORT = 5555
LOG_FILE = "server_log.txt"

def log_entry(entry):
    """Append log entries to the log file with timestamps."""
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {entry}\n")

def handle_client(client_socket, address):
    """Handles communication with a single client."""
    print(f"[+] Connection from {address}")
    log_entry(f"New connection from {address}")

    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break

            message = data.decode('utf-8').strip()
            md5_hash = hashlib.md5(message.encode()).hexdigest()

            log_entry(f"Received from {address}: {message}")
            log_entry(f"MD5 digest for {address}: {md5_hash}")

            client_socket.send(md5_hash.encode('utf-8'))
            print(f"[*] {address} -> {message} -> {md5_hash}")

    except ConnectionResetError:
        log_entry(f"Connection reset by {address}")
    finally:
        client_socket.close()
        log_entry(f"Connection closed for {address}")
        print(f"[-] Connection closed for {address}")

def start_server():
    """Starts the TCP server."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[+] Listening on port {PORT}...")
    log_entry(f"Server started on port {PORT}")

    try:
        while True:
            client_socket, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(client_socket, addr))
            thread.start()
    except KeyboardInterrupt:
        print("\n[!] Server shutting down...")
        log_entry("Server shutdown by user")
    finally:
        server.close()

if __name__ == "__main__":
    start_server()
