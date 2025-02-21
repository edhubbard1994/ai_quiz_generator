# Function to generate quiz questions dynamically using OpenAI API
import json
import openai


def generate_questions():
    client = openai.OpenAI(api_key="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")  # Initialize the OpenAI client
    prompt = "Generate five multiple-choice social studies questions for a 5th-grade quiz. Format: Question, Options (A, B, C, D), and Correct Answer."

    response = client.chat.completions.create(
        model="gpt-4-turbo",  # Updated to a later version
        messages=[
            {"role": "system", "content": "You are a helpful assistant generating educational quizzes."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

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


def read_quiz():
    with open("quiz.json","r") as file:
        print(file)
        data = json.load(file)  # Converts JSON string to a Python dictionary
    return data["quiz"]

