from time import sleep
from threading import Thread
from os import kill
from os import getpid
from sys import stdout
import socket, signal
global open, pid
open=[]
max=0
timeout=999
pid = getpid()
def kill_process():
    print("\nClosing process....")
    if hasattr(signal, 'SIGKILL'):
        kill(pid, signal.SIGKILL)
    else:
        kill(pid, signal.SIGABRT)
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
host=str(input("IP: ")).replace("https://","").replace("http://","").split("/")
while (max < 1) or (max > 65535):
    try:
        max=int(input("Max port: "))
    except KeyboardInterrupt:
        kill_process()
    except:
        print("\n Integer number [1-65535]\n Large port can take quite a while\n")
        max=0
while (timeout < 0) or (timeout > 10):
    try:
        timeout=float(input("Time port (Default: 0.002): "))
    except KeyboardInterrupt:
        kill_process()
    except:
        print("\n Float number [0-10] (Default: 0.002)\n Short time may cause the device to lag\n")
        timeout=999
print("\nScanning...")
for port in range(1,max+1,1):
    try:
        Thread(target=check_ip, args=(host[0],port)).start()
        i=int(100/max*port)
        stdout.write("\r[%-25s] %d%%" % ('='*int(i/4), i))
        stdout.flush()
        sleep(timeout)
    except KeyboardInterrupt:
        kill_process()
print("\nScan complete!")
sleep(5)
open = str(", ".join(open))
print(f"\nPort open: {open}")
kill_process()