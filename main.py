import sys

# check input
if len(sys.argv) != 2:
    print("invalid entry, try again")
    sys.exit()
else: 
    ip = sys.argv[1]


    fullIP = ip.split("/")
    ipSplited = fullIP[0].split(".")
    # print(ipSplited)    =>    output = ['127', '0', '0', '1'] => type str

    port = fullIP[1]
    # print(port)         =>    output = 24

    ipAdress = [int(i) for i in ipSplited]
    # print(ipAdress)     =>    output = [127, 0, 0, 1] => type int


class Solution:
    
    def __ipProces__(self, ipAdress):
        
        self.ip = ipAdress

        # The first octet of class A ( 0 - 127 )
        if (self.ip[0] < 127 or self.ip[0] == 127 and self.ip[3] > 0):
            
            if (self.ip[0] == 10):
                print("Class: A, Designation: Private")
            elif (self.ip[0] == 127 and self.ip[3] > 0):
                print("Class: A, Designation: special")
            else:
                print("Class: A, Designation: Public")


        # The first octet of class B ( 128 - 191 )
        elif (self.ip[0] > 127 and self.ip[0] <= 191):
            
            if (self.ip[0] == 172 and self.ip[1] >= 16 or self.ip[0] <= 31):
                print("Class: B, Designation: Private")
            else:
                print("Class: B, Designation: Public")


        # The first octet of class C ( 192 - 223 )
        elif (self.ip[0] > 191 and self.ip[0] <= 223):

            if (self.ip[0] == 192 and self.ip[1] == 168):
                print("Class: C, Designation: Private")
            else:
                print("Class: C, Designation: Public")


        # The first octet of class D ( 224 - 239 )
        elif (self.ip[0] > 223 and self.ip[0] <= 239):
            print("Class: D")


        # The first octet of class E ( 240 - 255 )    
        else:
            print("Class: E")


Solution().__ipProces__(ipAdress)



if __name__ == '__main__':
    pass