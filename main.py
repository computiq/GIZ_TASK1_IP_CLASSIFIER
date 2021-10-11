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

    # def print_class_desgination(IP_class, designation):
    #     print(f"Class: {IP_class}")
    #     print(f"Designation: {designation}")

    # def realize_class_desgination(first_octet, second_octet, third_octet, fourth_octet):
    # class A
    if (first_octet >= 1) and (first_octet <= 127):
        IP_class = 'A'
        if (first_octet == 10):
            designation = "Private"
        elif (first_octet < 127):
            designation = "Public"
        elif (first_octet == 127) and (second_octet == 0) and (third_octet == 0) and (fourth_octet == 0):
            designation = "Public"

    # class B
    elif (first_octet >= 128) and (first_octet <= 191):
        IP_class = 'B'
        if (first_octet == 172) and (second_octet >= 16) and (second_octet <= 31):
            designation = "Private"
        elif (first_octet < 191):
            designation = "Public"
        elif (first_octet == 191) and (second_octet < 255):
            designation = "Public"
        elif (first_octet == 191) and (second_octet == 255) and (third_octet == 0) and (fourth_octet == 0):
            designation = "Public"
            
    # class C
    elif (first_octet >= 192) and (first_octet <= 223):
        IP_class = 'C'
        if (first_octet == 192) and (second_octet == 168):
            designation = "Private"
        elif (first_octet == 223) and (second_octet == 255) and (third_octet == 255) and (fourth_octet == 0):
            designation = "Public"
        elif (first_octet >= 192) and (first_octet <= 222):
            designation = "Public"

    # class C, Special
    elif (first_octet == 127) and (fourth_octet >= 1):
        designation = "Special"

    # class D
    elif (first_octet >= 224) and (first_octet <= 239):
        IP_class = 'D'
        designation = "Special"
    
    # class E
    elif (first_octet >= 240) and (first_octet <= 255):
        IP_class = 'E'
        designation = "Special"

    else:
        invalid()

        # return f"Class: {IP_class} Designation: {designation}"

    # realize_class_desgination(first_octet, second_octet, third_octet, fourth_octet)
    # print_class_desgination(IP_class, designation)

    # print(realize_class_desgination())

    print(f"Class: {IP_class} Designation: {designation}")

    if __name__ == '__main__':
        pass