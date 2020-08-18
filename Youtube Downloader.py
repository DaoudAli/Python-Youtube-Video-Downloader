from tkinter import * #Tkinter used to make GUI for application
from pytube import YouTube

root = Tk()

#Default Window Size
root.geometry("500x300") 

#Ask user for link
fillerlabel = Label(root,text="                                                   ")
label1 = Label(root, text="Please Enter YouTube Link Below:")
link = Entry(root)

#Grid Placement of Widgets on GUI
fillerlabel.grid(row=0,column=0)
label1.grid(row=0, column=1)
link.grid(row=1,column=1)

#yt = YouTube(link.get)

#Getting the highest resolution possible
#ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
#ys.download()
print("Download completed!!")

root.mainloop()


