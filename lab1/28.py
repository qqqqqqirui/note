import math

def draw_circle(radius):
    for y in range(-radius, radius + 1):
        for x in range(-radius, radius + 1):
            if math.sqrt(x**2 + y**2) <= radius + 0.5:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


draw_circle(5)
