class Solution:
    
    def __init__(self, ip=''):
        
        self.ip=ip
        self.sp_ip = self.ip.split('/')
        self.n_ip = self.sp_ip[0].split('.')
        self.mask = self.sp_ip[1]

        
    # =============== checking  the entered IP =============
        if "/" in self.ip and "." in self.ip:
            self.check_ip()
            self.check_submask()
            self.ip_class()
        else:
            print("you should inter  vaild ip with subnet mask like x.x.x.x/x")
        
   
        
    

    #======================================
    def check_ip(self):
        
        self.ip_len=len(self.n_ip)
        self.c_ip=[0,0,0,0]
        
        if  self.ip_len == 4:
            for i in range(self.ip_len):
                self.c_ip[i]=int(self.n_ip[i])
            for i in range(4):
                if self.c_ip [i] > 255 or self.c_ip[i] <0:
                        print ("the limit of each digit in ip is between 0 and 255 ")
                else:
                    return(self.c_ip)
        else:
            print("your IP should be only 4 digit")

    #======================check the subnet mask ==================
    def check_submask(self):
        self.sub_mask=int(self.mask)
        if self.sub_mask >24 or self.sub_mask <0 :
            print("this subnet mask is un vaild")
            
        else:
            pass


    
    #======================== IP des ========================

    def ip_des(self):
        test=self.check_ip()
        des=''
        if test[0] == 10 :
            des='privte'
        elif test[0] == 169 and test[1] == 254:
            des='privte'
        elif test[0] == 172 and test[1] >= 16 and  test[1] <= 31 and  test[2] <= 255 and test[3] <= 255:
            des='privte'
        elif test[0] == 192 and test[1] == 168 and test[2] <= 255 and test[3] <= 255:
            des='privte'
        elif test[0] == 127 :
            des='Special'
        else:
            des= 'Public'
        return(des)


    # ==================== ip class ==================== 
    def ip_class(self):
        test=self.check_ip()
        ip_class=''

        if test[0] >=1 and test[0] <=127:
            ip_class='A'
        elif test[0] >=128 and test[0] <=191 and test[1] <= 255:
            ip_class='B'
        elif test[0] >=192 and test[0] <=223 and test[1] <= 255 and test[2] <= 255:
            ip_class='C'
        elif test[0] >=224 and test[0] <=239 and test[1] <= 255 and test[2] <= 255 and test[3] <= 255:
            ip_class='D'
        elif test[0] >=240 and test[0] <=255 and test[1] <= 255 and test[2] <= 255 and test[3] <= 255:
            ip_class='E'
        
        return(ip_class)


#=================================

if __name__ == '__main__':
    in_ip=input("inter your ip:")
    p1=Solution(ip=in_ip)
    des=p1.ip_des()
    ip_cls=p1.ip_class()
    print("Designation: " + des)
    print("Class: "+ip_cls)