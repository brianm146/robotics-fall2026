def build_pattern(pattern_name: str) -> list[Segment]:
    if pattern_name == "alternating_arcs":
        import math

        radius = 0.30          # m
        linear_x = 0.22        # m/s
        turn_angle = math.pi / 4  # 45 degrees

        # v = r * omega => omega = v / r
        angular_z = linear_x / radius  # 0.7333... rad/s

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