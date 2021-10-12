"""
Class A:
    1.0.0.0
    the first octet is the important here and it's maximum value is 128 to be in class A
    and for it to be private the first octet needs to be a ten

Class B:
    128.0.0.0
    For the IP to be in class B, the first octet should have a minimum value of 128 and a max of up to but
    not including 192 
    and for it to be private the fo(first octet) should be 172.16 or 172.31

Class C:
    192.0.0.0
    the first octet has a minimum value of 192 and a maximum of up to 223
    and for it to be private the fisrt octet needs to be 192 and the second one should be 168

Class D:
    224.0.0.0
    the fisrt octet has a minimum value of 224 and a maximum of up to but not including 240
    Can't be private

Class E:
    240.0.0.0
    the first octet needs to have a minimum value of 240 and a maximum of 255
    Can't be private

"""
import sys

def get_class(octets):
        first_octet = int(octets[0])
        if first_octet >= 1 and first_octet < 129:
            return "Class A"
        elif first_octet >= 128 and first_octet < 192:
            return "Class B"
        elif first_octet >= 192 and first_octet < 224:
            return "Class C"
        elif first_octet >= 224 and first_octet < 240:
            return "Class D"
        elif first_octet >= 240 and first_octet < 256:
            return "Class E"

def get_designation(octets):
        if int(octets[0]) == 10:
            return "Private"
        elif int(octets[0]) == 127:
            return "Special"
        elif int(octets[0]) < 128:
            return "Public1"
        elif int(octets[0]) == 172 and int(octets[1]) == 16:
            return "Private"
        elif int(octets[0]) < 192:
            return "Public2"
        elif int(octets[0]) == 192 and int(octets[1]) == 168:
            return "Private"
        elif int(octets[0]) < 224:
            return "Public"
        else:
            return "Special"

class Solution():
    def __init__(self, ip):
        self.octets = ip.split(".")
        self.clas = get_class(self.octets)
        self.designation = get_designation(self.octets)
        print(self.octets)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py IP address")
        exit()
    ip = Solution(sys.argv[1][:-3])
    print(ip.clas,", ", ip.designation)
    pass
