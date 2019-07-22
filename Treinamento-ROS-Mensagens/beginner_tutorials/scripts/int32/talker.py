#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def talker():
	pub = rospy.Publisher('chatter', Int32)
	rospy.init_node('talker')
	rate = rospy.Rate(1)
	num = 0
	while not rospy.is_shutdown():
		rospy.loginfo(num)
		pub.publish(num)
		num = num + 1
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
