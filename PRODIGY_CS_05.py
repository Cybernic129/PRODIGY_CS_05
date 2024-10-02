import scapy.all as scapy

# Function to capture and analyze network packets
def capture_packets(interface, count):
    print("Capturing packets on interface", interface)
    packets = scapy.sniff(iface=interface, count=count)
    print("Captured", len(packets), "packets")

    for packet in packets:
        print("Packet:", packet.summary())
        print("Source IP:", packet[scapy.IP].src)
        print("Destination IP:", packet[scapy.IP].dst)
        print("Protocol:", packet.protocol)
        print("Payload:", packet.payload)
        print()

# Main function
def main():
    # Get the interface from the user
    interface = input("Enter the interface to capture packets on (e.g. eth0, wlan0): ")

    # Get the number of packets to capture from the user
    count = int(input("Enter the number of packets to capture: "))

    # Capture and analyze packets
    capture_packets(interface, count)

if __name__ == "__main__":
    main()