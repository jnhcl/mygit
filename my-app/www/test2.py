#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zxy'
import sys
import codecopyDetection
import os,shutil
kit = codecopyDetection.codecopy_detection()

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
	flag = True
	with open(path,'r') as fr:
		str = ''
		for line in fr.readlines():
			if flag:
				flag = False; continue;
			str += line
	return str

def read_obj(path):
	#if not os.path.exists('./test/export_file/'):
	unzip(path,'./test2/test/')
	tlist = os.listdir('./test2/test/export_file/')
	str1 = './test2/test/export_file/'+str(tlist[0])+'/'
	mylist = os.listdir(str1)
	code_obj = []
	for fl in mylist:
		tname = str1+fl
		fullname = str(tname)+'/'+(os.listdir(tname))[-1]
		#print(fullname)
		code_obj.append(code(fl,read_file(fullname)))
	return code_obj

def movefile(srcfile,dstfile):
	if not os.path.isfile(srcfile):
		return
	else:
		fpath,fname=os.path.split(dstfile)    
		if not os.path.exists(fpath):
			os.makedirs(fpath)               
		shutil.move(srcfile,dstfile)         
		print('move %s -> %s' %( srcfile,dstfile))

def del_dir(path):
	mylist = os.listdir(path)
	for fl in mylist:
		fullname = path+fl
		print('del %s...'%fullname)
		if os.path.isdir(fullname):
			shutil.rmtree(fullname,True)
		else:
			os.remove(fullname)

class namefile:
	def __init__(self,tname,tlist,tcontent):
		self.name = tname
		self.list = tlist
		self.content = tcontent
class testFile2:
	def test(self):
		l1 = 0.75; l2 = 0.75
		data = read_obj('./test2/test/test.zip')
		n = len(data)
		namelist = []
		str2='-------------------------------------------------'
		print('checking...');book = False
		for i in range(n):
			plus = data[i].name+'\n'+data[i].codes+'\n\n'+str2; book = False
			message = [];
			for j in range(n):
				if j==i: continue
				#print('--------------------');
				#print(data[i].codes+'\n\n'+data[j].codes);
				kit.fit(data[i].codes,data[j].codes)
				if(kit.check(l1,l2)):
					book = True
					message.append(data[j].name)
					plus += data[j].name+'\n'+data[j].codes+'\n\n'+str2
			if book:
				if len(message) > 6:
					message = message[0:6]
				namelist.append(namefile(data[i].name,message,plus));
		print('checked ok');
		del_dir('./test2/test/')
		return namelist;

if __name__ == '__main__':
	path = './test/test.zip'
	test = testFile()
	test.test()
