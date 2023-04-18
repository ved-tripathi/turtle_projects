import turtle
import pdb
import time
#import graph_2

#z = turtle.Turtle()
f = open('maths_based_design_data_base_arm3.txt','a+')
t = turtle.Turtle()
scr = turtle.Screen()
turtle.color('black')
scr.bgcolor("#2ff702")
t.pensize(3)
t.hideturtle()
t.penup()                                                  #    {universal};{uncomment}
t.goto(0,43*2)
init_pos = t.pos()
#t.pendown()  # to be commented after removing triple quotes
t.speed('fastest')

def circle_about_a_point(radius, centre = type(tuple),angle_of_deviation = 30):
    global s
    s = turtle.Turtle()
    #s.pensize(2)
    s.speed('fastest')
    s.hideturtle()
    s.penup()
    s.goto(centre)                                          #   even comment
    s.rt(angle_of_deviation)
    s.fd(radius)
    #s.lt(90)
    s.pendown()
    s.circle(-radius,2)



def sec_circle_implementation(angle):
    global n,var_include_in_lst
    if angle == 1:
        n = 30
        circle_about_a_point(40*2,t.pos(),n)
        
    elif angle == 2:                                             #    even comment
        n = 150
        circle_about_a_point(40*2,t.pos(),n)

    elif angle == 3:
        n = 270
        circle_about_a_point(40*2,t.pos(),n)
    var_include_in_lst = n
    
inc_var = 0
sec_circle_implementation(int(input("enter arm number: ")))     #     even comment
lst_n = []

'''n = 30
inc_var = 0
lst_n = []
#l = 150
#m = 270
t.circle(-43*2,1)                                              #     {universal};{comment}
circle_about_a_point(40*2,t.pos(),n)
#circle_about_a_point(40*2,t.pos(),l)
#circle_about_a_point(40*2,t.pos(),m)'''
'''t.circle(-43*2,1)
circle_about_a_point(40*2,t.pos(),n)
lst_n.append(s.pos())
print(s.pos())
if var_include_in_lst == 30:
    final_data_30_1 = lst_n
elif var_include_in_lst == 150:
    final_data_150_2 = lst_n
elif var_include_in_lst == 270:
    final_data_270_3 = lst_n'''

for i in range(7213): #while t.pos() != init_pos: }replace to this after successful run                                      
    t.circle(-43*2,1) # 7213 is btained by running the arm 2 progam and printing the number of iterations performed to decrease the complexity
    circle_about_a_point(40*2,t.pos(),n)
    lst_n.append(s.pos())
    print(s.pos())
    if var_include_in_lst == 30:
        final_data_30_1 = lst_n
    elif var_include_in_lst == 150:
        final_data_150_2 = lst_n
        f.write(f'\n{s.pos()}')
    elif var_include_in_lst == 270:
        final_data_270_3 = lst_n
        f.write(f'\n{s.pos()}')#     even comment
    n += 2.65
    print(i)
#    inc_var += 1
    
print(lst_n)
print(t.pos())

    

'''final_data = [(-70.22,44.63), (-70.56,47.95), (-70.74,51.33), (-70.76,54.75), (-70.61,58.22), (-70.30,61.72), (-69.83,65.24), (-69.19,68.78), (-68.37,72.32), (-67.39,75.87), (-66.23,79.41), (-64.90,82.94), (-63.40,86.45), (-61.73,89.92), (-59.89,93.35), (-57.88,96.74), (-55.71,100.07), (-53.36,103.34), (-50.86,106.53), (-48.19,109.65), (-45.37,112.68), (-42.40,115.62), (-39.27,118.46), (-36.00,121.19), (-32.59,123.80), (-29.04,126.29), (-25.36,128.65), (-21.55,130.88), (-17.63,132.97), (-13.59,134.91), (-9.44,136.70), (-5.19,138.34), (-0.85,139.81), (3.59,141.11), (8.10,142.24), (12.68,143.20), (17.34,143.98), (22.04,144.58), (26.80,144.99), (31.60,145.21), (36.44,145.25), (41.30,145.09), (46.18,144.74), (51.06,144.20), (55.95,143.46), (60.83,142.53), (65.69,141.40), (70.53,140.07), (75.33,138.55), (80.09,136.84), (84.80,134.94), (89.45,132.85), (94.04,130.57), (98.55,128.11), (102.97,125.46), (107.31,122.64), (111.55,119.64), (115.68,116.48), (119.69,113.15), (123.59,109.65), (127.36,106.00), (130.99,102.21), (134.48,98.26), (137.83,94.18), (141.02,89.97), (144.06,85.63), (146.93,81.17), (149.63,76.60), (152.16,71.92), (154.51,67.15), (156.67,62.29), (158.65,57.34), (160.45,52.33), (162.04,47.24), (163.45,42.10), (164.66,36.91), (165.66,31.68), (166.47,26.41), (167.08,21.13), (167.48,15.82), (167.68,10.52), (167.68,5.21), (167.47,-0.09), (167.07,-5.36), (166.46,-10.61), (165.65,-15.82), (164.65,-20.99), (163.45,-26.11), (162.06,-31.16), (160.49,-36.14), (158.72,-41.05), (156.78,-45.87), (154.65,-50.60), (152.36,-55.23), (149.89,-59.75), (147.26,-64.16), (144.48,-68.44), (141.54,-72.60), (138.45,-76.63), (135.23,-80.51)]
t.penup()
t.goto(final_data[0])
t.pendown()                                                    #    odd comment
for i in final_data[1:-1]:
    t.goto(i)'''
    
    
    
#************************1.075**************= ratio of bigger line to smaller line
