#!/usr/bin/env python
import random
import rospy
from std_msgs.msg import String

def poly_talker():
	pub = rospy.Publisher('polycrier', String, queue_size = 10) #topic polycrier
	rospy.init_node('Crier', anonymous = True) #node name Crier
	rate = rospy.Rate(21)
	while not rospy.is_shutdown():
		num = random.randint(1,3) # random generator
		name_pub= "Inna"
		if (num == 1):
			name_pub = "Dean"
		elif (num == 2):
			name_pub = "Jon"
		elif (num == 3):
			name_pub = "Vamsi"
		rospy.loginfo(name_pub)
		pub.publish(name_pub)
		rate.sleep()


if __name__ == '__main__':
	try:
		poly_talker()
	except rospy.ROSInterruptException:
		pass
