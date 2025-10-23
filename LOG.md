# Daily work logs
## Before 6/19/25
- Robot came with Ubuntu 18.04(?), along with older ROS and Pyrobot packages.
- We made a backup image of the robot, then installed Ubuntu 24.04.
- I attempted to install ROS2 Jazzy onto my laptop, then realized that it was not working well.
	- This involved compiling multiple packages from source.
	- I did learn about MoveIt during this time period, which was beneficial for working with the actual robot.
- I then found that there was still an installer script for ROS2 on the Trossen Robotics documentation, setup for Ubuntu 22.04.
- The installer script didn't work for ROS2 Humble, so I modified the script to allow it to install the newest versions of the packages for Humble.
- Since we don't have a charger for either of the batteries on the robot, I started with configuring the realsense camera.
	- I was able to run both the demo nodes from Intel, and the demo nodes that come with the robots.
- I then attempted to run the Gazebo Classic simulator.
    - Initially, the simulator crashed, but I found that there was a version mismatch, along with needing to source the gazebo setup bash script.
- After finding a power supply for the servos, I attempted to run the ROS2 control package, but the servos turned out to be badly configured.
	- Neither of the two camera servos had the right ID.
	- I was able to install the debug software onto a windows PC and test each of the servos individually, along with configuring the proper ID's.
- This allowed me to run the actual MoveIt demos, along with continue learning how to use ROS2.