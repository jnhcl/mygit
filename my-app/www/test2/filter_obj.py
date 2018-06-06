#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zxy'

import re
def is_var(str):
	if str=='int' or str=='(int' or str=='(int)' or str=='for(int':
		return True
	if str=='short' or str=='(short' or str=='(short)' or str=='for(short':
		return True
	if str=='long' or str=='(long' or str=='(long)' or str=='for(long':
		return True
	if str=='char' or str=='(char' or str=='(char)' or str=='for(char':
		return True
	if str=='bool' or str=='(bool' or str=='(bool)' or str=='for(bool':
		return True
	if str=='void' or str=='(void' or str=='(void)' or str=='for(void':
		return True
	if str=='string' or str=='(string' or str=='(string)' or str=='for(string':
		return True
	return False

pattern1 = re.compile('/\*{1,2}[\s\S]*?\*/') #去除块级注释
pattern2 = re.compile('//[\s\S]*?\n') #去除行级注释
pattern3 = re.compile('^\s*\n')  #去除空白符
pattern4 = re.compile('[^\x00-\xff]+')  #去除中文
pattern5 = re.compile('[_a-zA-Z][_a-zA-Z0-9]*')  #匹配变量名
class filter(object):
	def clear_note(self,str):
		result = re.sub(pattern1,'', str)
		result = re.sub(pattern2,'',result)
		result = re.sub(pattern3,'',result)			
		result = re.sub(pattern4,'',result)
		return result

	def rep(self,str):
		result = re.sub(pattern5,'T',str)
		return result

	def rep_name(self,str):
		result = re.findall(pattern5,str)
		return result

	def rep_name2(self,str):
		result = re.findall(pattern5,str)
		if result==[]:
			return -1
		return result[0]

	def no_blank(self,str):
		str1 = ''
		for i in str:
			if i=='\r' or i=='\n' or i=='\t':
				pass
			else: str1 += i
		return str1

	def unnite_var(self,str):
		code = re.split(r'[\s]+',str)
		len1 = len(code)
		str1 = ''
		book = {}; temp = []
		for i in range(len1):
			if is_var(code[i]):
				if i!=len1-1:
					temp = self.rep_name(code[i+1])
					for j in temp:
						book[j] = 1;
		for i in range(len1):
			if self.rep_name2(code[i]) in book:
				str1 += self.rep(code[i])
			else:
				str1 += code[i]
		return str1

	def to_lower_case(self,str):
		code = str.lower();
		return code;

	def filter(self,str):
		str = self.clear_note(str)
		str = self.unnite_var(str)
		str = self.no_blank(str)
		str = self.to_lower_case(str);
		return str

'''
def test(path):
	str = ''
	with open(path,'r') as fr:
		str = fr.read()

	ft = filter()
	print(str)
	print("new line begin")
	print(ft.filter(str))
if __name__=='__main__':
	import sys
	args = sys.argv
	test('/media/zsy/WORK/mywork/test/e.cpp')
'''
