
class Solution:
    def __init__(self, ip_address):
        self.ip_address = ip_address
    
    # This function classify the IP address which is passed as an instance attribute
    def classify_ip(self):
        ip = self.ip_address.split('/')
        address = ip[0].split('.')

        _class = ''
        designation = ''

        i = int(address[0])
        _int = int(''.join(address))

        '''
            At first we check its class, and then we check the designation based on the class
        '''

        if (i >= 0 and i < 127):
            _class = 'A'
            if (i == 10):
                designation = 'Private'
            else:
                designation = 'Public'


        elif (i >= 128 and i < 192):
            _class = 'B'
            if (i == 172 and int(address[1]) >= 16 and int(address[1]) <= 31):
                designation = 'Private'
            else:
                designation = 'Public'


        elif ((i >= 192 and i < 224) or i == 127):
            _class = 'C'
            if (i == 192 and int(address[1]) == 168):
                designation = 'Private'
            elif (_int >= 127001 and _int <= 127255255):
                designation = 'Special'
            else:
                designation = 'Public'


        elif (i >= 224 and i < 240):
            _class = 'D'
            designation = 'Special'


        else:
            _class = 'E'
            designation = 'Special'


        return f"Class: {_class}, Designation: {designation}"




if __name__ == '__main__':
    s = Solution('192.168.1.1/24')
    print(s.classify_ip())
