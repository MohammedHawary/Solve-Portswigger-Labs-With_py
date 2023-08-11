import requests

							############ GET ############	
'''								
params = {"name":"Mohammed","age":22} # Create parameters with key and value

r = requests.get('http://httpbin.org/get',params=params) # send GET request to website with parameters 

print(r.text) # to print the response 

							############ POST ############

params = {"name":"Mohammed","age":22} # Create parameters with key and value

r = requests.post("http://httpbin.org/post" , data=params) # send POST request to website with parameters 

print(r.url)

						 ############ Upload files ############

url = 'http://httpbin.org/post'        # url variable

file = {"file":open("file1.txt", "rb")} # to upload one file

files = [           # to upload multible files

#   ("identfir", ("filename", open("file_path","rb"), "extintion"))
	("f1", ("file1.txt", open("file1.txt", "rb"), "txt")),	
	("f2", ("file2.txt", open("file2.txt", "rb"), "txt")),	
	("f3", ("file3.txt", open("file3.txt", "rb"), "txt"))
]

r = requests.post(url, files=files)

print(r.status_code)
print(r.text)

							 ############ get JSON Data ############

r = requests.get("https://api.github.com/events")

events = r.json()

print(events)
print(events[0])    
print(events[0]['id'])    

							 ############ send JSON Data ############

json_data = {		# json data format
	"firstName":"Mohammed",
	"lastName":"Hawary",
	"Age":22
}

r = requests.post("http://httpbin.org/post" , json=json_data)

print(r.text)

							 ############ HTTP Headers ############

headers = {"content-type":"text/php"}

r = requests.post("http://httpbin.org/post" , headers=headers)

print(r.request.headers)      # print request headers only
print(r.request.headers['User-Agent']) # print key value of User-Agent

							 ############ HTTP Cookies ############

url = "http://httpbin.org/cookies"
cookies = {"Location":"EGYPT"}

r = requests.get(url, cookies=cookies)
r2 = requests.get("https://google.com")

print(r.text)
print(r2.cookies)

						  # to custmize where we send our cookie 

url = "http://httpbin.org/cookies"

requestJar = requests.cookies.RequestsCookieJar()
requestJar.set("firstName","Mohammed", domain="http://httpbin.org", path="/cookies")
requestJar.set("lastName","Hawary",    domain="http://httpbin.org", path="/cookies")

r3 = requests.get(url, cookies=requestJar)
print(r3.text)
						############ error handling and time out############

url = "http://httpbin.org/status/200"
r = requests.get(url, timeout=1) 

print(r.raise_for_status()) 

							  ############ Redirection ############

# r = requests.get("http://github.com", allow_redirects=False)   # disable redirection to https
r = requests.get("http://github.com")
print(r.history)                                               # print all status code in order to complete our request
print(r.status_code)										   # print last status code in our request
print(r.url)                                                   # print request url
'''
							  ############ Proxes ############

proxies = {"http":"75.89.101.62:80"}          # proxy server address
r = requests.get("http://httpbin/ip", proxies=proxies) # add proxy to our request
print(r.text)
