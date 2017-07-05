import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update
import math

from spaceship import user
from rock import Rock


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False
cycle_count = 0
objs = set()
ship = user()
last_clicked = None

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,objs,last_clicked
    running     = False
    cycle_count = 0
    objs       = set()
    last_clicked = None


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#tep just one update in the simulation
def step ():
    global running
    running = True
    update_all()
    display_all()
    running = False
    


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global last_clicked
    last_clicked = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    if str(last_clicked) != 'Remove':
        a = eval(last_clicked + '(' + str(x) + ',' + str(y) + ')')
        add(a)
    else:
        rset = set()
        for o in objs:
            if o.contains((x,y)):
                rset.add(o)
        for r in rset:
            remove(r)
    
def up_key(*args):
    global ship
    print('up')
    ship.set_speed(ship.get_speed()+5)

def down_key(*args):
    global ship
    print('down')
    ship.set_speed(ship.get_speed()-5)
    
def left_key(*args):
    global ship
    print('left')
    ship.set_angle(ship.get_angle()-.3)
    
def right_key(*args):
    global ship
    print('right')
    ship.set_angle(ship.get_angle()+.3)
    


#add simulton s to the simulation
def add(s):
    objs.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    objs.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    rset = set()
    for o in objs:
        if p(o):
            rset.add(o)
    return rset


#call update for every simulton in the simulation
def update_all():
    global cycle_count,user
    if running:
        cycle_count += 1
        ship.update()
        cycle_count += 1
        eaten = set()
        for o in find(lambda x: not isinstance(x,Rock)):
            o.update()
        for b in find(lambda x: isinstance(x,Rock)):
            for d in b.update(objs):
                eaten.add(d)
        for e in eaten:
                remove(e)
                        
        


#delete from the canvas each simulton in the simulation; then call display for each
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    ship.display(controller.the_canvas)
    for o in objs:
        o.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(objs))+" balls/"+str(cycle_count)+" cycles")
