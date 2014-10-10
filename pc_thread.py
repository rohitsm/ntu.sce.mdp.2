import time
import threading
import Queue
from pc_comm import *

__author__ = 'Rohit'
# pc_q_lock = threading.Lock()

class PCThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.pc_api = PcAPI()
		self.pc_api.init_pc_comm()

	def writePC(self, to_pc_q):
		"""
		Invoke write_to_PC()
		"""
		time.sleep(0.2)
		print "inside writePC: "
		while True:
			# pc_q_lock.acquire()		# Lock the thread
			if (not to_pc_q.empty()):
				send_pc_msg = to_pc_q.get()
				self.pc_api.write_to_PC(send_pc_msg)
				print "Writing to PC: %s " % send_pc_msg
				time.sleep(0.5)
			# pc_q_lock.release()		# Release the lock

	# Takes two Qs as arguments and writes (put) value read
	# from PC into them depending on the header
	def readPC(self, to_bt_q, to_sr_q): # Include "to_sr_q" in the args
		"""
		Invoke read_from_PC()
		"""
		# time.sleep(0.5)		# Delay before reading
		print "Inside readPC:"
		while True:
			# pc_q_lock.acquire()				# Lock the thread
			try:
				time.sleep(0.5)	# Delay before reading from socket
				read_pc_msg = self.pc_api.read_from_PC()
				# print "Value received  from PC: %s " % read_pc_msg

				# Check header for Destination and strip out first char
				if (read_pc_msg[0].lower() == 'a'):	# send to android
					to_bt_q.put(read_pc_msg[1:]) 	# Strip header here
					# pc_q_lock.release()		# Release the lock
					# print "(inside readPC) QSIZE of to_bt_q = ", to_bt_q.qsize()
					print "testing bt q: Value written = %s " % read_pc_msg[1:]

				elif (read_pc_msg[0].lower() == 'h'):
					to_sr_q.put(read_pc_msg[1:])	# send to hardware
					# pc_q_lock.release()		# Release the lock
					print "testing sr q: Value written = %s " % read_pc_msg[1:]

				else:
					# pc_q_lock.release()		# Release the lock
					print "Incorrect header received from PC: [%s] " % read_pc_msg[0]

			except IndexError:
				# pc_q_lock.release()			# Release the lock
				print "Incorrect header format"

				
	def close_all_pc_sockets(self):
		self.pc_api.close_pc_socket()


# if __name__ == "__main__":
# 	print "main"
# 	pc_thread = PCThread()

# 	# Read thread
# 	rt = threading.Thread(target = pc_thread.readPC, name = 'ReadThread')
# 	print "created rt"
# 	# Write thread
# 	wt = threading.Thread(target = pc_thread.writePC, name = 'writeThread')
# 	print "created wt"

# 	rt.start()
# 	wt.start()
# 	print "start rt and wt"

# 	# rt.setDaemon(True)

# 	# thread_list.append(rt)
# 	# print "Append thread 'rt': %s " % rt.getName()
# 	# thread_list.append(wt)
# 	# print "Append thread 'wt': %s " % wt.getName()


# 	# for thread in thread_list:
# 	# 	print "%s.join()" % thread.getName()
# 	# 	thread.join()
	
# 	rt.join()
# 	wt.join()
# 	print "join rt and wt"
# 	pc_thread.close_all_pc_sockets()
# 	print "End thread"

