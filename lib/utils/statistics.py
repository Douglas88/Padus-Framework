import sys
import os

path = os.getcwd()
vul_scan = (path+'/lib/vul_scan')

files = os.listdir(vul_scan)
num_png = len(files)   
print("[INFO] Currently supports scanning for %d kinds of program vulnerabilities." %(num_png))    

