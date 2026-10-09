# Mission 2

## comparison

For the three window differences in the moving average configurations, the larger the window, the larger the numerical error as seen with a rmse of 0.1378 for the window of 3, a rmse of 0.1448 for the window of 5, and a rmse of 0.1507 for the window of 7. The larger windows also had a larger max error with a window of 7 having a max error of 1.1929. There is no delay differences with all the windows having a response delay of 1.1. For the matched median/moving-average pair with the same window of 3 and the same weight of 0.25, the numerical error was larger for the median with a rmse of 0.1413 compared to the moving-average with a rmse of 0.1378. The max error for the median was also greater at 1.229. There are no delay differences between the matched median/moving-average pair with both having a response delay of 1.1.

## fusion_choice

The greater the fusion weight is for sensor A, the greater the mean absolute error and max error with a mae of 0.0718 and max error of 1.229 for a weight of 0.25, a mae of 0.0732 and max error of 1.3493 for a weight of 0.5, and a mae of 0.0849 and a max error of 1.4697 for a weight of 0.75. However, the rmse seems to be smaller for larger values of weight. For a weight of 0.25, the readings might be less noisy since sensor A has a smaller weight, but might be more biased because of the higher weight for sensor B. For a weight of 0.5, the readings will be somewhat noisy and somewhat biased since the weight for both sensor A and sensor B are equal. For a weight of 0.75, the readings will be more outlier-prone and noisy due to the larger weight of sensor A, but less biased due to the smaller weight of sensor B.

## manual_average

4.167

## manual_fusion

2.25

## manual_median

2.3

## prediction_draft

I think that this configuration compared to the configuration of using the median with a window of 3 valid readings and a weight of 0.5 would increase error, but decrease response delay since the higher weight on sensor A of 0.75 would cause the fast, but noisy readings of sensor A to be more impactful. The other settings are the same so they would lead to the same impact on error and response delay compared to this configuration.

## responsiveness

Smoothing means that the noise is reduced since a window of previous readings is used. Even though the smoothing can reduce the noise, it can increase the amount of measured delays. Responsiveness means how quickly the robot can react to something with little to no delay. Even though good responsiveness can result in little to no delay, the readings can be noisy and inaccurate since the most recent readings are to be used. The delay could affect the amount of time the person has to respond to an incoming robot, possibly giving the nearby person more time to move out of the robot's path.

## selected

5
