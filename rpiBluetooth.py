from bluetooth import *

__author__ = 'Rohit'

# Server inits
btport = 4					# RFCOMM port 4
message = "Hello World" 	# message to be sent

# Creating the server socket and bind to port
server_socket = BluetoothSocket( RFCOMM )
server_socket.bind(("", btport))
server_socket.listen(1)			# Listen for requests

# port = server_socket.getsockname()[1]

# uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

# advertise_service( server_sock, "SampleServer",
#                    service_id = uuid,
#                    service_classes = [ uuid, SERIAL_PORT_CLASS ],
#                    profiles = [ SERIAL_PORT_PROFILE ],
# 				)

# print "Waiting for connection on RFCOMM channel %d" % port


# Accept requests
client_socket, client_address = server_socket.accept()
print "Accepted connection from ", client_address

data = client_socket.recv(1024)
print "Received [%s] " % data

# Close socket connections
server_socket.close()
client_socket.close()
print "end of program"
