import subprocess
import optparse
import re
import sys
import time

parser = optparse.OptionParser()
parser.add_option("-i","--interface",dest="interface",help="Interface to change its MAC Address")
parser.add_option("-m","--mac",dest="new_mac",help="New MAC Address")
(opt,args)=parser.parse_args()
if not opt.interface:
    parser.error(" [-] Please specify the interface name , for more info use -h or --help")
elif not opt.new_mac:
    parser.error(" [-] Please specify the new MAC Address ,for more info use -h or --help")

interface = opt.interface
new_mac = opt.new_mac

subprocess.call("clear",shell=True)
result = subprocess.check_output(["ifconfig",interface])
search_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",result)
if search_mac:
    current_mac = search_mac.group(0)
    print( " [+] Current MAC Address : " + current_mac)
    print("")
else:
    print(" [-] Could not read curent MAC Address. Please Check your interface and try again")
    print("")
    sys.exit()
    
print(" [+] Changing MAC address to " + new_mac + " ......")
time.sleep(3)

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
subprocess.call(["ifconfig",interface,"up"])

if current_mac == new_mac:
    print(" [-] MAC Address cannot be changed. Try using another MAC Address.")
else:
    print(" [+] MAC Address for interface " + interface + " has changed to " + new_mac + " successfully.")