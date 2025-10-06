import random
import time

def electro_flash():
    print("⚡ Welcome to Electro Flash! ⚡")
    print("Practice your multiplication tables the fun way.\n")

    # Step 1: Pick the table (only one input attempt)
    try:
        table = int(input("Pick a multiplication table (e.g. 2 for 2-times table): "))
    except ValueError:
        print("Invalid input. Starting with 2-times table by default.")
        table = 2

    print(f"\nGreat! Let's practice the {table}-times table.")
    print("You'll get 5 problems. Each problem gives you 2 tries.\n")
    
    # Step 2: Start timer
    start_time = time.time()
    score = 0
    total_questions = 5

    # Loop through problems
    for i in range(1, total_questions + 1):
        num = random.randint(1, 12)  # ask up to 12
        correct_answer = table * num
        tries = 2
        got_it = False

        for attempt in range(tries):
            try:
                answer = int(input(f"Problem {i}: {table} x {num} = "))
                if answer == correct_answer:
                    print("✅ Correct!\n")
                    score += 1
                    got_it = True
                    break
                else:
                    print("❌ Try again.")
            except ValueError:
                print("Please enter a number.")

        if not got_it:
            print(f"Answer was {correct_answer}\n")

    # Step 3: End game and show results
    end_time = time.time()
    elapsed = round(end_time - start_time, 2)

    print("⚡ Game Over! ⚡")
    print(f"Your score: {score} / {total_questions}")
    print(f"Time taken: {elapsed} seconds")

# Run the game
electro_flash()
