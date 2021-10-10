#using this module made my life alot easier after trying to code the whole identification system myself (and failed)
from ipaddress import IPv4Address, IPv4Network

class Solution:
    def __init__(self, ip_str):
        self.ip = IPv4Address(ip_str)     
        self.designation = None
        self.class_name = None
        self.ip_classes = {
            #I didn't code the D & E classes here in the dictionary because the IPv4Network class takes the
            #start and the subnet of the range as arguments and D,E does not have a subnet that I know of.
            'A': IPv4Network(("1.0.0.0", "255.0.0.0")),
            'B': IPv4Network(("128.0.0.0", "255.255.0.0")),
            'C': IPv4Network(("192.0.0.0", "255.255.255.0")),
        }

        for ip_class_name in self.ip_classes:
            ip_class = self.ip_classes[ip_class_name]
            if (self.ip in ip_class):
                self.class_name = ip_class_name
                break
        #the is_multicast property can detects the D class since the subnet of D is multicasting
        if (self.ip.is_multicast):
            self.class_name = 'D'
            self.designation = "Special"

        #and is-reserved does the same as well
        elif (self.ip.is_reserved):
            self.class_name = 'E'
            self.designation = "Special"

        elif (self.ip.is_loopback):
            self.designation = "Special"
        #I assumed all special ips are A class from the example you gave.
            self.class_name = 'A'

        #once again, using a property to make life easier
        elif (self.ip.is_private):
            self.designation = "Private"

        else:
            self.designation = "Public"
        #and after two days of struggle, we print :D
    def print(self):
        res = "Output: Class: {}, Designation: {}".format(self.class_name, self.designation)
        print(res)

if __name__ == '__main__':
    Solution("127.0.0.1").print()
