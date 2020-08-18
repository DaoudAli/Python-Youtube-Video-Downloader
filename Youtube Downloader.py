from tkinter import * #Tkinter used to make GUI for application
from pytube import YouTube #YouTube Package

root = Tk()
root.title('YouTube Video Downloader')
#Default Window Size
root.geometry("500x300") 

#Initial Video Detail Variables
title = ""
views = ""

#Download Button Function
def downloadButton():
    yt = YouTube(link.get())   #Acquire List of Streams Available 
    title = yt.title
    views = yt.views
    


#Create Labels 
fillerlabel = Label(root, text= "                                                   ")
label1 = Label(root, text = "Please Enter YouTube Link Below:")
fillerlabel2 = Label(root, text = "")
label2 = Label(root, text = f"Title: {title}")
label3 = Label(root, text = f"Views: {views}")
#Ask user for link
link = Entry(root)

#Download Video Button
button1 = Button(root, text = "Download Video", command=downloadButton)

#Grid Placement of Widgets on GUI
fillerlabel.grid(row=0,column=0)
label1.grid(row=0, column=1)
link.grid(row=1,column=1)
button1.grid(row=2,column=1)
fillerlabel2.grid(row=3,column=1)
label2.grid(row=4,column=1)
label3.grid(row=5,column=1)
#yt = YouTube(link.get)

#Getting the highest resolution possible
#ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
#ys.download()
print("Download completed!!")

root.mainloop()


