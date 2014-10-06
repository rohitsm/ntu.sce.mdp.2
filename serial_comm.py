import serial
import time

__author__ = "Rohit"

class SerialAPI(object):

	def __init__(self):
		self.port = '/dev/ttyACM0'
		self.baud_rate = 9600
		self.ser = None

	def connect_serial(self):
		"""
		Initialize serial socket
		"""
		self.ser = serial.Serial(self.port, self.baud_rate)


	def close_sr_socket(self):
		if (self.ser):
			self.ser.close()
			print "Closing serial socket"


	def write_to_serial(self, msg):
		"""
		Write to arduino
		"""
		self.ser.write(msg)
		print "Write to arduino: %s " % msg
		# time.sleep(0.5)

	def read_from_serial(self):
		"""
		Read from arduino

		Waits until data is received from arduino
		"""
		received_data = self.ser.readline()
		print "Received from arduino: %s " % received_data
		return received_data


if __name__ == "__main__":
	print "Running Main"
	sr = SerialAPI()
	sr.connect_serial()

	send_msg = raw_input()
	print "Writing [%s] to arduino" % send_msg
	sr.write_to_serial(send_msg)

	print "read"
	print "data received from serial" % sr.read_from_serial

	print "closing sockets"
	sr.close_sr_socket()


