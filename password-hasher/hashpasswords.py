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

	passfile = open('password.json', 'a')
	entry = {}
	entry['url'] = url
	entry['hashed password'] = hashed_password
	json.dump(entry, passfile)
	passfile.close()	
