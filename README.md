# ROS_RIA_007_ActionServer

In this exercise, we are creating a package with an action server that moves the AR Drone in a square. (Example package named as_ex with a dependency of rospy.)

  1. The size of the side of the square should be specified in the goal message as an integer.
  2. The feedback should publish the current side (as a number) while traversing the square.
  3. Result should publish total number of seconds it took drone to complete the square.
  4. Use Test.action message for action server. (Use ```find /opt/ros/kinetic/ -name Test.action``` to find where message is defined.)
  
  Once Action Server Launched, Use Separate Terminal To Run ```rostopic pub /move_drone_square_as/goal actionlib/TestActionGoal TAB-TAB``` And Edit To 'Goal: 2'.
