import json
import random
import openai

from helpers import read_quiz





def run_quiz():
    quiz_questions = read_quiz()
    for question in quiz_questions:
        print(question["question"])
        for option in enumerate(question["options"]):
            print(f"{option[0]}. {option[1]}")
        answer = input("your answer:")
        if int(answer) == question["answer_index"]:
            print("Correct")
        else:
            print("wrong")
            print(f"the correct answer is: {question["options"][question["answer_index"]]}\n")



if __name__ == "__main__":
    run_quiz()