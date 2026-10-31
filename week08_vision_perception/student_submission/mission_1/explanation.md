# mission_1

## diagnosis
The two images that I'm comparing are normal_1 and dim_1. For normal_1, the box is on the mug, but for dim_1, the box is not on the mug. For normal_1, the detector selected that region because most of the pixels lie on the mug for the mask, the largest contour is around the mug, and most of the pixels with that specific value/brightness of 25 to 70 lie on the mug. However, for dim_1, the detector missed that region because most of the pixels lie on the desk near the mug for the mask, the largest contour is around parts of the desk near the mug, and most of the pixels on the mug don't match the value/brightness level of 25 to 70 in the dimmer environment.

## limitations
During practice, the single parameter that I changed was the value/brightness from 25 to 180 to 25 to 70. The thing that changed in the selected box was that the box became smaller and specifically more around the mug rather than including parts of the desk or notepad because the range for pixels with that lower amount of brightness shrunk, filtering out pixels from the desk and notepad. The limitation that still remains for a different cup or background is if a different cup or background has pixels of different color or brightness, then the detector won't be able to recognize many pixels that lie on the cup when it should.
