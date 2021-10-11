class soulution:
    def __init__(self,ip):
        self.ip = ip
        self.t = t = []
        self.t = str(self.ip).split('.')
        if (len(t) != 3):
            print ("Error in IP address")

    #this method to fine the class of IP address  
    def ipclass(self):
        if (0 <= int(self.t[0]) <= 127):
            return "A"
        elif (128 <= int(self.t[0]) <= 191):
             return "B"
        elif (192 <= int(self.t[0]) <= 223):
            return "C"
        elif (224 <= int(self.t[0]) <= 239):
            return "D"
        else:
            return "E"
    
    ##this method is used to find the designation of the Ip address, note the conditions need to review
    def designation(self):
        self.t[0] = int(self.t[0])
        self.t[1] = int(self.t[1])
        if (self.t[0] != 10 and 1 <= self.t[0] <= 127) or (self.t[0] != 172 and 128 <= self.t[0] <= 191) or (self.t[1] != 168 and 192 <= self.t[0] <= 223) or (224 <= self.t[0] <= 239):
            return "Public"
        elif (self.t[0] == 10) or (self.t[0] == 172 and 16 <= self.t[1] <= 31 ) or (self.t[0] == 192 and self.t[1] == 168) or (240 <= self.t[0] <= 255):
            return "Privit"
        else:
            return "Special"

if __name__ == '__main__':
    i = soulution('137.32.7.9/24')
    print(f'Class: {i.ipclass()}, Designation: {i.designation()}')
