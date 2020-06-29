#!/usr/bin/env python3

import os
import datetime as dt
import reports
import emails
#import json
x_dat=[]
now = dt.datetime.now()
#files = os.listdir('./supplier-data/description')
for i in os.listdir('./supplier-data/descriptions/'):
	buff={}

	f=open('./supplier-data/descriptions/'+i)
	lines=f.readlines()

	buff["name"]=lines[0].strip()
	buff["weight"]=lines[1].strip()
	'''buff["description"]=lines[2].strip()
	buff["image_name"]=(i.strip('.txt'))+'.jpeg' '''
	f.close()
	x=('name: '+buff["name"]+'<br/>'+'weight: '+buff['weight'])
	x_dat.append(x)
x_dat='<br/><br/>'.join(x_dat)
reports.generate("processed.pdf", "Processed Update on "+now.strftime('%B %d,%Y'), x_dat)

sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = "Upload Completed - Online Fruit Store"
body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

message = emails.generate(sender, receiver, subject, body, "processed.pdf")
emails.send(message)
