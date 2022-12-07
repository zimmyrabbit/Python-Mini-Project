from tkinter import *
from tkinter import ttk
from pynput import mouse 
 
root = Tk()
root.title("마우스 좌표 찾기")
root.geometry("300x300")
 

entry1 = ttk.Entry(root, width=10 )
entry1.grid(row=0, column=1)
 
entry2 = ttk.Entry(root, width=10 )
entry2.grid(row=0, column=2)
 
button1 = ttk.Button(root, text="마우스위치", command = lambda:aaa())
button1.grid(row=0, column=3)
 
 
def aaa():
    with mouse.Listener( 
        on_click = bbb
        ) as listener:
        listener.join()
    ccc()    
 
def bbb(x, y, button, pressed):
    if pressed:
        global x1
        global y1
        x1 = x
        y1 = y
        
    if not pressed :
        return False
 
def ccc():
    entry1.delete(0,"end") 
    entry2.delete(0,"end")
    entry1.insert("end",x1) 
    entry2.insert(0,y1)     
 
root.mainloop()