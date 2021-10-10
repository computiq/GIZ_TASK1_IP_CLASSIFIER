#!/usr/bin/python
# -*- coding: utf-8 -*-


class Solution:

    def __init__(self, ip):
        self.ip = ip

    # input ip from the user :

    @classmethod
    def IP_input(self):
        ip = input('Enter your ip address: ')
        return self(ip)

    def check(self):
        ip_address = self.ip

        # a separate prefix from network id (/)

        prefix = []
        for i in ip_address.split('/'):
            prefix.append(i)

        # check if prefix in the range or not:

        if prefix[1] == '8' or prefix[1] == '16' or prefix[1] == '24':

            try:

                # this is the separate network id and then we convert it to an integer :

                check_ip = []
                for j in prefix[0].split('.'):
                    check_ip.append(int(j))

                index = len(check_ip)

               # check if ip in format : (x.x.x.x/x)

                if index == 4:
                    ID1 = check_ip[0]
                    ID2 = check_ip[1]
                    ID3 = check_ip[2]
                    ID4 = check_ip[3]

                    # Class A checking :

                    if ID1 >= 1 | ID1 <= 127 and ID2 == 0 and ID3 == 0 \
                        and ID4 == 0:
                        print ('Class: A, Designation: Public')
                    elif ID1 == 10 and ID2 >= 0 | ID2 <= 255 and ID3 \
                        >= 0 | ID3 <= 255 and ID4 >= 0 | ID4 <= 255:

                        print ('Class: A, Designation: Private')
                    elif ID1 == 127 and ID2 >= 0 | ID2 <= 255 and ID3 \
                        >= 0 | ID3 <= 255 and ID4 >= 1 | ID4 <= 255:

                        print ('Class: A, Designation: Special')
                    elif ID1 >= 128 | ID1 <= 191 and ID2 >= 0 | ID2 \
                        <= 255 and ID3 == 0 and ID4 == 0:

                    # Class B checking :

                        print ('Class: B, Designation: Public')
                    elif ID1 == 172 and ID2 >= 16 | ID2 <= 31 and ID3 \
                        >= 0 | ID3 <= 255 and ID4 >= 0 | ID4 <= 255:

                        print ('Class: B, Designation: Private')
                    elif ID1 >= 192 | ID1 <= 223 and ID2 >= 0 | ID2 \
                        <= 255 and ID3 >= 0 | ID3 <= 255 and ID4 == 0:

                    # Class C checking :

                        print ('Class: C, Designation: Public')
                    elif ID1 == 192 and ID2 == 168 and ID3 >= 0 | ID3 \
                        <= 255 and ID4 >= 0 | ID4 <= 255:

                        print ('Class: C, Designation: Private')
                    elif ID1 >= 224 | ID1 <= 239 and ID2 >= 0 | ID2 \
                        <= 255 and ID3 >= 0 | ID3 <= 255 and ID4 >= 0 \
                        | ID4 <= 255:

                    # Class D checking :

                        print('Class: D, Designation: Special')
                    elif ID1 >= 240 | ID1 <= 255 and ID2 >= 0 | ID2 \
                        <= 255 and ID3 >= 0 | ID3 <= 255 and ID4 >= 0 \
                        | ID4 <= 255:

                    # Class E checking :

                        print('Class: E, Designation: Special')
                    else:
                        print('enter the number in range(0-255)')
                else:
                    print(' IP address must be in format: x.x.x.x/x')
            except:

                print('please enter right value ')
        else:

            print ('/x must be 8-16-24')


IP = Solution.IP_input()

if __name__ == '__main__':
    IP.check()
