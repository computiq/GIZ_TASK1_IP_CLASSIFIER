class Solution:

    IP_address = str(input("Enter the IP address: "))

    def invalid():
        print("No such IP address!")
        exit(1)

    #Splitting the IP address for 2 slices to extract the mask
    def mask_split(IP_address):
        return[IP_address.split("/")]

    two_slices = mask_split(IP_address)
    two_slices = two_slices[0] #without this line, this variable will be like [['127.0.0.1', '24']] ~~~~ with double square brackets, idk why

    if len(two_slices) != 2:
        invalid()    
    mask = two_slices[1]
    mask = int(mask)
    octets_together = two_slices[0]

    #Splitting the IP address (without the mask) for 4 slices to extract each octet
    def octet_split(octets_together):
        return[octets_together.split(".")]

    four_octets = octet_split(octets_together)
    four_octets = four_octets[0] #without this line, this variable will be like [['127', '0', '0', '1']] ~~~~ with double square brackets, idk why

    if len(four_octets) != 4:
        invalid()

    first_octet = four_octets[0]
    second_octet = four_octets[1]
    third_octet = four_octets[2]
    fourth_octet = four_octets[3]

    first_octet = int(first_octet)
    second_octet = int(second_octet)
    third_octet = int(third_octet)
    fourth_octet = int(fourth_octet)

    if int(first_octet) > 255 or int(second_octet) > 255 or int(third_octet) > 255 or int(fourth_octet) > 255:
        invalid()

    if (mask != 8) and (mask != 16) and (mask != 24):
        invalid()

    IP_class = ''
    designation = ""


    if (first_octet == 10):
        IP_class = 'A'
        designation = "Private"

    elif first_octet == 172 and 16 <= second_octet <= 31:
        IP_class = 'B'
        designation = "Private"

    elif first_octet == 192 and second_octet == 168:
        IP_class = 'C'
        designation = "Private"
    
    # idk how to know if it's Class: C, Desgintion: Special
    # elif first_octet == 127 and fourth_octet >= 1:
    #     IP_class = 'C'
    #     designation = "Special"
    
    elif 224 <= first_octet <= 239:
        IP_class = 'D'
        designation = "Special"
    
    elif 240 <= first_octet <= 255:
        IP_class = 'E'
        designation = "Special"

    elif 1 <= first_octet <= 127:
        IP_class = 'A'
        designation = "Public"

    elif 128 <= first_octet <= 191:
        IP_class = 'B'
        designation = "Public"
    
    elif 192 <= first_octet <= 223:
        IP_class = 'C'
        designation = "Public"

    else:
        invalid()

    print(f"Class: {IP_class}, Designation: {designation}")

    if __name__ == '__main__':
        pass