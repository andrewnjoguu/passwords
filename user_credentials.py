import pyperclip
import random
import string


global users_list 
class User:
	'''
	allows usto create new users and save their information for future usage
	'''
	
	users_list = []
	def __init__(self,first_name,last_name,password):
		'''
		defining properties
		'''

		# In variables
		self.first_name = first_name
		self.last_name = last_name
		self.password = password

	def save_user(self):
		'''
		saves new user created
		'''
		User.users_list.append(self)
		
class Credential:
	'''
	account to save passwords info and new info
	'''
	# Class Variables
	credentials_list =[]
	user_credentials_list = []
	@classmethod
	def check_user(cls,first_name,password):
		'''
		checks if info entered matches that stored
		'''
		current_user = ''
		for user in User.users_list:
			if (user.first_name == first_name and user.password == password):
				current_user = user.first_name
		return current_user

	def __init__(self,user_name,site_name,account_name,password):
		'''
		defines users properties
		'''

	
		self.user_name = user_name
		self.site_name = site_name
		self.account_name = account_name
		self.password = password

	def save_credentials(self):
		'''
		Function to save a newly created user instance
		'''
	
		Credential.credentials_list.append(self)
	
	def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
		'''
	function that shows passwords
		'''
		gen_pass=''.join(random.choice(char) for _ in range(size))
		return gen_pass

	@classmethod
	def display_credentials(cls,user_name):
		'''
		displayed all listed info
		'''
		user_credentials_list = []
		for credential in cls.credentials_list:
			if credential.user_name == user_name:
				user_credentials_list.append(credential)
		return user_credentials_list
				

	
	@classmethod
	def find_by_site_name(cls, site_name):
		'''
		finds the system name
		'''
		for credential in cls.credentials_list:
			if credential.site_name == site_name:
				return credential

	@classmethod
	def copy_credential(cls,site_name):
		'''
		copies info entered
		'''
		find_credential = Credential.find_by_site_name(site_name)
		return pyperclip.copy(find_credential.password)

