class Solution:

    def __init__(self,input_ip):

        ip_range = input_ip.split("/")
        ip_range_list = ip_range[0].split(".")
        #convert string input to an integer by eval()
        ip_list_int = [eval(i) for i in ip_range_list]
        workingIP = [0, 0, 0, 0]


        for index in range(len(ip_range_list)):
            workingIP[index] = int(ip_list_int[index])
            if workingIP[index] > 255:
                raise ValueError
            if index > 3: raise ValueError

        class_type = ""
        designation = ""

        if 1 <= ip_list_int[0] <= 127:
            class_type = "A"
            if ip_list_int[0] == 10:
                designation = "Private:"
            else:
                designation = "special"
        
        elif 128 <= ip_list_int[0] <= 191:
            class_type = "B"
            if ip_list_int[0] == 172:
                designation = "Private:"
            else:
                designation = "Public"
        
        elif 192 <= ip_list_int[0] <= 223:
            class_type = "C"
            if ip_list_int[0] == 192:
                designation = "Private:"
            else:
                designation = "Public"

        elif 224 <= ip_list_int[0] <= 239:
            class_type = "D"

        elif 240 <= ip_list_int[0] <= 255:
            class_type = "E"

        elif class_type == "D" or class_type == "E":
            designation = "Special"
        elif ip_list_int[0] == 127 or ip_list_int[0] >= 1:
            designation = "Special"
        print(f"Class : {class_type} , Designation : {designation}")


if __name__ == '__main__':

        try:
            input_ip = input("Enter an IP address : - ")
            ipAddress = Solution(input_ip)

        except (ValueError):
            
            print('\nPlease give a valid IPv4/MASK address in #.#.#.#/# format,' '\n'
                '\tfor example: 192.168.1.1/24, or 10.10.10.1/28')
