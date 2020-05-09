
import os
from random import randint
import json


staff_session = []

#staff login function
def staff():
	print("Welcome back please enter your login details")
	username = input("username: ")
	password = input("password: ")
	staff_file = open('staff.txt','r')
	staff_file.read()
	for list in staff_file:
		extract = list.split(",")
		user = extract[0]
		pswd = extract[1]
		if username == user and password == pswd:
			print("successful")
		
#create session file for successful login
	session = {
		"username": username,
	"password": password
		}
	with open("data.txt","w") as file:
		json.dump(session, file)


#staff dashboard if login
def staffDashboard():
	print("\nLogin Successful")
	print("\nenter 'CNA' ->[Create New Account]")
	print("\nenter 'CAD' ->[Check Account Detail]")
	print("\nenter 'L' ->[Logout]")
	

def createAccount():
	acct_name = input("\nAccount Name \n> ")
	open_bal = int(input("\nOpening Balance \n> "))
	acct_type = input("\nAccount Type\n> ")
	acct_email = input("\nAccount Email\n> ")
	for i in range(10):
		acct_num = randint(0,9)
		print(acct_num, end="")
	each_user_data = {
			"Account_Name": acct_name,
			"Opening_Balance": open_bal,
			"Account_Type": acct_type,
			"Account_Email": acct_email,
			"Account_Number": acct_num
		}
	with open("customer.txt","a") as user:
		json.dump(each_user_data, user)
	
	
prompt1 = input("enter 'yes' to login 'no' to exit\n>> ").lower()
if prompt1 == 'yes':
  staff()
  staffDashboard()
  
	
prompt2 = input("\n>> ").lower()
if prompt2 == 'cna':
	createAccount()
	
		
else:	
	print("\nHave a nice day!")
	exit()