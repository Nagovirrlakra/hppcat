# this is the hppcat, the project of The_Anuan.
# this project is under the GNU GPL license, free to use and modify
# Hppcat: the file hidener that build for linux with python 



sudo su

echo

"_                           _   
 | |__  _ __  _ __   ___ __ _| |_ 
 | '_ \| '_ \| '_ \ / __/ _` | __|
 | | | | |_) | |_) | (_| (_| | |_ 
 |_| |_| .__/| .__/ \___\__,_|\__|
       |_|   |_|  "
       
 echo "Type a command: "
 
 read inp
 
 if [ $((inp)) == "gmn" ]; then
  echo "Command: 
gmn: Show this help 
shi: Hide the file 
rtn: Restore the file 
hflst: List the hidden files
dah: Exit"

if [[ $((inp)) == "shi" ]]; then

echo "type the file path to hide: " 

read hid

mv $hid /opt/.mksystem/.sra/.ArChiVe

if [[ $((inp)) == "rtn" ]]; then

echo "type the file name you want to restore: " 

read bc

mv /opt/.mksystem/.sra/.ArChiVe/$bc /home/$USERNAME/Documents

if [[ $((inp)) == "hflst" ]]; then

cd /opt/.mksystem/.sra/.ArChiVe
ls

if [] $((dah)) ]]; then
exit

fi
done




      
