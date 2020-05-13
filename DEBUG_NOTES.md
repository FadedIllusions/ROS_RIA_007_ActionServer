What The F**k!
--------------
roswtf

Check Launch File
-----------------
roswtf launch_file_name.launch

By default, roswtf checks two ROS fields:
  * File System Issues: Environmental variables, launch files, etc. 
  * Online/Graph Issues: Inconsistencies in connections between nodes,
    topics, actions, etc. (Not necessarily errors.)



ROS Logs:
---------
ROS logs have five logging levels, with each level including deeper levels.(In example, if you use the Error level, both Error and Fatal messages will be shown.)
  * Debug => rospy.logdebug(msg, args)
  * Info => rospy.loginfo(msg, args)
  * Warn => rospy.logwarn(msg, args)
  * Error => rospy.logerr(msg, args)
  * Fatal => rospy.logfatal(msg, *args)

Read all logs issued:
```rostopic echo /rosout```

Or, use the GUI:
```rqt_console```

The rqt_console is divided into three subpanels:
  * Panel One: Outputs Logs. Has data about the message, severity/level, the node generating the message, etc.
  * Panel Two: Allows you to filter the messages issued on first panel, excluding them based on criteria such as node, severity level, or keyword.
  * Panel Three: Allows you to highligh certain messages, while showing the others.



RQT Plot:
---------
What if you need to know if your speed, inclination, or torque readings are correct? Or if your laser is having anomalous readings? Let's use a graphical tool to receive our data in real-time:

```rqt_plot```



RQT Graph:
----------
Is your node connected to the right place? Why aren't you receiving data from a topi? rqt_graph displays a visual graph of nodes running in ROS and their topic connects.



ROSBags:
--------
ROSBags record all of the data passed through the ROS topics system and allows you to replay it any time through a simple file.

```rosbag record -O name_bag_file.bag name_topic_to_record_1 name_topic_to_record2 name_top...```

Extact General Info
-------------------
```rosbag info name_bag_file.bag```

Replay Bag File
---------------
```rosbag play name_bag_file.bag```

Note: Replaying data will make the rosbag publish the same topics with the same data, at the same time when the data was recorded. Can either ```rostopic echo /topic_name``` to echo the recorded values or ```rqt_plot /topic_name``` for a real-time plot.

Record ALL Topics:
------------------
```rosbag record -a```



RViz:
-----
RViz is a tool that allows you to visualize Images, PointClouds, Lasers, Kinematic Transforms, RobotModels, etc. You can even define your own markers.

Launch RViz
-----------
rosrun rviz rviz


