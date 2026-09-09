# Mission 2

## Predictions

{'straight': 'I predict the robot will finish 0.45 meters ahead of its starting point.', 'rotation': 'I predict its position will stay the same while its direction will be 1.5 radians to the left of its initial direction.', 'curve': 'I predict a curve-shaped arc to the right because the robot is moving forward while also turning to the right.', 'curve_modified': 'This curve should be wider and turn the other way because the turn radius is bigger and the turning speed is positive.'}

## Prediction Locks

{'straight': '2026-09-09T03:01:01.777667+00:00', 'rotation': '2026-09-09T03:02:47.296323+00:00', 'curve': '2026-09-09T03:05:03.382947+00:00', 'curve_modified': '2026-09-09T03:15:50.286304+00:00'}

## Motion Comparison

I choose the straight trial. The measured motion was close to my prediction, but it wasn't exact. The measured motion was 0.415 meters while my prediction was 0.45 meters.

## Measurement Explanation

I choose the non-modified curved trial. They describe different measurements because the estimated traveled path also adds small movements reported by odometry to the distance. The start-to-end distance is only the distance for the straight line between the starting and ending positions of the robot.

## Safety Explanation

The command guard checks the proposed driving commands to make sure that they are within the bounds and allowed for the robot. The final zero command indicates that the trial is finished, forcing the robot into a complete stop. The timeout is needed if there is a problem with a program crashing or if there is data from communication stops while the robot is still in motion.

## Modified Settings

{'linear_x': 0.12, 'angular_z': 0.2, 'duration': 4.0}
