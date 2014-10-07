import sys
import Queue
import threading
from pc_thread import *
from bt_thread import *
# from sr_thread import *

__author__ = 'Rohit'

# Create queues
to_bt = Queue.Queue() 
to_pc = Queue.Queue()
# to_sr = Queue.Queue()		// Serial queue

if __name__ == "__main__":
	pc_thread = PCThread()
	bt_thread = BTThread()
	# sr_thread = SRThread()

	# PC read and write thread
	rt_pc = threading.Thread(target = pc_thread.readPC, args = (to_bt,), name = "pc_read_thread")
	print "created rt_pc"
	wt_pc = threading.Thread(target = pc_thread.writePC, args = (to_pc,), name = "pc_write_thread")
	print "created wt_pc"

	# Bluetooth (BT) read and write thread
	rt_bt = threading.Thread(target = bt_thread.readBT, args = (to_pc,), name = "bt_read_thread")
	print "created rt_bt"
	wt_bt = threading.Thread(target = bt_thread.writeBT, args = (to_bt,), name = "bt_write_thread")
	print "created wt_bt"


	# Serial (SR) read and write thread
	# rt_sr = threading.Thread(target = sr_thread.readSR, args = (to_pc, to_bt,), name = "sr_read_thread")
	# print "created rt_sr"
	# wt_sr = threading.Thread(target = sr_thread.writeSR, args = (to_sr,), name = "sr_write_thread")
	# print "created wt_sr"


	# Start Threads
	rt_pc.start()
	wt_pc.start()

	rt_bt.start()
	wt_bt.start()

	# rt_sr.start()
	# wt_sr.start()
	print "start rt and wt"

	# print "Enter 'exit' to quit"
	# exit_msg = raw_input()
	# while True:
	# 	if (exit_msg == "exit"):
	# 		quit()
	# 		print "after quit"
	# 		sys.exit()
	# 	print "Enter 'exit' to quit"
	# 	exit_msg = raw_input()


	# Handle the joins
	rt_pc.join()
	wt_pc.join()

	rt_bt.join()
	wt_bt.join()

	# rt_sr.join())
	# wt_sr.join()

	print "end of joins"

	pc_thread.close_all_pc_sockets()
	bt_thread.close_all_bt_sockets()
	# sr_thread.close_all_sr_sockets()
	print "End thread"