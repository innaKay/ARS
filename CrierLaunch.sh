#!/bin/sh
clear
echo -e "Welcome to ROSCORE\n ----------------------------"
gnome-terminal -e ./Poly_Chatter.py 
gnome-terminal -e ./Poly_Listener.py 
roscore
rosrun rviz rviz

echo "Success"
