#/bin/env E:\Python27 (is my env)
#Shodan uses Murmur3 hash for favicons
#@clubmasterfu



import mmh3
import argparse
import urllib2
import base64

ap = argparse.ArgumentParser(description="Find Shodan by Favicon hash http.hash.favicon")
ap.add_argument("host", help="(Example: http://127.0.0.1).")
args = ap.parse_args()

request = urllib2.Request(args.host+"/favicon.ico")

response = urllib2.urlopen(request)
print response.info()
orginal = response.read()
#favicon = base64.b32encode(orginal)
favicon2 = base64.encodestring(orginal)
print "Base 64 String:", favicon2



hash = mmh3.hash(favicon2)
print 'Murmur hash of favicon should be: ', hash 
print "---------------------------------\n"


print "---------------------------------\n"

print ''









