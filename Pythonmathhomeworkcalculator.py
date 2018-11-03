# Ask the user to enter the math problem
problem = input("Enter a math problem, or 'q' to quit:")
# Keep going until the user presses 'q' to quit
while (problem != "q"):
    # Show the problem and answer using eval
    print("The answer to", problem, "is:", eval(problem))

    # Ask for another math problem
    problem = input("Enter another math problem of press 'q' to quit: ")

    # This loop will keep on going, until the user presses 'q' for quit

