class Solution:
 def Input_ip():
        ip = input('Enter your ip address: ')
        return ip
    

 def findClass(ip):
    if(ip[0] >= 0 and ip[0] <= 127):
        return "A"
    elif(ip[0] >=128 and ip[0] <= 191):
        return "B"
    elif(ip[0] >= 192 and ip[0] <= 223):
        return "C"
    elif(ip[0] >= 224 and ip[0] <= 239):
        return "D"
    else:
        return "E"


if __name__ == "__main__":
    ip = input('Enter your ip address: ')
    ip = ip.split(".")
    ip = [int(i) for i in ip]

#find class
Class = Solution.findClass(ip)
print(" Class: ",Class,",")