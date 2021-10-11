class Solution:
        def __init__(self, ip):
                self.ip = ip
        def handleIp(self):
                try:   
                    
        # taking the input as a string then convert it to a number
        
                        import sys
                        splitIp=self.ip.split("/")
                        mask = splitIp[1]
                        ipAd = splitIp[0].split(".")
                        seg1=(int(ipAd[0]))
                        seg2=(int(ipAd[1]))
                        seg3=(int(ipAd[2]))
                        seg4=(int(ipAd[3]))
                        seg5=(int(mask))
                        
        # validation test cases
        
                        if seg1 < 1 or seg1 > 255:
                                print('Unvalid IP Adress')
                                sys.exit()
                        elif seg2 < 0 or seg2 > 255 :
                                print('Unvalid IP Adress')
                                sys.exit()
                        elif seg3 < 0 or seg3 > 255 :
                                print('Unvalid IP Adress')
                                sys.exit()
                        elif seg4 < 0 or seg4 > 255 :
                                print('Unvalid IP Adress')
                                sys.exit()
                        elif seg5 != 8 and seg5 != 16 and seg5 != 24 :
                                print('Unvalid Subnetmask')
                                sys.exit()  
                        
                        
        # IP Class
                        if seg1 > 0 and seg1 < 128 :
                                print('Class: A')
                        elif seg1 > 127 and seg1 < 192 :
                                print('Class: B')
                        elif seg1 > 191 and seg1 < 224 :
                                print('Class: C')
                        elif seg1 > 223 and seg1 < 240 :
                                print('Class: D')
                        elif seg1 > 239 and seg1 < 256 :
                                print('Class: E')
        
                        
        # IP Designation
        
                        if seg1 == 10 or seg1 == 172 and seg2 > 15 and seg2 < 30 or seg1 == 192 and seg2 == 168 : 
                                print('Designation: Private')
                        elif seg1 == 127 and seg4 > 0:
                                print('Designation: Special')
                        else: print('Designation: Public') 
                except:
                    sys.exit()


if __name__ == '__main__':
        import sys
        ipInput = input("Enter an IP Adress \nor Press 'X' to Exit")
        if ipInput == 'x' or ipInput == 'X':
            sys.exit()
        sol = Solution(ipInput)
        sol.handleIp()