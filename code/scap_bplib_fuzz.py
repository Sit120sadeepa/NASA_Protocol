from scapy.layers.inet import IP, UDP
import socket
from bpcodec import Bundle
import random
import string

# Define the number of packets to send
num_packets = 100

# Generate random payloads
payloads = [''.join(random.choices(string.ascii_letters, k=random.randint(1, 20))) for _ in range(num_packets)]

# Establish a socket connection to a DTN node
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(("localhost", 4556))

# Send the encoded bundles to the DTN node
for payload in payloads:
    # Create a new DTN bundle packet with the payload
    bundle_packet = IP(dst="dtn://destination") / UDP() / Bundle(payload=payload)

    # Encode the bundle headers and payload using bpcodec
    encoded_bundle = bundle_packet[Bundle].encode()

    # Send the encoded bundle to the DTN node
    sock.send(encoded_bundle)

# Close the socket connection
sock.close()

