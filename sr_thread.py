import time
import threading
import serial
from sr_comm import *

__author__ = "Rohit"

class SRThread(threading.thread):
	def __init__(self):
		threading.thread.__init__(self)
		self.sr_api = SRThread()
		self.sr_api.connect_serial()

	def writeSR(self, to_sr_q):
		"""
		invoke write_to_serial()
		"""
		print "Sending text to Arduino: "
		while True:
			while not to_sr_q.empty():
				send_sr_msg = to_sr_q.get()
				self.sr_api.write_to_serial(send_sr_msg)
				
				print "Writing to SR: %s" % send_sr_msg
				time.sleep(0.5)
			# print "quit writeSR"

	# Takes two Qs as arguments and writes (put) value read
	# from SR into them depending on the header
	def readSR(self, to_bt_q, to_pc_q):
		"""
		Invoke read_from_serial()
		"""
		print "Inside readSR"
		while True:
			read_sr_msg = self.sr_api.read_from_serial()
			
			# Check header for destination and strip out first char
			if (read_sr_msg[0].lower() == 'p'): # send to PC
				to_pc_q.put(read_sr_msg[1:])	# strip header here
				print "testing pc q: Value written = %s " % read_sr_msg[1:]

			elif (read_sr_msg[0].lower() == 'a'):# send to android
				to_bt_q.put(read_sr_msg[1:])	#strip header here
				print "testing bt q: value written = %s " % read_sr_msg[1:]

			else:
				print "Incorrect header received from Arduino"

		print "quit readSR"

	def close_all_sr_sockets(self):
		"""
		invoke close_sr_socket()
		"""
		self.sr_api.close_sr_socket()

# Test code written in integrator.py


























