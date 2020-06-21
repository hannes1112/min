#Hannes Fehre
#URL finder without RegEx in HTML
#3.7.3

import urllib.request

fp = urllib.request.urlopen("http://www.python.org")
mybytes = fp.read()

html_var = mybytes.decode("utf8")
fp.close()

x = html_var.split('"')
j=0
for i in x:
    last = x[j]
    if (last[0:4] == "http")or(last[0:3] == "www"): 
        print(last)
    j += 1
