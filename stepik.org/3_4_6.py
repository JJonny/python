import requests
import sys
import re

sys.stdin = open('input_3_4_6.txt')

start = input()
end = input()


def find_href(request_res):
	o = re.compile(r'href="(.*?)"')	
	found = o.findall(request_res.text)		
	return found

def moveToLink2(link):
	res = requests.get(link)	
	if res.status_code == 200:	
		out = find_href(res)
		if end in out:
			return 'Yes'
		else:
			return 'No'


res = requests.get(start)	
if res.status_code == 200:
	hrefs = find_href(res)		
	for i in hrefs:		
		r = moveToLink2(i)
		print(r)
		



	
	