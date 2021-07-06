#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render

import json,paramiko

from dwebsocket.decorators import accept_websocket

def index(request):
	return render(request,'ssh.html',locals(),content_type='text/html; charset=utf-8')


@accept_websocket
def webssh(request):
	if request.is_websocket():
		try:
			ip="192.168.1.68"
			ssh=paramiko.SSHClient()
			ssh.load_system_host_keys()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh_client = paramiko.SSHClient()
			ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh_client.connect(username='root', password='xxx', hostname='192.168.1.68', port=22, timeout=10,look_for_keys=False)
			print '主机 192.168.1.68 连接成功！'
			sshsession = ssh_client.get_transport().open_session() #成功连接后获取ssh通道
			sshsession.get_pty(term="xterm", width=120, height=40) #获取一个终端
			sshsession.invoke_shell() #激活终端
			for i in range(2):
				req_message = {"message":sshsession.recv(1024),"statue":0}
				request.websocket.send(json.dumps(req_message,ensure_ascii=False).encode("utf-8"))

			#从ssh通道获取输出data，并发送到前端
			def srecv():
				while True:
					sshmess = sshsession.recv(1024)
					if not sshmess:break;
					req_message = {"message":sshmess,"statue":0}
					request.websocket.send(json.dumps(req_message,ensure_ascii=False).encode("utf-8"))
			try:
				for shell in request.websocket:
					json_tmp = json.loads(shell)
					print shell
					if json_tmp['status'] == 1:
						sshsession.resize_pty(width=int(json_tmp['cols']), height=int(json_tmp['rows']))
					else:
						sshsession.send(json_tmp['data'])
						threading.Thread(target=srecv, args=()).start()
						
			except Exception, e:
				sshsession.close()
				ssh_client.close()
				print "关闭连接:%s" %(ip)
		except Exception, e:
			print "==="
		
