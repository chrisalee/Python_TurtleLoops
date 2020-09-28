from turtle import *

# for i in range(1, 50):
#     forward(5*i)
#     left(90)


for i in range(5, 250, 5):  #There is also a way to make the loop counter itself jump in increments of 5: the command range can accept a third argument, after the start and stop values, namely, a step size. So the previous spiral can also be drawn like this:
    forward(i)
    left(90)

bye()