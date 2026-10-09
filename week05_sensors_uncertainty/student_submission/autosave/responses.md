# Week 5: Sensors, Noise, and Uncertainty

- course_id: 24594274
- email: BRIAN.MAI74@login.cuny.edu
- name: Brian Mai

## concepts.observation

When I increased noise, the readings are all more scattered, with various distance readings plotted rather than having all the readings centered around a specific distance. However, when I increased bias, the readings weren't scattered and remained the same centered around a specific value. But, this centered value was a specific shift away from the actual true distance.

## final.course_reflection

I think that this activity made me think that I am very interested in robotics and like going through the process of designing robotics, looking at many different considerations.  This activity made me more motivated in doing similar kinds of work in the future like doing testing in order to determine the best reading estimations for different deployment contexts. The value that I see in connecting technical work with human, ethical, and societal considerations is the ability make daily tasks easier for people like the assistive robot in mission 3. The thing that stood out to me in this activity was the importance of good reading estimations because inaccurate readings due to noise, bias, or delay could be very dangerous and harmful towards people.

## final.synthesis

As seen in mission 1, certain measurement properties like mean, median, variance, bias, number of dropouts, and number of outliers can help identify issues in the sample reading data which can affect the estimation choices to be made in mission 2 in order to make the best estimations with little to no noise and little to no bias. For example, in mission 1, the low variance meant that the issue was not due to noise since the readings weren't that spread out, but the high bias measurement with both the mean and median being shifted from the true value, meaning that outliers were not cause, meant that the readings were biased. In order to solve these issues of noise and bias that can be identified through measurement properties, certain estimation choices made in mission 2 like using a median instead of a moving average to remove resist outliers, increasing the window of valid readings to make the readings smoother and reduce noise, but increase delay, and to increase weight on certain sensors like sensor A in the fused estimation to lower delay, but increase noise. The deployment context can also affect estimation choices as seen in mission 3 with the need for a large window of 9 and large weight on sensor A of 0.75 in the assistive setting in order to decrease noise and no delay to not risk hitting people, specifically people with varied mobility in this setting.

## mission_1.bias

0.239

## mission_1.bias_vs_variance

My prediction was correct since for this biased reading, the variance stayed around the same as a true reading, with the variance being very small at 0.014 and the mean differed from the true mean distance with a large bias of 0.239. Bias and variance describe different failures since bias describes how much the readings are shifted from the actual true mean distance while the variance describes how spread out the readings are from the actual mean distance.

## mission_1.dropouts

3

## mission_1.mean

2.239

## mission_1.median

2.22

## mission_1.more_samples

More samples would not remove this sensor's main problem because all the readings in the distribution charts that are made are all shifted a certain distance from the true distance so the sample mean distance would remain around the same at 2.239 m since there is a bias in the readings of 0.239 m.

## mission_1.outliers

6

## mission_1.prediction

For biased readings, the variance would stay the same, but the mean and bias would change because the spread of the readings would stay the same, but the actual mean distance would be shifted from the actual true distance. For noisy readings, the bias and the mean would stay the same since the readings are still centered around the true distance but the variance would change since the readings would be more spread out.

## mission_1.prediction_draft

For biased readings, the variance would stay the same, but the mean and bias would change because the spread of the readings would stay the same, but the actual mean distance would be shifted from the actual true distance. For noisy readings, the bias and the mean would stay the same since the readings are still centered around the true distance but the variance would change since the readings would be more spread out.

## mission_1.profile

biased

## mission_1.robot_consequence

One robot decision that this imperfection could change would be the forward movement of the robot even when it detects a person in front of it. Since the bias causes the mean distance to overshoot at 2.239 m instead of the true target distance of 2 m, the robot risks hitting a person that is in front of it which can be dangerous.

## mission_1.variance

0.014

## mission_2.comparison

For the three window differences in the moving average configurations, the larger the window, the larger the numerical error as seen with a rmse of 0.1378 for the window of 3, a rmse of 0.1448 for the window of 5, and a rmse of 0.1507 for the window of 7. The larger windows also had a larger max error with a window of 7 having a max error of 1.1929. There is no delay differences with all the windows having a response delay of 1.1. For the matched median/moving-average pair with the same window of 3 and the same weight of 0.25, the numerical error was larger for the median with a rmse of 0.1413 compared to the moving-average with a rmse of 0.1378. The max error for the median was also greater at 1.229. There are no delay differences between the matched median/moving-average pair with both having a response delay of 1.1.

