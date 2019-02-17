#!/usr/bin/python
#-*- coding: utf-8 -*-

fin=open('ask3.txt','r')
fina=open('apantisi.txt','w')
fin.read()
for i in fin:
	if i=='#':
		i.pop()

fin.close()
fina.close()