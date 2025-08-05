balls = ["white"]
while True:
    x = 0
    your_ball_clr = input("Enter the ball color: ")
    while x < len(balls):
        my_ball_clr = balls[x]
        if (my_ball_clr == your_ball_clr):
            your_ball_clr = input("I've this one, Enter another color: ")
            x = 0
            continue
        x += 1
    balls.append(your_ball_clr)
    print(f"\nAdded to my balls: {balls}\n")