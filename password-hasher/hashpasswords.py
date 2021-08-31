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

	entry = {}
	entry['url'] = url
	entry['hashed password'] = hashed_password
	writeFile = open('password.json', 'a')
	json.dump(entry, writeFile)
	writeFile.close()
else:
	readFile = open('password.json', 'r')
	website = input('what is the url of the website that you need password for: ')
	list_pass = readFile.readlines()
	list_dict = []
	for x in list_pass:
		dict_pass = json.loads(x)
		list_dict.append(dict_pass)
	
	# finding password
	found = False
	for x in list_dict:
		if(website == x['url']):
			print( x['hashed password'])
			found = True
	if(not found):
		print('url not found')
