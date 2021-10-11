import re
from helper import decimalToBinary 
class IPSuite:
  def validateInput(givenIP):
    if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:/[0-2]\d|/3[0-2])", givenIP):
      result = True
    else:
      result = False
    return result
    
  def getIPClass(IP):
    firstOctet = IP.split(".")[0]
    firstOctetBin = decimalToBinary(int(firstOctet))
    print(firstOctetBin)
    if firstOctetBin[0] == "0":
      ipClass = "A"
    elif firstOctetBin[0:2] == "10":
      ipClass = "B"
    elif firstOctetBin[0:3] == "110":
      ipClass = "C"
    elif firstOctetBin[0:4] == "1110":
      ipClass = "D"
    elif firstOctetBin[0:4] == "1111":
      ipClass = "E"
    else:
      ipClass = False
    return ipClass

  def getIPDesignation(IP):
    octects = [int(oct) for oct in IP.split(".")]
    if octects[0] == 10 or (octects[0] == 172 and int(octects[1]) >= 16 and int(octects[1]) <= 31) or (octects[0] == 192 and octects[1] == 168):
      designation = "private"
    elif octects[0] == 127:
      designation = "special"
    else:
      designation = "public"
    return designation