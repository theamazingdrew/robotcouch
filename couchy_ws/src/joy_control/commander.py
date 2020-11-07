#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
#from adafruit_servokit import ServoKit

def callback(data):
   rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.linear.x)
   # This is where you put the motor calls and do the math to include angular z
   # round data.linear.x and angular.z to the nearest tenth?
   # then calculate the impact of data.angular.z
   # Then update the motor speed
   # kit.continuous_servo[1].throttle = xxx 
   # kit.continuous_servo[0].throttle = xxx 

def move():
    # Initiate the motor controllers
    #kit = ServoKit(channels=16) 
    #kit.continuous_servo[1].throttle = 0 # safety initiate 
    #kit.continuous_servo[0].throttle = 0 # safety initiate 
    rospy.init_node('commander', anonymous=True)
    
    # Starts a new node
    velocity_subscriber = rospy.Subscriber('/r2/cmd_vel', Twist, callback, queue_size=1)
    rospy.spin()

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
