from tkinter import * #Tkinter used to make GUI for application
from pytube import YouTube #YouTube Package

root = Tk()
root.title('YouTube Video Downloader')
#Default Window Size
root.geometry("500x300") 

#Initial Video Detail Variables
title = ""
views = ""
download_status = ""

#Download Button Function
def download_button():
    yt = YouTube(link.get())   
    title = yt.title
    views = yt.views
    
    #Pull highest res video from available streams
    ys = yt.streams.get_highest_resolution()

    #Download and update download status 
    download_status = "Downloading ..."
    ys.download()
    download_status = "Download Complete!"


#Create Labels 
filler_label = Label(root, text= "                                                   ")
label1 = Label(root, text = "Please Enter YouTube Link Below:")
filler_label2 = Label(root, text = "")
title_label2 = Label(root, text = f"Title: {title}")
views_label3 = Label(root, text = f"Views: {views}")
filler_label3 = Label(root, text = "")
download_status_label4 = Label(root, text = f"{download_status}")
#Ask user for link
link = Entry(root)

#Download Video Button
button1 = Button(root, text = "Download Video", command=download_button)

#Grid Placement of Widgets on GUI
filler_label.grid(row=0,column=0)
label1.grid(row=0, column=1)
link.grid(row=1,column=1)
button1.grid(row=2,column=1)
filler_label2.grid(row=3,column=1)
title_label2.grid(row=4,column=1)
views_label3.grid(row=5,column=1)
filler_label3.grid(row=6,column=1)
download_status_label4.grid(row=7, column=1)

root.mainloop()


