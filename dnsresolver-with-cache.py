import socket
import pandas as pd
import time

h=0
data= pd.read_csv ("Book10ks.csv")   
source=data["destinationaddress".strip()]
foundIPs = {}
def get_domain_name(ip_address):
    try:
        global h
        if ip_address in foundIPs:
            hostname = foundIPs[ip_address]
            return hostname
        else:
            hostname = socket.gethostbyaddr(ip_address)[0]
            foundIPs[ip_address] = hostname
            h=h+1
            return hostname
    except socket.herror:
        hostname = "No domain name found"
        foundIPs[ip_address] = hostname
        return hostname

domain_name_list=[]
h=0
for ipaddress in source:
    
        
    
    domain_name= get_domain_name(ipaddress)
    time.sleep(0.001)
    domain_name_list.append(domain_name)

data.insert(10,"DOMAIN_NAME_Destination",domain_name_list,True)
#print(data)
print("DNS hits= ",h)
data.to_csv('Book10ksd.csv')
