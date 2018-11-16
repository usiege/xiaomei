#-*-coding=utf-8-*-

from pathlib import Path

import urllib.request
import re
import os

url = "https://findicons.com/pack/2787/beautiful_flat_icons"


def url_request(url, save_path):

	webPage = urllib.request.urlopen(url)
	data = webPage.read().decode('utf-8')

	k = re.split(r'\s+', data)
	s = []
	sp = []
	si = []

	for i in k:
		if (re.match(r'src', i) or re.match(r'href', i)):
			if (not re.match(r'href="#"', i)):
				if (re.match(r'.*?png"', i) or re.match(r'.*?ico"', i)):
					if (re.match(r'src', i)):
						s.append(i)

	for it in s:
		if (re.match(r'.*?png"', it)):
			sp.append(it)

	cnt = 0
	cou = 1
	for it in sp:
		m = re.search(r'src="(.*?)"', it)
		iturl = m.group(1)
		print(iturl)
		if (iturl[0] == '/'):
			continue;
		web = urllib.request.urlopen(iturl)
		itdata = web.read()
		if (cnt % 3 == 1 and cnt >= 4 and cou <= 30):
			path = os.path.join(save_path, '{}.png'.format(str(cou)))
			f = open(path, 'wb')
			cou = cou + 1
			f.write(itdata)
			f.close()
			print(it)
		cnt = cnt+1


def main(path):

	url_request(url, path)

if __name__ == '__main__':
	# save_path = "F:\\working\\xiaomei"
	save_path = Path("F:/working/xiaomei/image")

	print(save_path)
	main(save_path)
