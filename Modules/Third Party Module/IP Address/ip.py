'''IMPORTANT PROPERTIES
ip.version
ip.is_private
ip.is_global
ip.is_loopback
ip.is_multicast
ip.is_unspecified'''

import ipaddress

ip=ipaddress.ip_address("192.168.1.10")
print(ip)
ip = ipaddress.ip_address("192.168.1.10")
print(ip)
print(type(ip))

a=ip.version
print(a)

x=ip.is_private
print(x)

i=ipaddress.ip_network("192.168.1.0/24")
print(i)
'''
y=network.hosts()
print(y)
'''