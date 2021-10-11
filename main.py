
from sys import argv

def split_theIP(IP):
  iplist=IP.split('/')
  IP_ORG=iplist[0]
  Ip_parts=IP_ORG.split('.')
  FIRST=int(Ip_parts[0])
  SECOND=int(Ip_parts[1])
  THIRD=int(Ip_parts[2])
  return [FIRST,SECOND,THIRD]

def check_if_the_ip_isValid(ip):
  
    if "/" not in ip:
        print (f"IP address1 {ip} is not valid")
        return False

    theIP= ip.split("/")
   

    ipAddress = theIP[0].split(".")

    if len(ipAddress) != 4:
        print(f"IP address2 {ip} is not valid")
        return False

    for part in ipAddress:
        if not isinstance(int(part), int):
          print(f"IP address3 {ip} is not valid")
          return False

        if int(part) < 0 or int(part) > 255:
          print(f"IP address4 {ip} is not valid")
          return False
 
def check_theClass_and_theDesignation (first,second,third):
     if first >= 1 and first <= 127:
            class_name = "A"
            if first == 10:
                designation = "Private"
            else:
                designation = "Public"

        
     elif first >= 128 and first <= 191:
            class_name = "B"
            if first == 172 and (second >=16 and second <=31):
                designation = "Private"
            else:
                designation = "Public"

     elif first >= 192 and second <= 223:
            class_name = "C"
            if first == 192 and second == 168:
                designation = "Private"
            else:
                designation = "Public"

     elif first >= 224 and first <= 239:
            class_name = "D"

     elif first >= 240 and first <= 250:
            class_name = "E"

     if class_name == "D" or class_name == "E" :
          designation = "Special"
          
     elif first == 127 and (third >= 1 and third <= 255):
            designation = "Special"

     print(f"Class: {class_name} Designation: {designation}")

def solution():
    the_ip_input=argv[1]
    if check_if_the_ip_isValid (the_ip_input):
      print("the IP is valid please wait for the result")
      first_Part,Second_Part,Third_Part=split_theIP(the_ip_input)
      check_theClass_and_theDesignation(first_Part,Second_Part,Third_Part)
    else :
        print("un valid input")

solution()
