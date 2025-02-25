quetions = {
     "What is 2 + 2?": {
        "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
        "answer": "B"
    },
    "What color is the sky on a clear day?": {
        "options":[
            "A) Red", "B) Blue", "C) Green", "D) Yellow"],
        "answer": "B"
    },
    "How many legs does a spider have?": {
        "options": ["A) 6", "B) 7", "C) 8", "D) 9"],
        "answer": "C"
    },
    "What sound does a cow make?": {
        "options":  ["A) Meow", "B) Bark", "C) Moo", "D) Quack"],
        "answer": "C"
    },
    "What is the opposite of 'hot'?": {
        "options":  ["A) Warm", "B) Cold", "C) cool", "D) Boiling"],                        
        "answer": "B"
    }
}


score = 0

for q, corrects in quetions.items():
    print("\n" + q)
    for option in corrects['options']:
        print(option)

    answer = input("Enter an option from A to D: ").strip().upper()
    if answer == corrects["answer"]:
        print("Correct answer")
        score += 1
    else:
        print("Incorect answer")


total_questions = len(quetions)
print(f"\nYour final score: {score}/{total_questions}")

# # Loop through the questions
# for q, detail


