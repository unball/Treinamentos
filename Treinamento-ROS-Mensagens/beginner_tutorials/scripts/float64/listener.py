#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %lf", data.data)

def listener():
	rospy.init_node('listener')
	rospy.Subscriber("chatter", Float64, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
