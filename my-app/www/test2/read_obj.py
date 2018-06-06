#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zxy'
from zipfile import ZipFile

def read_file(path):
	with open(path,'r') as fr:
		str = ''
		for line in fr.readlines():
			str += line
	return str

class code(object):
	def __init__(self,name,codes):
		self.name = name
		self.codes = codes
		self.str = ''

def read_obj(path):
	import os
	mylist = os.listdir(path)
	code_obj = []
	for fl in mylist:
	    fullname = path+fl
	    code_obj.append(code(fl,read_file(fullname)))
	return code_obj

def get_file(path):
	tzip = ZipFile(path,'r')
	code_obj = []
	for tname in tzip.namelist():
		for data in tzip.open(tname,'r'):
			files.append(code(tname,data));
	tzip.close()
	return code_obj

def test():
	a = input('输入一个地址')
	ans = read_obj(a)
	for ob in ans:
		print('%s %s\n'%(ob.name,ob.codes))

if __name__ == '__main__':
	test()