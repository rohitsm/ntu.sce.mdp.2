import Queue
import threading
from pc_thread import *
from bt_thread import *


__author__ = 'Rohit'

# Create queues
to_bt = Queue.Queue() 
to_pc = Queue.Queue()
# to_sr = Queue.Queue()		// Serial queue

if __name__ == "__main__":
	pc_thread = PCThread()
	bt_thread = BTThread()

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

	# Start Threads
	rt_pc.start()
	wt_pc.start()

	rt_bt.start()
	wt_bt.start()
	print "start rt and wt"

	# Handle the joins
	rt_pc.join()
	wt_pc.join()

	rt_bt.join()
	wt_bt.join()

	print "end of joins"

	pc_thread.close_all_pc_sockets()
	bt_thread.close_all_bt_sockets()
	print "End thread"