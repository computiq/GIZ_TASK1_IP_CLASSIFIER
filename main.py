from typing import ClassVar


class Solution:
    pass


if __name__ == '__main__':
    pass
# method to validate the input
def isIPv4(s):
        try: return str(int(s)) == s and 0 <= int(s) <= 255
        except: return False
        
IP =input('Enter IP address to validate =>')
# if input valid perceed
if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
    # x= int(IP.split('.')[0])
    arrayOfNumbers= IP.split('.')
    firstPosition = int(arrayOfNumbers[0])
    secondPosition = int(arrayOfNumbers[1])

    classA = range(0,127)
    classB = range(128,191)
    classC = range(192,223)
    classD = range(224,239)
    classE = range(240,255)
    # print(classA)
    if(firstPosition in classA):
        if(firstPosition == 10):
            print('classA , Designation =>  private')
        else:
            print('classA , Designation => public')

    elif(firstPosition in classB):
        if(firstPosition == 172) and (secondPosition in range(16 , 31) ):
            print('classB , Designation =>  private')
        else:
            print('classB , Designation =>  public')

    elif(firstPosition in classC):
        if(firstPosition == 192) and ( secondPosition == 168 ):
            print('classC , Designation =>  private')
        else:
            print('classC , Designation =>  public')

    elif(firstPosition in classD):
        print('classD')

    elif(firstPosition in classE):
        print('classE')

    else:
        print('none')

# if input not valid 
else:
    print('Invalid IP address')

