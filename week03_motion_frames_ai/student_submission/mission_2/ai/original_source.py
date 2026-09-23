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