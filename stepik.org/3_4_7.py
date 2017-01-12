import requests as rq
import re

pattern = r"((\w+\.)+[A-Za-z]{2,4})"
l=[]
r = rq.get("http://pastebin.com/raw/hLx3HeZV")

for ref in re.findall(pattern, r.text):	
	print(ref[0])
	


