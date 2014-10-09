import time
import threading
import serial
import Queue
from sr_comm import *

__author__ = "Rohit"
# sr_q_lock = threading.Lock()

class SRThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.sr_api = SerialAPI()
		self.sr_api.connect_serial()
		time.sleep(2)	#Sleep for 2 secs before starting

	def writeSR(self, to_sr_q):
		"""
		invoke write_to_serial()
		"""
		time.sleep(0.2)
		print "inside writeSR: "
		while True:
			# sr_q_lock.acquire()		# Lock the thread
			if (not to_sr_q.empty()):
				send_sr_msg = to_sr_q.get()
				self.sr_api.write_to_serial(send_sr_msg)
				print "Writing to SR: %s" % send_sr_msg
				# time.sleep(0.5)
			# sr_q_lock.release()		# Release the lock

	# Takes two Qs as arguments and writes (put) value read
	# from SR into them depending on the header
	def readSR(self, to_bt_q, to_pc_q):
		"""
		Invoke read_from_serial()
		"""
		time.sleep(0.5)
		print "Inside readSR"
		while True:
			# sr_q_lock.acquire()		# Lock the thread
			read_sr_msg = self.sr_api.read_from_serial()
			
			# Check header for destination and strip out first char
			if (read_sr_msg[0].lower() == 'p'): # send to PC
				to_pc_q.put(read_sr_msg[1:])	# strip header here
				# sr_q_lock.release()		# Release the lock
				print "testing pc q: Value written = %s " % read_sr_msg[1:]

			# elif (read_sr_msg[0].lower() == 'a'):# send to android
			# 	to_bt_q.put(read_sr_msg[1:])	#strip header here
			# 	print "testing bt q: value written = [%s] " % read_sr_msg[1:]

			else:
				print "Incorrect header received from Arduino: [%s]" %read_sr_msg[0]
				# sr_q_lock.release()		# Release the lock
			


	def close_all_sr_sockets(self):
		"""
		invoke close_sr_socket()
		"""
		self.sr_api.close_sr_socket()

# Test code written in integrator.py


























