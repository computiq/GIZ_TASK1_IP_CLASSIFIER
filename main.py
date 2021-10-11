class Solution:
    def __init__(self, ipaddress):
        self.ip = ipaddress

    @classmethod
    def IP_input(self):
        ip = input('Please insert Your IP : ')
        return self(ip)

    def check(self):
        ip_adrress = self.ip
        seperate = []
        for i in ip_adrress.split('/'):
            seperate.append(i)
        if seperate[1] == '8' or seperate[1] == '16' or seperate[1] == '24':

            try:
                check_ip = []
                for j in seperate[0].split('.'):
                    check_ip.append(int(j))

                index = len(check_ip)

                if index == 4:
                    netID1 = check_ip[0]
                    netID2 = check_ip[1]
                    netID3 = check_ip[2]
                    netID4 = check_ip[3]

                    # **************** Class A ****************#
                    if netID1 >= 1 | netID1 <= 127 and netID2 == 0 and netID3 == 0 and netID4 == 0:
                        print('Class: A, Designation: Public')

                    elif netID1 == 10 and netID2 >= 0 | netID2 <= 255 and netID3 >= 0 | netID3 <= 255 and netID4 >= 0 | netID4 <= 255:
                        print('Class: A, Designation: Private')

                    elif netID1 == 127 and netID2 >= 0 | netID2 <= 255 and netID3 >= 0 | netID3 <= 255 and netID4 >= 1 | netID4 <= 255:
                        print('Class: A, Designation: Special')

                    # **************** Class B ****************#
                    elif netID1 >= 128 | netID1 <= 191 and netID2 >= 0 | netID2 <= 255 and netID3 == 0 and netID4 == 0:
                        print('Class: B, Designation: Public')

                    elif netID1 == 172 and netID2 >= 16 | netID2 <= 31 and netID3 >= 0 | netID3 <= 255 and netID4 >= 0 | netID4 <= 255:
                        print('Class: B, Designation: Private')

                    # **************** Class B ****************#
                    elif netID1 >= 192 | netID1 <= 223 and netID2 >= 0 | netID2 <= 255 and netID3 >= 0 | netID3 <= 255 and netID4 == 0:
                        print('Class: C, Designation: Public')

                    elif netID1 == 192 and netID2 == 168 and netID3 >= 0 | netID3 <= 255 and netID4 >= 0 | netID4 <= 255:
                        print('Class: C, Designation: Private')

                    # **************** Class B ****************#
                    elif netID1 >= 224 | netID1 <= 239 and netID2 >= 0 | netID2 <= 255 and netID3 >= 0 | netID3 <= 255 and netID4 >= 0 | netID4 <= 255:
                        print('Class: D, Designation: Special')

                    # **************** Class E ****************#
                    elif netID1 >= 240 | netID1 <= 255 and netID2 >= 0 | netID2 <= 255 and netID3 >= 0 | netID3 <= 255 and netID4 >= 0 | netID4 <= 255:
                        print('Class: E, Designation: Special')
                    else:
                        print('number range between 0 and 255')
                else:
                    print('Please type IP address in format: x.x.x.x/x')

            except:
                print('IP address should by numbers *_\'')

        else:
            print('/x must be 8, 16 or 24')


IP = Solution.IP_input()


if __name__ == '__main__':
    IP.check()
