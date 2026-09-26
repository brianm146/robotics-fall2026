import os
import unittest
from week03_pattern.pattern import build_pattern
import math

class MyPatternTests(unittest.TestCase):
    def test_my_pattern_geometry(self):
        segments = build_pattern(os.environ["WEEK03_ASSIGNED_PATTERN"])
        # Add assertions for your assigned pattern.
        self.assertEqual(len(segments), 4)
        for segment in segments:
            self.assertGreater(segment.linear_x, 0.0)
            self.assertLessEqual(segment.linear_x, 0.22)
            self.assertLessEqual(abs(segment.angular_z), 0.80)
            self.assertAlmostEqual(abs(segment.angular_z * segment.duration), math.pi / 4, places=7)
            self.assertAlmostEqual(abs(segment.linear_x / segment.angular_z), 0.3)
            self.assertGreater(segment.duration, 0.0)
            self.assertLessEqual(segment.duration, 30.0)

        self.assertLessEqual(sum(segment.duration for segment in segments), 60.0)

    def test_my_pattern_order(self):
        # Check another property with a known expected result.
        segments = build_pattern(os.environ["WEEK03_ASSIGNED_PATTERN"])
        self.assertTrue(segments[0].angular_z > 0)
        self.assertTrue(segments[1].angular_z < 0)
        self.assertTrue(segments[2].angular_z > 0)
        self.assertTrue(segments[3].angular_z < 0)
        self.assertAlmostEqual(sum(segment.angular_z for segment in segments), 0.0)

