import json
import os
from random import*



#staff login function
def staff():
	print("Welcome back please enter your login details")
	username = input("username: ")
	password = input("password: ")
	staff_file = open('staff.txt','r')
	for list in staff_file:
		extract = list.split(",")
		user = extract[0]
		pswd = extract[1]
	if username == user and password == pswd:
		print("successful")
		staff_session = os.path('session.txt','w+')
		staff_session.write(username, password)
		staff_session.close()

#staff dashboard if login
def staffDashboard():
	print("\nLogin Successful")
	print("\nenter 'CNA' ->[Create New Account]")
	print("\nenter 'CAD' ->[Check Account Detail]")
	print("\nenter 'L' ->[Logout]")


#def createAccount():
	
	
	

prompt1 = input("enter 'yes' to login 'no' to exit\n>> ").lower()
if prompt1 == 'yes':
  staff()
  staffDashboard()


#prompt2 = input("\n>> ").lower()
#if prompt2 == 'cna':
	
		
else:
	print("\nHave a nice day!")
	exit()