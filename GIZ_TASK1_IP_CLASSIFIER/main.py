import sys
class Solution:
    print('Enter the IP/Mask please')
    inputip=input()
    ipclass=''
    ipdesignation=''
    tocheckip='000.000.000.000'
    subnetmask=0
    iplist=inputip.split('/')
    # seprate the subnetmask from the ip adress
    tocheckip=iplist[0]
    subnetmask=iplist[1]
    ipparts=tocheckip.split('.')
    # divide the ip adress into 4 parts
    a=int(ipparts[0])
    b=int(ipparts[1])
    c=int(ipparts[2])
    d=int(ipparts[3])
    if (a<=127):
                ipclass='A'
    elif(191>=a>=128 and b<=255):
                ipclass='B'
    elif(223>=a>=192 and b<=255 and c<=255 and d<=255):
                ipclass='C'
    elif(239>=a>=224 and b<=255 and c<=255 and d<=255):
                ipclass='D'
    elif(255>=a>=240 and b<=255 and c<=255 and d<=255):
                ipclass='E'
    if(ipclass=='A' and a==10):
            ipdesignation='Private'
    elif(ipclass=='A' and a!=10 and b==0 and c==0 and d==0):
            ipdesignation='Public'
    elif(ipclass=='A'):
            ipdesignation='Special'
    elif(ipclass=='B' and a==172 and 31>=b>=16):
            ipdesignation='Private'
    elif(ipclass=='B' and 255>=b>=0 and c==0 and d==0):
            ipdesignation='Public'
    elif(ipclass=='B'):
            ipdesignation='Special'
    elif(ipclass=='C' and a==192 and b==168 and 255>=c>=0 and 255>=d>=0):
            ipdesignation='Private'
    elif(ipclass=='C' and 255>=b>=0 and 255>=c>=0 and d==0):
            ipdesignation='Public'
    elif(ipclass=='C'):
            ipdesignation='Special'
    elif(ipclass=='D',ipclass=='E'):
            ipdesignation='N/A'    
    
    print("Class:",(ipclass) ,  "Designation:",ipdesignation)
        


    if __name__ == '__main__':
        pass
