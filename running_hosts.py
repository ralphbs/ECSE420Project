import socket;
import re;
count = 0

def is_ssh_reachable(hostname):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(1)
	result = 1
	try:
		result = sock.connect_ex((hostname,22))
	except:
		print "Exception when connecting to host " + hostname
	finally:
		sock.close()
		return result	
		
with open("HostList.txt") as f:
    hostname_list = f.readlines()
count = 0
output = open('./AvailableHosts.txt', 'w')
for hostname in hostname_list:
	hostname = hostname.strip('\n')
	if (is_ssh_reachable(hostname) == 0):
		count += 1
		output.write(hostname+'\n')
print "Reachable hosts count: " + str(count)
output.close()
   

	