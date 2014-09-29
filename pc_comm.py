import socket
import sys

__author__ = "Rohit"

tcp_ip = "192.168.2.2" # Connecting to IP address of MDPGrp2
port = "5143"

# Create a TCP/IP socket
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind((tcp_ip, port))

# Listen for incoming connection
conn.listen(1)

client, addr = conn.accept()
print "Connected! Connection address: ", addr

pc_data = client.recv(1024)
print "Data received: %s" %pc_data

# Close the connections
client.close()
conn.close()
print "end of program"


