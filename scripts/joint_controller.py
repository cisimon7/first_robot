import rospy

from sensor_msgs.msg import JointState

joint_state = JointState()

if __name__ == '__main__':
    joint_pub = rospy.Publisher("/joint_states", JointState, queue_size=1)
    rospy.init_node('robot_controller')

    joint_state.name = ['base_link_to_base_2_linear', 'base_head_to_upper_arm', 'upper_arm_to_lower_arm']

    rate = rospy.Rate(20)
    new = 0
    new1 = 0
    new1_inc = True
    new2 = 0
    new2_inc = True

    while not rospy.is_shutdown():
        joint_state.header.stamp = rospy.Time.now()
        new += 0.01

        if new1 > 1.21:
            new1_inc = False
        elif new1 < 0.01:
            new1_inc = True

        if new1_inc:
            new1 += 0.01
            print(new1)
        else:
            print(new1)
            new1 -= 0.01

        if new2 > 1.04:
            new2_inc = False
        elif new2 < -2.04:
            new2_inc = True

        if new2_inc:
            new2 += 0.01
            print(new2)
        else:
            print(new2)
            new2 -= 0.01

        joint_state.position = [new, new1, new2]
        joint_pub.publish(joint_state)
        rate.sleep()
