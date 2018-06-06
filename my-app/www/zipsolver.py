#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zxy'
import os, re
from zipfile import ZipFile

class code(object):
	def __init__(self,name,codes):
		self.name = name
		self.codes = codes
		self.str = ''

pattern1 = re.compile(r'^(\d+)/(\d+)/(\d+)')

def read_file(path):
	with open(path,'r') as fr:
		str = ''
		for line in fr.readlines():
			str += line
	return str

def get_file(path):
	tzip = ZipFile(path,'r')
	code_obj = []
	book = {}
	for tname in tzip.namelist():
		if(os.path.isdir(tname)): continue
		m = re.match(pattern1,str(tname))
		str1 = m.group(1)+m.group(2)
		if book.get(str1,-1)!=-1: continue
		book[str1] = 1;
		code_obj.append(code(tname,read_file(tname)));
	tzip.close()
	return code_obj

def test(path):
	files = get_file(path)
	message = ''
	for data in files:
		message+=(str(data.name)+'\n'+str(data.codes))
		message+=str('\n\n\n\n\n\n\n\n\n\n\n')
	f = open('show.html','w')
	f.write(message)
	f.close()
	
if __name__=='__main__':
	path = './test.zip'
	test(path);	
