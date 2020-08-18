#A simple script to download 720p videos from YouTube. 
#Uses Tkinter and Pytube3 packages

from tkinter import * #Tkinter used to make GUI for application
from pytube import YouTube #YouTube Package

root = Tk()
root.title('YouTube Video Downloader')

#Download Button Function
def download_button():

    yt = YouTube(link.get())   
    title = str(yt.title)
    views = str(yt.views)

    title_label2.config(text = f"Title: {title}")
    views_label3.config(text = f"Views: {views}")


    #Pull highest res video from available streams
    ys = yt.streams.get_highest_resolution()

    #Download and update download status 
    ys.download()
    download_status_label.config(text = r"Download Complete! Please check directory where downloader is running.")


#Create Labels 
label1 = Label(root, text = "Please Enter YouTube Link Below:")
filler_label = Label(root, text = "")
title_label2 = Label(root, text = "Title: ")
views_label3 = Label(root, text = "Views: ")
filler_label2 = Label(root, text = "")
download_status_label = Label(root, text = " ")
#Ask user for link
link = Entry(root,width = 60)

#Download Video Button
button1 = Button(root, text = "Download Video", command=download_button)

#Grid Placement of Widgets on GUI
label1.grid(row=0, column=1)
link.grid(row=1,column=1)
button1.grid(row=2,column=1)
filler_label.grid(row=3,column=1)
title_label2.grid(row=4,column=1)
views_label3.grid(row=5,column=1)
filler_label2.grid(row=6,column=1)
download_status_label.grid(row=7, column=1)

root.mainloop()


