# usr/bin/env python3
# _*_ coding: utf-8 _*_
__author__ = 'zxy'


'''
this is a test program
'''

from codecopyDetection import *

kit = codecopy_detection()
t = 1;
print('if you don\'t want to continue,you can type exit');
while(True):
	print('test %d begin'%t)
	t += 1
	str1 = input()
	if(str1=='exit'):
		break;
	str2 = input()
	kit.fit(str1,str2)
	print(kit.code1+"\n"+kit.code2);
	print(kit.predict())
	print(kit.print())