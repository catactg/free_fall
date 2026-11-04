# Time for an object to free fall from a given height
gravity = 24.79
height = 10
import math
time = math.sqrt(2 * height / gravity)
time_round = round(time, 2)
print("A stone dropped from", height, "m hits the ground after", time_round, "s")
