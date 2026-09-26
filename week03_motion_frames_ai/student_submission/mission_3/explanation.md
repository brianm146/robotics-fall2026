# Mission 3

## Assigned Pattern

alternating_arcs

## Original Output

Assuming the existing `Segment` constructor is `Segment(linear_x, angular_z, duration)`, this implementation uses the minimum allowed forward speed, which keeps the required angular rate below the `0.80 rad/s` limit.

```
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
```

 ### Assumptions

 - `Segment` accepts `(linear_x, angular_z, duration)` in that order.
- A positive `angular_z` represents the required initial positive 45° turn.
- Each segment represents exactly 45° of heading change:
  - `+45°`
  - `-45°`
  - `+45°`
  - `-45°`
- The radius is `0.30 m`, so `ω = v/r = 0.22/0.30 ≈ 0.7333 rad/s`.
- Each duration is approximately `1.071 s`, since the arc length is `0.30π/4 ≈ 0.236 m`.
- Total duration is approximately `4.283 s`, well below the 60-second limit.
- The alternating signed turns cancel to zero net heading change, so the robot finishes facing its initial direction.
- I would leave the course wrapper and its final zero command unchanged.

 ### Tests I would add/run

```
import math
import pytest

def test_alternating_arcs():
    segments = build_pattern("alternating_arcs")

    assert len(segments) == 4

    for segment in segments:
        assert segment.duration > 0
        assert segment.duration <= 30.0
        assert 0.0 < segment.linear_x <= 0.22
        assert abs(segment.angular_z) <= 0.80

    assert [s.angular_z > 0 for s in segments] == [
        True, False, True, False
    ]

    total_duration = sum(s.duration for s in segments)
    assert total_duration <= 60.0

    # Each arc turns 45 degrees.
    for segment in segments:
        assert math.isclose(
            abs(segment.angular_z) * segment.duration,
            math.pi / 4,
            rel_tol=1e-9,
        )

    # Net heading change is zero.
    net_heading = sum(s.angular_z * s.duration for s in segments)
    assert math.isclose(net_heading, 0.0, abs_tol=1e-9)

def test_unknown_pattern():
    with pytest.raises(ValueError):
        build_pattern("not_a_pattern")
```

 The chosen `0.22 m/s` is intentional: with a `0.30 m` radius it produces `0.733 rad/s`, satisfying the angular-speed limit while exactly meeting the stated lower/upper linear-speed bound. The four short arcs also give substantial margin under the per-segment and total-duration requirements.

## Original Prompt

This is a ROS 2 Jazzy Python package. Implement only build_pattern(pattern_name: str) -> list[Segment] for 'alternating_arcs' in the existing pattern.py.
The course-provided pattern_node.py calls this function, publishes the returned segments repeatedly through /student_cmd_vel, and sends the final zero command.
Use the existing Segment class with linear_x (m/s), angular_z (rad/s), and duration (s).
Return the ordered segments for the assigned specification and raise ValueError for an unknown pattern name.
Stay within 0.22 m/s, 0.80 rad/s, 30 seconds per segment, and 60 seconds total.
Do not replace the wrapper or course checks. Explain assumptions and propose tests.

This is the specification:
The intended sequence of the robot is to perform alternating arcs with four forward arcs, starting with positive 45 degrees and alternating the sign for each turn while keeping the turning at 45 degrees with each arc having a radius of 0.30 meters. The speeds should be bounded between 0.22 m/s and 0.80 m/s. The robot should stop after performing the four arcs and facing the initial direction. Some measurable success criteria is ensuring that only positive durations are used, the robot moves at most 30 seconds per each segment and that it takes at most 60 seconds total for all the segments, and that this sequence is done in a 2 m by 2 m area.

## Original Source

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

## Saved Specification

The intended sequence of the robot is to perform alternating arcs with four forward arcs, starting with positive 45 degrees and alternating the sign for each turn while keeping the turning at 45 degrees with each arc having a radius of 0.30 meters. The speeds should be bounded between 0.22 m/s and 0.80 m/s. The robot should stop after performing the four arcs and facing the initial direction. Some measurable success criteria is ensuring that only positive durations are used, the robot moves at most 30 seconds per each segment  and that it takes at most 60 seconds total for all the segments, and that this sequence is done in a 2 m by 2 m area.

