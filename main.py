import sys
import os
class Solution:
    def __init__(self,first,second,third,fourth,fifth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth =fourth
        self.fifth = fifth
    def enterdIp(self,first,second,third,fourth,fifth) :
        return "{}.{}.{}.{}/{}".format(self.first,second,third,fourth,fifth)

def checkIp(first,second,third,fourth,fifth):
    if first < 1 or first > 255 :
        print('Please enter a valid ip')
        sys.exit()
    elif second < 0 or second > 255 :
        print('Please enter a valid ip')
        sys.exit()
    elif third < 0 or third > 255 :
        print('Please enter a valid ip')
        sys.exit()
    elif fourth < 0 or fourth > 255 :
        print('Please enter a valid ip')
        sys.exit()
    elif fifth != 8 and fifth != 16 and fifth != 24 :
        print('Please enter a valid subnetmask')
        sys.exit()
    else : pass    
def anyclass(first):
    if first > 0 and first < 128 :
       print('This IP from class A')
    elif first > 127 and first < 192 :
        print('This IP from class B')
    elif first > 191 and first < 224 :
        print('This IP from class C')
    elif first > 223 and first < 240 :
        print('This IP from class D')
    elif first > 239 and first < 256 :
        print('This IP from class E')

def designationIp(first, second, fourth):
      if first == 10 or first == 172 and second > 15 and second < 30 or first == 192 and second == 168 : 
          print('This ip is private')
      elif first == 127 and fourth > 0:
          print('This ip is Spicial')
      else: print('This ip is public') 

if __name__ == '__main__':
    choosen = input('\nPlease choose what you want:\na.if you want to know the class of the ip.\nb.if you want to know if the ip is private or public or spicial.\nc.if you want to know both choice above.\nd.if you want to exit enter d or any key.\n')
    if choosen == 'd' or choosen == 'D' :
        sys.exit()
    elif choosen == 'a' or choosen == 'b' or choosen == 'c' or choosen == 'A' or choosen == 'B' or choosen == 'C' : 
        givenIp = input('\nPlease enter the IP address\n')
        sp = givenIp.split('.')
        first = int(sp[0])
        second = int(sp[1])
        third = int(sp[2])
        spp = sp[3].split('/')
        fourth = int(spp[0])
        if len(spp) == 1 :
            print('Please enter a valid subnetmask')
            sys.exit()
        else:
            fifth = int(spp[1])
        checkIp(first,second,third,fourth,fifth)
        if choosen == 'a' or choosen == 'A':
            os.system('cls')
            myIp = Solution(first, second, third, fourth, fifth)
            print('Your entered Ip adress is:', myIp.enterdIp(first, second, third, fourth, fifth))
            anyclass(first)
        elif choosen == 'b' or choosen == 'B':
            os.system('cls')
            myIp = Solution(first, second, third, fourth, fifth)
            print('Your entered Ip adress is:', myIp.enterdIp(first, second, third, fourth, fifth))
            designationIp(first,second,fourth)
        elif choosen == 'c' or choosen == 'C':
            os.system('cls')
            myIp = Solution(first, second, third, fourth, fifth)
            print('Your entered Ip adress is:', myIp.enterdIp(first, second, third, fourth, fifth))
            anyclass(first)
            designationIp(first,second,fourth)
        else: sys.exit()