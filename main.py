class Solution:
    def __init__(self, ip):
        self.ip = ip
    # user input
    @classmethod
    def IP_input(self):
        ip = input('Enter ip ip adrress: ')
        return self(ip)


    def check(self):
        ip_adrress=self.ip
        # seperate prefix from network id
        seperate=[]
        for i in ip_adrress.split('/'):
            seperate.append(i)
        # check if prefix in the range or not
        if seperate[1]=='8' or seperate[1]=='16' or seperate[1]=='24':

            try:
            # seperate network id and convert it to integer
                check_ip=[]
                for j in seperate[0].split('.'):
                    check_ip.append(int(j))

 
                index=len(check_ip)
                # check if ip in format : x.x.x.x/x 
                if index == 4:
                    netID1=check_ip[0]
                    netID2=check_ip[1]
                    netID3=check_ip[2]
                    netID4=check_ip[3]

                    # =========== check class a =============
                    if netID1 >=1 | netID1 <=127 and netID2 ==0 and netID3 ==0 and netID4 ==0:
                        print('Class: A, Designation: Public')

                    elif netID1 ==10 and netID2 >=0 | netID2 <=255 and netID3 >=0 | netID3 <=255 and netID4 >=0 | netID4 <=255:
                        print('Class: A, Designation: Private')

                    elif netID1 ==127 and netID2 >=0 | netID2 <=255 and netID3 >=0 | netID3 <=255 and netID4 >=1 | netID4 <=255:
                        print('Class: A, Designation: Special')

                    # ============= check class b================
                    elif netID1 >=128 | netID1 <=191 and netID2 >=0 | netID2 <=255 and netID3 ==0 and netID4 ==0:
                        print('Class: B, Designation: Public')

                    elif netID1 ==172 and netID2 >=16 | netID2 <=31 and netID3 >=0 | netID3 <=255 and netID4 >=0 | netID4 <=255:
                        print('Class: B, Designation: Private')

                    # ============= check class c ================
                    elif netID1 >=192 | netID1 <=223 and netID2 >=0 | netID2 <=255 and netID3 >=0 | netID3 <=255 and netID4 ==0:
                        print('Class: C, Designation: Public')

                    elif netID1 ==192 and netID2 ==168 and netID3 >=0 | netID3 <=255 and netID4 >=0 | netID4 <=255:
                        print('Class: C, Designation: Private')

                    # ============= check class d ===============
                    elif netID1 >=224 | netID1 <=239 and netID2 >=0 | netID2 <=255 and netID3 >=0 | netID3 <=255 and netID4 >=0 | netID4 <=255:
                        print('Class: D, Designation: Special')

                    # ==============check class e ===============
                    elif netID1 >=240 | netID1 <=255 and netID2 >=0 | netID2 <=255 and netID3 >=0 | netID3 <=255 and netID4 >=0 | netID4 <=255:
                        print('Class: E, Designation: Special')
                    else:
                        print('number range between 0 and 255')
                else:
                    print('Please type IP address in format: x.x.x.x/x')
                    
            except:
                print('please enter numbers (-_-)')

            
        else:
            print('/x must be 8, 16 or 24')



        
IP = Solution.IP_input()


if __name__ == '__main__':
    IP.check()