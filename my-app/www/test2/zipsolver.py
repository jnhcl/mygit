#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zxy'
import os, re
import zipfile

class code(object):
	def __init__(self,name,codes):
		self.name = name
		self.codes = codes

def unzip(zpath,upath):
	try:
		with zipfile.ZipFile(zpath) as zfile:
			zfile.extractall(path=upath)
	except zipfile.BadZipFile as e:
		print(zpath+' is a bad zip file')

pattern1 = re.compile(r'^(\d+)/(\d+)/(\d+)')

def read_file(path):
	with open(path,'r') as fr:
		str = ''
		flag = False
		for line in fr.readlines():
			if not flag:
				flag = True
				continue
			str += line
	return str

def read_obj(path):
	#if not os.path.exists('./test/export_file/'):
	unzip(path,'./test/')
	tlist = os.listdir('./test/export_file/')
	str1 = './test/export_file/'+str(tlist[0])+'/'
	mylist = os.listdir(str1)
	code_obj = []
	for fl in mylist:
		tname = str1+fl
		fullname = str(tname)+'/'+(os.listdir(tname))[-1]
		print(fullname)
		code_obj.append(code(fl,read_file(fullname)))
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

