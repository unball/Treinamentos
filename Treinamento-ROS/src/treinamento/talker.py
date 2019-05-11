import rospy
from treinamento.msg import mymessage

message = mymessage()
message.impar = 1

def plusOne(arg):
	arg.impar = arg.impar + 2
	arg.par = arg.par + 2
	return arg

publisher = rospy.Publisher('FaladorNovo', mymessage, queue_size=1)
rospy.init_node('newtalker', anonymous=True)
rate = rospy.Rate(1)

while not(rospy.is_shutdown()):
	message = plusOne(message)
	publisher.publish(message)
	rate.sleep()
