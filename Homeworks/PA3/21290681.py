from tkinter import *
from tkinter import messagebox
def main():
    root=Tk()
    main_frame=Frame(root)
    main_frame.pack(padx=20,pady=20)
    rate_per_minute=DoubleVar()
    b1=Radiobutton(main_frame,text="Daytime (6:00 a.m. through 5:59 p.m.)",variable=rate_per_minute, value=0.07)
    b1.pack()
    b2 = Radiobutton(main_frame, text="Evening (6:00 p.m. through 11:59 p.m.)",variable=rate_per_minute, value=0.12)
    b2.pack()
    b3 = Radiobutton(main_frame, text="Off-Peak (midnight through 5:59 a.m.)",variable=rate_per_minute, value=0.05)
    b3.pack()
    frame1=Frame(main_frame)
    frame1.pack()
    msg=Label(frame1,text="Enter the number of minutes:")
    msg.grid(row=0,column=0)
    ent = Entry(frame1)
    ent.grid(row=0, column=1)
    frame2 = Frame(main_frame)
    frame2.pack()
    def run():
        messagebox.showinfo("Total Charges", "Your total charges = $"+str(round(rate_per_minute.get()*int(ent.get()),2)))
    def shut_down():
        root.quit()

    disp=Button(frame2,text="Display Charges",command=run)
    disp.grid(row=0,column=0)
    quit_button = Button(frame2, text="Quit", command=shut_down)
    quit_button.grid(row=0, column=1)


    root.mainloop()

main()