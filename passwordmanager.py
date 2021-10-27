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



