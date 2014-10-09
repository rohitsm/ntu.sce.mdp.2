import time
import threading
import Queue
from bt_comm import *

__author__ = 'Rohit'
bt_q_lock = threading.Lock()

class BTThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.bt_api = AndroidAPI()
		self.bt_api.connect_bluetooth()

	def writeBT(self, to_bt_q):
		"""
		Invoke write_to_bt()
		"""
		time.sleep(0.2)
		print "Sending text to Andorid: "
		while True:
			bt_q_lock.acquire()		# Lock the queue
			if (not to_bt_q.empty()):
				send_bt_msg = to_bt_q.get()
				self.bt_api.write_to_bt(send_bt_msg)
				print "Writing to BT: %s" % send_bt_msg
			time.sleep(0.2)
			bt_q_lock.release()		# Release the lock
		
	# Takes two Qs as arguments and writes (put) value read
	# from BT into them depending on the header
	def readBT(self, to_pc_q, to_sr_q): # Include "to_sr_q" in the args
		"""
		Invoke read_from_bt()
		"""
		time.sleep(0.5)	# Delay before reading
		print "readBT: to_pc_q = %s " %to_pc_q
		while True:
			bt_q_lock.acquire()		# Lock the queue
			read_bt_msg = self.bt_api.read_from_bt()
				
			# Check header for Destination and strip out first char
			if (read_bt_msg[0].lower() == 'p'): # send to PC
				to_pc_q.put(read_bt_msg[1:]) 	# strip header here
				bt_q_lock.release()	# Release the lock
				print "testing pc q: Value written = %s " % read_bt_msg[1:]
			
			# elif (read_bt_msg[0].lower() == 'h'):	# send to hardware (serial)
			# 	to_sr_q.put(read_bt_msg[1:]) 	# strip header here
			# 	print "testing serial q: Value written = %s " % read_bt_msg[1:]
			
			else:
				bt_q_lock.release()	# Release the lock
				print "Incorrect header received from BT: [%s]" %read_bt_msg[0]

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



