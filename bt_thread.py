import threading
import Queue
from bt_comm import *

__author__ = 'Rohit'

class BTThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.bt_api = AndroidAPI()
		self.bt_api.init_bluetooth()

	def writeBT(self, to_bt_q):
		"""
		Invoke write_to_bt()
		"""
		print "Sending text to Andorid: "
		while True:
			while not to_bt_q.empty():
				send_bt_msg = to_bt_q.get()
				# print "write_to_bt(): %s " % send_bt_msg
				self.bt_api.write_to_bt(send_bt_msg)
				if len(send_bt_msg) == 0 or send_bt_msg == 'q':
					#Send message in anycase and then quit
					print "quitting..."
					break
				print "Writing to BT: %s" % send_bt_msg
		print "quit writeBT"
		# return send_bt_msg

	# Receives two Qs as arguments and writes (put) to them
	def readBT(self, to_pc_q): # Include "to_sr_q" in the args
		"""
		Invoke read_from_bt()
		"""
		print "inside readBT"
		while True:
			read_bt_msg = self.bt_api.read_from_bt()
			if len(read_bt_msg) == 0 or read_bt_msg == 'q':
				print "quitting..."
				break
			to_pc_q.put(read_bt_msg) # Strip header here
			print "Message received from BT: %s. Put in queue" % read_bt_msg
		print "quit readBT"

	def close_all_bt_sockets(self):
		self.bt_api.close_bt_socket()

# if __name__ == "__main__":
# 	print "main"
# 	bt_thread = BTThread()

# 	#Read thread
# 	rt = threading.Thread(target = bt_thread.readBT, name = 'ReadBT')
# 	print "created rt"
# 	#Read thread
# 	wt = threading.Thread(target = bt_thread.writeBT, name = 'Write')
# 	print "created wt"

# 	rt.start()
# 	wt.start()
# 	print "start rt and wt"

# 	rt.join()
# 	wt.join()
# 	print "join rt and wt"
# 	bt_thread.close_all_bt_sockets()
# 	print "End thread"



