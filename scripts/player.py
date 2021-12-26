#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
    global n
    n = message.data

if n %2 == 0:
    print('半')
else:
    print('丁') 

if __name__ == '__main__': 
    rospy.init_node('player')
    sub = rospy.Subscriber('dealer', Int32, cb)
    rospy.spin()
    #pub = rospy.Publisher('player', Int32, queue_size=1) 
    #while 1:
    #    pub.publish(n)