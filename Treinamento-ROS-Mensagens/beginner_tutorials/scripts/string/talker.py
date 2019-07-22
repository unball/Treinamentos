#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
	pub = rospy.Publisher('chatter', String)
	rospy.init_node('talker')
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		hello_str = "Hello world %s" % rospy.get_time()
		rospy.loginfo(hello_str)
		pub.publish(hello_str)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
