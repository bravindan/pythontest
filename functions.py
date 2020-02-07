def printme(x,y):
    return x+y

print(printme(30,40))

def getName():
    name = input("Name?")
    print(name)
getName()
#working on a function with no parameters
def calc():#function
    len=int(input("length: "))#taking user input
    width=int(input("width: "))
    ht=int(input("heigth: "))
    area=len*width #finding the area 
    vol=len*width*ht #finding the volume
  #  return area,vol
   # return vol
    print(area)
    print(vol)
calc()#function call
