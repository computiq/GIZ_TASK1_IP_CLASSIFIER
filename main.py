class Solution:
    
    #   getting theIP value from user 
    ipval = input("Enter the IP address to classify  :    ")
    
        
    # checking the format of the given IP address whether it's correct or not
    def isFormatCorrect(IP):
        
         
        IP= IP.strip() # removing spaces if there is any
        
        x=IP.split('/') # splitting the subnetting mask 
        if len(x)<2:
            return False
        
        
        a = x[0].split('.')
        
        if len(a) != 4:
            return False
        for x in a:
            if not x.isdigit():
                return False
            i = int(x)
            if i < 0 or i > 255:
                return False
        return True
    
  
    def ipclassification(IP):
        
        t = IP.split('.')
        a = [int(i) for i in t] # converting str elements in the list to int
        
        # Class A from 0 to 127.255.255.255
        if a[0]>= 0 and a[0]<128:
            
            classOfIp="A"
            
            if a[0]==10:        # Class A Private Range: 10.0.0.0 to 10.255.255.255
                Designation="Private"
            
            elif (a[0]==127 and a[3]>0) or (a[0]==127 and (a[1]>0 or a[2]>0)) :  # Special IP Addresses IP Range: 127.0.0.1 to 127.255.255.255 
                Designation="Special"
            else:
                Designation="Public"
            
            
            # Class B from 128 to 191.255.255.255
        elif a[0]>= 128 and a[0]<192:
            
            classOfIp="B"
            
            if (a[0]==169 and a[1]==254) or (a[0]==172 and a[1]>16 and a[1]<32): # Class B Private APIPA Range: 169.254.0.0 to 169.254.255.255  and Class B Private Range: 172.16.0.0 to 172.31.255.255
                Designation="Private"
            else:
                Designation="Public"    
            
            
            
            #  Class C from 192 to 223.255.255.255
        elif a[0]>= 192 and a[0]<224:
            
            classOfIp="C"
            
            if a[0]==192 and a[1]==168 : # Class C Private Range: 192.168.0.0 to 192.168.255.255
                Designation="Private"
            else:
                Designation="Public"     
            
            
             # Class D from 224 to 239.255.255.255
        elif a[0]>= 224 and a[0]<240:    
            classOfIp="D"
            Designation="Public"
            
        # Class E from 240 to 255.255.255.255
        else:
            classOfIp="E"
            Designation="Public"
        #end of classes
        return "Class: "+classOfIp+",  Designation: "+Designation
    
    if isFormatCorrect(ipval)==False:
        print("\n Please enter the IP in the correct format x.x.x.x/x")
    else:
        x=ipval.split('/') # splitting the subnetting mask 
        ipval=x[0]
        
        print("\n"+ipclassification(ipval))
    







if __name__ == '__main__':
    pass
