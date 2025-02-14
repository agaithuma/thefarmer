import turtle as t

# Create a turtle screen
screen = t.Screen()

# Set up the turtle
track_drawer = t.Turtle()
track_drawer.speed(1)  # Set the drawing speed (adjust as needed)

# Define track segments with lengths for a continuous F1 circuit
track_segments = [
    ("Start-Finish Straight", 400),
    ("Turn 1 (Hairpin Right)", 100),
    ("Straight", 150),
    ("Turn 2 (Medium Left)", 75),  # Left turn
    ("Straight", 200),
    ("Turn 3 (Chicane Right-Left)", 50),  # Right turn
    ("Straight", 300),
    ("Turn 4 (High-Speed Sweeper)", 150),
    ("Straight", 80),
    ("Turn 5 (Medium Right)", 75),  # Left turn
    ("Straight", 100),
    ("Turn 6 (Medium Left)", 75),  # Left turn
    ("Finish Straight", 200),  # Leads to Start-Finish Straight
]

# Initialize the total distance and starting position
total_distance = 0
x, y = 0, 0
track_drawer.penup()
track_drawer.goto(x, y)
track_drawer.pendown()

# Draw the track with segments and straights
for item in track_segments:
    segment_name = item[0]
    distance = item[1]
    total_distance += distance
    track_drawer.forward(distance)
    x, y = track_drawer.pos()
    track_drawer.write(f"{segment_name}\n{total_distance} meters", align="center")

# Close the drawing window when clicked
screen.exitonclick()
