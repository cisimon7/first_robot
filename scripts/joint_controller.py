import rospy

from sensor_msgs.msg import JointState

joint_state = JointState()

if __name__ == '__main__':
    joint_pub = rospy.Publisher("/joint_states", JointState, queue_size=1)
    rospy.init_node('robot_controller')

    joint_state.name = ['base_link_to_base_2_linear', 'base_head_to_upper_arm', 'upper_arm_to_lower_arm']

    rate = rospy.Rate(20)
    new = 0

    while not rospy.is_shutdown():
        joint_state.header.stamp = rospy.Time.now()
        new += 0.01
        joint_state.position = [new, 0, 0]
        joint_pub.publish(joint_state)
        rate.sleep()
