
#first we must split
ip=input("please enter an IP address:")
spliting=ip.split('.')
a='.'
address=int(spliting[0])
#classes
ClassApri=range(10)
spi=range(127)
classBpri=range(172)
classCpri=range(192)
ClassA= range(0,127)
ClassB= range(128,191)
ClassC= range(192,223)
ClassD= range(224,239)
ClassE= range(240,255)

if address in ClassApri:
    print("Class A Designation private")
elif address in spi:
    print("Class A  Designation special")
elif address in ClassA:
    print("Class A Designation public")
elif address in classBpri:
    print("Class B Designation private")
elif address in ClassB:
    print("Class B public")
elif address in classCpri:
    print("Class C Designation private")
elif address in ClassC:
    print("Class C Designation public")
elif address in ClassD:
    print("Class D Designation public")
elif address in ClassE:
    print("Class E Designation public")




