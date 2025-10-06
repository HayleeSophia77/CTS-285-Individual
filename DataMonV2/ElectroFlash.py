import random
import time

def electro_flash():
    print("⚡ Welcome to Electro Flash! ⚡")
    print("Practice your multiplication tables the fun way.\n")

    try:
        table = int(input("Pick a multiplication table (e.g. 2 for 2-times table): "))
    except ValueError:
        print("Invalid input. Defaulting to 2.")
        table = 2

    print(f"\nGreat! Let's practice the {table}-times table.")
    print("You'll get 5 problems. Each problem gives you 2 tries.\n")

    start_time = time.time()
    score = 0
    total_questions = 5

    for i in range(1, total_questions + 1):
        num = random.randint(1, 12)
        correct_answer = table * num
        got_it = False

        for attempt in range(2):
            try:
                ans = int(input(f"Problem {i}: {table} x {num} = "))
                if ans == correct_answer:
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

    elapsed = round(time.time() - start_time, 2)
    print(f"⚡ Game Over! ⚡\nScore: {score}/{total_questions}\nTime: {elapsed} seconds")

if __name__ == "__main__":
    electro_flash()
