class Solution(object):

    def __init__(self, givenIP):
        # Split user's input based on '/', to separate the IP from the mask
        ip_mask = givenIP.split('/')
        splitMask = ip_mask[1]
        # ---------------------------------

        # Split IP segments based on '.'
        splitIP = ip_mask[0].split('.')
        splitIP = [int(i) for i in splitIP]
        self.splitIP = splitIP
        self.splitMask = splitMask
        # ----------------------------------
        if len(splitMask) < 2 or int(splitMask) > 32 or len(splitIP) != 4:
            raise ValueError
    
    def classifyClasses(self):
        if(self.splitIP[0] == 10 and 0 <= self.splitIP[1] <= 255):
            print("class A, Designation: Private")

        elif(self.splitIP[0] == 172 and 16 <= self.splitIP[1] <= 31):
            print("class B, Designation: Private")

        elif(self.splitIP[0] == 192 and self.splitIP[1] == 168):
            print("class C, Designation: Private")

        elif(1 <= self.splitIP[0] <= 127):
            print("Class A, Designation: Public")    

        if(128 <= self.splitIP[0] <= 191):
            print("class B, Designation: Public")

        if(192 <= self.splitIP[0] <= 223):
            print("class C, Designation: Public")

        if(224 <= self.splitIP[0] <= 239):
            print("class D, Designation: Special")

        if(240 <= self.splitIP[0] <= 255):
            print("class E, Designation: Special")


if __name__ == '__main__':
    i = input('Please enter an ip address: x.x.x.x/x\n')
    try:
        solution = Solution(i)
        solution.classifyClasses()
    except ValueError:
        print('Please enter a valid address in this format: x.x.x.x/x')