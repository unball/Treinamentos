import rospy
from std_msgs.msg import Int64

global message
message = Int64()

def callback(data):
	message.data = data.data + 1

publisher = rospy.Publisher('FaladorEscutador', Int64, queue_size=1)
rospy.init_node('talkerlistener',anonymous=True)
rospy.Subscriber('Falador',Int64,callback)
rate = rospy.Rate(1)

while not(rospy.is_shutdown()):
	publisher.publish(message)
	rate.sleep()
