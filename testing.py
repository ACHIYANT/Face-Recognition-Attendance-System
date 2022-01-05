from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

def main():
    class register_sys():
         def __init__(self,master):
            # master = master
            # master=Tk()
            master.geometry("1440x900+0+0")
            master.title("Register")
            # master.mainloop()
            # pass
    master=Tk()
    obj=register_sys(master)
    master.mainloop()
if __name__ == "__main__":
    main()