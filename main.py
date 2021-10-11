from ipaddress import IPv4Address, ip_address 
import ipaddress
class Solution:
    
    def fragmentip(self,ip) -> None:
        self.ip=ip
        
        ip=str(ip)
        cl=""
        des="" #des
        
        co=0 #count to calc len of ip
        br=0 #var to break the loop 
        for i in ip:
            if i=="." :
                br=1
                for d in range(co,len(ip)):
                    if(ip[d]=="."):
                       continue
                    elif (ip[d]=="/") :
                        break
                    else:
                        des+=ip[d]
            elif br==1:
               break           
            else :
               co+=1
               cl+=i
        return cl
    def find(self,p):
        orginal=p
        obj=Solution()
        self.p=p
        ip=obj.fragmentip(p)
        ipclass=int(ip)
       
        ipdes=orginal
        #class A
        if (ipclass>=1) and (ipclass<=127):
            if(ipdes>=ip_address("10.0.0.0"))and (ipdes<=ip_address("10.255.255.255")):
                 print("class A , designated private")
            elif(ipdes>=ip_address("1.0.0.0")and (ipdes<=ip_address("127.0.0.0"))):
                print("class A , designated public")  
          
            else:
                 print("class A , designated Special ")
        #class B
        elif (ipclass>=128) and (ipclass<=191):
            if(ipdes>=ip_address("172.16.0.0"))and (ipdes<=ip_address("172.31.255.255")):
                 print("class B , designated private")
                 print(ipdes)
            elif(ipdes>=ip_address("128.0.0.0"))and (ipdes<=ip_address("191.255.0.0")):
                print("class B , designated public")  
          
            else:
                 print("class B , designated Special ")
        #class C
        elif (ipclass>=192) and (ipclass<=223):
            
            if(ipdes>=ip_address("192.168.0.0"))and (ipdes<=ip_address("192.168.255.255")):
                 print("class C , designated private")
            elif ipdes>=ip_address("192.0.0.0")and ipdes<=ip_address("223.255.255.0"):
                print("class C , designated public") 
                
            else:
                 print("class C , designated Special ")         
   
 



if __name__ == '__main__':
    obj=Solution()
    ip=ip_address("192.168.0.0")
    obj.find(ip)
