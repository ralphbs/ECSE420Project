import paramiko

def is_ssh_reachable(hostname):
	result = 1
	client = paramiko.SSHClient()
	client.load_system_host_keys()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #avoid unknown hostkey error
	paramiko.util.log_to_file("filename.log")
	try:
		client.connect(hostname, timeout = 1)
	except paramiko.ssh_exception.AuthenticationException as e:
		result = 0
	except:
		print "Exception when connecting to host " + hostname
	finally:
		client.close()
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