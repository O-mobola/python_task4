

import json


#staff login function
def staff():
	print("Welcome back please enter your login details")
	username = input("username: ")
	password = input("password: ")


def staffDashboard():
	print("\nLogin Successful")
	print("\nenter 'CNA'[Create New Account]")
	print("\nenter 'CAD'[Check Account Detail]")
	print("\nenter 'L'[Logout]")
	prompt2 = input()
	

prompt1 = input("enter 'yes' to login 'no' to exit\n>> ").lower()

if prompt == 'yes':
  staff()
	staff_file = open("staff.txt", "r")
	staff_file.read()
if username and password is in staff_file:
	staffDashboard()
		
else:
	print("\nHave a nice day!")
	exit()