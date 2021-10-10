
class Solution:


 def classTypeIP(ip):
    if ip[0] >= 0 and ip[0] <= 127:
        return "A"
    elif ip[0] >=128 and ip[0] <= 191:
        return "B"
    elif ip[0] >= 192 and ip[0] <= 223:
        return "C"
    elif ip[0] >= 224 and ip[0] <= 239:
        return "D"
    elif ip[0]>=  240 and ip[0] <=255:
        return "E"
    else:
        return "please enter ip true"


 def designationTypeIP(ip):
     if  (ip[0]== 10 and ip[1]>=0 and ip[1]<=255 and ip[2]>=0 and ip[2]<=255 and  ip[3]>=0 and ip[3]<=255) or (ip[0] == 169 and ip[1] >= 254 and ip[2] >= 0 and ip[2] <= 255 and ip[3] >= 0 and ip[3] <= 255) or (ip[0] == 172 and ip[1] >= 16 and ip[1] <= 31 and ip[2] >= 0 and ip[2] <= 255 and ip[3] >= 0 and ip[3] <= 255)  or(ip[0] == 192 and ip[1] == 168 and ip[2] >= 0 and ip[2] <= 255 and ip[3] >= 0 and ip[3] <= 255):
         return  "Private "

     elif (ip[0] >= 1 and ip[0] <= 127 and ip[1] == 0 and ip[2] == 0 and ip[3] == 0) or (ip[0] >= 128  and ip[0] <= 191 and ip[1] == 0 and ip[1] <= 255 and ip[2] == 0 and ip[3] == 0)   or ( ip[0] >= 192 and ip[0] <= 223 and ip[1] >= 0 and ip[1] <= 255 and ip[2] >= 0 and ip[2] <= 255 and ip[ 3] == 0)or (ip[0]== 224 and ip[0]<239 and ip[1]>=0 and ip[1]<=255 and ip[2]>=0 and ip[2]<=255 and  ip[3]>=0 and ip[3]<=255)or(ip[0]== 240 and ip[0]<255 and ip[1]>=0 and ip[1]<=255 and ip[2]>=0 and ip[2]<=255 and  ip[3]>=0 and ip[3]<=255):
         return "Pubilc"
     else:
         return "Special"



if __name__ == "__main__":
    ip = input('Enter ip address formate x.x.x.x/x :')
    ip_split = ip.split("/")
    ip = ip_split[0].split(".")
    ip = [int(i) for i in ip]

# object Solution
class_type_ip = Solution.classTypeIP(ip)
designation_type_ip=Solution.designationTypeIP(ip)
print(" Class: ",class_type_ip,"Designation:",designation_type_ip)




