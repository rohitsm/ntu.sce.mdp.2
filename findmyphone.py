from bluetooth import *

target_name = "Nexus 7 Group 2"
target_address = None

nearby_devices = discover_devices()

for address in nearby_devices:
	if target_name == lookup_name(address):
		target_address = address
		break

if target_address is not None:
	print "found target BT device with address" , target_address
else:
	print "couldn't find anything"
