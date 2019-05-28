#Shodan uses Murmur3 hash for favicons
#@clubmasterfu
#http.favicon.hash:


import mmh3
import argparse
import urllib3
import base64

ap = argparse.ArgumentParser(description="Find Shodan by Favicon hash http.hash.favicon")
ap.add_argument("host", help="(Example: http://127.0.0.1).")
args = ap.parse_args()

http = urllib3.PoolManager()
url = args.host+"/favicon.ico"

response = http.request('GET', url)
print (response.info())
favicon = base64.encodebytes(response.data)
print ("Base 64 String:", favicon)



hash = mmh3.hash(favicon)
print ('Murmur hash of favicon should be: ', hash) 
print ("---------------------------------\n")


print ("---------------------------------\n")

print ('')









