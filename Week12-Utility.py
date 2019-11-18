#Breven Jackson
#CS - 102
#Week12 - Utility

def PrintOutput(x):
    print('OUTPUT',x)
    
def PrintOutput2(y,x):
    print('OUTPUT',y,x)

def TriangleArea(x,y):
    z = float((x*y)/2)
    PrintOutput(z)

def FeetToMeters(x):
    y = float(x*.3048)
    PrintOutput(y)
def PolarCoords(x,y):
    import math
    x = float(x)
    y = float(y)
    r = math.sqrt((x**2)+(y**2))
    theta = math.atan(y/x)
    theta = (theta * 180)/3.141592
    theta = round(theta,1)
    PrintOutput2('r:',r)
    PrintOutput2('theta:',theta)
    
def EurosToDollars(x):
    x = x*1.12
    x = round(x,2)
    PrintOutput(x)
