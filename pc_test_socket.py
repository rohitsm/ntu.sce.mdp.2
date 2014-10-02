import socket
import string

__author__ = "Rohit"

# Dummy client code


ip = "192.168.2.2" # Connecting to IP address of MDPGrp2
port = 5143
# message = "Hello World!"
message = list(string.ascii_lowercase)


# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, port))

while True:
	# Send data

	for item in message:
		client_socket.send(item)
		print "sending: ", item

	# Receive data
	data = client_socket.recv(1024)
	print "Data received: %s " % data
	if (data == 'q' or len(data) == 0):
		break


# Close connections
client_socket.close()
print "End of client program"