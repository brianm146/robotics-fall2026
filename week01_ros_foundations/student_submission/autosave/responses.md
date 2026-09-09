# Week 1: Discovering a Robot Through ROS 2

## Student

- Name: Brian Mai
- Email: BRIAN.MAI74@login.cuny.edu

## final.architecture_evidence

The evidence that supports calling my node reactive is that the decision of the robot was made only based on whether the LiDAR reported that an object was too close. Some sort of map and planner would need to be added to create routes around the object would have to be added for a genuinely hybrid system.

## final.course_reflection

This activity made me realize that I am interested in working with hardware more. It made me think about how challenging designing a robot or coherent system is since there are more problems to consider other than the technical ones. This activity made me more motivated to work with hardware more in the future although I'm not sure if it will be strictly robotics that I would want to work on. In connecting technical work with human, ethical, and societal considerations, many tasks could be made more efficient and could also be used to improve current services like sanitation and public libraries. The consideration for slippery floors stood out to me because I was thinking more about sensor failures rather than environmental differences.

## final.hardware_next

Before using the behavior on hardware, I would test other environments that have special surroundings like slippery floors or loud noises to see if the robot works just as well in those types of environments.

## final.middleware_debugging

The ROS graph would help you diagnose a command that never reaches the robot by using the commands to determine the connections between the different nodes that the command has to travel through by looking at their subscribers and publishers and determining where the command stops traveling.

## final.system_synthesis

Robotics software is difficult because a robot is composed of a complex system of components in order to sense, decide, and act. Since the robot must interact with the physical world and will affect people and society, many ethical concerns like safety, accessibility, and privacy must be addressed. Also, technical problems such as inaccurate sensors which can be affected by noise, bias, delay, or simply not being able to do a reading, determining appropriate speeds and navigation, and environmental challenges like slippery floors can make robotics software more difficult. The architecture that I implemented was a reactive architecture,  where the robot immediately acted on the action of stopping once the sensor detected an object that was too close. The trade-offs of this architecture is that it doesn't need to store a map or plan of its surroundings which makes the response time of it faster. However, once the robot has sensed an object and stopped, it doesn't know how to continue and finish the rest of its tasks without any of the stored data. ROS 2 middleware connected the /ros_gz_bridge node, the /course_cmd_vel_guard node, the /student_cmd_vel node, the /cmd_vel node, and /scan. /student_cmd_vel is a subscriber of /course_cmd_vel_guard and /cmd_vel is a publisher of /course_cmd_vel_guard. A proposed command would come through /student_cmd_vel into /course_cmd_vel_guard and the approved command would be published to /cmd_vel. Also, /cmd_vel is a subscriber of /ros_gz_bridge and /ros_gz_bridge is a publisher of /scan. Timing affected safety because if the timing of the data was delayed, the robot would be using old data which resulted in the robot stopping after desired stopping line and could collide into a person. Invalid data affected safety since we are unable to determine whether something might actually be in the way or not, risking a collision so it forces us to stop the robot immediately when invalid  data is detected. A separate safety layer could restrict unsafe motion by checking the proposed command and issuing a safety override if the command is unsafe.

## final.timing_evidence

The sensor-failure result that most affected my understanding of robot safety was the delay in which a measurement may take to arrive resulting in late and dangerous responses to that measurement.

## mission_1.command_path_explanation

A proposed command travels on /student_cmd_vel. The guard receives the proposed command and decides if the command is allowed to reach the robot. Then the guard publishes the allowed command to /cmd_vel.

## mission_1.graph_explanation

A ROS 2 graph shows the relationship between the different software components and shows how these components communicate with each other. One node from this mission is /ros_gz_bridge and one topic from this mission is /scan.

## mission_1.guided_checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## mission_1.scan_observation

I found that range_max is 3.5, which represents the maximum distance of an object from the robot.

## mission_1.tools_explanation

Gazebo is responsible for handling the physics for the virtual world, like motion, wheels, and sensor readings while RViz is responsible for displaying the information like robot position and sensor readings, but doesn't simulate any of the physics

## mission_2.measurement_explanation

I choose the non-modified curved trial. They describe different measurements because the estimated traveled path also adds small movements reported by odometry to the distance. The start-to-end distance is only the distance for the straight line between the starting and ending positions of the robot.

## mission_2.modified_settings

{'linear_x': 0.12, 'angular_z': 0.2, 'duration': 4.0}

## mission_2.motion_comparison

I choose the straight trial. The measured motion was close to my prediction, but it wasn't exact. The measured motion was 0.415 meters while my prediction was 0.45 meters.

## mission_2.prediction_locks

{'curve': '2026-09-09T03:05:03.382947+00:00', 'curve_modified': '2026-09-09T03:15:50.286304+00:00', 'rotation': '2026-09-09T03:02:47.296323+00:00', 'straight': '2026-09-09T03:01:01.777667+00:00'}

## mission_2.predictions

{'curve': 'I predict a curve-shaped arc to the right because the robot is moving forward while also turning to the right.', 'curve_modified': 'This curve should be wider and turn the other way because the turn radius is bigger and the turning speed is positive.', 'rotation': 'I predict its position will stay the same while its direction will be 1.5 radians to the left of its initial direction.', 'straight': 'I predict the robot will finish 0.45 meters ahead of its starting point.'}

## mission_2.safety_explanation

The command guard checks the proposed driving commands to make sure that they are within the bounds and allowed for the robot. The final zero command indicates that the trial is finished, forcing the robot into a complete stop. The timeout is needed if there is a problem with a program crashing or if there is data from communication stops while the robot is still in motion.

## mission_3.data_to_command

My two functions turn a list of LiDAR distances into a move-or-stop command by first processing the distances through the front_distance() function to determine the nearest finite and positive reading in the front sector. Then, the decide_velocity() function takes the distance and determines whether to move or stop depending on the distance to the object.

## mission_3.missing_data_safety

The robot stops when there is no valid front measurement instead of treating the path as clear because the invalid measurement may come from various areas, like faulty sensors which could incorrectly detect whether an object is present. The safest approach when the measurement is unknown is to simply stop the robot.

## mission_3.system_layers

My decision functions, the supplied ROS node, and the command guard work together by first having the supplied ROS node receive the readings from LiDAR on /scan and then calling the decision functions to process those readings and decide whether to move or stop. The result is then published to the command guard.

## part_1.activity

{'sensor': {'normal': True, 'changed': True}, 'timing': {'normal': True, 'changed': True}, 'hardware': {'normal': True, 'changed': True}}

## part_2.activity

{'reactive': {'normal': True, 'changed': True}, 'behavior': {'normal': True, 'changed': True}, 'deliberative': {'normal': True, 'changed': True}, 'hybrid': {'normal': True, 'changed': True}, 'safety': {'normal': True, 'changed': True}}

## part_3.activity

{'middleware': {'single': True, 'multiple': True}, 'communication': {'topic': True, 'service': True}, 'failure': {'healthy': True, 'sensor': True, 'type': True, 'visualization': True}, 'inspection': {'nodes': True, 'node_info': True, 'topics': True, 'topic_info': True, 'echo': True, 'services': True, 'broken': True}}
