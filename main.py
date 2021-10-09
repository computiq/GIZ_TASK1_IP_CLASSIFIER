import sys

class Solution:
    # Assign attribute for Class & Designation of IP
    IpClass = ""
    Designation = ""

    def __init__(self, ip):
        """

        [1] Passing Ip4v From user to Class
        [2] Check if Ip is Valid with Subnet Mask & without spaces
        [3] Check if ip Between 1.0.0.0 & 255.255.255.255
        [4] Assign attributes for Ip Octal

        """
        self.Ip = ip
        self.Subnet = self.Ip[self.Ip.find("/") + 1::]
        if "/" in self.Ip and " " not in self.Ip:
            self.Ip = self.Ip[:self.Ip.find("/")].split(".")
            for i in self.Ip:
                if int(i) > 255 or int(self.Ip[0]) == 0:
                    raise ValueError
                else:
                    # Assign attributes for Ip Octal
                    self.FirstO = int(self.Ip[0])
                    self.Second0 = int(self.Ip[1])
                    self.ThirdO = int(self.Ip[2])
                    self.FourthO = int(self.Ip[3])
        else:
            raise ValueError

    def IpScanner(self):

        """

        Check Range Of Ip To Assign Class & Designation

        """
        # Check if Class is A
        if 0 <= self.FirstO <= 127:
            self.IpClass = "A"
            # Check Designation
            if self.FirstO == 10:
                self.Designation = "Private"
            elif self.FirstO == 127 and self.FourthO >= 1:
                self.Designation = "Special"
            else:
                self.Designation = "Public"

        # Check if Class is B
        elif 128 <= self.FirstO <= 191:
            self.IpClass = "B"
            # Check Designation
            if self.FirstO == 172 and (16 <= self.Second0 <= 32):
                self.Designation = "Private"
            else:
                self.Designation = "Public"

        # Check if Class is C
        elif 192 <= self.FirstO <= 223:
            self.IpClass = "C"
            # Check Designation
            if self.FirstO == 192 and self.Second0 == 168:
                self.Designation = "Private"
            else:
                self.Designation = "Public"

        # Check if Class is D
        elif 224 <= self.FirstO <= 239:
            self.IpClass = "D"
            self.Designation = "(There is no Designation for Class D)"

        # Check if Class is E
        elif 240 <= self.FirstO <= 255:
            self.IpClass = "E"
            self.Designation = "(There is no Designation for Class E)"

        else:
            raise ValueError

    def __str__(self):

        """

        [1] Run IpScanner() Method To Find Class & Designation
        [2] Assign Ip Attribute again to Print it
        [3] Return Result

        """
        self.IpScanner()
        self.Ip = f"{self.FirstO}.{self.Second0}.{self.ThirdO}.{self.FourthO}"
        return f"Ip : {self.Ip}\nSubnet Mask : {self.Subnet}\nClass : {self.IpClass}\nDesignation : {self.Designation}"

# --------------------------------------

def RunScript():
    # Get Ip From User
    Ip = input("Enter IPv4/MASK : ")

    # Handle Errors
    try:
        print(Solution(Ip))
    except(IndexError, ValueError):
        if Ip == "x":
            print("Thank You For Using My Program")
            sys.exit()
        print('\nPlease give a valid IPv4/MASK address in #.#.#.#/# format without Spaces' '\n'
              '\tfor example: 192.168.1.1/24, or 10.10.10.1/28'
              '\n\tRange of Valid IP : (1.0.0.0/# - 255.255.255.255/#)')
        RunScript()


if __name__ == '__main__':
    print("This Program Find the Class & Designation of IPv4 Address \n© Copyright to Ghaith Ahmed\n Enter x to Exit")
    RunScript()
