from Myro import *
init("sim") 
def dsquare(y):
    for i in range(y):
        penDown()
        forward(3,1)
        turnBy(90)
    
dsquare(4)