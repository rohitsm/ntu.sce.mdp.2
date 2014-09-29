import socket

__author__ = "Rohit"

# Dummy client code


ip = "192.168.2.2" # Connecting to IP address of MDPGrp2
port = 5143
message = "Hello World!"


# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, port))

# Send data
client_socket.send(message)

# Close connections
client_socket.close()
print "End of client program"