#! /usr/bin/env python3
import os
import requests
data1=[]
for i in os.listdir('./supplier-data/descriptions/'):
	buff={}
	f=open('./supplier-data/descriptions/'+i)
	lines=f.readlines()
	buff["name"]=lines[0].strip()
	buff["weight"]=lines[1].strip().strip(' lbs')
	buff["description"]=lines[2].strip()
	buff["image_name"]=(i.strip('.txt'))+'.jpeg'
	data1.append(buff)
	f.close()
	print(data1)
	x=requests.post('http://35.192.55.78/fruits/',json=buff)
	print(x.status_code)

	if x.status_code==201:
		print('Success')
	else:
		print('Fail')
