"""AI-assisted motion pattern implementation.

Preserve the original AI response in Streamlit. Review it, then implement a safe
version here. The node accepts only segments returned by ``build_pattern``.
"""
from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Segment:
    linear_x: float
    angular_z: float
    duration: float

def build_pattern(pattern_name: str) -> list[Segment]:
    """Return ordered, bounded motion segments for the assigned pattern.

    Supported assignments are ``rounded_rectangle``, ``l_path``, and
    ``alternating_arcs``. Do not include the final stop; the ROS wrapper always
    publishes it and the evaluator verifies it.
    """

    if pattern_name == "alternating_arcs":
        import math

        radius = 0.30          # m
        linear_x = 0.15        # m/s
        turn_angle = math.pi / 4  # 45 degrees

        # v = r * omega => omega = v / r
        angular_z = linear_x / radius  # 0.5 rad/s

        # Arc length = r * theta; duration = arc length / speed.
        duration = (radius * turn_angle) / linear_x

        # Four 45-degree arcs: +45, -45, +45, -45 degrees.
        return [
            Segment(linear_x, +angular_z, duration),
            Segment(linear_x, -angular_z, duration),
            Segment(linear_x, +angular_z, duration),
            Segment(linear_x, -angular_z, duration),
        ]

    raise ValueError(f"Unknown pattern name: {pattern_name}")


