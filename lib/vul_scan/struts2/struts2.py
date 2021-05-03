# -*- coding: utf-8 -*-
import os
import json

#PATH
path = os.getcwd()
logs_dir = (path+'/logs')
struts2_poc = (path+'/vul/poc/struts2')
struts2_vul_scan = (path+'/lib/vul_scan/struts2')

os.environ["struts2poc"]=struts2_poc

os.system("cp %s/standard %s/final_execute"%(struts2_vul_scan,struts2_vul_scan))

target = open(logs_dir + '/url.log','r')
target = target.read()
print("[+] Target:",target)

port = open(logs_dir + '/port.log','r')
port = port.read()
print("[+] Port:",port)



os.system("sed -i 's/<url>/%s/g' %s/final_execute"%(target,struts2_vul_scan))
os.system("sed -i 's/<port>/%s/g' %s/final_execute"%(port,struts2_vul_scan))



os.system("sh %s/final_execute"%(struts2_vul_scan))
os.system("rm -rf %s/final_execute"%(struts2_vul_scan))
