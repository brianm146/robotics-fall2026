"""Mission 2 student implementation.

Complete only ``transform_camera_point`` after preserving the initial AI output
in the guide. Course tests supply both real and simulated TF buffers.
"""

from geometry_msgs.msg import PointStamped
import tf2_geometry_msgs  # Registers PointStamped TF2 conversions.
# from tf2_ros import Buffer, TransformException
import tf2_ros

def transform_camera_point(tf_buffer, point: PointStamped) -> PointStamped | None:
    """Return a hall_camera point expressed in base_link, or None if unavailable."""
    
    if point.header.frame_id != "hall_camera":
        raise ValueError(
            f"Expected point in 'hall_camera', "
            f"got '{point.header.frame_id}'"
        )

    try:
        return tf_buffer.transform(
            point,
            "base_link",
        )
    except (
        tf2_ros.LookupException,
        tf2_ros.ConnectivityException,
        tf2_ros.ExtrapolationException,
        tf2_ros.TransformException
    ):
        return None