## Specification

The intended sequence of the robot is to perform alternating arcs with four forward arcs, starting with positive 45 degrees and alternating the sign for each turn while keeping the turning at 45 degrees with each arc having a radius of 0.30 meters. The speeds should be bounded between 0.22 m/s and 0.80 m/s. The robot should stop after performing the four arcs and facing the initial direction. Some measurable success criteria is ensuring that only positive durations are used, the robot moves at most 30 seconds per each segment  and that it takes at most 60 seconds total for all the segments, and that this sequence is done in a 2 m by 2 m area.

## Assumptions

Some assumptions that the AI made about motion, units, frames, or timing are that the motion segments' constructor is Segment(linear_x, angular_z, duration), the allowed forward speed of 0.22 m/s is to be used, that a positive angular_z represented the initial positive 45 degrees turn, each duration is about 1.071 seconds, totaling to 4.283 seconds for the 4 segments, and that all the alternating turns would cancel out, resulting in the robot facing its initial direction. It also assumes that course wrapper and the final zero velocity command remains the same so that those components don't have to implemented here.

## Problems

Some errors, omissions, or uncertain claims that I identified was whether the robot is performing the sequence in a 2 m by 2 m area and whether rounding errors with the calculations of movement and duration could affect the sequence. Even though the code initially looked correct, I checked whether all the speeds and durations stayed within the bounded requirements and checked the calculations to make sure that they were correct.

## Test Plan

A pattern behavior test would check whether the there are exactly 4 segments, that for each segment the angle calculated with angular_z and duration is actually 45 degrees, and whether the robot is facing its initial direction after all its segments by checking if the sum of its turns is a multiple of 360 degrees (i.e., 0 degrees). It would only return true if all these conditions are true. A velocity-limit test would check whether for every segment, the linear_x is bounded between 0 and 0.22 m/s and whether the abs(angular_z) is at most 0.80 rad/s. The test would return true if these conditions are met. The stop test would return true if after completing the 4 segments of the pattern, the robot would stop with a linear_x and angular_z both equal to 0 m/s and 0 rad/s, respectively.

## Modifications

The significant change that I made was changing the linear_x velocity from 0.22 m/s down to 0.15 m/s which also changed my angular_z velocity down from about 0.73 rad/s down to 0.5 rad/s with the required radius of 0.3 m and also changed my duration for each segment from about 1.071 seconds up to about 1.571 seconds and the total duration for all 4 segments from about 4.28 seconds to about 6.28 seconds. The reason for this was that after the change, the duration constraint was still met and reducing the linear_x velocity and therefore also the angular_z velocity prevents the speeds from going over the limit due to difference in measured motion due to environmental issues.

## Live Pending

False

## Evidence Analysis

The important tests establish that there is exactly 4 segments for this pattern, all the durations were positive, the linear_x speeds were bounded by 0 and 0.22 m/s, the angular_z speeds were limited to 0.80 rad/s, each of the forward arcs derived from the segments were 45 degrees with a radius of 0.30 meters, the duration for each segment was at most 30 seconds, the total duration for all segments was at most 60 seconds, the segments followed the correct order of alternating angles (i.e., positive, negative, positive, negative), and the robot finished facing its initial direction by testing that its net heading was 0 degrees. My robot passed those tests resulting in a starting pose of 0.77 degrees and an ending pose of 0.78 degrees and a position_error of 0.072 and heading_error of 0.018 for the final checkpoint due to measured motion due to measured motion differences. These tests do not establish whether or not this sequence is performed in a 2 m by 2 m area. One additional test I would need is to check the initial position of the robot to create the 2 m by 2 m area around it and then check if the position at any point ever outside of the bounding box.

## Ai Disclosure

The AI tool that I used was ChatGPT in order to implement initial code for the build_pattern(pattern_name: str) -> list[Segment] function for the alternating arcs command, explain its assumptions in this implementation, and and propose some test ideas to test the function. I personally reviewed that the initial code performed the pattern correctly, that all the constraints were followed, and the assumptions and tests which were proposed. I also reviewed the calculations performed by the initial code to check whether or not they were correct. I changed the linear_x velocity from 0.22 m/s down to 0.15 m/s in order to ensure that measured motion differences doesn't cause my motion to exceed speed limits.
