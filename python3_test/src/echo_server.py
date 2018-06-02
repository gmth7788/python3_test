#!/usr/bin/evn python3
#coding=utf-8

#echo server

import socket
import threading
import time

def deal_client(sock, addr):
    print('建立连接 %s:%s ...' % addr)
    sock.send(b'Hello, I am server!')
    while(True):
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        print('-->%s!', data.decode('utf-8'))
        sock.send(('msg:%s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('连接关闭 %s:%s.' % addr)
            
        


if __name__=="__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9999))
    s.listen(5)
    print('等待连接...\n')
    while(True):
        sock, addr = s.accept()
        t = threading.Thread(target=deal_client, args=(sock, addr))
        t.start()
