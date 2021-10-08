import sys
class Solution:
    def __init__(self, cidr):
        self.ip , self.mask = self.validate_and_calc_cidr(cidr)

    def validate_and_calc_cidr(self, cidr):

        ''' 

            This method used For
            1 - Validate IP if the ip address octet in range 0-255
                or the ip address is Valid or Not

            2 - Validate mask by check if mask number in range 0-32
                or valid mask

            3 - convert ip address to binary 
                Because ip address classes ( A , B , C , D and E ) depend on
                Binary digits
            
            4 - get ip class type to check if not mask presents from the user
                generate mask depends on the class type

        '''

        if not "/" in cidr:
            raise ValueError("IPV4/MASK does'nt match x.x.x.x/x format !\n")

        ip , mask  = cidr.split("/")
        self.ip_splited = ip.split(".")
        if len(self.ip_splited) > 4:
            raise ValueError("IPV4/MASK does'nt match x.x.x.x/x format !\n")

        for num in self.ip_splited:
            num = int(num)
            if num >255 or num <0:
                raise ValueError("IPV4 Octet not in Range 0-255\n")

        self.get_bin_ipv4()
        self.get_class_type()
        if not mask:
            if self.class_type == 'A':
                mask = 8

            elif self.class_type == 'B':
                mask = 16

            elif self.class_type == 'C':
                mask = 24

            else:
                mask = None
        
        elif int(mask) > 32 or int(mask) < 0:
            raise ValueError("MASK not in Range 0-32\n")
        
        return ip , int(mask)
    
    def get_bin_ipv4(self):
        
        '''

            this method used for
            Convert ip address to Binary

        '''

        self.bin_ipv4 = ".".join([format(int(x),'b').zfill(8) for x in self.ip_splited])
        return self.bin_ipv4

    def get_class_type(self):
                
        '''

            this method used for
            Calculate the class type of the ip address
            depends on the binary version from ip address

        '''

        if self.bin_ipv4[:1] == '0':
            self.class_type = 'A'

        elif self.bin_ipv4[:2] == '10':
            self.class_type = 'B'

        elif self.bin_ipv4[:3] == '110':
            self.class_type = 'C'

        elif self.bin_ipv4[:4] == '1110':
            self.class_type = 'D'

        else:
            self.class_type = 'E'
        
        return self.class_type

    def get_designation(self):
                        
        '''

            this method used for
            Calculate the designation type of the ip address (Private , Public , Special)
            depends on class_type and some cases
            https://www.meridianoutpost.com/resources/articles/IP-classes.php

        '''

        first_two_octet = ".".join(self.ip_splited[:2])
        if self.class_type == 'A':

            if self.ip_splited[0] == '10':
                self.designation = "Private"

            elif self.ip_splited[0] == '127' or self.ip_splited[0] == '0':
                self.designation = "Special"

            elif self.mask <= 8:
                self.designation = "Public"
        
        elif self.class_type == 'B':
            if first_two_octet == '172.16' or first_two_octet == '172.31':
                self.designation = "Private"
            
            elif self.mask <= 16:
                self.designation = "Public"
        
        elif self.class_type == 'C':
            if first_two_octet == '192.168' or first_two_octet == '192.168':
                self.designation = "Private"

            elif self.mask<=24:
                self.designation = "Public"

        else:
            self.designation = "Special"            

        return self.designation

    def print(self):
        
        '''

            this method used for
            print information about ip address

        '''

        print(f"Class: {self.class_type}, Designation: {self.get_designation()}")

if __name__ == '__main__':
        '''

            receive the ip address from the user
            then Reterive the wanted data
            in the Task


            References:

            https://www.meridianoutpost.com/resources/articles/IP-classes.php

            https://github.com/laith43d/ipcalculator-LZ-

            https://www.calculator.net/ip-subnet-calculator.html

        '''

        if len(sys.argv) == 1:
            cidr = input('to exit type : 0\nType IP address (IP/MASK) like x.x.x.x/x Format : ')
        else:
            cidr = sys.argv[1]
        while cidr != '0':
            try:
                ip_address = Solution(cidr)
                ip_address.print()
                cidr = '0'
            except Exception as e:
                if cidr == '0':
                    sys.exit()
                else:
                    print(e)
                    cidr = input('to exit type : 0\nType IP address (IP/MASK) like x.x.x.x/x Format : ')
                    
