import socket

target = input ('\nEnter the IP address ti scan: ')
portrange = input('\nEnter the port range to scan (es 5-200): ')

lowport = int (portrange.split('-')[0])
highport = int (portrange.split('-')[1])

print ('\nScanning host ', target, ' from port ', lowport, ' to port', highport)

for port in range(lowport,highport):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	status = s.connect_ex((target,port))
	if (status == 0):
		print ('\n*** Port ', port, '- OPEN ***')

