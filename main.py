import sys

class Solution:
    userip = input("")
    cutIp = userip.split("/")
    ip = cutIp[0].split(".")
    ip1 = int(ip[0])
    ip2 = int(ip[1])
    ip3 = int(ip[2])
    ip4 = int(ip[3])
    # to check ip range between 0 and 255
    for i in range(len(ip)):
        ipi = int(ip[i])
        if ipi < 0 or ipi > 255 :
            a = 1
        else :
            a = 0

        i = i + 1
    # to check input of users if not ip
    if "/" not in userip or len(ip) != 4 or a == 1 :
        print(" please enter a valid ip ")
    elif  a != 1 :
        #for class A
        if 0 <= ip1 <= 127 :
           className = "A"
           if ip1 == 0 or 127 <= ip1 < 128:
               desgination = "special"
           elif ip1 == 10 :
            desgination = "Private"
           else:
            desgination = "public"
        #for class B
        elif 128 < ip1 < 191 and ip2 <= 255 :
            className = "B"
            if ip1 == 172 and ip2 <= 16 and ip3 <= 255 :
              desgination = "private"
            else :
              desgination = "public"
            # for class C
        elif 192 <= ip1 < 224:
            className = "C"
            if ip1 == 192 and ip2 == 168:
                desgination = "private"
            else:
                desgination = "public"
        # for class D
        elif 224 <= ip1 < 240:
            className = "D"
            designation = "special"
        # for class E
        elif 240 <= ip1 < 256:
            className = "E"
            desgination = "special"

        print(f"class : {className} , designation : {desgination}")
if __name__ == '__main__':
    Solution()
