# Mission 1

## bias

0.239

## bias_vs_variance

My prediction was correct since for this biased reading, the variance stayed around the same as a true reading, with the variance being very small at 0.014 and the mean differed from the true mean distance with a large bias of 0.239. Bias and variance describe different failures since bias describes how much the readings are shifted from the actual true mean distance while the variance describes how spread out the readings are from the actual mean distance.

## dropouts

3

## mean

2.239

## median

2.22

## more_samples

More samples would not remove this sensor's main problem because all the readings in the distribution charts that are made are all shifted a certain distance from the true distance so the sample mean distance would remain around the same at 2.239 m since there is a bias in the readings of 0.239 m.

## outliers

6

## prediction

For biased readings, the variance would stay the same, but the mean and bias would change because the spread of the readings would stay the same, but the actual mean distance would be shifted from the actual true distance. For noisy readings, the bias and the mean would stay the same since the readings are still centered around the true distance but the variance would change since the readings would be more spread out.

## prediction_draft

For biased readings, the variance would stay the same, but the mean and bias would change because the spread of the readings would stay the same, but the actual mean distance would be shifted from the actual true distance. For noisy readings, the bias and the mean would stay the same since the readings are still centered around the true distance but the variance would change since the readings would be more spread out.

## profile

biased

## robot_consequence

One robot decision that this imperfection could change would be the forward movement of the robot even when it detects a person in front of it. Since the bias causes the mean distance to overshoot at 2.239 m instead of the true target distance of 2 m, the robot risks hitting a person that is in front of it which can be dangerous.

## variance

0.014
