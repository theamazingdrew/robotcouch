#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from adafruit_servokit import ServoKit #Requires Python3

def callback(data, kit):
   print("hi")
   #THE CALCULATIONS AREN'T RIGHT FOR THE TWO MOTORS YET
   rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.linear.x)
   # This is where you put the motor calls and do the math to include angular z
   left = data.linear.x
   right = data.linear.x
   if data.linear.z < 0:
      left = data.linear.x - data.angular.z
   else:
      right = data.linear.x + data.angular.z
   print(left)
   print(right)
   #kit.continuous_servo[1].throttle = round(data.linear.x, 2) 
   #kit.continuous_servo[0].throttle = round(data.linear.x, 2)
   kit.continuous_servo[1].throttle = round(left, 2) 
   kit.continuous_servo[0].throttle = round(right, 2)
   # round data.linear.x and angular.z to the nearest tenth?
   # then calculate the impact of data.angular.z
   # Then update the motor speed
   # kit.continuous_servo[1].throttle = xxx 
   # kit.continuous_servo[0].throttle = xxx 

def move():
    # Initiate the motor controllers
    print("1")
    kit = ServoKit(channels=16) 
    kit.continuous_servo[1].throttle = 0 # safety initiate 
    kit.continuous_servo[0].throttle = 0 # safety initiate 
    print("2")
    rospy.init_node('commander', anonymous=True)
    print("3")
    # Starts a new node
    velocity_subscriber = rospy.Subscriber('/r2/cmd_vel', Twist, callback, (kit), queue_size=1)
    print("4")
    rospy.spin()

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
