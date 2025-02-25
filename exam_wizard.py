# # Project Overview:
# # Develop an Exam Wizard program in Python that hardcodes a set of at least 5 theory 
# # questions and evaluates the student's answers based on the presence of specific keywords or phrases. The program should ask these questions to the user one by one and display the user's score at the end.

# # Requirements:
# # Hardcode Questions and Keywords:
# # Create at least 5 theory questions.
# # For each question, determine the essential keywords or phrases that should be included in the ideal answer.
# # Assign weights to each keyword based on its importance.
# # Question Prompting:
# # Prompt the user with each question one by one.
# # Allow the user to input their answer for each question.
# # Scoring System:
# # Evaluate the user's answers based on the presence of the specified keywords..
# # Keep track of the user's score.
# # Display Results:
# # At the end of the quiz, display the user's total score out of the max score e.g. 10/12.
# Photosynthesis (2 points)
# Light energy (1 point)
# Chemical energy (1 point)
# Chloroplasts (2 points)
# Chlorophyll (1 point)
# Carbon dioxide (1 point)
# Water (1 point)
# Glucose (1 point)
# Oxygen (1 point)
# ATP (1 poin


questions = {
    "what is photosytensis?": {
        "keywords":["Photosynthesis", "Light energy", "Chemical energy", "Chloroplasts", "Chlorophyll", "Carbon dioxide", "Water", "Glucose", "Oxygen", "ATP"]
    },
    "Define noun": {
        "keywords":["name","person","animal","place","things"]
    }, 
    "What is a mass": {
        "keywords": ["weight","space"]
    },
    "What is a verb": {
        "keywords":["action","words"]
    },
    "qoute john 3 vs 16":{
        "keywords":["God","love","world","son","perish","everlasting", "life"]
    }
}


def grade_answers(question, answer):
    keywords = questions.get(question, {}).get("keywords", [])
    correct_keywords = [keyword for keyword in keywords if keyword.lower() in answer.lower()]
    total_keywords = len(keywords)
    score = len(correct_keywords)
    return score, total_keywords, correct_keywords



for question in questions:
    print(question)
    stuudent_answer = input("Enter your answer: ")
    score, total, correct = grade_answers(question, stuudent_answer)
    print(f"Score: {score}/{total} - Keywords correct: {correct}\n")





    
