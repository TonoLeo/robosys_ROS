#!/usr/bin/env python3

"""
BSD 3-Clause License

Copyright (c) 2021 Ryuichi Ueda + Leon Tonouchi.
All rights reserved.
"""

import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
    global n
    n = message.data

    while 1:
        if n %2 == 0:
            rospy.loginfo('丁')
            break
        else:
            rospy.loginfo('半')
            break

if __name__ == '__main__': 
    rospy.init_node('player')
    sub = rospy.Subscriber('dealer', Int32, cb)
    rospy.spin()
   