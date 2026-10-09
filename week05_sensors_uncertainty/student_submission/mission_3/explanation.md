# Mission 3

## Assistive.prediction_draft

I think that the scenarios that will challenge this policy are the ones where there are sudden changes since the window of 9 is large. I think that the error rates will decrease compared to the first baseline policy since the window of valid readings is increased from 3 to 9 and the delay will also stay the same as the baseline at 0 even through the window of valid readings is large at 9 since the weight of sensor A, which is fast, is high at 0.75.

## Warehouse.prediction_draft

I think that the scenarios that will challenge this policy are the ones in which outliers are problematic which can cause the robot to make unnecessary stops and perform late stops since the weight on sensor A is high at 0.9. I think that the error rates might increase, but the delay will decrease as compared to the policy with a window of 7, but a weight of 0.75 because the larger weight of 0.9 on sensor A will make the readings more noisy, but also faster.

## context_comparison

The final warehouse policy and the final assistive policy differ in their false-safe rates, maximum detection delays, and unnecessary-stop rates. The final assistive policy has both a lower false-safe rate at 0 compared to 0.0185 for the final warehouse policy and a lower maximum detection delay at 0 compared to 0.05 for the final warehouse policy, but has a higher unnecessary-stop rate of 0.0338 compared to 0 for the final warehouse policy. The lower false-safe rates and lower maximum detection delay can make it safer for people as the robot will detect people faster and be less likely to move near and hit them. Moreover, the higher unnecessary-stop rate can also be safer for people, not risking hitting them, but can reduce the amount of useful work that the robot is doing.

## error_costs

In the warehouse setting, the robot bore the false-safe costs with a baseline false-safe rate of 0.0062 and a false safe-rate of 0.0185 for the revised results compared to the false-safe rate of 0 in the assistive setting for both the baseline and revised results. In the assistive setting, the robot bore the unnecessary-stop costs with both the baseline and revised results having an unnecessary-stop rate of 0.0338 compared to the baseline unnecessary-stop rate of 0.051 being reduced to 0 in the revised results for the warehouse setting.

## limitations

These seven tests establish that the robot can react effectively to various basic scenarios like the path being clearly safe with no obstacles in the way, conflicting sensor values to fuse, and when there is some stationary danger in the way of the robot, but does not establish that the robot performs well in every possible scenario. One stakeholder of importance to consult could be people in wheelchairs which the robot has to navigate safety around and one additional test before deployment could be multiple moving objects instead of just testing stationary dangers.
