# Autosaved responses

- Name: Brian Mai
- Student ID: BRIAN.MAI74@login.cuny.edu
- Section: 01

## Check-in answers

### m3_prediction

I predict that increasing forward speed could increase the tracking error and lower the pedestrian clearance, risking hitting the pedestrian. I predict that too little derivative control would also increase the tracking error and lower the pedestrian clearance by failing to slow down quick enough, potentially hitting and harming the pedestrian.

### m3_technical

I predicted that both increasing forward speed and too little derivative control can increase tracking error and lower pedestrian clearance which was correct since it was causing the robot to go off course getting closer to the pedestrian safety zones. The next route point becomes a heading command by having the robot compute the needed heading based on error in order to reach the next route point without going into the pedestrian safety zone. The PID changes steering by using the heading error to determine how much to turn through the P term, closing the gap from the accumulated heading error through the I term, and slowing down the robot turning when it gets close to the next route point through the D term. The inaccurate wheel radius can make a well-tuned controller follow the wrong physical path because if the wheel radius is too small, it will undershoot the actual distance traveled and if the wheel radius is too large, it will overshoot the actual distance traveled.

### m3_human

The most consequential failure for a pedestrian would be the robot going to fast, hitting and harming the person. A clearance and speed trade-off would be the robot having a low clearance making it easier to hit a pedestrian, but having a very high speed robot. The engineer is responsible for verifying that decision before deployment through testing in real-world scenarios to ensure that the robot maintains a good speed while also preventing any dangerous speeds that could endanger the pedestrian.

### final_reflection

This activity made me realize that I'm very interested in robotics and other engineering related work. This activity made me feel more motivated to do other similar kinds of work in the future involving the design of robots. The value that I see in connecting technical work with human, ethical, and societal considerations is providing people with helpful robots that help them complete tasks more efficiently while also maintaining trust and safety between the robot and people. The idea of tuning and making sure that the robot behaves similarly to its estimates through testing stood out in this activity because I was observing how much the robot was off its target before tuning it and how different the estimates were from the actual path of the robot.

## Mission explanations

### mission_3

**technical_analysis**: I predicted that both increasing forward speed and too little derivative control can increase tracking error and lower pedestrian clearance which was correct since it was causing the robot to go off course getting closer to the pedestrian safety zones. The next route point becomes a heading command by having the robot compute the needed heading based on error in order to reach the next route point without going into the pedestrian safety zone. The PID changes steering by using the heading error to determine how much to turn through the P term, closing the gap from the accumulated heading error through the I term, and slowing down the robot turning when it gets close to the next route point through the D term. The inaccurate wheel radius can make a well-tuned controller follow the wrong physical path because if the wheel radius is too small, it will undershoot the actual distance traveled and if the wheel radius is too large, it will overshoot the actual distance traveled.

**human_centered_analysis**: The most consequential failure for a pedestrian would be the robot going to fast, hitting and harming the person. A clearance and speed trade-off would be the robot having a low clearance making it easier to hit a pedestrian, but having a very high speed robot. The engineer is responsible for verifying that decision before deployment through testing in real-world scenarios to ensure that the robot maintains a good speed while also preventing any dangerous speeds that could endanger the pedestrian.
