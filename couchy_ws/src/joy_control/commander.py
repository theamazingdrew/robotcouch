#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from adafruit_servokit import ServoKit #Requires Python3

#A tester
def callback(data, kit):
   # TRY USING LINEAR.Z AS THE REVERSE BUTTON. wHEN IT'S -1, GO INTO REVERSE.
   rospy.loginfo(rospy.get_caller_id() + " I heard %s", data)
   # This is where you put the motor calls and do the math to include angular z
   left = data.linear.x
   right = data.linear.x
   reverse = data.linear.z
   # NEED TO CHECK IF IT'S IN REVERSE. AND FIX THE CALCULATION. if IT'S IN REVERSE, ONLY HAVE NEGATIVE LINEAR.X. OTHERWISE IT HAS TO BE POSITIVE.
   # AND IF HAS TO BE BETWEEN 1 AND 0. ADD ERROR CATCHING FOR THAT.
   # SOMEWHERE IN HERE YOU NEED TO TEAR DOWN THE ADAFRUIT_SERVOKIT AT CLOSE
   #######
   if data.linear.z == -1:
      if data.angular.x > 0:
         right = max(data.linear.x - data.angular.x, 0)
         left = max(data.linear.x, 0)
      else:
         left = max(data.linear.x + data.angular.x, 0)
         right = max(data.linear.x, 0)
   else:
      if data.angular.x < 0:
         right = max(data.linear.x + data.angular.x, 0)
         left = max(data.linear.x, 0)
      else:
         left = max(data.linear.x - data.angular.x, 0)
         right = max(data.linear.x, 0)
   print(left)
   print(right)
   #######
   #kit.continuous_servo[1].throttle = round(data.linear.x, 2) 
   #kit.continuous_servo[0].throttle = round(data.linear.y, 2)
   #IF THE THROTTLE IS GREATER THAN 1 OR LESS THAN -1, IT NEEDS TO CATCH 
   # THE ERROR AND CORRECT. PUT ERROR CATCHING IN HERE BELOW
   kit.continuous_servo[1].throttle = left 
   kit.continuous_servo[0].throttle = right
   # round data.linear.x and angular.z to the nearest tenth?
   # then calculate the impact of data.angular.z
   # Then update the motor speed
   # kit.continuous_servo[1].throttle = xxx 
   # kit.continuous_servo[0].throttle = xxx 

def move():
    # Initiate the motor controllers
    kit = ServoKit(channels=16) 
    kit.continuous_servo[1].throttle = 0 # safety initiate 
    kit.continuous_servo[0].throttle = 0 # safety initiate
    rospy.init_node('commander', anonymous=True)
    # Starts a new node
    velocity_subscriber = rospy.Subscriber('/r2/cmd_vel', Twist, callback, (kit), queue_size=1)
    print("Up")
    rospy.spin()

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
