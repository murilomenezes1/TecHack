from socket import *


# reference: https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_network_scanner.htm



if __name__ == "__main__":
	
	target = input("Input host address: ")
	PortRange  = input("Input Port Number Range (ex: #:#): ")
	
	PortInput = PortRange.split(':')
	
	for i in range(int(PortInput[0]), int(PortInput[1])):
	
		s = socket(AF_INET, SOCK_STREAM)
		
		conn = s.connect_ex((target, i))
		
		if (conn == 0):
			
			service = getservbyport(i, "udp")
		
			print('Port {} is OPEN and is running {}'.format(i, service))
			
		s.close()
		
	print("End of scan")
	
	

	