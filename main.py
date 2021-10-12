class Solution():

    def __init__(self, givenIP):
        # Split user's input based on '/', to separate the IP from the mask
        ip_mask = givenIP.split('/')
        splitMask = ip_mask[1]
        # ---------------------------------

        # Split IP segments based on '.'
        splitIP = ip_mask[0].split('.')
        splitIP = [int(i) for i in splitIP]

        # print(splitIP) o/p is a list [x,x,x,x]

        # ----------------------------------
        if len(splitMask) < 2 or not(0 <= int(splitMask) <= 32) or len(splitIP) != 4:
            raise ValueError

        self.splitIP = splitIP
        self.splitMask = splitMask

    
    def classifyClasses(self):
        if(1 <= self.splitIP[0] <= 127):
            print("Class A")    

        if(128 <= self.splitIP[0] <= 191):
            print("class B")

        if(192 <= self.splitIP[0] <= 223):
            print("class C")

        if(224 <= self.splitIP[0] <= 239):
            print("class D")

        if(240 <= self.splitIP[0] <= 255):
            print("class E")

    def classifyDesignation(self):
        if(self.splitIP[0] == 10 and 0 <= self.splitIP[1] <= 255):
            print("Designation: Private")

        elif(self.splitIP[0] == 172 and 16 <= self.splitIP[1] <= 31):
            print("Designation: Private")

        elif(self.splitIP[0] == 192 and self.splitIP[1] == 168):
            print(" Designation: Private")

        elif(224 <= self.splitIP[0] <=255):
            print(" Designation: Special")

        else:
            print("Designation: Public")

if __name__ == '__main__':
    i = input('Please enter an ip address: x.x.x.x/x\n')
    try:
        solution = Solution(i)
        solution.classifyClasses()
        solution.classifyDesignation()
    except ValueError:
        print('Please enter a valid address in this format: x.x.x.x/x')
