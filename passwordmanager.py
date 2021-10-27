#! /usr/bin/env python3.8 2021
import pyperclip
from user_credentials import User, Credential

def create_user(fname,lname,password):
	'''
	allows us to create a new user
	'''
	new_user = User(fname,lname,password)
	return new_user

def save_user(user):
	'''
	allows us to save the user if they are new
	'''
	User.save_user(user)



def verify_user(first_name,password):
	'''
	this allows to to clarify users before they enter information
	'''
	checking_user = Credential.check_user(first_name,password)
	return checking_user

def generate_password():
	'''
	
	'''
	gen_pass = Credential.generate_password()
	return gen_pass

def create_credential(user_name,site_name,account_name,password):
	'''
	Function to create a new information
	'''
	new_credential=Credential(user_name,site_name,account_name,password)
	return new_credential

def save_credential(credential):
	'''
	Function to save a newly created credential
	'''
	Credential.save_credentials(credential)

def display_credentials(user_name):
	'''
	Allows us to view information of a certain user
	'''
	return Credential.display_credentials(user_name)
	
def copy_credential(site_name):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credential.copy_credential(site_name)

def main():
	print(' ')
	print('You are now using Andrew Koikais app for managing passwords.')
	while True:
		print(' ')
		print("-"*60)
		print('Select below whether you would like to create a new password or log in: \n ca-Create an Account \n li-Log In \n ex-Exit')
		short_code = input('Enter a choice: ').lower().strip()
		if short_code == 'ex':
			break

		elif short_code == 'ca':
			print("-"*60)
			print(' ')
			print('enter below to join us and have new account:')
			first_name = input('Enter your  name below eg. Andrew - ').strip()
			last_name = input('Enter your nickname for example Waba - ').strip()
			password = input('Enter a password to create a new account with us - ').strip()
			save_user(create_user(first_name,last_name,password))
			print(" ")
			print(f'you are: {first_name} {last_name} using password: {password} welcome to our app!')
		elif short_code == 'li':
			print("-"*60)
			print(' ')
			print('thank you for returning to us, login in kindly! We have missed you:')
			user_name = input('Enter your  name - ').strip()
			password = str(input('Enter your password - '))
			user_exists = verify_user(user_name,password)
			if user_exists == user_name:
				print(" ")
				print(f'Welcome {user_name}. Please choose an option to continue.')
				print(' ')
				while True:
					print("-"*60)
					print('Navigation codes: \n cc-fill in info you want to save \n dc-Display info you already have \n copy-Copy Password \n ex-Exit')
					short_code = input('Enter an option from the four available: ').lower().strip()
					print("-"*60)
					if short_code == 'ex':
						print(" ")
						print(f'Hope to see you again sir/madam {user_name}')
						break
					elif short_code == 'cc':
						print(' ')
						print('Enter your information:')
						site_name = input('Kindly enter you system name for eg. Facebook, Onlyfans- ').strip()
						account_name = input('Kindly enter the name of your account below - ').strip()
						while True:
							print(' ')
							print("-"*60)
							print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
							psw_choice = input('Enter an option: ').lower().strip()
							print("-"*60)
							if psw_choice == 'ep':
								print(" ")
								password = input('Enter your password: ').strip()
								break
							elif psw_choice == 'gp':
								password = generate_password()
								break
							elif psw_choice == 'ex':
								break
							else:
								print('Sadly, you have entered thewrong option. Kindly try again.')
						save_credential(create_credential(user_name,site_name,account_name,password))
						print(' ')
						print(f'Info saved: System Name: {site_name} - Account Name: {account_name} - Password: {password}')
						print(' ')
					elif short_code == 'dc':
						print(' ')
						if display_credentials(user_name):
							print('Here is a list of all your previous information')
							print(' ')
							for credential in display_credentials(user_name):
								print(f'system Name: {credential.site_name} - Account Name: {credential.account_name} - Password: {credential.password}')
							print(' ')	
						else:
							print(' ')
							print("You have not saved anything yet")
							print(' ')
					elif short_code == 'copy':
						print(' ')
						chosen_site = input('Enter the site name for the info password to copy: ')
						copy_credential(chosen_site)
						print('')
					else:
						print('Sadly, you have entered the wrong option. Try again.')

			else: 
				print(' ')
				print('Sadly, you have entered the wrong details. Why dont you try again or make a new account with us?.')		
		
		else:
			print("-"*60)
			print(' ')
			print('Sadly, You have entered the wrong option. Kindly attempt once more.')
				






if __name__ == '__main__':
	main()

