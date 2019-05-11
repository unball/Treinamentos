import rospy
from std_msgs.msg import Int64

def plusOne(arg):
	return arg+1

message = 0
publisher = rospy.Publisher('Falador', Int64, queue_size=1)
rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(1)

while not(rospy.is_shutdown()):
	message = plusOne(message)
	publisher.publish(message)
	rate.sleep()
