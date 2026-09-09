# Mission 3

## Data To Command

My two functions turn a list of LiDAR distances into a move-or-stop command by first processing the distances through the front_distance() function to determine the nearest finite and positive reading in the front sector. Then, the decide_velocity() function takes the distance and determines whether to move or stop depending on the distance to the object.

## Missing Data Safety

The robot stops when there is no valid front measurement instead of treating the path as clear because the invalid measurement may come from various areas, like faulty sensors which could incorrectly detect whether an object is present. The safest approach when the measurement is unknown is to simply stop the robot.

## System Layers

My decision functions, the supplied ROS node, and the command guard work together by first having the supplied ROS node receive the readings from LiDAR on /scan and then calling the decision functions to process those readings and decide whether to move or stop. The result is then published to the command guard.
