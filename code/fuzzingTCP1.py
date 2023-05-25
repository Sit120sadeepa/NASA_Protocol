from scapy.all import *

def fuzz_tcp(node_ip, node_port):
    # Craft TCP packet with fuzzing payload
    packet = IP(dst=node_ip) / TCP(dport=node_port, flags="S") / "FuzzPayload"

    # Send the packet to the target node
    response = sr1(packet, timeout=1)

    if response and TCP in response:
        # Analyze the response received from the target node
        if response[TCP].flags == "SA":
            print("Received SYN-ACK response from {}:{}:{}".format(node_ip, node_port, response.summary()))
            # Further analysis and processing of the SYN-ACK response can be performed here
        else:
            print("Received response from {}:{}:{}".format(node_ip, node_port, response.summary()))
            # Further analysis and processing of the response can be performed here


# List of target node IP addresses
target_nodes = ["10.0.0.1", "10.0.0.2", "10.3.3.2", "10.3.3.1"]

# Fuzz each target node in DNS and observe behavior
for node_ip in target_nodes:
    fuzz_tcp(node_ip, 80)

