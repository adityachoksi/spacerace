from simulton import Simulton
from mortal import Mortal
import math
class Rock(Simulton):


    _radius = 15
    
    def __init__(self,x,y):
        self.radius = Rock._radius
        Simulton.__init__(self,x,y,self.radius*2,self.radius*2)
        
    def update(self,objs):
        inset = set()
        for i in objs:
            (x,y) = Simulton.get_location(i)
            if self.contains((x,y)) and isinstance(i,Mortal):
                inset.add(i)
        return inset
        
    def display(self,canvas):
        (x,y) = Simulton.get_location(self)   
        canvas.create_oval(x - self.radius, y - self.radius, 
                           x + self.radius, y + self.radius,
                           fill='Black')

    def contains(self,xy):
        (a,b) = Simulton.get_location(self)
        x,y = xy[0],xy[1]
        return math.sqrt(math.pow(abs(x-a),2) + math.pow(abs(y-b),2)) < self.radius
    
    def set_radius(self,r):
        self.radius = r
        
    def get_radius(self):
        return self.radius
            
            
        
        