import threading
from pc_comm import *


__author__ = 'Rohit'

class TestThread(object):
	def __init__(self):
		self.pc_api = PcAPI()
		pc_api.init_pc_comm()

	def writePC(self, msg):
		"""
		Invoke write_to_PC()
		"""
		print "Enter text: "
		send_msg = raw_input()
		# print "write_to_PC(): %s " % send_msg	
		self.pc_api.write_to_PC(msg)
		print "Writing to PC: %s " % msg

	def readPC(self, msg):
		"""
		Invoke read_from_PC()
		"""
		read_msg = self.pc_api.read_from_PC()
		print "Message received from PC %s ", %read_msg

	def close_all_sockets():
		self.pc_api.close_sock()


if __name__ = "__main__":
	print "main"

	pc_thread = TestThread()

	# Read thread
	rt = threading.Thread(target = pc_thread.readPC(), name = 'ReadThread')
	# Write thread
	wt = threading.Thread(target = pc_thread.writePC(msg), name = 'writeThread')

	rt.start()
	wt.start()

	# rt.setDaemon(True)

	rt.join()
	wt.join()
	pc_thread.close_all_sockets()
	print "End thread"

