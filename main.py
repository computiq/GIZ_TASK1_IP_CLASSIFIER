import sys
class Solution:

   # Verify that the IP is correct

    def ValidatingIP(self,ip):
        ip = ip.split("/")
        ip_without_mask = ip[0].split(".")
        valid=True
        # print("len",len(ip_without_mask))
        if len(ip_without_mask) != 4 or ip_without_mask[0] == '0' :
            valid = False
            return valid
        else:
            for i in range(4):
                if ip_without_mask[i] >'255':
                    valid = False
                    break
            return valid
              
         

    # To Get The IP Class Name 

    def ip_class(self,ip):
        ip = ip.split(".")
        ip=int(ip[0])

        if   ip > 0  and  ip < 127:
            return "Class: A "
        elif (ip > 126 and  ip < 192 )  :
            return "Class: B "
        elif (ip > 191 and  ip < 224 )  :
            return "Class: C "
        elif (ip > 223 and  ip < 248 )  :
            return "Class: D "
        elif (ip > 247 and  ip < 255 )  :
            return "Class: E "

        
    # To Get The IP Designation   
       
    def ip_Designation(self,ip):
        ip_s = ip.split(".")
        ip2=int(ip[1]) 
        ip_s=int(ip_s[0]) 
        

        #    private Designation

        if ip_s == 10  or (ip_s == 192 and ip2 > 167 ) or (ip_s == 172 and (ip2 > 16 and ip2 < 32) ):
            return " Designation: private IP"

         #    public Designation
        elif ip_s > 0  and  ip_s < 224:
            return " Designation: public IP"
        
        #    Special Designation

        else :
            return " Designation: Special"
   
    # checking For The NetMask 

    def NetMask(self,ip,classType):
        mask = ip.split("/")
        mask = mask[1]

        if classType == 'A' and  mask == 8 :
            return True
        elif classType == 'B' and  mask == 16 :
            return True
        elif classType == 'C' and  mask == 24 :
            return True
        elif classType == 'D' and  mask == 24 :
            return True
        elif classType == 'E' and  mask == 24 :
            return True
        else : return False
        
    


if __name__ == '__main__':
    
    ip_address= Solution()
    ip_entered= input("Enter The IP : ")
    ip_entered = str(ip_entered)
    # ip_entered='11.11.11.11/22'
    valid_NetMask =ip_address.NetMask(ip_entered,ip_address.ip_class(ip_entered))  
    valid_IP = ip_address.ip_class(ip_entered)
    if( ip_address.ip_class(ip_entered ) ): 
        print( ip_address.ip_class(ip_entered) ) 
        print(   ip_address.ip_Designation(ip_entered) )
 
    else: print("Invalid IP !!!")
    sys.exit()
 
      
 
    


