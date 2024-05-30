from tkinter import *
import speedtest


def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    download = str(round(sp.download()/(10**6),3))+" Mbps"
    upload = str(round(sp.upload()/(10**6),3))+" Mbps"
    lab_d.config(text=download)
    lab_u.config(text=upload)


sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x650")
sp.config(bg="Blue")
lab = Label(sp,text="Internet Speed Test",font=("Times New Roman",25,"bold"),bg="Blue",fg="White")
lab.place(x=65,y=40,height=50,width=380)

lab = Label(sp,text="Download Speed",font=("Times New Roman",25,"bold"),bg="Blue",fg="White")
lab.place(x=65,y=130,height=50,width=380)

lab_d = Label(sp,text="00",font=("Times New Roman",25,"bold"),bg="Blue",fg="White")
lab_d.place(x=65,y=200,height=50,width=380)

lab = Label(sp,text="Upload Speed",font=("Times New Roman",25,"bold"),bg="Blue",fg="White")
lab.place(x=65,y=290,height=50,width=380)

lab_u = Label(sp,text="00",font=("Times New Roman",25,"bold"),bg="Blue",fg="White")
lab_u.place(x=65,y=360,height=50,width=380)

button = Button(sp,text="Check Speed",font=("Times New Roman",25,"bold"),relief=RAISED,bg="Red",fg="White",command=speedcheck)
button.place(x=65,y=410,height=50,width=380)

sp.mainloop()