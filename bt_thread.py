import threading
from bt_comm import *

__author__ = 'Rohit'

class BTThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.bt_api = AndroidAPI()
		self.bt_api.init_bluetooth()

	def writeBT(self):
		"""
		Invoke write_to_bt()
		"""
		print "Enter text to send to Andorid: "
		send_bt_msg = raw_input()
		# print "write_to_bt(): %s " % send_bt_msg
		while True:
			self.bt_api.write_to_bt(send_bt_msg)
			if len(send_bt_msg) == 0 or send_bt_msg == 'q':
				#Send message in anycase and then quit
				print "quitting..."
				break
			print "Writing to BT: %s" % send_bt_msg
			print "Enter text to send: "
			send_bt_msg = raw_input()
		print "quit writeBT"
		return send_bt_msg


	def readBT(self):
		"""
		Invoke read_from_bt()
		"""
		print "inside readBT"
		while True:
			read_bt_msg = self.bt_api.read_from_bt()
			if len(read_bt_msg) == 0 or read_bt_msg == 'q':
				print "quitting..."
				break
			print "Message received from BT: %s" % read_bt_msg
		print "quit readBT"

	def close_all_bt_sockets(self):
		self.bt_api.close_bt_socket()

if __name__ == "__main__":
	print "main"
	bt_thread = BTThread()

	#Read thread
	rt = threading.Thread(target = bt_thread.readBT, name = 'ReadBT')
	print "created rt"
	#Read thread
	wt = threading.Thread(target = bt_thread.writeBT, name = 'Write')
	print "created wt"

	rt.start()
	wt.start()
	print "start rt and wt"

	rt.join()
	wt.join()
	print "join rt and wt"
	bt_thread.close_all_bt_sockets()
	print "End thread"



