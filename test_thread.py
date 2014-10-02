import threading
from pc_comm import *


__author__ = 'Rohit'

class TestThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.pc_api = PcAPI()
		self.pc_api.init_pc_comm()

	def writePC(self):
		"""
		Invoke write_to_PC()
		"""
		print "Enter text to send: "
		send_msg = raw_input()
		# print "write_to_PC(): %s " % send_msg	
		while True:
			self.pc_api.write_to_PC(send_msg)
			if len(send_msg) == 0 or send_msg == 'q':
				# Send message in anycase and then quit
				print "quitting..."	
				break
			print "Writing to PC: %s " % send_msg
			print "Enter text to send: "
			send_msg = raw_input()
		print "quit writePC"


	def readPC(self):
		"""
		Invoke read_from_PC()
		"""
		print "inside readPC"
		while True:
			read_msg = self.pc_api.read_from_PC()
			if len(read_msg) == 0 or read_msg == 'q':
				print "quitting..."
				break
			print "Message received from PC %s " %read_msg
		print "quit readPC"

	def close_all_sockets(self):
		self.pc_api.close_sock()


if __name__ == "__main__":
	print "main"

	thread_list = []
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

	# thread_list.append(rt)
	# print "Append thread 'rt': %s " % rt.getName()
	# thread_list.append(wt)
	# print "Append thread 'wt': %s " % wt.getName()


	# for thread in thread_list:
	# 	print "%s.join()" % thread.getName()
	# 	thread.join()
	
	rt.join()
	wt.join()
	print "join rt and wt"
	pc_thread.close_all_sockets()
	print "End thread"

