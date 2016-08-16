# -*- coding: utf-8 -*-
# @Author leehdsniper
import psutil
import types
import smtplib
import time
from email.mime.text import MIMEText

from_addr='email_account'#like example@exam.com
passwd='email_password'
smtp_server='#send_mail_server'#like smtp.sina.com
to_addr='send_to_where'#like toemail@exam.com
pid_list=[]

def send_mail(msg):
	server=smtplib.SMTP(smtp_server,25)
	server.set_debuglevel(1)
	server.login(from_addr,passwd)
	msg=MIMEText(msg,'plain','utf-8')
	server.sendmail(from_addr,[to_addr],msg.as_string())
	server.quit()
while 1:
	pid=raw_input("Input PID:[input -1 to end]:\n")
	if(pid=='-1'):
		break
	try:
		pid=int(pid)
	except Exception,e:
		print 'PID must be number:'
		continue
	try:
		pid=psutil.Process(pid)
	except Exception,e:
		print 'PID does not exist'
		continue
	pid_list.append(pid)
if len(pid_list)<=0:
	print "No PID to detect"
	exit()
while 1:
	done=0
	for pid in pid_list:
		if pid.pid not in psutil.pids():
			done=done+1
	if done==len(pid_list):
		send_mail('All tasks has been done！')
		break