## mission_2.fusion_choice

The greater the fusion weight is for sensor A, the greater the mean absolute error and max error with a mae of 0.0718 and max error of 1.229 for a weight of 0.25, a mae of 0.0732 and max error of 1.3493 for a weight of 0.5, and a mae of 0.0849 and a max error of 1.4697 for a weight of 0.75. However, the rmse seems to be smaller for larger values of weight. For a weight of 0.25, the readings might be less noisy since sensor A has a smaller weight, but might be more biased because of the higher weight for sensor B. For a weight of 0.5, the readings will be somewhat noisy and somewhat biased since the weight for both sensor A and sensor B are equal. For a weight of 0.75, the readings will be more outlier-prone and noisy due to the larger weight of sensor A, but less biased due to the smaller weight of sensor B.

## mission_2.manual_average

4.167

## mission_2.manual_fusion

2.25

## mission_2.manual_median

2.3

## mission_2.prediction_draft

I think that this configuration compared to the configuration of using the median with a window of 3 valid readings and a weight of 0.5 would increase error, but decrease response delay since the higher weight on sensor A of 0.75 would cause the fast, but noisy readings of sensor A to be more impactful. The other settings are the same so they would lead to the same impact on error and response delay compared to this configuration.

## mission_2.responsiveness

Smoothing means that the noise is reduced since a window of previous readings is used. Even though the smoothing can reduce the noise, it can increase the amount of measured delays. Responsiveness means how quickly the robot can react to something with little to no delay. Even though good responsiveness can result in little to no delay, the readings can be noisy and inaccurate since the most recent readings are to be used. The delay could affect the amount of time the person has to respond to an incoming robot, possibly giving the nearby person more time to move out of the robot's path.

## mission_2.selected

5

## mission_3.Assistive.prediction_draft

I think that the scenarios that will challenge this policy are the ones where there are sudden changes since the window of 9 is large. I think that the error rates will decrease compared to the first baseline policy since the window of valid readings is increased from 3 to 9 and the delay will also stay the same as the baseline at 0 even through the window of valid readings is large at 9 since the weight of sensor A, which is fast, is high at 0.75.

## mission_3.Warehouse.prediction_draft

I think that the scenarios that will challenge this policy are the ones in which outliers are problematic which can cause the robot to make unnecessary stops and perform late stops since the weight on sensor A is high at 0.9. I think that the error rates might increase, but the delay will decrease as compared to the policy with a window of 7, but a weight of 0.75 because the larger weight of 0.9 on sensor A will make the readings more noisy, but also faster.

## mission_3.context_comparison

The final warehouse policy and the final assistive policy differ in their false-safe rates, maximum detection delays, and unnecessary-stop rates. The final assistive policy has both a lower false-safe rate at 0 compared to 0.0185 for the final warehouse policy and a lower maximum detection delay at 0 compared to 0.05 for the final warehouse policy, but has a higher unnecessary-stop rate of 0.0338 compared to 0 for the final warehouse policy. The lower false-safe rates and lower maximum detection delay can make it safer for people as the robot will detect people faster and be less likely to move near and hit them. Moreover, the higher unnecessary-stop rate can also be safer for people, not risking hitting them, but can reduce the amount of useful work that the robot is doing.

## mission_3.error_costs

In the warehouse setting, the robot bore the false-safe costs with a baseline false-safe rate of 0.0062 and a false safe-rate of 0.0185 for the revised results compared to the false-safe rate of 0 in the assistive setting for both the baseline and revised results. In the assistive setting, the robot bore the unnecessary-stop costs with both the baseline and revised results having an unnecessary-stop rate of 0.0338 compared to the baseline unnecessary-stop rate of 0.051 being reduced to 0 in the revised results for the warehouse setting.

## mission_3.limitations

These seven tests establish that the robot can react effectively to various basic scenarios like the path being clearly safe with no obstacles in the way, conflicting sensor values to fuse, and when there is some stationary danger in the way of the robot, but does not establish that the robot performs well in every possible scenario. One stakeholder of importance to consult could be people in wheelchairs which the robot has to navigate safety around and one additional test before deployment could be multiple moving objects instead of just testing stationary dangers.
