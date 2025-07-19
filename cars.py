import turtle

class Car:
    def __init__(self, color, x, y, scale=1.0):
        self.color = color
        self.x = x
        self.y = y
        self.scale = scale
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(0)  # Fastest drawing
        
    def draw(self):
        self.turtle.penup()
        self.turtle.goto(self.x, self.y)
        self.turtle.pendown()
        self.turtle.color(self.color)
        
        # Draw car body
        self.turtle.begin_fill()
        self.turtle.setheading(0)
        for _ in range(2):
            self.turtle.forward(100 * self.scale)
            self.turtle.left(90)
            self.turtle.forward(40 * self.scale)
            self.turtle.left(90)
        self.turtle.end_fill()
        
        # Draw car top
        self.turtle.penup()
        self.turtle.goto(self.x + 15 * self.scale, self.y + 40 * self.scale)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.setheading(0)
        for _ in range(2):
            self.turtle.forward(70 * self.scale)
            self.turtle.left(90)
            self.turtle.forward(30 * self.scale)
            self.turtle.left(90)
        self.turtle.end_fill()
        
        # Draw wheels
        wheel_positions = [
            (self.x + 20 * self.scale, self.y - 10 * self.scale),
            (self.x + 80 * self.scale, self.y - 10 * self.scale)
        ]
        
        for pos in wheel_positions:
            self.turtle.penup()
            self.turtle.goto(pos)
            self.turtle.pendown()
            self.turtle.color("black")
            self.turtle.begin_fill()
            self.turtle.circle(15 * self.scale)
            self.turtle.end_fill()
        
        self.turtle.penup()

# Set up the screen
screen = turtle.Screen()
screen.title("Simple Cars with Turtle")
screen.bgcolor("lightgray")

# Create and draw two cars
car1 = Car("red", -150, 0, 1.0)
car2 = Car("blue", 50, 0, 1.5)

car3 = Car("green", 150, 100, 3)

car1.draw()
car2.draw()
car3.draw()

# Hide turtles and display
turtle.done()