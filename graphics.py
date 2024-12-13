import turtle

# Create a turtle object
pen = turtle.Turtle()
pen.speed(100)

# Define colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Draw a circle for each color
for i in range(500):
    pen.color(colors[i % len(colors)])  # Cycle through colors
    pen.circle(140)                    # Draw a circle of radius 100
    pen.right(500)                      # Rotate 10 degrees

# Keep the window open
turtle.done()