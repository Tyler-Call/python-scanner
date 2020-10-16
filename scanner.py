#!usr/bin/python

#port_scanner.py

import socket
import time
import ipaddress

def header():
    print(
    '''
        Scan Result
    <------------------->
    ''')

def scan_port(host, port):
    ipaddr = socket.gethostbyname(host)     # Resolve t_host to IPv4 address
    print ipaddr      # Print the IP address

    # this try statement attempts to create a connection through the port
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)			
        sock.settimeout(10)
	res = sock.connect((ipaddr, port))
	print "Port {}: Open" .format(port)
	sock.close()
    except:
	print "Port {}: Closed" .format(port)
	
    print "Port Scanning complete"

def scan_udp_port(host, port):
    ipaddr = socket.gethostbyname(host)     # Resolve t_host to IPv4 address
    print ipaddr      # Print the IP address

    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)			
        sock.settimeout(10)
	res = sock.connect((ipaddr, port))
	print "UDP Port {}: Open" .format(port)
	sock.close()
    except:
	print " UDP Port {}: Closed" .format(port)
	
    print "Port Scanning complete"


# Port Scanner
choice = ""
while choice != exit:
    choice = input(
    '''
    Choose which option you would like or type exit:
    ------------------------------------------------
    1: Scan a host
    2: Scan multiple hosts (listed)
    3: Scan hosts from a text file
    4: Scan a subnet
    5: Scan a UDP port (TCP is the default)
    6: Scan multiple ports on a host
    '''
    )

    # Scan a single host
    if choice==1:    
        # read in host and port from user
        host = str(raw_input("Enter the host you want to  scan: "))   # Target Host, www.example.com
        port = int(raw_input("Enter the port: "))	   # Enter the port to be scanned
        
        #print results
        header()
        scan_port(host, port)
        
    # Scan multiple hosts from a list
    elif choice==2:
        # creating an empty list 
        lst = []

        # number of elements as input 
        n = int(input("Enter number of hosts: ")) 

        # iterating till the range 
        for i in range(0, n): 
            ele = raw_input("host:")
            print(ele)
            lst.append(ele) # adding the element 
        
        # get port from user
        port = int(raw_input("Enter the port: "))	   # Enter the port to be scanned

        # print results
        header() 
        for j in lst:
            scan_port(j, port)

    #Scan hosts from a text file
    elif choice==3:
        # get filepath and read file
        file_input = str(raw_input("Input Filepath: "))
        f = open(file_input, 'r+')
        lines = [line for line in f.readlines()]
        f.close()
        
        # get port from user
        port = int(raw_input("Enter the port: "))	   # Enter the port to be scanned

        # print results
        header()
        for j in lines:
            final_j = j.rstrip("\n")
            scan_port(final_j, port)

    # Scan a a subnet
    elif choice==4:
        subnet = unicode(raw_input("Enter subnet: "))
        print subnet
        net4 = ipaddress.ip_network(subnet)
        port = int(raw_input("Enter the port: "))
        header()
        for host in net4.hosts():
                scan_port(str(host), port)
    
    # Scan a UDP port
    elif choice==5:
        # read in host and port from user
        host = str(raw_input("Enter the host you want to  scan: "))   # Target Host, www.example.com
        port = int(raw_input("Enter the UDP port: "))          # Enter the port to be scanned

        #print results
        header()
        scan_udp_port(host, port)

    #Scan multiple ports on a host
    elif choice==6:
        # creating an empty list 
        lst = []

        host = str(raw_input("Enter the host: "))	   # Enter the host to be scanned

        # number of elements as input 
        n = int(input("Enter number of ports: ")) 

        # iterating till the range 
        for i in range(0, n): 
            ele = int(raw_input("port:"))
            print(ele)
            lst.append(ele) # adding the element 
        
        # print results
        header() 
        for j in lst:
            scan_port(host, j)

    #Error catching and allowing for exit
    elif choice > 6 and choice!=exit:
        print ("Invalid Choice selection!")
