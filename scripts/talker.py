#!/usr/bin/python

import rospy
from std_msgs.msg import String

def talker():
    rospy.init_node('talker')
    chatter_publisher = rospy.Publisher('chatter', String, queue_size=1000)
    loop_rate = rospy.Rate(10)
    
    counter = 0
    while not rospy.is_shutdown():
        message = String()
        message.data = 'Talker says hi # ' + str(counter)

        rospy.loginfo('%s', message.data)

        chatter_publisher.publish(message)
        loop_rate.sleep()
        counter += 1


if __name__ == '__main__':
    talker()
