class Solution:
    def Classfinder(ip):
        if (ip[0] >= 1 and ip [0] <= 127):
            return "A"

        elif (ip[0] >= 128 and ip[0] <= 191):
            return "B"

        elif (ip[0] >= 192 and ip[0] <= 223):
            return "C"

        elif (ip[0] >= 224 and ip[0] <= 239):
            return "D"
        elif (ip[0] >= 240 and ip[0] <= 255):
            return "E"
        else:
            return "Wrong IP!"


    def designation(ip, className):
        if (className == "A"):
            if ((ip[0] >= 0 and ip[0] <= 127) and (ip[1] == 0) and (ip[2] == 0) and (ip[3] <= 0)):
                print("designation: public")
            elif ((ip[0] == 10) and (ip[1] <= 0 and ip[1] >= 255) and (ip[2] <= 0 and ip[2] >= 255)and (ip[3] <= 0 and ip[3] >= 255)):
                print("designation: private")
            else:
                print("designation: Special")

        elif (className == "B"):
            if ((ip[0] >= 128 and ip[0] <= 191) and (ip[1] >=0 and ip[1] <=255)and (ip[2] == 0)and (ip[3] == 0)):
                print("designation: public")
            elif ((ip[0] == 172) and (ip[1] >= 16 and ip[1] <= 31)and (ip[2] >= 0 and ip[2] <= 255) and (ip[3] >= 1 and ip[3] <= 255)):
                print("designation: private")
            else:
                print("designation: Special")

        elif (className == "C"):
            if ((ip[0] >= 192 and ip[0] <= 223) and (ip[1] >= 0 and ip[1] <= 255) and (ip[2] >= 0 and ip[2] <= 255) and (ip[3] == 0)):
                print("designation: public")
            elif ((ip[0] == 192) and (ip[1] >= 168) and (ip[2] >= 0 and ip[2] <= 255) and (ip[3] >= 0 and ip[3] <= 255)):
                print("designation: private")
            else:
                print("designation: Special")

        elif (className == "D"):
            if ((ip[0] >= 240 and ip[0] <= 239) and (ip[1] >= 0 and ip[1] <= 255) and (ip[2] >= 0 and ip[2] <= 255) and (ip[3] >= 0 and ip[3] <= 255)):
                print("designation: public")
            else:
                print("designation: Special")

        elif (className == "E"):
            if ((ip[0] >= 240 and ip[0] <= 255) and (ip[1] >= 0 and ip[1] <= 255) and (ip[2] >= 0 and ip[2] <= 255) and (ip[3] >= 1 and ip[3] <= 255)):
                print("designation: public")
            else:
                print("designation: Special")

        else:
            print("unknown")


    if __name__ == '__main__':
        ip = "254.0.0.1"
        ip = ip.split(".")
        ip = [int(i) for i in ip]

        #network class
        classnamee = Classfinder(ip)
        print("class:", classnamee)

        designation(ip, classnamee)
