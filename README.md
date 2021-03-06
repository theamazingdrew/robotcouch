# robotcouch
ROS-based remote-controlled robot utilizing a PCA9685 motor driver interfaced with (in this case) a Jetson Nano. Using ROS Melodic on Ubuntu 18.04. Early derivatives of this code also worked on a Raspberry Pi


This is currently alpha code, but it does work (although there are plenty of bugs and almost no error checking). The following are some relevant notes for running.

To test the adafruit controls when plugging in the PCA9685:
1. Open Python3
>> from adafruit_servokit import ServoKit

>> kit = ServoKit(channels=16)

>> kit.continuous_servo[1].throttle = 0 # safety initiate

>> kit.continuous_servo[0].throttle = 0 # safety initiate

 then enter different throttle amounts (between -1 and 1) to test

Good references for joystick control:
http://wiki.ros.org/joy/Tutorials/ConfiguringALinuxJoystick
http://ros-developer.com/2017/07/28/control-your-robot-with-a-joystick-in-ros/

To start the joystick and steer the motors on your laptop:
>> rosrun joy joy_node dev:=/dev/input/js0 

Your user account needs access. You may have to sudo chmod js0

>> rosparam load joystick_param.yaml 

Don't forget there's a deadman switch! If you aren't holding that, you won't go anywhere
Then fire up the joystick connected to your laptop. On your laptop run...

>> rosrun joy_teleop joy_teleop.py

Then commander.py is run on the robot itself. Also, you'll need to pip install the Adafruit library for a PCA9685. The adafruit library requires python3

>> python3 commander.py