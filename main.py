import sys


class Solution:
    # variables to store results in
    ipClass = ""
    designation = ""

    # constructor
    def __init__(self, ipInput):

        self.ipInput = ipInput
        self.subNet = ipInput[ipInput.find("/") + 1::]

        # checking input format for spaces and subnet
        if "/" in ipInput and " " not in ipInput and self.subNet != "":
            self.ipInput = self.ipInput[:self.ipInput.find("/")].split(".")
            ipInput = ipInput[:ipInput.find("/")].split(".")

            # checking if the first octet equals zero

            if int(ipInput[0]) == 0:
                # input error
                print("wrong input format, please pay some attention!")

            # checking if any octet value is more than 255

            for octet in ipInput:
                if int(octet) > 255:
                    # input error
                    print("wrong input format, please pay some attention!")

            # storing each octet value
            self.firstOctet = int(ipInput[0])
            self.secondOctet = int(ipInput[1])
            self.thirdOctet = int(ipInput[2])
            self.fourthOctet = int(ipInput[3])

        else:
            # input error
            print("wrong input format, please pay some attention!")

    # my main function for calculating
    # conditions are concluded from https://www.meridianoutpost.com/resources/articles/IP-classes.php
    def ipCalcMain(self):

        # checking if the class is A (where first octet must be >= 0 and <= 127)
        if self.firstOctet >= 0 and self.firstOctet <= 127:
            self.ipClass = "A"

            # checking the designation

            if self.firstOctet == 10:
                self.designation = "Private"
            elif self.firstOctet == 127 and self.fourthOctet >= 1:
                self.designation = "Special"
            else:
                self.designation = "Public"

        # checking for class be
        elif self.firstOctet >= 128 and self.firstOctet <= 191:
            self.ipClass = "B"

            # checking the designation
            if self.firstOctet == 172 and self.secondOctet >= 16 and self.secondOctet <= 32:
                self.designation = "Private"
            else:
                self.designation = "Public"

        # checking for class c
        elif self.firstOctet >= 192 and self.firstOctet <= 223:
            self.ipClass = "C"

            # checking the designation
            if self.firstOctet == 192 and self.secondOctet == 168:
                self.designation = "Private"
            else:
                self.designation = "Public"

        # checking for class D
        elif self.firstOctet >= 224 and self.firstOctet <= 239:
            self.ipClass = "D"
            # since D class does not have any designation
            self.designation = "(There is no Designation for class D)"

        # checking for E class
        elif self.firstOctet >= 240 and self.firstOctet <= 255:
            self.ipClass = "E"

            # since D class does not have any designation
            self.designation = "(There is no Designation for class E)"

    def __str__(self):
        # hey Laith, this comment is for me in the future when I try to understand why I did I use __str__()
        # https://realpython.com/lessons/how-and-when-use-str/

        # executing my main function

        self.ipCalcMain()

        # formatting the output
        return f"Class : {self.ipClass}, Designation : {self.designation}"


if __name__ == '__main__':

    #running and printing
    print(Solution(sys.argv[1]))
