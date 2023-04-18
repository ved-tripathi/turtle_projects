import turtle

t = turtle.Turtle()
with open('maths_based_design_data_base_arm3.txt') as f:
    arm3 = [tuple(map(float, i.split(','))) for i in f]

print(arm3)

t.hideturtle()
t.speed('fastest')
t.penup()
t.goto(arm3[0])
t.pendown()
for i in arm3[1:-1]:
    t.goto(i)

print(len(arm3))
