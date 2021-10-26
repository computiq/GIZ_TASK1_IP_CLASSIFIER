class Solution:
    
    def __init__(self, give_ip: str = None):
        self.chack_eror = False
        ip = give_ip.split('/')
        self.ip_num = ip[0].split('.')
        if len(ip) < 2 or len(self.ip_num) != 4:
            self.chack_eror = True

        else:
            self.chak_ip()
            print(f'class: {self.class_ip}  Designation: {self.Designation} ')    

            


    def chak_ip (self):
        self.class_ip = ''
        self.Designation = ''
        
        if int(self.ip_num[0]) == 127:
            print('kjkkk')
            self.class_ip = 'A'
            self.Designation = 'Special'

        elif int(self.ip_num[0]) == 10:
            self.class_ip = 'A'
            self.Designation= 'Private'

        
        elif 1 <= int(self.ip_num[0]) <= 127:
            self.class_ip = 'A'
            self.Designation= 'Public'
        elif 128 <= int(self.ip_num[0]) <= 191:
            self.class_ip = 'B'
            self.Designation= 'Public'
       
        elif int(self.ip_num[0]) == 172 and 16 <= int(self.ip_num[1]) <= 31:
            self.class_ip = 'B'
            self.Designation= 'Private'
       
        elif int(self.ip_num[0]) == 192 and int(self.ip_num[1]) == 168:
            self.class_ip = 'C'
            self.Designation= 'Private'
        
        elif int(self.ip_num[0]) == 192 or 173 <= int(self.ip_num[0]) < 224:
            self.class_ip = 'C'
            self.Designation= 'Public'
      
        elif 224 <= int(self.ip_num[0]) <= 255:
            self.class_ip = 'D or E'
            self.Designation = 'Special'

        


if __name__ == '__main__':
    i = input('Please enter an ip address: x.x.x.x/x\n')
    s = Solution(i)

if s.chack_eror == True:
    print('Please enter a valid address in this format: x.x.x.x/x')
