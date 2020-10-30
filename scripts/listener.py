#!/usr/bin/python

import rospy
from std_msgs.msg import String

def print_log(data):
    rospy.loginfo('Listener heard: "%s"', data.data)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter', String, print_log)
    rospy.spin()

if __name__ == '__main__':
    listener()
