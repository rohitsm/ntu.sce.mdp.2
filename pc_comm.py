import socket
import sys

__author__ = "Rohit"

class PcAPI(object):

	def __init__(self):
		self.tcp_ip = "192.168.2.2" # Connecting to IP address of MDPGrp2
		self.port = 5143
		self.conn = None
		self.client = None
		self.addr = None
		self.is_connect = False

	def close_sock(self):
		"""
		Close socket connections
		"""
		if self.conn:
			print "Closing server socket"
			self.conn.close()
		if self.client:
			print "Closing client socket"
			self.client.close()
		self.is_connect = False

	def is_connected(self):
		"""
		Check status of connection to PC
		"""
		return self.is_connect

	def init_pc_comm(self):
		"""
		Initiate PC connection over TCP
		"""
		# Create a TCP/IP socket
		self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.conn.bind((self.tcp_ip, self.port))
		self.conn.listen(1)		#Listen for incoming connections
		self.client, self.addr = self.conn.accept()
		print "Connected! Connection address: ", self.addr
		self.is_connect = True


	def write_to_PC(self, message):
		"""
		Write message to PC
		"""
		while self.is_connected():
			if len(message) == 0:
				break
			self.client.sendto(message, self.addr)
			print "Send to PC: %s " % message

	def read_from_PC(self):
		"""
		Read incoming message from PC
		"""
		while self.is_connected():
			if len()
			pc_data = self.client.recv(1024)
			if len(pc_data) == 0:
				break
			print "Data received: %s" % pc_data
		return pc_data

if __name__ == "__main__":
	print "main"
	pc = PcAPI()
	pc.init_pc_comm()

	send_msg = raw_input()
	print "write_to_PC(): %s " % send_msg
	pc.write_to_PC(send_msg)

	# print "read"
	# print "data received: %s " % pc.read_from_PC()

	print "closing sockets"
	bt.close_sock()