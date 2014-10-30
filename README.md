# RASPBERRY PI #

###About###
The Raspberry Pi (RPi) board is a credit card-sized single-board computer. It is based on an ARM 11 processor based system on a chip (SoC) which also contains a GPU that actually performs the boot-up of the board. The Pi originally shipped with 256MB of RAM and uses a Secure Digital card for persistent storage. The RPi runs a version of the popular Debian Linux OS called Raspbian.

![alt text](https://github.com/rohitsm/ntu.sce.mdp.2/blob/master/Images/Rpi.jpg "Raspberry Pi")

In the setup of the mobile robotic system, the Raspberry Pi (RPi) serves as the key component that forms the command centre. It forms the main platform of the system interfacing with the rest of the components as shown in figure 2 below. It coordinates and passes information between the different system components and can also execute extensive functions if required.

![alt text](https://github.com/rohitsm/ntu.sce.mdp.2/blob/master/Images/Setup.png "Setup")


###Interface Setup###

The interfaces are setup as follows:

**Wi-Fi:** The RPi is setup as a wireless access point through which the PC running the algorithm is interfaced. During the developmental phases, it is accessed over Secure Shell (SSH). The RPi is setup as a DHCP server with a static private IP that is broadcast at boot time – 192.168.2.2

**Bluetooth:** The RPi interfaces with the Nexus 7 tablet using the RFCOMM protocol. The Media Access Control (MAC) address of the tablet is hard coded into the configuration file of the Bluetooth module so that device pairing is enabled as soon as the python program starting the interface has begun.

**Serial Communication:** The RPi is interfaced with the Arduino through the USB cable using the Abstract Control Model (ACM) serial interface (ttyACM), which is similar to the USB Virtual COM but normally used when connecting to a micro-controller.

In addition to the above interface setup, a program was written in Python that handled the  communication specific to the mobile robot. The program was multithreaded to be able to handle all the three communications simultaneously. This was essential primarily for the rapid movement of data between the three modules.


###Information and Data Flow:###

The mobile robot is initialized by starting the python program designed to handle the communications. Once all the three devices are connected through the various interfaces, the robot is ready for work. Sensor information and data are passed between each other in the form of messages. The Python program has a modular implementation with separate functions that cater to the communications with the different interfaces.

Handling data transfer between the various modules requires tagging the message with appropriate headers. These headers contain the source and destination information required for the Pi to correctly channel the message. The typical structure of a message is as follows:

`[destination] [source] : [Actual message content]`

The source and the destination headers are single characters that have been decided and agreed upon by the team. They are as follows:

![alt text][logo]

[logo]: https://github.com/rohitsm/ntu.sce.mdp.2/blob/master/Images/table1.png "Table 1"

###Message passing:###

Using the above information, we can construct a simple message that can be sent from the PC to the Android tablet as follows:

`AP:Hello`

This is an actual message that was used for testing. Note that the headers are case insensitive as the RPi caters for all cases.

When the message is first sent to the RPi, it strips out the first character in the header (Destination) and passes it to the appropriate function handling the communication with that device. The above message is dealt with by the following code snippet.

```python

	read_pc_msg = self.pc_thread.read_from_PC()

	# Check header for destination and strip out first char
	
	if(read_pc_msg[0].lower() == 'a'):		# send to android
		self.writeBT(read_pc_msg[1:])		# strip the header
		print "value written to BT from PC: %s" % read_pc_msg[1:]

	elif(read_pc_msg[0].lower() == 'h'):	# send to arduino
		self.writeSR(read_pc_msg[1:])		# strip the header
		print "value written to SR from PC: %s" % read_pc_msg[1:]

	else:
		print "incorrect header received from PC: [%s]" % read_pc_msg[0]
		time.sleep(1)

```


It is important to leave the Source header of the message intact for the receiver because of the way the data needs to be handled. For example, the PC might receive data from, both, the Arduino and the Android device (Nexus 7 tablet). However, the operations that deal with the message content in both cases are different. The receiver therefore has an additional operation that identifies and strips the source header of the message before operating upon the actual data contained in the message.

The colon ‘:’ is used to indicate the start of the message content. Therefore, the receiver parses the message and extracts the contents after the colon.

Communication between the other devices are also handled in a similar fashion. It is important to note that the RPi does not read any of the actual message contents by itself to avoid any form of data corruption. It simply strips out the first header.






