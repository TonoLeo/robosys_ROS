#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32
import random

rospy.init_node('dice')
pub = rospy.Publisher('dealer', Int32, queue_size=1)
x = random.randint(1,6)
y = random.randint(1,6)
sum = x + y

print(x)
print(y)
print(sum)

#rospy.init_node('dice')
pub.publish(sum)