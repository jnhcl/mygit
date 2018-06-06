#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zxy'

class Suffixarray(object):
	def check(self):
		str1 = self.str1
		str2 = self.str2
		mid = len(str1)+1
		self.work(mid)
		begin, mx = self.begin, self.mx
		if begin==len(str1) and mx==1:
			return ''
		else:
			return str1[begin:begin+mx]

	def __init__(self,str1,str2):
		self.ch = []
		self.ch.append(256)
		for i in str1:
			self.ch.append(i)
		self.ch.append(257)
		for i in str2:
			self.ch.append(i)
		self.ch.append(258)
		self.begin = 0
		self.mx = 0
		self.str1 = str1
		self.str2 = str2

	def work(self,mid):
		ch = self.ch
		n = len(ch)-2; m = max(n+1,5000);
		sa = [0 for i in range(m+1)]
		tsa = [0 for i in range(m+1)]
		rank = [0 for i in range(m+1)]
		height = [0 for i in range(m+1)]
		A = [0 for i in range(m+1)]
		B = [0 for i in range(m+1)]
		cntA = [0 for i in range(m+1)]
		cntB = [0 for i in range(m+1)]

		for i in range(1,n+1):
			cntA[ch[i]] += 1
		for i in range(1,256):
			cntA[i] += cntA[i-1]
		for i in range(n,-1,-1):
			sa[cntA[ch[i]]] = i
			cntA[ch[i]] -= 1
		rank[sa[1]] = 1
		for i in range(2,m):
			rank[sa[i]] = rank[sa[i-1]]
			if ch[sa[i]] != ch[sa[i-1]]:
				rank[sa[i]] += 1
		l = 1
		while(rank[sa[n]]<n):
			for i in range(n+1):
				cntA[i] = 0
				cntB[i] = 0
			for i in range(1,n+1):
				A[i] = rank[i]
				if i+l<=n:
					B[i] = rank[i+l]
				else:
					B[i] = 0
				cntA[A[i]] += 1
				cntB[B[i]] += 1
			for i in range(1,n+1):
				cntB[i] += cntB[i-1]
			for i in range(n,-1,-1):
				tsa[cntB[B[i]]] = i
				cntB[B[i]] -= 1
			for i in range(1,n+1):
				cntA[i] += cntA[i-1]
			for i in range(n,-1,-1):
				sa[cntA[A[tsa[i]]]] = tsa[i]
				cntA[A[tsa[i]]] -= 1
			rank[sa[1]] = 1
			for i in range(2,n+1):
				rank[sa[i]] = rank[sa[i-1]]
				if A[sa[i]] != A[sa[i-1]] or B[sa[i]] != B[sa[i-1]]:
					rank[sa[i]] += 1
			l <<= 1

		j = 0
		for i in range(1,n+1):
			if j>0:
				j -= 1
			while(i+j<=n and sa[rank[i]-1]+j<=n and ch[i+j]==ch[sa[rank[i]-1]+j]):
				j += 1;
			height[rank[i]] = j
		mx = 0; begin = 0
		for i in range(1,n+1):
			if (sa[i]>mid and sa[i-1]<mid):
				if mx<height[i]:
					mx = height[i]
					begin = sa[i-1]
			elif (sa[i]<mid and sa[i-1]>mid):
				if mx<height[i]:
					mx = height[i]
					begin = sa[i]
		self.begin = begin-1
		self.mx = mx

