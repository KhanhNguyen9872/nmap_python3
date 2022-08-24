from time import sleep
from threading import Thread
from os import name
from os import system
import socket
from sys import stdout
global open
open=[]
max=0

def kill_process():
    if (name == 'nt'):
        system("taskkill /f /im python.exe >null 2>&1")
    else:
        system("killall python3 >/dev/null 2>&1")
    exit()

def check_ip(host,port):
    s = socket.socket()
    try:
        s.connect((host, int(port)))
    except:
        pass
    else:
        s.close()
        open.append(f"{port}")

host=str(input("IP: "))
while (max == 0) or (max < 1) or (max > 65535):
    try:
        max=int(input("Max port scan: "))
    except KeyboardInterrupt:
        kill_process()
    except:
        print("\n Input number [1-65535]\n Large port can take quite a while\n")
        max=0

print("Scanning...")
for port in range(1,max+1,1):
    try:
        Thread(target=check_ip, args=(host,port)).start()
        i=int(100/max*port)
        stdout.write("\r[%-25s] %d%%" % ('='*int(i/4), i))
        stdout.flush()
        sleep(0.001)
    except KeyboardInterrupt:
        kill_process()

print("\nScan complete!")
sleep(6)
open = str(", ".join(open))
print(f"\nPort open: {open}")
print("\nClosing process....")
kill_process()