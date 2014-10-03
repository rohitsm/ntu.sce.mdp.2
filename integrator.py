import Queue
import threading
from pc_thread import *
from bt_thread import *


__author__ = 'Rohit'

# Create queues
to_bt = Queue.Queue() 
to_pc = Queue.Queue()


def send_to_pc():
	


	




def send_to_bt():





if __name__ == "__main__":
	pc_thread = PCThread()

	# PC read and write thread
	rt_pc = threading.Thread(target = pc_thread.readPC, name = "pc_read_thread")
	print "created rt_pc"
	wt_pc = threading.Thread(target = pc_thread.writePC, name = "pc_write_thread")
	print "created wt_pc"

	# Bluetooth (BT) read and write thread
	rt_bt = threading.Thread(target = pc_thread.readBT, name = "bt_read_thread")
	print "created bt_pc"
	wt_bt = threading.Thread(target = pc_thread.writeBT, name = "bt_write_thread")
	print "created bt_pc"

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

	pc_thread.close_all_bt_sockets()
	print "End thread"