import sys


class Solution:
    def __init__(self) -> None:
        # To get the IP address
        ip = input("Enter the ip: ")
        ip_range = ip.split("/")
        first_ip = ip_range[0].split(".")
        first_ints = [eval(i) for i in first_ip]
        second_ip = int(ip_range[1])
        class_type = "None"
        des_type = "None"
        # A class condition
        if 1 <= first_ints[0] <= 127:
            class_type = "A class"
            if first_ints[0] == 10:
                des_type = "Private:"
            else:
                des_type = "Public"
        # B Class condition
        elif 128 <= first_ints[0] <= 191:
            class_type = "B class"
            if first_ints[0] == 172:
                des_type = "Private:"
            else:
                des_type = "Public"
        # C class condition
        elif 192 <= first_ints[0] <= 223:
            class_type = "C class"
            if first_ints[0] == 192:
                des_type = "Private:"
            else:
                des_type = "Public"
        # D class condition
        elif 224 <= first_ints[0] <= 239:
            class_type = "D class"
        # E class condition
        elif 240 <= first_ints[0] <= 255:
            class_type = "E class"

        if class_type == "D class" or class_type == "E class":
            des_type = "Special"
        elif first_ints[0] == 127 or first_ints[0] >= 1:
            des_type = "Special"
        print(f"The Class is : {class_type}")
        print(f"The Designation is : {des_type}")


if __name__ == '__main__':
    Solution()
