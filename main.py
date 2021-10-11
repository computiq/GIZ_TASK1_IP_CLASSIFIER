from ip_suite import IPSuite as IPSuite
import sys

class Solution:
  def main(self):
    given = ""
    while not given:
      given = str(input("Please enter a valid IPV4 address in the form of IP/mask:  (enter q to quit) "))
      if given == "q":
        sys.exit(0)
      else:
        if IPSuite.validateInput(given):
          ip, mask = given.split("/")
          ipClass = IPSuite.getIPClass(ip)
          ipDesignation = IPSuite.getIPDesignation(ip)
          if ipClass and ipDesignation:
            print("IP: {} \nSubnet Mask: {} \nClass: {} \nDesignation: {} \n".format(ip, mask, ipClass, ipDesignation))
          else:
            print("Something went wrong! \n")
            sys.exit(0)
        else:
          given = ""

if __name__ == '__main__':
    Solution().main()
