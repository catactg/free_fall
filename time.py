# Time for an object to free fall from a given height
gravity = 9.81
height = 10
import math
time = math.sqrt(2 * height / gravity)
time_round = round(time, 2)
print("An object dropped from", height, "m reaches the ground after", time_round, "s")
