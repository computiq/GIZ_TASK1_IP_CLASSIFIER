import re

class Solution:
    Designation = ''
    ipClass = ''

    def get_class_designation(self):
        
        while True:
            ip = input("enter IP address in xxx.xxx.xxx.xxx/x format OR enter exit : ")
            if re.match('^(([01]?\d{1,2}|2[0-4]\d|25[0-5])\.){3}([01]?\d{1,2}|2[0-4]\d|25[0-5])(/([12]?[0-9]|3[01]))$', ip):
                break
            elif ip == 'exit':
                print('bye bye')
                exit()
            else:
                print("dude! follow the format")

        first_octet, *otherOctets = list(map(int, ip[:ip.index("/")].split('.')))

        if 1 <= first_octet <= 127:
            self.ipClass = 'A'
            if first_octet == 10 and all(0 <= octets <= 255 for octets in otherOctets):
                self.Designation = 'Private'
            elif all(octets == 0 for octets in otherOctets):
                self.Designation = 'Public'
            else:
                self.Designation = 'Special'

        elif 128 <= first_octet <= 191:
            self.ipClass = 'B'
            self.Designation = 'Public'
            sec_octet = otherOctets[0]
            if first_octet == 172 and 16 <= sec_octet <= 31 and all(0 <= octets <= 255 for octets in otherOctets[1:3]):
                self.Designation = 'Private'

        elif 192 <= first_octet <= 223:
            self.ipClass = 'C'
            self.Designation = 'Public'
            sec_octet = otherOctets[0]
            if first_octet == 192 and sec_octet == 168 and all(0 <= octets <= 255 for octets in otherOctets[1:3]):
                self.Designation = 'Private'

        elif 224 <= first_octet <= 239:
            self.ipClass, self.Designation = 'D', 'Special'

        elif 240 <= first_octet <= 255:
            self.ipClass, self.Designation = 'E', 'Special'

        else:
            print('Try another ip ')

        print(f'Output: Class: {self.ipClass}, Designation: {self.Designation}')

        
if __name__ == '__main__':
    solution = Solution()
    solution.get_class_designation()
