from tkinter import Tk,Frame,TOP,LEFT,BOTTOM,RAISED,BOTH

# import controller to call/create widgets and position them in the view
import model
import controller


# Construct a simple root window
root = Tk()
root.title("Simulation")
root.resizable(width=False, height=False)
root.protocol("WM_DELETE_WINDOW",quit)

frame = Frame(root)

# Place buttons simply at the top
frame.pack(side=TOP)
controller.reset_button (frame,text="Reset")     .pack(side=LEFT)
controller.start_button (frame,text="Start")     .pack(side=LEFT)
controller.stop_button  (frame,text="Stop")      .pack(side=LEFT)
controller.step_button  (frame,text="Step")      .pack(side=LEFT)
controller.object_button(frame,text="Rock").pack(side=LEFT)
controller.object_button(frame,text="Hunter")    .pack(side=LEFT)
controller.object_button(frame,text="Remove")    .pack(side=LEFT)
controller.progress     (frame,text="0 updates/0 simultons",width=25,relief=RAISED).pack(side=LEFT)
root.bind("<KeyPress-Up>", model.up_key)
root.bind("<KeyPress-Right>", model.right_key)
root.bind("<KeyPress-Left>", model.left_key)
root.bind("<KeyPress-Down>", model.down_key)
 
# Place canvas in the space below
controller.simulation_canvas(root,width=500,height=500,bg="white").pack(side=BOTTOM,expand=True,fill=BOTH)