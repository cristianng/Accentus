#!/usr/bin/env python
import roslib 
roslib.load_manifest('rosaria')
import rospy
from geometry_msgs.msg import Twist
import curses.wrapper
import curses

def talker(screen):
	rover=rospy.Publisher('/RosAria/cmd_vel',Twist)
	pub=rospy.Publisher('/cmd_vel',Twist)
	rospy.init_node('keyboard_vel_cmd')
	twist=Twist()
	twist2=Twist()
	while not rospy.is_shutdown():
		key=screen.getch()
		screen.refresh()
		if key == curses.KEY_UP:
			twist.linear.x=2.0
			twist2.linear.x=0.0001
		elif key == curses.KEY_DOWN:
			twist.linear.x=-2.0
			twist2.linear.x=-0.0001
		elif key == curses.KEY_RIGHT:
			twist.angular.z=-1.0
			twist2.angular.z=-0.01
		elif key == curses.KEY_ENTER:
			twist.angular.z=0
			twist2.angular.z=0
		elif key == curses.KEY_LEFT:
			twist.angular.z=1.0
			twist2.angular.z=0.01
		else:
			twist=Twist()
			twist2=Twist()
		pub.publish(twist)
		rover.publish(twist)
#		rospy.sleep(0.1)
		
if __name__=='__main__':
	try:
		curses.wrapper(talker)
	except rospy.ROSInterruptException:
		print "exception raised"
		pass

