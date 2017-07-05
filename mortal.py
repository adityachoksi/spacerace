from mobilesimulton import Mobile_Simulton


class Mortal(Mobile_Simulton):
    def __init__(self,x,y,width,height,angle,speed):
        Mobile_Simulton.__init__(self,x,y,width,height,angle,speed)