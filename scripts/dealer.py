#!/usr/bin/env python3

from re import A
import rospy
from std_msgs.msg import Int32
import random
import sys

rospy.init_node('dice')
pub = rospy.Publisher('dealer', Int32, queue_size=1)
x = random.randint(1,6)
y = random.randint(1,6)
n = x + y
#a = input('どっちも：')

print('壺を被せて壺被ります！')

a = input('どっちも：')
print(a)
#print(x, y)
print('はたして。。。', x, 'と',y)
#print(y)
print(n)

#rospy.init_node('dice')
#while not rospy.is_shutdown():
pub.publish(n)
rospy.spin()
    #rate.sleep()
