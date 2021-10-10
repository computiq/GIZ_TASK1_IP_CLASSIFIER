import sys

def validate_ip_address(address):
    if "/" not in address:
        print ("IP address {} is not valid".format(address))
        return False

    parts = address.split("/")
    if not isinstance(int(parts[1]), int):
        print ("IP address {} is not valid".format(address))
        return False

    ipAddress = parts[0].split(".")

    if len(ipAddress) != 4:
        print("IP address {} is not valid".format(address))
        return False

    for part in ipAddress:
        if not isinstance(int(part), int):
            print("IP address {} is not valid".format(address))
            return False

        if int(part) < 0 or int(part) > 255:
            print("IP address {} is not valid".format(address))
            return False
 
    # IP Address is valid

    ipClass = ""
    ipDesignation = ""
    firstPart = int(ipAddress[0])
    secondPart = int(ipAddress[1])
    lastPart = int(ipAddress[3])

    if validate_range(firstPart, 0, 127): # Class A
        ipClass = "A"
        if validate_range(firstPart, 10,10):
            ipDesignation = "Private"
        elif validate_range(firstPart,127,127) and validate_range(lastPart,1,1):
            ipDesignation = "Special"
        else : ipDesignation = "Public"
    elif validate_range(firstPart, 128, 191): # Class B
        ipClass = "B"
        if validate_range(firstPart,172,172) and validate_range(secondPart,16,31):
            ipDesignation = "Private"
        else : ipDesignation = "Public"
    elif validate_range(firstPart, 192, 223): # Class C
        ipClass = "C"
        if validate_range(firstPart,192,192) and validate_range(secondPart,168,168):
            ipDesignation = "Private"
        else : ipDesignation = "Public"
    elif validate_range(firstPart, 224, 239): # Class D
        ipClass = "D"
        ipDesignation = "Public"
    elif validate_range(firstPart, 240, 255): # Class E
        ipClass = "E"
        ipDesignation = "Public"

    print(f"Class: {ipClass}, Designation: {ipDesignation}")
    return True 

def validate_range(part, min,max):
    if part >= min and part <= max:
        return True
    return False

if len(sys.argv) > 1 :
    validate_ip_address(sys.argv[1])
else : print("Please provide a valid ip address")