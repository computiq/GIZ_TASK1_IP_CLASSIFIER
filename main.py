#function to determine the class of an Ip address
def findClass(ip):
    if(ip[0] >= 0 and ip[0] <= 127):
        return "A"

    elif(ip[0] >=128 and ip[0] <= 191):
        return "B"

    elif(ip[0] >= 192 and ip[0] <= 223):
        return "C"

    elif(ip[0] >= 224 and ip[0] <= 239):
        return "D"

    else:
        return "E"
#function to determine the Designation
def findDesignation(ip):
    if(ip[0] == 10 or (ip[0] ==169 and ip[1]==254)or(ip[0] ==172 and(ip[1] >= 16 and ip[1] <= 31))or(ip[0] ==192 and ip[1]==168)):
        return "Private"
    elif(ip[0] == 127):
        return "Special"
    else:
        return "Puplic"

if __name__ == "__main__":

    ip = input('Enter an IP address (IP/MASK): ').split("/")
    ip = ip[0].split(".")  
    ip = [int(i) for i in ip]

#getting the network class and the designation
networkClass = findClass(ip)
Designation=findDesignation(ip)
print("Given IP address belongs to class", networkClass,"And it's designation is",Designation)
