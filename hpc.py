#!/usr/bin/python
'''
 this is the hppcat, the project of The_Anuan.
this project is under the GNU GPL license, free to use and modify

Hppcat: the file hidener that build for linux with python
''' 

call ("sudo su", shell=true)

while = true:

print (""" 
 _                           _   
| |__  _ __  _ __   ___ __ _| |_ 
| '_ \| '_ \| '_ \ / __/ _` | __|
| | | | |_) | |_) | (_| (_| | |_ 
|_| |_| .__/| .__/ \___\__,_|\__|
      |_|   |_|                 
                        """) 
                        
inp = input ("Type a Command: ")

print (inp) 

elif inp == 'gmn':

print (""" 
Command: 
gmn: Show this help 
shi: Hide the file 
rtn: Restore the file 
hflst: List the hidden files
dah: Exit
""")

elif inp == 'shi':

hid = input ("type the file path to hide: ")

print (hid) 

call ("cp {} ~/opt/.mksystem/.sra/.ArChive".format(hid), shell=True)
elif   inp == 'rtn':
    
blk = input ("type the file name you want to restore: ")

print (blk)
call ("mv /opt/.mksystem/.sra/.ArChive/{} /home/\$USERNAME/Documents/restored".format(blk), shell=True)     

elif inp == 'hflst':
call ("cd /opt/.mksystem/.sra/.archive && ls")

elif inp == 'dah':
sys.Exit(0)
else:

print ("wrong password")
