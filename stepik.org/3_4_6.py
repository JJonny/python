import requests as rq
import sys
import re

sys.stdin = open('input_3_4_6.txt')

start = input()
end = input()
 
pattern = "href *= *[\'\"](.*?)[\'\"]"
 
try:
  r = rq.get(start)
  for ref in re.findall(pattern, r.text):
    try:
      r = rq.get(ref)
      if end in re.findall(pattern, r.text):
        print("Yes")
        break
    except:
      pass
  else:        
    print("No")
except:
  print("No")

