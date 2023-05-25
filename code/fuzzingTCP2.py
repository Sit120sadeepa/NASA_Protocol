import socket
import random
import string
import struct
from scapy.all import *
# without dpkt

def fuzz_tcp(node_ip, node_port):
    # Craft a TCP packet with a fuzzed payload
    fuzz_payload = generate_fuzzed_payload()
    tcp_packet = struct.pack('!H H I I B B H H', random.randint(1, 65535), node_port, 0, 0, 0x50, 6, 0, 0) + struct.pack('!I', 0)
    fuzz_payload.encode()

    # Create a TCP socket and connect to the target node
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect((node_ip, node_port))

    # Send the TCP packet to the target node
    tcp_socket.send(tcp_packet)

    # Receive the TCP response
    response = tcp_socket.recv(1024)

    # Process the TCP response, add your response processing logic here
    print("Received response from {}:{}".format(node_ip, node_port))

    tcp_socket.close()

def generate_fuzzed_payload():
    # Implement your payload fuzzing logic here
    # Return a fuzzed payload as a string
    payload_length = random.randint(10, 20)
    fuzzed_payload = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(payload_length))
    return fuzzed_payload



# Target node IP and port
target_node_ip = "10.0.0.1"
target_node_port = 4556

# Fuzz the target node's TCP
fuzz_tcp(target_node_ip, target_node_port)
