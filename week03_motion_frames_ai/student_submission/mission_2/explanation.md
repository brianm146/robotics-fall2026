# Mission 2

## Frame Context

The rear-camera transform stays fixed while the hallway-camera-to-base_link transform changes as the robot moves because the rear camera is attached to the robot so as base_link changes as the robot moves, so does the rear camera by the same amount. However, since the hallway camera is fixed while the robot is moving and the hallway camera isn't attached to the robot, the hallway-camera-to-base_link transform will change whenever the robot moves.

## Improved Changes

The improved prompt changes its use of TF by importing all of tf2_ros and tf2_geometry_msgs so that tf2_ros can transform PointStamped messages. The improved prompt handles the failure behavior by only accepting a point if the header.frame_id is "hall_camera" and raising a ValueError otherwise and returning None if the transform is unavailable (i.e., catching a TransformException). The improved prompt also changes the source/target frames by assuming that the camera publishes geometry_msgs.msg.PointStamped with an id of hall_camera and does not publish any robot motion from the frames and changes timestamp handling by transforming using when the camera observed the point (i.e., the point's timestamp) instead of using the newest transform.

## Initial Analysis

Some assumptions are that the camera is assumed to publish geometry_msgs/PointStamped in its frame camera_link and the robot is assumed to publish its camera-to-robot TF. Some other omissions are which timestamp is used, what exceptions are raised when there are unavailable transforms, and if this converted point is published to any robot motion topics.

## Initial Output

Assuming the camera publishes a `geometry_msgs/PointStamped` in its optical frame (e.g. `camera_link`), the standard ROS 2 approach is to use **TF2** to transform that point into `base_link`.

```
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PointStamped
from tf2_ros import Buffer, TransformListener
from tf2_geometry_msgs import do_transform_point

class PointTransformer(Node):
    def __init__(self):
        super().__init__('point_transformer')

        # TF2 buffer + listener
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        # Point detected by the hallway camera
        self.subscription = self.create_subscription(
            PointStamped,
            '/camera/detected_point',
            self.point_callback,
            10
        )

        # Transformed point in base_link
        self.publisher = self.create_publisher(
            PointStamped,
            '/base_link/detected_point',
            10
        )

    def point_callback(self, point_msg: PointStamped):
        try:
            # Transform from the point's frame to base_link.
            transform = self.tf_buffer.lookup_transform(
                'base_link',                  # target frame
                point_msg.header.frame_id,    # source frame
                rclpy.time.Time()
            )

            transformed_point = do_transform_point(
                point_msg,
                transform
            )

            self.publisher.publish(transformed_point)

            self.get_logger().info(
                f'Point in base_link: '
                f'x={transformed_point.point.x:.3f}, '
                f'y={transformed_point.point.y:.3f}, '
                f'z={transformed_point.point.z:.3f}'
            )

        except Exception as e:
            self.get_logger().warn(
                f'Could not transform point: {e}'
            )

def main(args=None):
    rclpy.init(args=args)

    node = PointTransformer()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
```

 ### How it works

 If the camera detects:

```
PointStamped
  frame_id = "camera_link"
  point = (1.2, 0.3, 2.0)
```

 and TF contains:

```
base_link
   |
   └── camera_link
```

 then:

```
lookup_transform(
    'base_link',
    'camera_link',
    ...
)
```

 gets the transform between the two frames, and:

```
do_transform_point(point_msg, transform)
```

 applies the translation **and rotation** to produce the point in `base_link`.

 Make sure your robot is actually publishing the camera-to-robot TF, typically through `robot_state_publisher` or a static transform publisher. You can verify the TF tree with:

```
ros2 run tf2_tools view_frames
```

 and inspect a particular transform with:

```
ros2 run tf2_ros tf2_echo base_link camera_link
```

 You may need the `tf2_geometry_msgs` dependency in your ROS 2 package.

## Initial Prompt

Write ROS 2 Python code that converts a point detected by the hallway camera into the robot's base_link frame.

## Initial Source

#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PointStamped
from tf2_ros import Buffer, TransformListener
from tf2_geometry_msgs import do_transform_point


class PointTransformer(Node):
    def __init__(self):
        super().__init__('point_transformer')

        # TF2 buffer + listener
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        # Point detected by the hallway camera
        self.subscription = self.create_subscription(
            PointStamped,
            '/camera/detected_point',
            self.point_callback,
            10
        )

        # Transformed point in base_link
        self.publisher = self.create_publisher(
            PointStamped,
            '/base_link/detected_point',
            10
        )

    def point_callback(self, point_msg: PointStamped):
        try:
            # Transform from the point's frame to base_link.
            transform = self.tf_buffer.lookup_transform(
                'base_link',                  # target frame
                point_msg.header.frame_id,    # source frame
                rclpy.time.Time()
            )

            transformed_point = do_transform_point(
                point_msg,
                transform
            )

            self.publisher.publish(transformed_point)

            self.get_logger().info(
                f'Point in base_link: '
                f'x={transformed_point.point.x:.3f}, '
                f'y={transformed_point.point.y:.3f}, '
                f'z={transformed_point.point.z:.3f}'
            )

        except Exception as e:
            self.get_logger().warn(
                f'Could not transform point: {e}'
            )


def main(args=None):
    rclpy.init(args=args)

    node = PointTransformer()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

## Live Issue

The error was that the evaluator returned point:null even though all five tests passed and the tf2_echo shows the transform between "hall_camera" and "base_link". I tried sync the timing of for them to see if it was a timing issue. The live transform remains unverified even though tf2_echo shows the transform after a few seconds.

## Live Pending

True

## Snapshot

{'captured_at': '2026-09-24T15:47:35.603574+00:00', 'frame_chain': ['hall_camera', 'odom', 'base_link', 'base_scan', 'rear_camera_link'], 'frames': ['odom', 'base_link', 'base_scan', 'rear_camera_link', 'hall_camera'], 'point_prompts': {'hall_camera_point': 'Transform point (0.5, 0.0, 0.0) from hall_camera to base_link.'}, 'schema_version': 2, 'source': 'live', 'transformed_points': {'hall_camera_point_in_base': {'x': -9.602645760038367e-09, 'y': -1.5}, 'rear_camera_point_in_base': {'x': -1.18, 'y': -1.0206624774663903e-11}, 'scan_point_in_base': {'x': 0.968, 'y': 0.0}}, 'transforms': {'base_scan_to_base_link': {'translation': {'x': -0.032, 'y': 0.0, 'z': 0.172}, 'yaw': 0.0}, 'hall_camera_to_base_link': {'translation': {'x': -9.59986379379943e-09, 'y': -2.0, 'z': 1.19}, 'yaw': 1.5707963268004606}, 'rear_camera_to_base_link': {'translation': {'x': -0.18, 'y': 0.0, 'z': 0.22}, 'yaw': -3.1415926535795866}}}

## Synthesis

The initial AI output assumed which timestamp was used for the transform and the behavior if there are unavailable transformations. Also, the camera was assumed to publish geometry_msgs/PointStamped. The improved prompt changed the program by adding exceptions that caught any TransformException and returned None, didn't command any robot motion, and preserved and used the point's timestamp for the transformation. The improved prompt also made it so that only points produced by a header.frame_id that is "hall_camera" would be accepted, returning a ValueError otherwise. If the wrong transform were used, the robot could harm the people around it. Since its estimations of its location relative the hall_camera is wrong, the robot might accidentally crash into someone, not giving the person enough time to react. The tests that detect that problem are tests 2 and 3 which ensures that the robot doesn't publish motion and that None is returned when a transformation is unavailable, respectively. When the transform data is unavailable and None is returned, the robot should stay stationary and not make any movements.
