class Solution:
    ip=input("IP Address: ")
    splitIP =ip.split('/')[-2].split('.')
    listOfOctets=[int(i) for i in splitIP]

    #Check the IP address is valid or not
    if len(listOfOctets) == 4 and all(0 <= int(i) < 256 for i in listOfOctets ) :
        firstOctet,secondOctet=listOfOctets[0],listOfOctets[1]
        firstTwoOctets=[firstOctet,secondOctet]
          
    else:
        print(" Invalid -_- ")
        exit()
     #get Class of ip address   
    def getClassIp(octet):
        calsses={
        'A':tuple(range(0,128)),
        'B':tuple(range(128,192)),
        'C':tuple(range(192,224)),
        'D':tuple(range(224,240)),
        'E':tuple(range(240,256)),
            
        }
        for key,value in calsses.items():
            if  octet in value:
                return key
    #get range of second octet in class A of private and Special     
    def getRangeOfOctet1(oct1):
         for i in range(0,255):
              if i == oct1:
                return i
    #get range of second octet in class B of private           
    def getRangeOfOctet2(oct2):
         for i in range(15,37):
              if i == oct2:
                return i
    #Classes of IpV4 
    designation={
        'Private':{
            'A':[10,getRangeOfOctet1(secondOctet)],
            'B':[172,getRangeOfOctet2(secondOctet)],
            'c':[192,168]
            },
        'Public':{
            'A':tuple(range(0,127)),
            'B':tuple(range(128,192)),
            'C':tuple(range(192,224)),
        },
        'Special':{
            's':[127,getRangeOfOctet1(secondOctet)],
        },
}
    for key,value in designation.items():
        for id,values in value.items():
            if  firstTwoOctets == values:
                print('classs:',getClassIp(firstOctet),'Designation:',key)
                exit()
            elif firstOctet in values:
                print('classs:',getClassIp(firstOctet),'Designation:',key)
            



if __name__ == '__main__':
   pass
  