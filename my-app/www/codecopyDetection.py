#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zxy'
import sys
sys.path.append('./test2/')

import check_it as ct
import filter_obj as flt
#import logmoudle as log
from suffix_array import Suffixarray

class codecopy_detection(object):
	def __init__(self):
		self.str1 = ''
		self.str2 = ''
		self.book1 = ''
		self.book2 = ''
		self.code1 = ''
		self.code2 = ''
		self.samePoint = 0.0
		self.sameStr = ''

	def fit(self,str1,str2):
		self.str1 = str1
		self.str2 = str2
		ft = flt.filter()
		self.code1 = ft.filter(str1)
		self.code2 = ft.filter(str2)
		checktor = ct.winnowing(self.code1.encode('ascii'),self.code2.encode('ascii'))
		self.samePoint = checktor.check()
		sub_str = Suffixarray(self.code1.encode('ascii'),self.code2.encode('ascii'))
		self.sameStr = sub_str.check();

	def predict(self):
		return self.samePoint

	def predict2(self):
		temp = min(len(self.code1),len(self.code2));
		if temp==0: return 0;
		else: return len(self.sameStr)/temp;

	def check(self,l1=0.75,l2=0.75):
		if(self.predict()>l1 or self.predict2()>l2):
			return True
		return False

	def print(self):
		return self.sameStr