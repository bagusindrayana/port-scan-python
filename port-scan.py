import sys 
import socket 
import time
startTime = time.time()

   
target = ''
limit = 10
con = 'All'
if len(sys.argv) >= 2: 
    target = socket.gethostbyname(sys.argv[1])  
else: 
    print("Invalid ammount of Argument") 

if len(sys.argv) >= 3: 
    limit = int(sys.argv[2]) 

if len(sys.argv) >= 4: 
    con = str(sys.argv[3]) 

print("==================")
print("Scan Port In :",target)
def checkTcp(t,p):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    socket.setdefaulttimeout(1) 
    result = s.connect_ex((t,p)) 
    if result ==0: 
        print("TCP Port {} is open".format(p)) 
        return True
    s.close() 
    return False

def checkUdp(t,p):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    socket.setdefaulttimeout(1) 
    result = s.connect_ex((t,p)) 
    if result ==0: 
        print("UDP Port {} is open".format(p)) 
        return True
    s.close() 
    return False

i = 0
try: 
    for port in range(1,65535): 
        if(i <= limit):
            if con == 'TCP':
                if(checkTcp(target,port)):
                    i = i + 1
            elif con == 'UDP':
                if(checkUdp(target,port)):
                    i = i + 1
            else:
                if(checkTcp(target,port)):
                    i = i + 1
                if(checkUdp(target,port)):
                    i = i + 1
        else:
            break

except KeyboardInterrupt: 
    print("Time taken:", time.time() - startTime) 
    print("\n Exitting Program !!!!") 
    sys.exit() 
except socket.gaierror: 
    print("Time taken:", time.time() - startTime) 
    print("\n Hostname Could Not Be Resolved !!!!") 
    sys.exit() 
except socket.error: 
    print("Time taken:", time.time() - startTime) 
    print("\ Server not responding !!!!") 
    sys.exit() 

print("Time taken:", time.time() - startTime) 
print("Finish!!!")
sys.exit() 

