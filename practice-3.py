import turtle

graph = turtle.Turtle()

dot_distance = 25
width = 5
height = 7

graph.penup()

for y in range(height):
    for i in range(width):
        graph.dot()
        graph.forward(dot_distance)
    graph.backward(dot_distance * width)
    graph.right(90)
    graph.forward(dot_distance)
    graph.left(90)

turtle.done()