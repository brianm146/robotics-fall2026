# mission_1 Submission

- Name: Brian Mai
- Section: 01

## Explanations

### prediction

With too little Kp, I expect the arm to move too slowly to reach the target. With too little Kd, I expect the arm to move too quickly without slowing down fast enough when trying to reach the target.

### tuning_analysis

I predicted that a very small Kp would cause the arm to move too slowly towards the target and that a small Kd would cause the arm to move to quickly towards the target which might overshoot it. I changed the Kd, Ki, and Kd terms of the arm, increasing all of them, especially the Ki term so that the arm close in on the gap making it closer to the target. The hold phase showed the improvement with the arm stopping and holding nearly on top of the exact target. Gravity compensation helped hold the elbow more smoothly near the target when it was oscillating far off from the target before the gravity compensation for one of the poses.