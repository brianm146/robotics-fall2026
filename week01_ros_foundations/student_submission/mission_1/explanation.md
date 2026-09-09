# Mission 1

## Command Path Explanation

A proposed command travels on /student_cmd_vel. The guard receives the proposed command and decides if the command is allowed to reach the robot. Then the guard publishes the allowed command to /cmd_vel.

## Graph Explanation

A ROS 2 graph shows the relationship between the different software components and shows how these components communicate with each other. One node from this mission is /ros_gz_bridge and one topic from this mission is /scan.

## Guided Checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## Scan Observation

I found that range_max is 3.5, which represents the maximum distance of an object from the robot.

## Tools Explanation

Gazebo is responsible for handling the physics for the virtual world, like motion, wheels, and sensor readings while RViz is responsible for displaying the information like robot position and sensor readings, but doesn't simulate any of the physics
