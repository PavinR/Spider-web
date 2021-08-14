import turtle as t
import random

########### body fill method ########

def body_fill (x_start,x_stop,y_start,y_stop):
        for i in range(0,10):
                t.fillcolor("black")
                t.begin_fill()
                t.penup()
                x=random.randint(x_start,x_stop)
                y=random.randint(y_start,y_stop)
                t.setpos(x,y)
                t.pendown()
                t.circle(1)
                t.end_fill()

#####################


# define turtle speed
t.speed(2)
t.bgcolor("gray")


t.pencolor("darkkhaki")# Pen color

# radical thread
for i in range(6):
	t.forward(200)
	t.backward(200)
	t.right(60)

# spiral thread length
side = 150
# spider

# Pen colors
t.pencolor("darkkhaki")

# Spider web color
t.fillcolor("")

# building web
t.begin_fill()

for i in range(10):
	t.penup()
	t.goto(0,0)
	t.pendown()
	t.setheading(0)
	t.forward(side)
	t.right(120)

	for j in range(6):
		t.forward(side-2)
		t.right(60)
	side = side - 35

t.end_fill()

####    Spider  #############

t.setpos(0.00,0.00)
t.setheading(0)         # cursor angle to 0
t.pencolor("black")
t.fillcolor("olive")
t.begin_fill()
t.circle(8)
t.circle(-15)
t.end_fill()

####    Spider Eyes  #############

t.fillcolor("Black")
# Eye One
t.begin_fill()
t.penup()
t.setpos(-3,7)
t.pendown()
t.circle(2)
t.end_fill()

# Eye One
t.begin_fill()
t.penup()
t.setpos(3,7)
t.pendown()
t.circle(2)

t.penup()
t.end_fill()


#########    Body ink    #################

body_fill (-12,12,-25,-5)

t.hideturtle()          # hide cursor

####################
