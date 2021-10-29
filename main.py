class ipaddress:

    def Class(ip):
        if(ip[0] >= 0 and ip[0] <= 127):
            return "A"
        elif(ip[0] >= 128 and ip[0] <= 191):
            return "B"
        elif(ip[0] >= 192 and ip[0] <= 223):
            return "C"
        elif(ip[0] >= 224 and ip[0] <= 239):
            return "D"
        else:
            return "E"

    def Designation(ip):
        if(ip[0] == 10 or (ip[0] == 169 and ip[1] == 254) or (ip[0] == 172 and (ip[1] >= 16 and ip[1] <= 31)) or (ip[0] == 192 and ip[1] == 168)):
            return "Private"
        elif(ip[0] == 127):
            return "Special"
        else:
            return "Puplic"


if __name__ == "__main__":
    ip = input('check ip like :x.x.x.x/x ')
    ip_slash = ip.split("/")
    ip = ip_slash[0].split(".")
    ip = [int(i) for i in ip]


Class = ipaddress.Class(ip)
Designation = ipaddress.Designation(ip)
print("The class is: ", Class)
print("The Designation is: ", Designation)
