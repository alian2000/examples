import socket
import pandas as pd
import time

data= pd.read_csv ("sample.csv")   
source=data["destinationaddress".strip()]

def get_domain_name(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)[0]
        return hostname
    except socket.herror:
        return "No domain name found"

domain_name_list=[]
for ipaddress in source:
    if ipaddress =="10.10.10.1":
        domain_name="router"
        domain_name_list.append(domain_name)
        
    else:
        domain_name= get_domain_name(ipaddress)
        time.sleep(0.1)
        domain_name_list.append(domain_name)

data.insert(10,"DOMAIN_NAME",domain_name_list,True)
#print(data)
data.to_csv('sampled.csv')

    
