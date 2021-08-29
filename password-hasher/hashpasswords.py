from hashlib import sha256
import json

#creating instance of sha256 class

sha_class = sha256()

userAction = input("do you want to read or write from pasword file: ")

if(userAction == "WRITE"):
	url = input("what is the url of the website: ")
	user_normal_password = input('enter password that you want to hash: ')
	user_pass_encode = user_normal_password.encode()
	sha_class.update(user_pass_encode)
	hashed_password = sha_class.hexdigest()
	print("password hashed")

	passfile_read = open('password.json', 'r')
	passwords = passfile_read.readlines()
	passfile_read.close()
	entry = {}
	entry['url'] = url
	entry['hashed password'] = hashed_password
	passwords.append(entry)
	writeFile = open('password.json', 'w')
	json.dump(passwords, writeFile)
	writeFile.close()	
