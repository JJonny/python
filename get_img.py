import requests as rq
import sys
import re
import shutil

# pattern = "href *= *[\'\"](.*?)[\'\"]"
pattern = "src *= *[\'\"](.*?jpg)[\'\"]"
out_path = './images/'

def get_url_images(site):
    try:
        r = rq.get(site)
        for ref in re.findall(pattern, r.text):
            # if 'http' in ref or 'https' in ref:
            print(ref + '\n')
            download_wget(ref)
    except:
        print("No")


def download_wget(url):
    r = rq.get(url, stream=True)
    if r.status_code == 200:
        # get file name
        filename = url.split('/')[-1]
        print(filename)
        with open(out_path + filename, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)


get_url_images('https://kamana.ua/')
# download_wget('https://kamana.ua/img/kamana-logo-1495379753.jpg')
