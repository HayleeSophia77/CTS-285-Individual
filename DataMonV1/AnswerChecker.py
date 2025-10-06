# Importing necessary library
import operator

# A dictionary of operators and their corresponding functions
operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

# Function to check the user's input answer
def check_answer(problem):
    try:
        # Split the user input into components (e.g., "4+4=8")
        # Find the position of '=' and separate the user answer
        equation, user_answer = problem.split('=')
        
        # Split the equation into the first number, operator, and second number
        # Example: "4+4" -> "4", "+", "4"
        for operator_symbol in operators.keys():
            if operator_symbol in equation:
                first_num, second_num = equation.split(operator_symbol)
                first_num = float(first_num)
                second_num = float(second_num)
                break
        else:
            print("Invalid equation format.")
            return False
        
        # Perform the calculation using the operator
        operator_function = operators[operator_symbol]
        correct_answer = operator_function(first_num, second_num)

        # Compare the user's answer with the correct answer
        if float(user_answer) == correct_answer:
            print("Correct!")
            return True
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")
            return False

    except Exception as e:
        print(f"Error: {e}")
        return False

# Main function to run the program
def run_math_quiz():
    score = 0  # Initialize score
    problem_count = 0  # Keep track of how many problems have been entered

    while problem_count < 10:  # Ask for 10 problems
        print(f"\nProblem {problem_count + 1}:")
        
        # Ask the user to enter the math problem with answer (e.g., "4+4=8")
        problem = input("Enter a math problem (e.g., 4+4=8): ").strip()

        # Check the answer for the entered problem
        if check_answer(problem):
            score += 1  # Increment score if correct
        
        problem_count += 1  # Increment problem count

    # After 10 problems, show the score
    print(f"\nYou answered {score} out of 10 problems correctly!")
    
    # Ask if the user wants to try again or exit
    while True:
        retry = input("Do you want to try again? (y/n): ").strip().lower()
        if retry == 'y':
            run_math_quiz()  # Restart the quiz
            break
        elif retry == 'n':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

# Run the quiz
run_math_quiz()
