
import os
from random import randint
import json


staff_session = []
prompt = ""
#staff login function
def staff():
	print("Welcome back please enter your login details")
	username = str(input("username: "))
	password = str(input("password: "))
	staff_file = open("staff.txt","r")
	staff_file.readline()
	#staff_file.close()
	for words in staff_file:
		extract= words.split(",")
		user = str(extract[0])
		pswd = str(extract[1])
	if username == user and password == pswd:
			print("Login Successful")
	else:
			print("\nIncorrect login details")
			exit()
		
#create session file for successful login
	session = {
		"username": username,
	"password": password
		}
	with open("session.txt","w") as file:
		json.dump(session, file)


#function staff dashboard if login
def staffDashboard():
	print("\nWelcome Back")
	print("\nenter 'CNA' ->[Create New Account]")
	print("\nenter 'CAD' ->[Check Account Detail]")
	print("\nenter 'L' ->[Logout]")
	

#function create account (cna)
def createAccount():
	acct_name = input("\nAccount Name \n> ").upper()
	open_bal = int(input("\nOpening Balance \n> "))
	acct_type = input("\nAccount Type\n> ").upper()
	acct_email = input("\nAccount Email\n> ").lower()
	for i in range(10):
		acct_num = randint(0,9)
		print(acct_num, end="")
	each_user_data = {
						"Account_Name": acct_name,
						"Opening_Balance": open_bal,
						"Account_Type": acct_type,
						"Account_Email": acct_email,
						#"Account_Number": acct_num
					}
	with open("customer.txt","w") as user:
			json.dump(each_user_data, user)
	
		
#function check account detail	(cad)
def checkAccount():
	acct_num = int(input("\nEnter Account Number\n>> "))
	with open("customer.txt","r") as fetch:
		user_data = json.load(fetch)
		print(user_data)
	
#prompt for login
prompt1 = input("enter 'yes' to login 'no' to exit\n>> ").lower()
if prompt1 == 'yes':
  staff()
  staffDashboard()
else:
	exit()
  	
prompt2 = input("\n>> ").lower()
if prompt2 == 'cna':
	createAccount()
	staffDashboarf()
	
	#call cad function if prompt is cad	
elif prompt2 == 'cad':
	checkAccount()
	staffDashboard()
	
	#call l to logout
elif prompt2 == 'l':
		print("\nsee ye around!")
		os.remove("session.txt")
		staff()
else:	
	print("\nHave a nice day!")
	os.remove('session.txt')
	exit()