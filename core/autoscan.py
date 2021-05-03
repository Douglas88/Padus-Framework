#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import socket
import re
from re import fullmatch
import time
import os
import  fileinput


path = os.getcwd()
logs_dir = (path+'/logs')
utils = (path+'/lib/utils')
config = (path+"/config.ini")
url_dir = (logs_dir+"/url.log")
port_dir = (logs_dir+"/port.log")


with open(url_dir, 'r') as f:
    url = f.read()
    print("[INFO] Target: ",url)


with open(port_dir, 'r') as f:
    port = f.read()
    print("[INFO] Port: ",port)


print("[INFO] Checking enabled modules, please wait...")


for  tmp_config  in  fileinput. input ( config ):
	#print (tmp_config)
	if "wafmodule = true" in tmp_config:
		print("[INFO] WAF Scan: \033[1;36m True\033[0m")
		wafmodule_status = "True"
	elif "ipinfo = true" in tmp_config:
		print("[INFO] IP Info: \033[1;36m True\033[0m")
		ipinfo_status = "True"
	elif "shodanmodule = true" in tmp_config:
		print("[INFO] Shodan: \033[1;36m True\033[0m")
		shodanmodule_status = "True"
	elif "fofamodule = true" in tmp_config:
		print("[INFO] Fofa: \033[1;36m True\033[0m")
		fofamodule_status = "True"
	elif "cmsmodule = true" in tmp_config:
		print("[INFO] CMS Scan: \033[1;36m True\033[0m")
		cmsmodule_status = "True"
	elif "dirmodule = true" in tmp_config:
		print("[INFO] Directory Scan: \033[1;36m True\033[0m")
		dirmodule_status = "True"
	elif "portmodule = true" in tmp_config:
		print("[INFO] Port Scan: \033[1;36m True\033[0m")
		portmodule_status = "True"
	elif "middleware = true" in tmp_config:
		print("[INFO] Middleware Scan: \033[1;36m True\033[0m")
		middleware_status = "True"
	elif "vulmodule = true" in tmp_config:
		print("[INFO] Vulnerability Scan: \033[1;36m True\033[0m")
		vulmodule_status = "True"
time.sleep(3)
os.system("clear")
#RUNNING


if wafmodule_status == "True":
	print("[+] WAF Scan")
	os.popen("wafw00f %s -o %s/waf.log" %(url,logs_dir)).read()
	with open(logs_dir+"/waf.log", 'r') as f:
    		waf = f.read()
    		print("[+] WAF: ",waf)

else:
	pass


###Get IP Address
try:
	ip = socket.gethostbyname(url)
except:
	print("[ERROR] Failed to obtain the target IP address.")
	exit()


if ipinfo_status == "True":
	print("[+] IP Info")
	country = os.popen("curl -s http://ip-api.com/line/%s?fields=country"%(ip)).read()
	city = os.popen("curl -s http://ip-api.com/line/%s?fields=city"%(ip)).read()
	isp = os.popen("curl -s http://ip-api.com/line/%s?fields=isp"%(ip)).read()
	print("\033[1;34m[+] Country: %s\033[0m" %(country))
	print("\033[1;34m[+] City: %s\033[0m" %(city))
	print("\033[1;34m[+] ISP: %s\033[0m" %(isp))
else:
	pass

if shodanmodule_status == "True":
	print("[+] Shodan")
	os.popen("shodan search --fields ip_str,port,org,hostnames %s > %s/shodan.log" %(url,logs_dir)).read()
	with open(logs_dir+"/shodan.log", 'r') as f:
    		shodan_info = f.read()
    		print("[+] Shodan Search Result: \n",shodan_info)


if fofamodule_status == "True":
	print("[+] Fofa")


if cmsmodule_status == "True":
	print("[+] CMS Scan")
	os.system("python3 %s/cmsscan.py" %(utils))
else:
	pass

if dirmodule_status == "True":
	print("[+] Directory Scan")
	os.system("python3 %s/dirscan.py %s -n 30" %(utils,url))

if portmodule_status == "True":
	print("[+] Port Scan")
	os.system("python3 %s/portscan.py %s " %(utils,ip))
	

if middleware_status == "True":
	print("[+] Middleware Scan")

if vulmodule_status == "True":
	print("[+] Vulnerability Scan")






'''
web = input("[*] Is the web page running on the target server? [Y/N] ")
if web == "Y" and "y":
	os.system("python3 %s/cmsscan.py" %(utils))
else:
	print("[-] Ignore CMS scan.")
'''

