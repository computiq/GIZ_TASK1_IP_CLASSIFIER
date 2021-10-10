class Solution:
    def __init__(self,ip) -> None:
        self.splitIP , self.mask = self.split_ip(ip)

        #getting both class and designation 
        self.find_class_designation()

    def split_ip(self,ip):
        if ip and "/" in ip and "." in ip:
            #checking the mask if its correct
            SplitIP ,mask = ip.split("/")
            mask = int(mask)
            if mask not in range(1,33): raise ValueError("subnet mask is wrong")

            #checking the ipv4 address
            SplitIP = SplitIP.split(".")
            if len(SplitIP) != 4 : raise ValueError("its not 4 octet numbers in the ip address")
            
            #checking each octet in the ipv4 address
            for x in range(len(SplitIP)):
                SplitIP[x] = int(SplitIP[x])
                if SplitIP[x] > 255 or SplitIP[x] < 0: raise ValueError("the ip octet numbers are wrong")

            return  SplitIP , mask
        else : raise ValueError("enter the right ip address")
    
    def find_class_designation(self):
        self.the_class = ""
        self.designation = ""

        #checking class and designation , we don't need subnet mask to find these 2 requirements 
        #and we don't need to get the Supernetting

        #class A
        if self.splitIP[0] in range(0,128):
            self.the_class = "A"
            if self.splitIP[0] == 10:
                self.designation = "Private"
            elif self.splitIP[0] == 127 or self.splitIP[0] == 0:
                self.designation = "Special"
            else: 
                self.designation = "Public"

        #class B
        elif self.splitIP[0] in range(128,192):
            self.the_class = "B"
            
            if self.splitIP[0] == 172 and self.splitIP[1] in range(16,32):
                self.designation = "Private"
            else:
                self.designation = "Public"

        #class C
        elif self.splitIP[0] in range (192,224):
            self.the_class = "C"
            
            if self.splitIP[0] == 192 and self.splitIP[1] == 168:
                self.designation = "Private"
            else:
                self.designation = "Public"
        
        #class D
        elif self.splitIP[0] in range (224,240):
            self.the_class = "D"
            self.designation = "Special"

        #class E
        else:
            self.the_class = "E"
            self.designation = "Special"


def main():
    try:
        ip = Solution(input("enter ip address in x.x.x.x/x format: "))
        print(f"Class: {ip.the_class}, Designation: {ip.designation}")
    except ValueError as err:
        print(err)
        main()

if __name__ == '__main__':
    main()