from turtle import Turtle, Screen

turtle = Turtle()


def spirograph(marker, diameter, angle_shift):
    """
    Makes a spirograph using the turtle library
    marker - turtle object
    diameter - diameter of the circle
    angle_shift - the angle shift after each circle
    """
    marker.speed("fastest")
    original_circle = 360 / angle_shift
    num_rotations = 0
    num_circles = original_circle
    while round(num_circles, 4) != int(round(num_circles, 4)):
        num_rotations += 1
        num_circles = original_circle*num_rotations
    print(num_circles)
    print(num_rotations)
    for _ in range(int(num_circles)):
        marker.circle(diameter / 2)
        marker.left(angle_shift)


spirograph(turtle, 150, 61)

screen = Screen()
screen.exitonclick()
