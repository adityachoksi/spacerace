from mortal import Mortal
import math

class user(Mortal):
    radius = 5
    
    def __init__(self):
        Mortal.__init__(self,200,200,10,10,math.pi/2,0)
        
    
        
    def display(self,canvas):
        (x,y) = Mortal.get_location(self)   
        canvas.create_oval(x - user.radius, y - user.radius, 
                           x + user.radius, y + user.radius,
                           fill='Blue')
    
    def update(self):
        Mortal.move(self)
        