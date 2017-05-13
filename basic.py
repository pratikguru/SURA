from Tkinter import *
from tkMessageBox import *
import ttk 
from tkFileDialog   import askopenfilename
import os
from  SimpleCV import *
import serial

#ardu = serial.Serial('/dev/ttyUSB0', 9600)

#
box = Tk()

# frame1
x = StringVar()
var =IntVar()
ardu = serial.Serial('/dev/ttyUSB0', 115200)
            
def openGripper(event):
    #print "gripper Opening"
    lb.insert(END, "Gripper opening")
    ardu.write('1')
    
def closegripper(event):
    #print "Gripper closing"
    lb.insert(END, "Gripper closing")
    ardu.write('2')

def StopRot(event):
    print "stopping_rotation" 
    ardu.write('s')   
    lb.insert(END,"rot_stopped")

def exit(event):
    print "Bye"
    lb.insert(END, "BYE")
    import sys; sys.exit() 


def setRes():
    if x.get() == 0:
        print "No resolution set"
        lb.INSERT(END, "No resolution set")
    box.geometry(x.get())
        




def fullScreen(event):
    box.geometry('1300x768')    #changes based on your resolution


def smallScreen(event):
    box.geometry('1000x400')
    print "small screen"
    lb.insert(END, "Small screen")

def LEDon():
    print "LED ON"
    lb.insert(END, "LED on")
    ardu.write('o')
    #os.system("cvlc  %s" %("vid.mp4"))
   

def LEDoff():
    print("LED OFF")
    ardu.write('l')
    lb.insert(END, "LED off")

def ClockWise(event):
    print("ClockWise Rotation")
    lb.insert(END, "Clockwise rotation")
    ardu.write('4')	
def antiCW(event):
    print ("Anit-ClockWise rotation")
    ardu.write('5')
    lb.insert(END, "Anti-ClockWise rotation")


def doNothing(event):
    #print("Do nothing");
    lb.insert(END, "Do nothing")

def HelpSheet():
    print "Opened help sheet!"
    qbox = Tk()
   
    explanation = """  
    
    This is a control sheet, Most of the ROV's controls are placed on the keyboard, except a few on screen buttons,
    These controls are desgined for detect edge detection.
    ---------------------------------------------------------------------------------------------------------------
    Forward  : w
    Backward  : s
    Left  : a
    Right  : d
    roll  : "yet to be defined"
    pitch  : "" 
    yaw   : ""
    +++++++++++++++++++++++++++++++
    Gripper Open  : up
    Gripper close  : down
    Gripper ClockWise Rotation : right
    Gripper Anti-CW   Rotation : Left
    Led on  : l
    Bluetooth data  : b
    ---------------------------------------------------
    For opening sensor data log, in Help -> open Sensor log.
    quit = File Meunu -> quit
    Controls  = Help -> controls
    """
    label = Label(qbox, text = explanation, compound = RIGHT).place(relx = 0.01, rely = 0.01, anchor = NW)
    qbox.geometry('720x400')
    
def OpenFile():
    name = askopenfilename()
    print name


def About():
    print "This is a simple example of a menu"
    lb.insert(END, "This is a simple example of menu, please add code")

def KeyControls():
            box.bind("<Up>", openGripper)
            box.bind("<KeyRelease-Up>", doNothing)

            box.bind("<Down>", closegripper)
            box.bind("<KeyRelease-Down>", doNothing)
                        
            box.bind("<Left>", antiCW)
            box.bind("<KeyRelease-Left>", StopRot)
                        
            box.bind("<Right>", ClockWise)
            box.bind("<KeyRelease-Right>", StopRot)


def menu():
        menu = Menu(box)
        box.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Help", menu=filemenu)
        filemenu.add_command(label="Controls", command=HelpSheet)
        filemenu.add_command(label="Open sensor log", command=OpenFile)
       
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=box.quit)

        helpmenu = Menu(menu)
        menu.add_cascade(label="Self test", menu=helpmenu)
        helpmenu.add_command(label="About", command=About)





def TitleBar():
    f = Frame(box, width = 300, height = 450)
    xf = Frame(f, relief = GROOVE, borderwidth = 2.5)
                #heading = Label(xf,text = "Team Ahti, ROV control System", font = ("aerial", 12)).grid()
    system = Label(xf,text = "System controls").grid(row = 0, column = 0)
    ledon = Button(xf,text = "LED ON", command = LEDon).grid(row = 1,column = 0 , pady =5)
    ledoff = Button(xf,text = "LED OFF", command = LEDoff).grid(row = 2,column = 0,pady = 5)    
    resoLabel = Label(xf,text = "Console Resolution").grid(row = 39, pady = 10)
    entry = Entry(xf,textvariable = x).grid(row = 40)
    resolutionButton = Button(xf, text = "Get Res", command = setRes).grid(row = 41,pady = 5)    
    refresh = Button(xf, text = "Refresh console", command = fresh).grid()
    xf.place(x = 0, y = 1)
    f.pack(side = LEFT, padx= 20)


def fresh():
    lb.delete(0, END)


def input_choice():
         
    if var.get() == 1:
        print "You chose keyboard Control"
        lb.insert(END, "You chose keyboard control")
    elif var.get() == 2:
        print "You chose on screen control"
        lb.insert(END, "You chose on screen control")

def Control_choice():

    g = Frame(box, width = 500, height = 450)
    xg = Frame(g, relief=GROOVE, borderwidth = 2.5)
    title = Label(xg,text = "Optional onscreen controls").pack()
    ##
    openGrp = Button(xg,text = "Open gripper")
    close = Button(xg,text = "Close gripper")
    openGrp.bind("<ButtonPress-1>", openGripper)
    openGrp.bind("<ButtonRelease-1>", doNothing)
    close.bind("<ButtonPress-1>", closegripper)
    close.bind("<ButtonRelease-1>", doNothing)
    openGrp.pack(padx =10, pady =10, side = RIGHT)
    close.pack(padx =10, pady =10, side = LEFT)
    ##
    ##
    rotGrp = Button(xg,text = "Clock Wise")
    rotGrp2 = Button(xg,text = "Anti-Clock wise")
    rotGrp.bind("<ButtonPress-1>", ClockWise)
    rotGrp.bind("<ButtonRelease-1>", StopRot)
    rotGrp2.bind("<ButtonPress-1>", antiCW)
    rotGrp2.bind("<ButtonRelease-1>", doNothing)
    rotGrp.pack(side = BOTTOM, pady = 20)
    rotGrp2.pack(side = BOTTOM, pady = 20, padx = 10)
    xg.place(x = 1, y = 0)
    g.pack(side = LEFT)



def autoScroll():
    lb.insert("end")
    lb.see("end")
    box.after(1,autoScroll )

#init
#def consoleBox():
frame = Frame(box, bd = 1, relief = SUNKEN)
scroll = Scrollbar(frame, takefocus = 1)
lb = Listbox(frame, bd = 0, yscrollcommand = scroll.set, width = 100) 
lb.pack(side =LEFT, fill = BOTH, padx =75 , pady = 10)
    #adjust
scroll.config(command = lb.yview)
scroll.pack(side = RIGHT, fill = Y)
lb.see(END)
autoScroll()
frame.pack(side = BOTTOM, fill = X,pady = 20)


#loop
menu()
KeyControls()
TitleBar()
Control_choice()
input_choice()

  
#############################

box.bind("<Control-c>", exit)
box.bind("<Control-f>",fullScreen)
box.bind("<Control-g>", smallScreen)
box.geometry('1000x500')

box.mainloop()

 
