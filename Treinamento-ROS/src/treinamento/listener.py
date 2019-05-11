import rospy
from std_msgs.msg import Int64

def funcaoqueprinta(data):
	print(data)

rospy.init_node('Ouvidor',anonymous=True)
rospy.Subscriber('Falador',Int64,funcaoqueprinta)
rospy.spin()
