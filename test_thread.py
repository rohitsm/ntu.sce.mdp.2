import threading
from pc_comm import *


__author__ = 'Rohit'

class TestThread(object):
	def __init__(self):
		self.pc_api = PcAPI()
		self.pc_api.init_pc_comm()

	def writePC(self):
		"""
		Invoke write_to_PC()
		"""
		print "Enter text to send: "
		send_msg = raw_input()
		# print "write_to_PC(): %s " % send_msg	
		while len(send_msg) != 0 or send_msg == 'q':
			self.pc_api.write_to_PC(msg)
			print "Writing to PC: %s " % msg

	def readPC(self):
		"""
		Invoke read_from_PC()
		"""
		print "inside readPC"
		while True:
			read_msg = self.pc_api.read_from_PC()
			if len(read_msg) == 0 or read_msg == 'q':
				break
		print "Message received from PC %s " %read_msg

	def close_all_sockets():
		self.pc_api.close_sock()


if __name__ == "__main__":
	print "main"

	pc_thread = TestThread()

	# Read thread
	rt = threading.Thread(target = pc_thread.readPC, name = 'ReadThread')
	print "created rt"
	# Write thread
	wt = threading.Thread(target = pc_thread.writePC, name = 'writeThread')
	print "created wt"

	rt.start()
	wt.start()
	print "start rt and wt"

	# rt.setDaemon(True)

	rt.join()
	wt.join()
	print "join rt and wt"
	pc_thread.close_all_sockets()
	print "End thread"

