from sys import argv


class Solution:
    @staticmethod
    def print_response(ip_class, designation):
        print(f"Class: {ip_class}, Designation: {designation}")

    @staticmethod
    def validate_ip(provided_ip):
        """
            This method checks for everything possible
            If anything goes wrong it will raise an appropriate Exception
            Else, it will return the ip list of octets in decimal, of course.
        """
        # checks if . or / dont exist
        if "." not in provided_ip or "/" not in provided_ip:
            raise Exception("Invalid IP adress format. Try again.")

        provided_ip = provided_ip.split("/")
        ip = provided_ip[0].split(".")

        # check for the right amount of octets
        if len(ip) != 4:
            raise Exception("IP adress should have 4 octets o.o.o.o")

        # check if the octets are really octets or not
        for octet in ip:
            # checks for correct length
            if len(octet) < 1 or len(octet) > 3:
                raise Exception(
                    "Octets length shouldn't be greater than 3 digits nor less than 1")

            # checks for any non-digit characters
            if not octet.isdigit():
                raise Exception("Only use digits 0-9.")
            # checks if digits are in the corrects range
            if int(octet) < 0 or int(octet) > 255:
                print(octet)
                raise Exception("octets should be in range 0-255")

        # finally return the usuable form
        return list(map(int, ip))  # turn every element to digits

    @staticmethod
    def classify():
        # check whether the correct amount of arguments are provided
        if len(argv) != 2:
            raise Exception(
                "Error, try: python main.py <IP adress for example 192.168.1.1/24>")

        user_input = argv[1]

        # check if the ip provided is valid then returns ip in a list form
        ip = Solution.validate_ip(user_input)

        octet1, octet2, octet3, octet4 = ip

        # Class A
        if octet1 >= 1 and octet1 <= 127:
            if octet1 == 127 and (octet2, octet3, octet4) != (0, 0, 0):
                Solution.print_response("A", "Special")
            elif octet1 == 10:
                Solution.print_response("A", "Private")
            else:
                Solution.print_response("A", "Public")

        # Class B

        if octet1 >= 128 and octet1 <= 191:
            if octet1 == 172 and octet2 >= 16 and octet2 <= 32:
                Solution.print_response("B", "Private")
            else:
                Solution.print_response("B", "Public")

        # Class C

        if octet1 >= 192 and octet1 <= 223:
            if octet1 == 192 and octet2 == 168:
                Solution.print_response("C", "Private")
            else:
                Solution.print_response("C", "Public")

        # Class D

        if octet1 >= 224 and octet1 <= 239:
            Solution.print_response("D", "Special")

        # Class E

        if octet1 >= 240 and octet1 <= 255:
            Solution.print_response("E", "Special")


if __name__ == '__main__':
    Solution.classify()
