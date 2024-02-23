import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("#000000")  # Set the background color to black
screen.setup(width=800, height=600)  # Set the screen width and height
screen.title("Santa Claus")  # Set the window title

# Create the turtle
t = turtle.Turtle()  # Create a new turtle object
t.speed(0)  # Set the turtle's speed to 0 to make the drawing smooth
t.penup()  # Lift the pen so it doesn't draw when moving
t.hideturtle()  # Hide the turtle so we can see the drawing better

# Draw the hat
t.goto(0, 150)  # Move the turtle to the starting position for the hat
t.seth(0)  # Set the turtle's heading to 0 degrees
t.fillcolor("#FF0000")  # Set the fill color to red
t.pendown()  # Put the pen down to start drawing
t.begin_fill()  # Start filling the shape
for i in range(5):  # Draw the five stripes of the hat
    t.forward(30)
    t.left(90)
    t.forward(60)
    t.right(90)
t.penup()  # Lift the pen to stop drawing
t.goto(0, 210)  # Move the turtle to the starting position for the hat pom-pom
t.fillcolor("#FFFFFF")  # Set the fill color to white
t.pendown()  # Put the pen down to start drawing
t.begin_fill()  # Start filling the shape
t.circle(15)  # Draw the pom-pom
t.end_fill()  # Stop filling the shape

# Draw the face
t.penup()  # Lift the pen to stop drawing
t.goto(0, 100)  # Move the turtle to the starting position for the face
t.fillcolor("#FFCC99")  # Set the fill color to a light orange
t.pendown()  # Put the pen down to start drawing
t.begin_fill()  # Start filling the shape
t.circle(50)  # Draw a circle for the face
t.end_fill()  # Stop filling the shape

# Draw the eyes
t.penup()  # Lift the pen to stop drawing
t.goto(-20, 120)  # Move the turtle to the starting position for the left eye
t.fillcolor("#000000")  # Set the fill color to black
t.pendown()  # Put the pen down to start drawing
t.begin_fill()  # Start filling the shape
t.circle(5)  # Draw a circle for the left eye
t.end_fill()  # Stop filling the shape

t.penup()  # Lift the pen to stop drawing
t.goto(20, 120)  # Move the turtle to the starting position for the right eye
t.pendown()  # Put the pen down to start drawing
t.begin_fill()  # Start filling the shape
t.circle(5)  # Draw a circle for the right eye
t.end_fill()  # Stop filling the shape

# Draw the nose
t.penup()  # Lift the pen to stop drawing
t.goto(0, 110)  # Move the turtle to the starting position for the nose
t.fillcolor("#FF0000")  # Set the fill color to red
t.pendown()  # Put the pen down to start drawing
t.begin_fill()  # Start filling the shape

# Draw a triangle for the nose
t.goto(10, 0)
t.goto(-10, 0)
t.goto(0, 15)

t.end_fill()  # Stop filling the shape

# Draw the mouth
t.penup()  # Lift the pen to stop drawing
t.goto(0, 90)  # Move the turtle to the starting position for the mouth
t.pendown()  # Put the pen down to start drawing
t.seth(-45)  # Set the turtle's heading to -45 degrees
t.forward(20)  # Draw the left side of the mouth
t.penup()  # Lift the pen to stop drawing
t.goto(0, 90)  # Move the turtle to the starting position for the mouth
t.pendown()  # Put the pen down to start drawing
t.seth(45)  # Set the turtle's heading to 45 degrees
t.forward(20)  # Draw the right side of the mouth

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
