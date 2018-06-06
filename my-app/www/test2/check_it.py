#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zxy'

INF = int(1e10+7)
MOD = int(1e9+7)
from collections import deque

def hash_str(s):
    ha = 0;seed = 233
    for i in range(len(s)): ha = (ha*seed)%MOD + int(s[i])
    return ha
class node(object):
    def __init__(self,t1,t2):
        self.key = t1
        self.value = t2
class winnowing(object):
    def __init__(self,in1,in2):
        self.str1 = in1; self.str2 = in2
        self.k = 5;self.w = 8
        self.kg1 = [];self.kg2 = []
        self.fp1 = [];self.fp2 = []

    def k_gram(self):
        k = self.k
        len1 = len(self.str1);len2 = len(self.str2)
        
        #init hash
        seed = 233;
        p = 1;
        for i in range(k-1):
            p = (p*seed)%MOD

        #k-grams
        thash = 0;
        for i in range(len1):
            if i<k:
                thash = (thash*seed)%MOD+int(self.str1[i]);
            else:
                thash = thash-(p*int(self.str1[i-k]))%MOD
                while thash<0:
                    thash += MOD
                thash = (thash*seed)%MOD+int(self.str1[i])
            if i>=k-1:
                self.kg1.append(thash)

        thash = 0;
        for i in range(len2):
            if i<k:
                thash = (thash*seed)%MOD+int(self.str2[i]);
            else:
                thash = thash-(p*int(self.str2[i-k]))%MOD
                while thash<0:
                    thash += MOD
                thash = (thash*seed)%MOD+int(self.str2[i]) 
            if i>=k-1:   
                self.kg2.append(thash)

    def select_hash(self):
        mini = INF;
        kg1 = self.kg1; kg2 = self.kg2
        len1 = len(kg1);len2 = len(kg2)
        p = 0; k = self.k; w = self.w
        que = deque([]);
        for i in range(len1):
            while len(que)>0 and que[-1].value>kg1[i]:
                que.pop()
            que.append(node(i,kg1[i]))
            if i>=w:
                if len(que)>0 and que[0].key<=i-w:
                    que.popleft()
            if i>=w-1:
                self.fp1.append(que[0].value)
        
        while len(que)>0:
            que.pop()
        
        for i in range(len2):
            while len(que)>0 and que[-1].value>kg2[i]:
                que.pop()
            que.append(node(i,kg2[i]))
            if i>=w:
                if len(que)>0 and que[0].key<=i-w:
                    que.popleft()
            if i>=w-1:
                self.fp2.append(que[0].value)  

    def check(self):
        self.k_gram();self.select_hash()
        fp1 = self.fp1; fp2 = self.fp2
        fp1 = sorted(fp1); fp2 = sorted(fp2)
        ins_cnt = 0;uni_cnt = 0
        len1 = len(fp1);len2 = len(fp2)
        p=0;q=0
        while p<len1 and q<len2:
            if fp1[p]<fp2[q]: p+=1;
            elif fp1[p]>fp2[q]: q+=1;
            else:
                p+=1;q+=1;ins_cnt+=1
        uni_cnt = len1+len2-ins_cnt;
        if uni_cnt == 0:
            return 0
        return float(ins_cnt)/uni_cnt;