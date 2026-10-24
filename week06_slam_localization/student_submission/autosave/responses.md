# Week 6: SLAM and Mapping

- email: BRIAN.MAI74@login.cuny.edu
- name: Brian Mai

## final.course_reflection

This activity made me realize that I still very interested in robotics and other related work like embedded systems. This activity made me more motivated to do similar kinds of work in the future since I found this activity very interesting and fun. The value that I see in connecting technical work with human, ethical, and societal considerations is the ability to help humans with tasks that they find difficult like using the robot using map from this activity to help guide blind people around certain areas. Something that stood out to me about the activity was the duplicated walls when using the second route since I thought it would have corrected itself like in the first route since it spent more time traversing and revisiting certain areas in the house.

## final.synthesis

From the map using the first route, the robot can know where the entrance is, where the walls for every single room is, and the existence of the two tables, garbage cans, and left side shelves, but cannot know about what is beyond the tables in the large rooms of the house and where the shelf is on the right side of the house. From the map using the second route, the robot can know where all the tables, garbage cans, and shelves are and what is at every area of the house, but cannot know where the entrance is and where the exact walls for certain rooms and corridors are since some of the walls are duplicated. In the map from the first route, there was bad LiDAR coverage because of the tables blocking its line of sight and resulting in bad coverage of the areas beyond that point, a map correction of the wall on a revisit to the corridor above the entrance, and visible map limitations at the points passed the tables in the big rooms since there is little coverage there. In the map from the second route, there was good LiDAR coverage on the whole house since the route explored it fully and no map corrections on revisits with duplicated walls left over which are visible map limitations. The mapping time of the first route was less than the second route since it had a shorter path to traverse, but both had motion-estimate errors with the final pose of the robot on the map being further than in real-time. I would trust the map using the first route more for a later task because the map is more accurate with no duplicated walls even though it has less coverage.

## mission_1.drift_and_revisit

When I returned to an area that I had already scanned, the new scan did end up lining up with its mapped walls. An old wall visibly shifted to the correct position on the map upon the revisit to that area. After exploring the right side rooms of the house and revisiting the intersection near the entrance, the mapped walls ended up lining up with the new scan.

## mission_1.limitations

An area that remained unknown when I stopped is the middle region to the left and up from the entrance to the house which is seen in the gray area to the left and up from the opening at the bottom which is the entrance of the house in my RViz screenshot. My route left that gap by not fully going up into that area to go explore it more and the LiDAR's line of sight left that gap by not being able to fully determine that area because of the table there that was blocking the LiDar's line of sight on what is behind it.

## mission_1.route.original_prediction

My route is to is drive straight from the starting point, go into the house, then turn right and drive up into the room at the top on the right side, then drive out of the room and drive down into the room at the bottom on the right side, and finally drive to the left into the top the area on the left and drive into the bottom room. The place that I will revisit is the intersection between the left and right side of the house at the entrance of the house. I think that the map coverage may be weak in the middle region to the left of the entrance inside the house since there is a table there that may prevent exploration there since I don't drive fully into that area.

## mission_1.route.prediction_draft

My route is to is drive straight from the starting point, go into the house, then turn right and drive up into the room at the top on the right side, then drive out of the room and drive down into the room at the bottom on the right side, and finally drive to the left into the top the area on the left and drive into the bottom room. The place that I will revisit is the intersection between the left and right side of the house at the entrance of the house. I think that the map coverage may be weak in the middle region to the left of the entrance inside the house since there is a table there that may prevent exploration there since I don't drive fully into that area.

## mission_2.comparison

In the table above, the first route has an elapsed time of 12 minutes while the second route has an elapsed time of 13 minutes. The first route has a known area of 79.29 m^2 and a quality score of 72.7 while the second route has a known area of 83.37 m^2 and a quality score of 79.7. For the time spent, I think that the first route gave more useful coverage because it took less time and had an accurate map. My prediction was supported because the second route was slower than the first route and had more coverage than the first route. However, even though the second route had more coverage, the entrance seems to be missing and there is some duplicated walls in the map of the second route and it took longer than the first route. The tradeoff between speed and map quality is that a faster time can result in less coverage of the map, but more coverage of the map can lead to a slower time.

## mission_2.map_choice

I would trust the map using the first strategy more for a later robot task because even though there is less coverage around the tables in both the left and right side of the map, the map using the first strategy is more accurate with clear wall alignment while the map using the second strategy has the entrance to the house missing and has duplicated walls for the top room on the right side of the house, near the entrance of the house, and near the entrance of the bottom room in the left side of the house. One limit of what these map images and numbers can prove is geometric correctness in which the walls are exactly correct with extremely precise placement.

## mission_2.strategy.original_prediction

My new route will differ from the Mission 1 route by driving further into the rooms, traveling around the table on the right side of the house in order to reach the bottom room on the right side of the house, and traveling more around the table in the area of intersection going left and up from the entrance of the house. Even though the route of visiting the rooms from right to the left remains the same, the route and areas that the robot is visiting in order to get to each room is different. I think that this second route will map the accessible space slower than than first route because it takes a longer path to reach each room leading to more time needed, but I think that the second route will produce a clearer map because the route is traversing more areas and thus covering more ground for the map.

## mission_2.strategy.prediction_draft

My new route will differ from the Mission 1 route by driving further into the rooms, traveling around the table on the right side of the house in order to reach the bottom room on the right side of the house, and traveling more around the table in the area of intersection going left and up from the entrance of the house. Even though the route of visiting the rooms from right to the left remains the same, the route and areas that the robot is visiting in order to get to each room is different. I think that this second route will map the accessible space slower than than first route because it takes a longer path to reach each room leading to more time needed, but I think that the second route will produce a clearer map because the route is traversing more areas and thus covering more ground for the map.
