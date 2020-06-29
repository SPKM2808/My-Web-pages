#!/usr/bin/env python3
import psutil
import emails
import socket
import os

def hostname_resolves(hostname):
    try:
        socket.gethostbyname(hostname)
        return socket.gethostbyname(hostname)
    except socket.error:
        return 0

sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))

body = "Please check your system and resolve the issue as soon as possible."


if psutil.cpu_percent()>80 :
    subject = "Error - CPU usage is over 80%"
    message = emails.generate(sender, receiver, subject, body)
    emails.send(message)
    
if psutil.disk_usage('/').percent > 80:
    subject = "Error - Available disk space is less than 20%"
    message = emails.generate(sender, receiver, subject, body)
    emails.send(message)
    
if psutil.virtual_memory().free /1024/1024 < 500:
    subject = "Error - Available memory is less than 500MB"
    message = emails.generate(sender, receiver, subject, body)
    emails.send(message)
    
if hostname_resolves('localhost')=='127.0.0.1':
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    message = emails.generate(sender, receiver, subject, body)
    emails.send(message)

