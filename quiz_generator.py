import random
import openai

# Function to generate quiz questions dynamically using OpenAI API
def generate_questions():
    prompt = "Generate five multiple-choice social studies questions for a 5th-grade quiz. Format: Question, Options (A, B, C, D), and Correct Answer."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant generating educational quizzes."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def parse_questions(response_text):
    questions = []
    for q in response_text.strip().split('\n\n'):
        lines = q.split('\n')
        if len(lines) >= 3:
            question = lines[0]
            options = lines[1:5]
            answer = lines[5].split(':')[-1].strip()
            questions.append({"question": question, "options": options, "answer": answer})
    return questions

def run_quiz():
    response_text = generate_questions()
    questions = parse_questions(response_text)
    score = 0
    random.shuffle(questions)
    
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q["options"]:
            print(option)
        
        answer = input("Enter the letter of your answer: ").strip().upper()
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {q['answer']}.")
    
    print(f"\nYou got {score} out of {len(questions)} correct!")

if __name__ == "__main__":
    run_quiz()
