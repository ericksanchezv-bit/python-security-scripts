"""
Firewall Log Parser (PCAP Analyzer)

This script analyzes PCAP files and extracts network communication
patterns including hosts, protocols, and observed ports.

Author: Erick Sanchez Valenzuela
"""
import os
import sys
from scapy.all import Ether, IP, TCP, UDP
from scapy.utils import PcapReader
from prettytable import PrettyTable

def process_pcap(pcapFile):
    print(f"\nProcessing: {pcapFile}")

    connections = set()
    ports = {}

    with PcapReader(pcapFile) as pcap:
        for pkt in pcap:
            if not pkt.haslayer(Ether) or IP not in pkt:
                continue

            srcIP, dstIP = pkt[IP].src, pkt[IP].dst
            proto = pkt[IP].proto
            sport, dport = None, None

            if TCP in pkt:
                sport, dport = pkt[TCP].sport, pkt[TCP].dport
            elif UDP in pkt:
                sport, dport = pkt[UDP].sport, pkt[UDP].dport

            connections.add((srcIP, dstIP, proto, sport, dport))
            if sport:
                ports.setdefault(srcIP, set()).add(sport)
            if dport:
                ports.setdefault(dstIP, set()).add(dport)

    # Generate Tables
    connTable = PrettyTable(["Source", "Destination", "Protocol", "Src Port", "Dst Port"])
    for c in connections:
        connTable.add_row(c)

    portTable = PrettyTable(["Host", "Ports"])
    for host, portset in ports.items():
        portTable.add_row([host, ", ".join(str(p) for p in sorted(portset))])

    # Print to Console
    print("\nConnection Summary:")
    print(connTable)
    print("\nObserved Ports by Host:")
    print(portTable)

    # Save to File
    reportName = os.path.splitext(pcapFile)[0] + "_report.txt"
    with open(reportName, "w") as f:
        f.write(f"Report for: {pcapFile}\n\n")
        f.write("=== Connection Summary ===\n")
        f.write(connTable.get_string() + "\n\n")
        f.write("=== Observed Ports by Host ===\n")
        f.write(portTable.get_string() + "\n")

    print(f"\nReport saved as: {reportName}\n")


if __name__ == "__main__":
    targetPath = input("Target PCAP File or Folder: ").strip()

    if os.path.isdir(targetPath):
        pcapFiles = [os.path.join(targetPath, f) for f in os.listdir(targetPath) if f.lower().endswith(".pcap")]
    elif os.path.isfile(targetPath) and targetPath.lower().endswith(".pcap"):
        pcapFiles = [targetPath]
    else:
        print("Invalid path or no .pcap files found.")
        sys.exit(1)

    for pcapFile in pcapFiles:
        process_pcap(pcapFile)

    print("\nAll reports generated successfully.")
