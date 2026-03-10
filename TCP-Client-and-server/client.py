"""
TCP Client (MD5 Sender)

Connects to the TCP server, sends messages, and receives the MD5 hash
of each message. Logs all activity with timestamps.

"""
import socket
import time
from datetime import datetime

SERVER_HOST = '127.0.0.1'  
SERVER_PORT = 5555
LOG_FILE = "client_log.txt"

def log_entry(entry):
    """Append log entries to the log file with timestamps."""
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {entry}\n")

def main():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((SERVER_HOST, SERVER_PORT))
        print(f"[+] Connected to {SERVER_HOST}:{SERVER_PORT}\n")
        log_entry(f"Connected to {SERVER_HOST}:{SERVER_PORT}")

        for i in range(1, 11):
            message = f"Message number {i}"
            print(f"[*] Sending: {message}")
            log_entry(f"Sent: {message}")

            client.send(message.encode('utf-8'))
            response = client.recv(1024).decode('utf-8')

            print(f"[+] Received MD5 digest: {response}\n")
            log_entry(f"Received MD5 digest: {response}")

            time.sleep(1)

        print("[*] All messages sent successfully. Closing connection...")
        log_entry("All messages sent. Connection closed normally.")

    except ConnectionRefusedError:
        print("[!] Connection failed. Make sure the server is running.")
        log_entry("Connection failed — server not running.")
    except Exception as e:
        print(f"[!] Error: {e}")
        log_entry(f"Error: {e}")
    finally:
        client.close()
        print("[*] Connection closed.")
        log_entry("Socket closed.")

if __name__ == "__main__":
    main()
