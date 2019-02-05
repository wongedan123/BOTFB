echo "STARTING INSTALL..."
sleep 3
pkg update && pkg upgrade
echo ""
clear
echo ""
echo "Pleas wait :) ...."
echo ""
sleep 4
pip2 install mechanize
sleep 2
pip2 install requests
sleep 2
pkg install python
sleep 2
clear
echo ""
echo "INSTALLING FINISH please enter python2 BOTFB.py"
