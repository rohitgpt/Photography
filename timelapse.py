from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal, os, subprocess
 
shot_date = datetime.now().strftime("%Y-%m-%d")
picID = "temp"
 
clearCommand = ["--folder", "/store_00010001/DCIM/101D3500","-R",
"--delete-all-files"]
bulb = 5
triggerCommand = ["--bulb="+str(bulb), "--trigger-capture", "--capture-image"]
downloadCommand = ["--get-all-files"]
 
folder_name = shot_date + picID
save_location = "/home/pi/gphoto/" + folder_name
 
def createSaveFolder():
    try:
        os.makedirs(save_location)
        print("New save directory created for today!")
    except:
        print("Already created this save directory for today")
    os.chdir(save_location)
 
def captureImages():
    gp(triggerCommand)
    sleep(5)
    gp(downloadCommand)
    sleep(1)
    gp(clearCommand)
 
def renameFiles (ID):
    for filename in os.listdir("."):

        if 'KLN' in filename:
            if filename.endswith(".JPG"):
                os.rename(filename, (ID + ".JPG"))
                print("Sucess!") 
            elif filename.endwith (".CR2"):
                os.rename(filename, (shot_time + ID + ".CR2"))
                print ("Hurray! Raw file renamed")
 
gp(clearCommand)
createSaveFolder()
n = 3 
count = 0
print(datetime.now())
start_time = datetime.now()
while count<n:
    shot_time = datetime.now().strftime("%Y-%m-%d" "-%H.%M.%S")
    captureImages()
    renameFiles(shot_time+picID)
    print("Saved "+str(count+1)+"/"+str(n)+" shots")
    sleep (1)
    count+=1
print(datetime.now()-start_time)
