import turtle

def koch_curve(t, length, depth):
    """Recursive function to draw a Koch curve."""
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, depth - 1)
        t.left(60)
        koch_curve(t, length, depth - 1)
        t.right(120)
        koch_curve(t, length, depth - 1)
        t.left(60)
        koch_curve(t, length, depth - 1)

def draw_snowflake(t, length, depth):
    """Draws a geometric Koch snowflake using 3 Koch curves."""
    for _ in range(3):
        koch_curve(t, length, depth)
        t.right(120)

def main():
    # User-defined screen parameters and RGB background fills
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.colormode(255)
    screen.bgcolor(20, 20, 40) # Dark RGB background
    screen.title("Turtle Fractal Renderer")

    # Custom drawing pen setup
    pen = turtle.Turtle()
    pen.speed(0) # Fastest rendering
    pen.color((0, 255, 150)) # Vibrant RGB vector graphics
    pen.pensize(2)
    
    # Directional movements and positioning
    pen.penup()
    pen.goto(-150, 100) 
    pen.pendown()

    # Render recursive fractal
    draw_snowflake(pen, 300, 4) # Length 300, recursion depth 4

    pen.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()