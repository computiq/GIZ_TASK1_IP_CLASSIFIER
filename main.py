import sys

class Solution:
    def __init__(self, arg):

        self.ip = ''
        self.cidr = ''

        while self.isInvalid(arg):
            arg = input(
                '\nEnter an IPv4 address in (x.x.x.x/x) format: ')

        print('Class: ', self.findClass(self.ip))
        print('Designation: ', self.findDesignation(self.ip))

    def isInvalid(self, arg):

        if type(arg) == list and len(arg) == 1:
            return True

        elif type(arg) == list and len(arg) > 2:
            print('This program only accepts one IP address at a time.')
            return True

        if type(arg) == list:
            address = arg[1]
        else:
            address = arg

        if len(address.split('/')) == 2:
            ip, cidr = address.split('/')[0].split('.'), address.split('/')[1]
            if ip == '' or cidr == '':
                print('Invalid input: no cidr or ip provided')
                return True
            ip = self.ip = [int(x) for x in ip]
            cidr = self.cidr = int(cidr)

        else:
            print('Invalid input: no cidr or ip provided')
            return True

        if len(ip) != 4:
            print('Invalid input: only 4 octets are allowed')
            return True
        for i in ip:
            if i < 0 or i > 255:
                print('Invalid input: number not in range (0-255)')
                return True
        if cidr < 0 or cidr > 32:
            print('Invalid input: CIDR out of range (0-32)')
            return True

    def findClass(self, ip):
        if(ip[0] >= 0 and ip[0] <= 127):
            return 'A'
        elif(ip[0] >= 128 and ip[0] <= 191):
            return 'B'
        elif(ip[0] >= 192 and ip[0] <= 223):
            return 'C'
        elif(ip[0] >= 224 and ip[0] <= 239):
            return 'D'
        else:
            return 'E'

    def findDesignation(self, ip):

        if ip[0] == 10:
            return 'Private'

        elif ip[0] == 127:
            return 'Special'

        elif ip[0] == 169 and ip[1] == 254:
            return 'Automatic Private IP Addressing (APIPA)'

        elif ip[0] == 172 and ip[1] > 15 and ip[1] < 32:
            return 'Private'

        elif ip[0] == 192 and ip[1] == 168:
            return 'Private'

        elif self.findClass(ip) == 'D' or self.findClass(ip) == 'D':
            return 'Special'

        else:
            return 'Public'

if __name__ == '__main__':
    calculate = Solution(sys.argv)
