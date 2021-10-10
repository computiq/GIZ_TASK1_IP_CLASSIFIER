import sys

class Solution(object):
    def __init__(self, givenIP):

        # Split IP address and convert into list of integer
        self.splitIP = [n for n in givenIP.split('/') ] 
        self.addressIP = list(map(int, self.splitIP[0].split("."))) 

        """
        IP Validation, Make sure the IP that:
        1. In correct format
        2. Within the range 
        """
        if len(self.addressIP) != 4 or len(self.splitIP) != 2 :
            print("\nInvalid format, Please enter your IP in format x.x.x.x/x")

        for index in self.addressIP:
            if index < 0 or index > 255: raise ValueError
        if int(self.splitIP[1]) > 32 or int(self.splitIP[1]) < 0: raise ValueError


    """
    Get the class of IP Function,
    this fuction should return one class(A, B, C, D or E) based on the IP range
    """
    def getClass(self):

        self.ipClass = ''

        if 1 <= self.addressIP[0]  <= 127:
	        self.ipClass = 'A'

        elif 128 <= self.addressIP[0]  <= 191:
	        self.ipClass = 'B'

        elif 192 <= self.addressIP[0]  <= 223:
	        self.ipClass = 'C'

        elif 224 <= self.addressIP[0]  <= 239:
	        self.ipClass = 'D'

        elif 240 <= self.addressIP[0]  <= 255:
	        self.ipClass = 'E'

        return self.ipClass

    """
    Get the Designatio of IP Function,
    this fuction should return (Special, Private or Public) based on the IP range
    """
    def getDesignation(self):
        self.ipDesignation = ''

        if self.addressIP[0] == 127 and 1 <= self.addressIP[3] <= 255:
            self.ipDesignation = "Special"

        elif self.addressIP[0] == 10 and 0 <= self.addressIP[1] <= 255:
            self.ipDesignation = "Private"

        elif self.addressIP[0] == 169 and self.addressIP[1] == 254:
            self.ipDesignation = "Private"

        elif self.addressIP[0] == 172 and 16 <= self.addressIP[1] <= 31:
            self.ipDesignation = "Private"

        elif self.addressIP[0] == 192 and self.addressIP[1] == 168:
            self.ipDesignation = "Private"

        else:
	        self.ipDesignation = "Public"

        return self.ipDesignation
        
    
    """
    Represent Output Function,
    to show the final output
    """
    def representOutput(self, givenIP):
        print('Class: {}, Designation: {}'.format(self.getClass(), self.getDesignation()))

                


"""
Main Function,
to excute the program
"""
def main():
    if len(sys.argv) > 1:
        givenIP = sys.argv[1]
        try:
            ipAddress = Solution(givenIP)
            ipAddress.representOutput(givenIP)

        except (IndexError, ValueError):
            print("Your IP is invalid format, Please try again!")

if __name__ == '__main__':
    main()
