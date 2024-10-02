Network Packet analyzer

How it Works
The packet sniffer uses the Scapy library to capture and analyze network packets on a specified interface. Here's a step-by-step explanation of the process:

Packet Capture: The program uses the scapy.sniff function to capture a specified number of packets on the specified interface. This function returns a list of packets, which are then analyzed by the program.
Packet Analysis: The program iterates over the captured packets and extracts relevant information, including:
Source IP Address: The IP address of the device that sent the packet.
Destination IP Address: The IP address of the device that the packet is intended for.
Protocol: The protocol used to transmit the packet (e.g. TCP, UDP, ICMP).
Payload Data: The actual data being transmitted in the packet.
Data Display: The program displays the extracted information for each packet, providing a detailed view of the network traffic.
Technical Details
The program uses the Scapy library to interact with the network interface and capture packets.
The scapy.sniff function is used to capture packets, and the scapy.Packet class is used to represent each captured packet.
The program uses the scapy.IP class to extract IP address information from each packet.
The program uses the scapy.payload attribute to extract the payload data from each packet
