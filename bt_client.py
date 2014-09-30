from bluetooth import *

btaddr = "08:60:6E:A5:82:C8"
port = 4
uuid = "00001101-0000-1000-8000-00805F9B34FB"

sock = BluetoothSocket( RFCOMM )

#print "nearby devices..." 
#nearby_devices = discover_devices()
#for address in nearby_devices:
#	print address

service_match = find_service(uuid = uuid, address = btaddr)
print "Connecting..."
while len(service_match) == 0:
	service_match = find_service(uuid = uuid, address = btaddr)

first_match = service_match[0]
port = first_match["port"]
host = first_match["host"]

sock.connect((host, port))
print "Connected to ", str(host)
sock.send("hello!")
print "write to andorid"

sock.close()
print "end"
