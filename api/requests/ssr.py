# -*- coding:utf-8 -*-

import requests
from lxml import etree

def get_ssr():
	ssr_url =  'https://github.com/Alvin9999/new-pac/wiki/ss%E5%85%8D%E8%B4%B9%E8%B4%A6%E5%8F%B7'
	r = requests.get(ssr_url)
	content = etree.HTML(r.content)
	elements = content.xpath('//p//img/@src')
	return elements[1]


def file_path(url):
	result = ''
	if url:
		ss = url.split('/')
		ss_len = len(ss)
		result = ss[ss_len-1]
	return result


def save_file(url):
	if url:
		r = requests.get(url,stream=True)
		filename = file_path(url)
		if filename:
			with open(filename,'wb') as f:
				for c in r.iter_content():
				    f.write(c)
        

def image_ocr(url):
	# pip install Pillow(PIL)
	# pip install pytesser3
	# pip install pytesseract
	# sudo apt-get install tesseract-ocr
	import pytesseract
	from PIL import Image
	im = Image.open(file_path(url))
	text = pytesseract.image_to_string(im)
	print(text)


if __name__=='__main__':
	image_ocr(get_ssr())