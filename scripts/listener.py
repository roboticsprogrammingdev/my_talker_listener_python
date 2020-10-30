#!/usr/bin/python

import rospy
from std_msgs.msg import String

def print_log(message):
    rospy.loginfo('Listener heard: "%s"', message.data)

def listener():
    rospy.init_node('listener')
    rospy.Subscriber('chatter', String, print_log)
    rospy.spin()

if __name__ == '__main__':
    listener()
