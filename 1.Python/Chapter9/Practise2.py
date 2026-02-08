import random

def game():
    print("You are playing the game")
    score = random.randint(1, 100)

    try:
        with open("Game2.txt", "r") as f:
            highScore = f.read()
            highScore = int(highScore) if highScore else 0
    except FileNotFoundError:
        highScore = 0

    if highScore >= 100:
        highScore = 0

    print(f"Your Score: {score}")
    print(f"High Score: {highScore}")

    if score > highScore:
        with open("Game2.txt", "w") as f:
            f.write(str(score))
        print("🎉 New High Score!")

    return score

game()
