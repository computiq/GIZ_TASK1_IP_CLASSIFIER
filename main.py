import sys
# Print the Class and Designation of IP Address
# Classes: A, B, C, D, E
# Designation: Private, Public, Special
# Run: python main.py 192.168.1.1/24
# Output: Class: C, Designation: Private

class Solution:
    def __init__(self) -> None:
        # get the input IP Addres and Information we Need
        ip = sys.argv[1]
        ip_range = ip.split(".")
        address_range = int(ip_range[0])
        second_range = int(ip_range[1])
        last_range = int((ip_range[-1].split("/")[0]))
        # Specify defult name for Class name and Designation
        class_name = "Invalid"
        designation = "Invalid"

        # IP Class A:	1 to 126
        # Private IP: 10.0.0.0 — 10.255.255.255
        if address_range >= 1 and address_range <= 127:
            class_name = "A"
            if address_range == 10:
                designation = "Private"
            else:
                designation = "Public"

        # IP Class B:	128 to 191
        # Private IP: 172.16.0.0 — 172.31.255.255
        elif address_range >= 128 and address_range <= 191:
            class_name = "B"
            if address_range == 172 and (second_range >=16 and second_range <=31):
                designation = "Private"
            else:
                designation = "Public"

        # IP Class C:	192 to 223
        # Private IP: 192.168.0.0 — 192.168.255.255
        elif address_range >= 192 and second_range <= 223:
            class_name = "C"
            if address_range == 192 and second_range == 168:
                designation = "Private"
            else:
                designation = "Public"

        # IP Class D:	224 to 239  Special IP
        elif address_range >= 224 and address_range <= 239:
            class_name = "D"
        # IP Class E:	240 to 250  Special IP
        elif address_range >= 240 and address_range <= 250:
            class_name = "E"

        # check the Special designation
        if class_name == "D" or class_name == "E" :
          designation = "Special"
        # Special IP:   127.0.0.1 - 127.255.255.255
        elif address_range == 127 and last_range >= 1:
            designation = "Special"

        print(f"Class: {class_name}, Designation: {designation}")


if __name__ == '__main__':
    Solution()
