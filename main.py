import re

class Solution:
    pass
      
    
    def parse_ip(self):
          classname= ''
          designation =''

          while True:
               
               ip = input('input ip addess : ')
               
               
               if re.match('^(([01]?\d{1,2}|2[0-4]\d|25[0-5])\.){3}([01]?\d{1,2}|2[0-4]\d|25[0-5])(/([12]?[0-9]|3[01]))$',ip):
                   break
               else:

                   print('inset other format')
          
          
          firstoct, *remainoct =  list(map(int, ip[:ip.index("/")].split('.')))

          if(firstoct >= 0 and firstoct <= 127):
               classname= "A"
               if firstoct ==10 and all(0 <= i <= 255 for i in remainoct):
                    designation='private'
                 
               else:
                    designation='special'
          

          elif(firstoct >=128 and firstoct <= 191):
               classname= "B"
               #designation='public'
               secondoct = remainoct[0]
               if firstoct==172 and (secondoct >= 16 and secondoct <= 31) and all(0 <= i <= 255 for i in remainoct[1:3]):
                    designation='private'
               else:
                    designation='public'
          
          elif(firstoct >= 192 and firstoct <= 223):
               classname= "C"
               secondoct = remainoct[0]
               if firstoct == 192 and secondoct== 168 and all(0 <= i <= 255 for i in remainoct[1:3]):
                    designation='private'
               else:
                    designation='public'
          
          elif(firstoct >= 224 and firstoct <= 239):
               classname= "D"
               designation='special'
          
          else:
               print("not valid ip")

          print("ip class is  "+ classname + " and desifnation :" + designation)
          





if __name__ == '__main__':
     pass
     
     sample= Solution()
     sample.parse_ip()
    
    
        
    
    
   
        
