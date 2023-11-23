# ---- scapy library import ----
from scapy.all import *

# ---- function to create and send ICMP packets in fragments ----
def send_fragmented_icmp_packets(destination_ip, payload):

# ---- fragmentation of the load into pieces (adjustable size) ----    
    fragment_size = 1
    payload_fragments = [payload[i:i+fragment_size] for i in range(0, len(payload), fragment_size)]

    # ---- each fragment is sent as a separate ICMP packet ----
    for fragment in payload_fragments:

        # ---- creating ICMP Echo Request packet with payload fragment ----
        icmp_packet = IP(dst=destination_ip) / ICMP() / Raw(load=fragment)

        # ---- showing the ICMP fragmented packet ----
        print(f"Fragmented ICMP packet:")
        icmp_packet.show()

        # ---- package shipping ----
        send(icmp_packet)

# ---- example of use ----s
if __name__ == "__main__":

    # destination IP and custom payload 
    target_ip = "192.168.3.20"
    custom_payload = "SSI{H4ck3rs_w1n}"

    # ---- call function to send payload fragments in ICMP packets ----
    send_fragmented_icmp_packets(target_ip, custom_payload)