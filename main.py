class Solution:
    def IP_ADD():

        Enter = input("Enter Your IP: ")
        first_sp = Enter.split("/")
        second_sp = first_sp[0].split(".")
        print(second_sp)

        # Class A Public & Private IP Address Range
        if (int(second_sp[0]) >= 1 and int(second_sp[0]) <= 127):

            if (int(second_sp[0]) == 10):
                print("Class: A, Designation: Private")
            elif (int(second_sp[0]) == 127 and int(second_sp[1]) == 0 and int(second_sp[2]) == 0 and int(second_sp[3]) > 0):
                print("Class: A, Designation: Spical")
            else:
                print("Class: A, Designation: Public")


        #Class B Public & Private IP Address Range
        if (int(second_sp[0]) >= 128 and int(second_sp[0]) <= 191):

            if (int(second_sp[0]) == 172 and int(second_sp[1]) >= 16 and int(second_sp[1]) <= 31):
                print("Class: B, Designation: Private")

            print("Class: B, Designation: Public")



        #Class C Public & Private IP Address Range
        if (int(second_sp[0]) >= 192 and int(second_sp[0]) <= 223):
            
            if (int(second_sp[0]) == 192 and int(second_sp[1]) == 168):
                print("Class: C, Designation: Private")

            elif (int(second_sp[0]) >= 192 and int(second_sp[0]) <= 223):
                print("Class: C, Designation: Public")



        #Class D IP Address Range
        if (int(second_sp[0]) >= 224 and int(second_sp[0]) <= 239):
            print("Class: D")



        #Class E IP Address Class
        if (int(second_sp[0]) >= 240 and int(second_sp[0]) <= 255):
            print("Class: E")



Solution.IP_ADD()
if __name__ == '__main__':
    pass