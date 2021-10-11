

__author__ = 'laithzahid'
__version__ = "0.1"
class ipCalcMainClass(object):
    _maskList = {
        0:'0.0.0.0',
        1:'128.0.0.0',
        2:'192.0.0.0',
        3:'224.0.0.0',
        4:'240.0.0.0',
        5:'248.0.0.0',
        6:'252.0.0.0',
        7:'254.0.0.0',
        8:'255.0.0.0',
        9:'255.128.0.0',
        10:'255.192.0.0',
        11:'255.224.0.0',
        12:'255.240.0.0',
        13:'255.248.0.0',
        14:'255.252.0.0',
        15:'255.254.0.0',
        16:'255.255.0.0',
        17:'255.255.128.0',
        18:'255.255.192.0',
        19:'255.255.224.0',
        20:'255.255.240.0',
        21:'255.255.248.0',
        22:'255.255.252.0',
        23:'255.255.254.0',
        24:'255.255.255.0',
        25:'255.255.255.128',
        26:'255.255.255.192',
        27:'255.255.255.224',
        28:'255.255.255.240',
        29:'255.255.255.248',
        30:'255.255.255.252',
        31:'255.255.255.254',
        32:'255.255.255.255',
        }

def __init__(self, givenIP = ''):
        
        
        
        self.workingIP = [0, 0, 0, 0]
        self.workingMask = 0
        self.workingMaskInt = [0, 0, 0, 0]
      

       
        self.ipmask = givenIP.split('/')
        self.splitMask = self.ipmask[1]
       
        
        self.splitIP = self.ipmask[0].split('.')
       
        
        for index in range(len(self.splitIP)):
            self.workingIP[index] = int(self.splitIP[index])
            if self.workingIP[index] > 255: raise ValueError
            if index > 3: raise ValueError
      
        self.workingMask = int(self.splitMask)
        if self.workingMask > 32 or self.workingMask < 0: raise ValueError
        if not self.workingMask:
            test = self.getClass()
            if test == 'A':
                self.workingMask = 8
            if test == 'B':
                self.workingMask = 16
            if test == 'C':
                self.workingMask = 24
            if test == 'D':
                print('Multicast Address, using /24')
                self.workingMask = 24
            if test == 'E':
                print('Reserved Address, using /24')
                self.workingMask = 24
            del test
        self.workingMaskListSplit = (self._maskList.get(self.workingMask)).split('.')
        self.workingMaskDotted = self._maskList.get(self.workingMask)
        for index in range(len(self.workingMaskListSplit)):
            self.workingMaskInt[index] = int(self.workingMaskListSplit[index])

def representOutput(self, givenIP):
        print(givenIP)
        print('->')
        print('Address:   {:15}  -  {:35}'.format(self.ipIntCalc(), self.ipBinCalc()))
        print('Netmask:   {:15}  -  {:35}'.format(self.workingMaskDotted, self.maskBinCalc()))
        print('Wildcard:  {:15}  -  {:35}'.format(self.wildNetCalcInt(), self.wildNetCalcBin()))
        print('->')
        print('Network:   {:15}  -  {:35}'.format(self.netCalcInt(), self.netCalcBin()))
        print('Broadcast: {:15}  -  {:35}'.format(self.broadcastCalcInt(), self.broadcastCalcBin()))
        print('->')
        print('# of Hosts: {}  '.format(self.hostsCalc()[0], self.hostsCalc()[1]))
        
        temp = self.rangeCalc()
        print('1st Host:   {}'.format(temp[1]))
        print('Last Host:  {}'.format(temp[2]))
        print(temp[0])
        print('Class: {}, Designation: {}'.format(self.getClass(), self.getDesignation()))
        print('Finished')
        
def getClass(self):
        """
        This method calculates the class of the given IP address.
        1. It works on a dotted binary string IP address.
        2. Returns a string 'A', 'B', 'C', 'D' or 'E'
        """

        self.ipClass = ''
        test = self.ipBinCalc()
        if test[0] == '0':
            self.ipClass = 'A'

        if test[:2] == '10':
            self.ipClass = 'B'

        if test[:3] == '110':
            self.ipClass =  'C'

        if test[:4] == '1110':
            self.ipClass = 'D'

        if test[:4] == '1111':
            self.ipClass = 'E'

        return self.ipClass
def getDesignation(self):
        """
        1. Works on various variables to find the designation of the given IP
        2. Return the designation self.ipDesignation as a string
        """

        self.ipDesignation = ''
        test = self.ipBinCalc()
        if test[0] == '0' and self.workingMask == 0:
            self.ipDesignation = 'Internet Block'
        elif test[:2] == '10' and self.workingIP[0] == 172 and self.workingIP[1] == 16 and self.workingMask >= 24:
            self.ipDesignation = 'Internet Special Address'
        else:
            self.ipDesignation = 'Internet Private Address'

        return self.ipDesignation




if __name__ == '__main__':
    representOutput()
    getClass()
    getDesignation()
