from hashlib import sha256
import json

def add_to_file(url, password):
	sha_class = sha256()
	user_pass_encode = password.encode()
	sha_class.update(user_pass_encode)
	hashed_password = sha_class.hexdigest()
	print("password hashed")

	entry = {}
	entry['url'] = url
	entry['hashed password'] = hashed_password
	writeFile = open('password.json', 'a')
	json.dump(entry, writeFile)
	writeFile.close()

def read_from_file(url):
	readFile = open('password.json', 'r')
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
def updating_from_file(url):
	readFile = open('password.json','r')
	inputpass = input("Enter new password that you want to hash")
	index_password = 0
	passwordlist = readFile.readlines()
	readFile.close()
	
	shaobj = sha256()
	encode = inputpass.encode()
	hashed = shaobj.hexdigest()

	writefile = open('password.json', 'w')

	for x in passwordlist:
		dictpass = json.loads(x)
		if(dictpass['url'] == 'url'):
			dictpass['hashed password'] = hashed
		json.dump(dictpass, writeFile)
	
	writeFile.close()	


def main():
	userAction = input("do you want to read or write from pasword file: ")
	if(userAction == "WRITE"):
		url = input("what is the url of the website: ")
		user_normal_password = input('enter password that you want to hash: ')
		add_to_file(url, user_normal_password)
	elif(userAction == 'FIND'):
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
if __name__ == "__main__":
	main()
