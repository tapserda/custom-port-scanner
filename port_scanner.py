#!/usr/bin/python
#port_scanner.py

from os import system, name
import socket

the_host = str(raw_input("Enter ip to be scanned : "))
the_ip = socket.gethostbyname(the_host)
print the_ip

def clear():
   if name == 'nt':
       _ = system('cls')
   else:
       _ = system('clear')

def pi():
   while 1:
       the_port = int(raw_input("Enter the port you want to scan :"))
       try:
		sock	=	socket.socket()
		res	=	sock.connect((the_ip, the_port))
		print "Port {}: Open" .format(the_port)
		sock.close()
       except:
		print "Port {}: Closed" .format(the_port)
       break
pi()

choice=False
while choice is not True:
   lilchoice = input("\n1 - Continue Scan \n2 - Exit\n")
   if lilchoice == 1:
	clear()
	pi()
   elif lilchoice == 2:
	choice=True
	exit()
   else:
	print("Wrong Number!")


