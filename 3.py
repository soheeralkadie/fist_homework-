import json

def load_questions(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_results(file_path, user_name, score):
    result = {"name": user_name, "score": score}
    with open(file_path, 'a', encoding='utf-8') as f:
        json.dump(result, f)
        f.write('\n')

def quiz_user(questions):
    score = 0
    for i, qa in enumerate(questions, 1):
        print(f"Question {i}: {qa['question']}")
        answer = input("True or False? ").strip().lower()
        if answer == 'true' and qa['answer'] or answer == 'false' and not qa['answer']:
            score += 1
    return score

def main():
    question_file = "Quiz.json"
    questions = load_questions(question_file)
    user_name = input("Enter your name: ").strip()
    score = quiz_user(questions)
    print(f"Your score is {score}/{len(questions)}")
    result_file ="results.csv"
    save_results(result_file,user_name,score)

if __name__ == "__main__":
    main()

