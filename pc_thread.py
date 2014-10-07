import threading
import Queue
from pc_comm import *

__author__ = 'Rohit'

class PCThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.pc_api = PcAPI()
		self.pc_api.init_pc_comm()

	def writePC(self, to_pc_q):
		"""
		Invoke write_to_PC()
		"""
		print "Sending to PC: "
		while True:
			while not to_pc_q.empty():
				send_pc_msg = to_pc_q.get()
				self.pc_api.write_to_PC(send_pc_msg)
				# if len(send_pc_msg) == 0 or send_pc_msg == 'q':
				# 	# Send message in anycase and then quit
				# 	print "quitting..."	
				# 	break
				print "Writing to PC: %s " % send_pc_msg
		print "quit writePC"
		# return send_pc_msg

	# Takes two Qs as arguments and writes (put) value read
	# from PC into them depending on the header
	def readPC(self, to_bt_q): # Include "to_sr_q" in the args
		"""
		Invoke read_from_PC()
		"""
		print "Inside readPC:"
		while True:
			try:
				read_pc_msg = self.pc_api.read_from_PC()
				# if len(read_pc_msg) == 0 or read_pc_msg == 'q':
				# 	print "quitting..."
				# 	break

				# Check header for Destination and strip out first char
				if (read_pc_msg[0].lower() == 'a'):	# send to android
					to_bt_q.put(read_pc_msg[1:]) 	# Strip header here
					print "testing pc q: Value written = %s " % read_pc_msg[1:]

				elif (read_pc_msg[0].lower() == 'h'):
					# to_sr_q.put(read_pc_msg[1:])	# send to hardware
					print "testing pc q: Value written = %s " % read_pc_msg[1:]

				else:
					print "Incorrect header received from PC"
			
			except IndexError:
				print "Incorrect header format"
				continue
				# print "Message received from PC %s. Put in queue " %read_pc_msg
		print "quit readPC"

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

