def printme(x,y):
    return x+y

print(printme(30,40))

def getName():
    name = input("Name?")
    print(name)
getName()

def calc():
    len=int(input("length: "))
    width=int(input("width: "))
    ht=int(input("heigth: "))
    area=len*width
    vol=len*width*ht
  #  return area,vol
   # return vol
    print(area)
    print(vol)
calc()