cmake_minimum_required(VERSION 3.0.2)
project(first_robot)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  rviz
  sensor_msgs
  std_msgs
  tf
  urdf
  xacro
)

catkin_package( )

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  scripts/joint_controller.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)