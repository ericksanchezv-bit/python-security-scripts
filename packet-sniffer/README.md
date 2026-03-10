# Packet Sniffer 🌐

## Overview

This project is a simple Python packet sniffer that captures raw IP packets and displays basic network traffic information.

It shows:

* Source IP address
* Destination IP address
* Protocol type (TCP, UDP, ICMP)
* Packet occurrence counts

The script also aggregates packet traffic to show common communication patterns.

## Requirements ⚙️

* Python 3
* prettytable

Install dependency:

```
pip install prettytable
```

⚠️ Running this script requires **administrator/root privileges** because it uses raw sockets.

## Usage ▶️

Run the script:

```
python packet_sniffer.py
```

The program will start capturing packets and display a table of observed network traffic.

## Attribution 📚

This project is based on examples from the book:

**Black Hat Python** by Justin Seitz.

The code was adapted and extended for educational purposes to demonstrate packet capture and basic network traffic analysis.

## Disclaimer ⚠️

This project is intended for **educational use only**. Packet sniffing should only be performed on networks you own or have permission to analyze.
