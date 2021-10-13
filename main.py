import sys
class Solution:
      
    
    def parse_ip(self, ip):
        classname= ''
        designation =''
        if(ip[0] >= 0 and ip[0] <= 127):
          classname= "A"
          if (ip[1] >= 0 and ip[1] <= 255 and ip[2] >=0 and ip[2] <=255 and ip[3] >=0 and ip[3] <=255):
               designation='special'
          else:
               designation='private'
        
   
        elif(ip[0] >=128 and ip[0] <= 191):
             classname= "B"
             if (ip[1] >= 16 and ip[1] <= 31):
               designation='private'
        
        elif(ip[0] >= 192 and ip[0] <= 223):
             classname= "C"
             if (ip[1] >= 168 and ip[1] <= 255):
               designation='private'
        
        elif(ip[0] >= 224 and ip[0] <= 239):
             classname= "D"
             if (ip[1] >= 0 and ip[1] <= 255):
               designation='private'
        
        else:
             classname= "special"
        return classname, designation
        
    




if __name__ == '__main__':
    #ip = input('')
    #ip= input.split("/")
    #print(input)
    ip = "192.226.12.11"
    ip = ip.split(".")
    sample = Solution()
    
    ip = [int(i) for i in ip]

    #getting the network class
    networkcalss= sample.parse_ip(ip)
    print("ip class is: "+ networkcalss[0], "the IP address designation : "+ networkcalss[1])
    
   
        
