from math import tan
side=int(input("No of sides: "))
Ingt = float(input("Lenght of side: "))
area= side*(Ingt**2)/(4*tan(3.14/side))
print('The area of polygon with', side,'sides and lenght',Ingt,'cm is', area,' units.')
