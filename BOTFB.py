#!/usr/bin/python2

# -*- coding: utf-8 -*-
#BOT FB
#coded by Mr.w0n63d4n


try:
    import mechanize,requests,os,sys,subprocess,cookielib,time,random,urllib
except ImportError:
    subprocess.call("pip2 install requests mechanize", shell=True)
subprocess.call("clear",shell=True)


#color
green = "\033[1;32m"
normal = "\033[0m"
red = "\033[1;31m"
cyan = "\033[1;36m"

#symbols
good = "\033[1;32m[\033[1;36m+\033[1;32m]\033[0m"
bad = "\033[1;32m[\033[1;31m!\033[1;32m]\033[0m"

#kondisi
success = "\033[1;32mSuccessful\033[0m"
failed = "\033[1;31mFailed\033[0m"
def login():
		os.system ("toilet -f slant --gay login")
		print
		password = "wongedan"
		mlebu = raw_input("enter the password: ")
		if mlebu == password:
			titit()
		else:
				print "{} error, please enter the password correctly!".format(bad)
				sys.exit()
		
def titit():
		os.system ("clear")
		os.system ("toilet -f banner --gay bot fb")
		print menu
#banner
menu = """

	coded   : {}Mr.w0n63d4n{}
	Github  : {}https://github.com/wongedan123{}
	Youtube : \033[92mwongedan official\033[0m
	wongedan kui bebas :v

----------|\033[92mMenu Bot\033[0m|----------

	[1] Login Fb
	[2] Auto Like Fb On 100+
	[3] Auto Commentar Fb On
	[4] Auto Friend Requests On Your Account

""".format(green,red,cyan,normal)

banner = """
	{}have fun using wisely:D hopefully you can enjoy:P{}
""".format(green,cyan,red,)

#wongedan
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_cookiejar(cookielib.LWPCookieJar())
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
info = time.strftime("%S:%M:%H")

def token():
		os.system("clear")
		print banner
		print
		username = raw_input("[+] username : ")
		password = raw_input("[+] password : ")
		print "[{}]{} being processed please wait....".format(info,good)
		time.sleep(5)
		if len(username) == 0:
			print "[{}]{} You Must Input Your {}Username{} !!!".format(info,good)
		elif len(password) == 0:
			print "[{}]{} You Must Input Your {}Password{} !!!".format(info,good)
		else:
				token_parsing = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + username + "&locale=en_US&password=" + password + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6").read()
				file_token_access = open("token.txt","w")
				file_token_access.write(str(token_parsing))
				file_token_access.close()
		try:
			print "[{}]{} STATUS : {}".format(info,good,success)
			print "[{}]{} SAVED FILE WITH NAME : token.txt".format(info,good)
			print "[{}]{} retype python2 BOTFB.py enter the selection again :)".format(info,good)
		except:
			print "[{}]{} Error Operation System".format(info,bad)
def autolike():
    	print banner
    	print
    	token = open("token.txt","r").read()
    	a = br.open("https://yolikers.com/")
    	br.select_form(nr=0)
    	br.form["access_token"] = token
    	br.submit()
    	try:
        		react = raw_input("[+] type reaction ['LIKE','LOVE','HAHA','WOW','SAD','ANGRY'] : ")
        		d = br.open("https://yolikers.com/like.php?type=status")
        		br.select_form(nr=0)
        		br.form["type"] = [""+react]
        		br.submit()
        		print "[{}][+] Success Sending Like..".format(info,good)
    	except:
        		print "[{}]{} This tool can only be used twice on the same status using the second time by re-logging".format(failed,bad)

def comment():
    	print banner
    	print
    	print "[{}]{} Sending Commenter On Your Newest Post Please Wait...".format(info,good)
    	token = open("token.txt","r").read()
    	a = br.open("https://yolikers.com/commenter.php?type=status")
    	br.select_form(nr=0)
    	br.form["access_token"] = token
    	br.submit()
    	try:
        		b = br.open("https://yolikers.com/commenter.php?type=status")
        		br.select_form(nr=0)
        		br.submit()
        		print "[{}]{} Sending Commenter Success..".format(info,good)
    	except:
        		print "[{}]{} This tool can only be used twice on the same status using the second time by re-logging".format(info,bad)

def friend():
    	print banner
    	print
    	print "[{}]{} Sending 30 Friend Request On Your Facebook Account...".format(info,good)
    	token = open("token.txt","r").read()
    	a = br.open("https://yolikers.com/")
    	br.select_form(nr=0)
    	br.form["access_token"] = token
    	try:
        		b = br.open("https://yolikers.com/autorequest.php?type=profile")
        		br.select_form(nr=0)
        		br.submit()
        		print "[{}]{} Sending 30 Friend Request Success...".format(info,good)
    	except:
        		print "[{}]{} This tool can only be used twice on the same status using the second time by re-logging".format(info,good)

print login()
pilih_menu = raw_input("[+] Enter Your Choice : ")
if len(pilih_menu) == 0:
		print "{} you haven't chosen!!!".format(bad)
elif pilih_menu == "1":
		token()
		time.sleep(5)
elif pilih_menu == "2":
		autolike()
		time.sleep(5)
elif pilih_menu == "3":
		comment()
		time.sleep(5)
elif pilih_menu == "4":
		friend()
		time.sleep(5)
