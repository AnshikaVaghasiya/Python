import json
import random

# Sample quiz questions stored in a JSON-like dictionary
quiz_data = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Rome", "Berlin"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
    {"question": "In which country was ice cream invented?", "options": ["China", "Japan", "Russia", "New Zealand"], "answer": "China"},
    {"question": "Which country is known as the 'Land of the Rising Sun'?", "options": ["China", "South Korea", "Thailand", "Japan"], "answer": "Japan"},
    {"question": "Which country is often regarded as the oldest republic in the world?", "options": ["Greece", "Italy", "San Marino", "Switzerland"], "answer": "San Marino"},
    {"question": "What is the most widely consumed fruit in the world?", "options": ["Apple", "Banana", "Mango", "Kiwi"], "answer": "Mango"},
    {"question": "Which soft drink was originally created as a medicinal tonic?", "options": ["Coco-Cola", "Pepsi", "Sprite", "Fanta"], "answer": "Coco-Cola"},
    {"question": "Which flower symbolizes friendship and new beginning?", "options": ["Rose", "Lily", "Tulip", "Daffodil"], "answer": "Daffodil"},
    {"question": "How many hearts does an octopus have?", "options": ["1", "3", "5", "8"], "answer": "3"},
    {"question": "Which planet has a day longer than its year?", "options": ["Venus", "Mercury", "Neptune", "Mars"], "answer": "Venus"},
]

# Function to run the quiz
def run_quiz():
    score = 0
    random.shuffle(quiz_data)  # Shuffle questions for randomness
    
    for q in quiz_data:
        print("\n" + q["question"])
        for i, option in enumerate(q["options"], start=1):
            print(f"{i}. {option}")
        
        try:
            answer_index = int(input("Enter the number of your answer: ")) - 1
            if q["options"][answer_index] == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {q['answer']}")
        except (ValueError, IndexError):
            print("Invalid choice, moving to next question.")
    
    print(f"\nQuiz finished! Your final score is {score}/{len(quiz_data)}")

# Run the quiz
run_quiz()
