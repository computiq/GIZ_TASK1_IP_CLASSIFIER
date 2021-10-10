#A class=0-126               privat 10    ex- 10.0.0.0---10.255.255.255 
#B=128-191                   privat  B 172.16-31.
#c=192-223                   pravit  C=192.168.
#D=244-239
#E=240-254           



class Solution:
    

    def is_ipv4(ip):
        ip = ip.split('/')
        ip = ip[0].split('.')
        ip = [int(i) for i in ip]
   
        if(ip[0]>=1 and ip[0]<=126 and ip[0] !=10):
            print("Class: A, Designation: pulic")  
        elif(ip[0]==10 ):
            print("Class: A, Designation: privat")  
        elif(ip[0]==127 or ip[0]==0 ):
            print("Class: A, Designation: Special")
        elif(ip[0]>=128 and ip[0]<=191 and ip[1]!=16 and  ip[1]!=31 ):
            print("Class: B, Designation: pulic") 
        elif(ip[0]==172 and ip[1]>=16 and  ip[1]<=31):
            print("Class: B, Designation: privte")
        elif(ip[0]>=192 and ip[0]<=223 and ip[1]!=168):
            print("Class:C, Designation:pulic")  
        elif(ip[0]==192 and ip[1]==168):
            print("Class: C, Designation: privte")
        elif(ip[0]==192 and ip[1]==168):
            print("Class: C, Designation: privte")    
       
        elif(ip[0]>=224 and ip[0]<=239):
            print("Class: E, Designation: Special")  
        elif(ip[0]>=240 and ip[0]<=254):
            print("Class:D, Designation: Special")
        
        
         
    


if __name__ == '__main__':
    #test cod 
    ip='127.0.0.1/24'
    s=Solution
    s.is_ipv4(ip)

 