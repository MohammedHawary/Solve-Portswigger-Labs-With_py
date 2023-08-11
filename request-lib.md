### GET request

```python
import requests
# Create parameters with key and value
params = {"name":"Mohammed","age":22} 

# send GET request to website with parameters 
r = requests.get('http://httpbin.org/get',params=params) 

# to print the response 
print(r.text) 
```

### POST request

```python
import requests
# Create parameters with key and value
params = {"name":"Mohammed","age":22} 

# send POST request to website with parameters 
r = requests.post("http://httpbin.org/post" , data=params) 

# print request url
print(r.url)
```

### Upload files

**upload one file**

```py
import requests
# save url in variable
url = 'http://httpbin.org/post'        

# open file that you will upload it
file = {"file":open("file1.txt", "rb")} 

# upload file
r = requests.post(url, files=files)

# print status code request of upload file  
print(r.status_code)

# to print the response 
print(r.text)
```

**to upload multible files**

```py
import requests
# save url in variable
url = 'http://httpbin.org/post'        

# open files that you will upload
files = [           
# ("identfir", ("filename", open("file_path","rb"), "extintion"))
    ("f1", ("file1.txt", open("file1.txt", "rb"), "txt")),    
    ("f2", ("file2.txt", open("file2.txt", "rb"), "txt")),    
    ("f3", ("file3.txt", open("file3.txt", "rb"), "txt"))
]

# upload file
r = requests.post(url, files=files)

# print status code request of upload file  
print(r.status_code)

# to print the response 
print(r.text)
```

### GET JSON Data

```py
import requests

# send GET request to website
r = requests.get("https://api.github.com/events")

# GET json data
events = r.json()

# print all json data
print(events)

# print the first element of the list events
print(events[0])

# print the value of the key id in the first element of the list events
print(events[0]['id'])
```

### POST JSON Data

```py
import requests

# json data format
json_data = {        
    "firstName":"Mohammed",
    "lastName":"Hawary",
    "Age":22
}

# send json data with POST request
r = requests.post("http://httpbin.org/post" , json=json_data)

# to print the response 
print(r.text)
```

### HTTP Headers

```py
import request
# header variable syntax
headers = {"content-type":"text/php"}

# send POST request with header
r = requests.post("http://httpbin.org/post" , headers=headers)

# print request headers only
print(r.request.headers)

# print key value of content-type from request
print(r.request.headers['content-type'])
```

### HTTP Cookies

```py
import requests
# save url in variable
url = "http://httpbin.org/cookies"

# create Cookie
cookies = {"Location":"EGYPT"}

# get request with cookie 
r = requests.get(url, cookies=cookies)

# send get request to google
r2 = requests.get("https://google.com")

# to print the response 
print(r.text)

# to print googles' cookie
print(r2.cookies)
```

**To custmize where we send our cookie**

```py
import requests
# save url in variable
url = "http://httpbin.org/cookies"

# Create requestJar variable
requestJar = requests.cookies.RequestsCookieJar()

# set cookie value and path in requestJar variable
requestJar.set("firstName","Mohammed", domain="http://httpbin.org", path="/cookies")

# send cookie
r = requests.get(url, cookies=requestJar)

# to print the response 
print(r.text)
```

### Redirection

```py
import requests
# disable redirection to https
r = requests.get("http://github.com", allow_redirects=False)   

# by default redirection allowed 
r = requests.get("http://github.com")

# print all status code in order to complete our request
print(r.history)                                               

# print last status code in our request
print(r.status_code)                   

# print request url
print(r.url)                                                   
```

### Proxes

```py
import requests
# proxy server address
proxies = {"http":"75.89.101.62:80"}

# add proxy to our request
r = requests.get("http://httpbin/ip", proxies=proxies)

# to print the response 
print(r.text)
```

### Error handling and time out

```py
import requests
# save url in variable
url = "http://httpbin.org/status/200"

# send get request with timeout 1s
r = requests.get(url, timeout=1)

# if there are error raise it 
print(r.raise_for_status())  
```
