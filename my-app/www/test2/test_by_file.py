# usr/bin/env python3
# _*_ coding: utf-8 _*_

__author__ = 'zxy'

'''
test by file:
the file path: ./test
'''

from codecopyDetection import *;
import read_obj as ro;


kit = codecopy_detection();

def test():
	files = ro.read_obj('./test/');
	n = len(files);
	book = {};
	for i in range(n):
		vis = []
		for j in range(n):
			if i!=j:
				kit.fit(files[i].codes,files[j].codes);
				if(kit.predict()>0.8 or kit.predict2()>0.7):
					vis.append([files[j].name,kit.print().decode('utf-8')]);
		book[files[i].name] = vis;
	return book;

