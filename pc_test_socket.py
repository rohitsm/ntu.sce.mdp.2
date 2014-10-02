import socket
import string
import time
import threading

__author__ = "Rohit"

# Dummy client code


ip = "192.168.2.2" # Connecting to IP address of MDPGrp2
port = 5158
# message = "Hello World!"
message = list(string.ascii_lowercase)


# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, port))


# Send data
def write():
	print "Enter text to send: "
	msg = raw_input()
	while True:
		client_socket.send(msg)
		if len(msg) == 0 or msg == 'q':
			# Send message in anycase and then quit
			print "quitting..."
			break
		print "sending: ", msg
		print "Enter text to send: "
		msg = raw_input()
	print "quit write()"

# Receive data
def receive():
	while True:
		data = client_socket.recv(1024)
		if len(data) == 0 or data == 'q':
			print "quitting..."
			break
		print "Data received: %s " % data
		# while True:
		# 	if (data == 'q' or len(data) == 0):
		# 		break
	print "quit receive()"
	

# while True:

# 		time.sleep(0.5)c

thread_list = []
rt = threading.Thread(target = receive)
wt = threading.Thread(target = write)

rt.start()
wt.start()
print "start rt and wt"

thread_list.append(rt)
thread_list.append(wt)

for thread in thread_list:
	print "%s.join()" %s thread.getName()
	thread.join()
# rt.join()
# wt.join()
print "stop rt and wt"

# Close connections
client_socket.close()
print "End of client program"