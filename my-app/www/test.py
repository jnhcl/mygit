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
	with open(path,'r') as fr:
		str = ''
		for line in fr.readlines():
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
		os.remove(fullname)

class testFile:
	def test(self):
		l1 = 0.65; l2 = 0.75
		if not os.path.exists('./test2/test/show/'):
			os.mkdir('./test2/test/show/')
		else:
			del_dir('./test2/test/show/')

		data = read_obj('./test2/test/test.zip')
		n = len(data)

		namelist = []
		str2='-------------------------------------------------'
		print('checking...');
		for i in range(n):
			message = ''; plus = data[i].codes+'\n\n'+str2; book = False
			for j in range(n):
				if j==i: continue
				kit.fit(data[i].codes,data[j].codes)
				if(kit.check(l1,l2)):
					book = True
					message += str(data[j].name)+'\n'
					plus += data[j].codes+'\n\n'+str2
			if book:
				namelist.append(data[i].name)
				with open('./test2/test/show/'+data[i].name,'w') as f:
					f.write(str(message)+'\n\n'+plus)
		azip = zipfile.ZipFile('show.zip', 'w')
		for current_path, subfolders, filesname in os.walk(r'./test2/test/show'):
			for file in filesname:
				print(current_path,subfolders,filesname)
				azip.write(os.path.join(current_path, file))
		print('checked ok');
		movefile('./show.zip','./test2/test/show.zip');
		return azip;

if __name__ == '__main__':
	path = './test/test.zip'
	test = testFile()
	test.test()