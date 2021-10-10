import sys

class Solution:
    is_valid = ''

    ip_class = ''
    ip_designation = ''

    def __init__(self, ip_address = ''):
        self.ip_address = ip_address

    def exit_invalid(self):
        print('The ip address is invalid. Please try again')
        sys.exit()

    def classify_ip(self):
        # Check if valid
        if '/' in self.ip_address and '.' in self.ip_address:

            #check if the right side is a digit
            if not self.ip_address.split('/')[1].isdigit():
                self.exit_invalid()

            octetsString  = self.ip_address.split('/')[0]
            octetsArray = octetsString.split('.')
            if len(octetsArray) != 4:
                self.exit_invalid()

            for octet in octetsArray:
                if not octet.isdigit():
                    self.exit_invalid()

            for octet in octetsArray:
                if int(octet) < 0 or int(octet) > 255:
                    self.exit_invalid()
        else:
            self.exit_invalid()

         # Octets
        octet1 = int(octetsArray[0])
        octet2 = int(octetsArray[1])
        octet4 = int(octetsArray[3])

        #Class A 1.0.0.0 to 127.0.0.0
        if octet1 >=1 and octet1 <=127:
            self.ip_class = 'A'
            # Class A Private Range: 10.0.0.0 to 10.255.255.255
            if octet1 == 10:
                self.ip_designation = 'Private'
            # Special: 127.0.0.1 to 127.255.255.255
            elif octet1 == 127 and octet4 >=1:
                self.ip_designation = 'Special'
            else:
                self.ip_designation = 'Public'

        #Class B 128.0.0.0 to 191.255.0.0
        if octet1 >=128 and octet1 <=191:
            self.ip_class = 'B'
            #Class B Private Range: 172.16.0.0 to 172.31.255.255
            if octet1 == 172 and octet2 >= 16 and octet2 <= 31:
                self.ip_designation = 'Private'
            else:
                self.ip_designation = 'Public'

        #Class C
        if octet1 >=192 and octet1 <=223:
            self.ip_class = 'C'
            #Class C Private Range: 192.168.0.0 to 192.168.255.255
            if octet1 == 192 and octet2 == 168:
                self.ip_designation = 'Private'
            else:
                self.ip_designation = 'Public'

        #Class D 224.0.0.0 to 239.255.255.255
        if octet1 >=224 and octet1 <=239:
            self.ip_class = 'D'
            self.ip_designation = 'Special'

        #Class E 240.0.0.0 to 255.255.255.255
        if octet1 >=240 and octet1 <=255:
            self.ip_class = 'E'
            self.ip_designation = 'Special'

        print(f'Class: {self.ip_class}, Designation: {self.ip_designation}')
        

if __name__ == '__main__':
    pass
    
ip_address_input = input('Please enter a valid ip address in the format (x.x.x.x/x): ')
ip_address1 = Solution(ip_address_input)
ip_address1.classify_ip()

