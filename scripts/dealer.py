#!/usr/bin/env python3

"""
BSD 3-Clause License

Copyright (c) 2021 Ryuichi Ueda + Leon Tonouchi.
All rights reserved.
"""

import rospy
from std_msgs.msg import Int32
import random

rospy.init_node('dice')
pub = rospy.Publisher('dealer', Int32, queue_size=1)
n = 0

x = random.randint(1,6)
y = random.randint(1,6)
n = x + y

print('壺を被せて壺被ります！')

a = input('どっちも：')
print(a)
print('はたして。。。', x, 'と',y)
print(n)

pub.publish(n)
  