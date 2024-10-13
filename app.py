from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "Where is Taj Mahal located?", "answer": "Agra"},
    {"question": "What is the color of the sky?", "answer": "Blue"},
    {"question": "What is the national bird of India?", "answer": "Peacock"},
    {"question": "How many vowels are there in the English alphabet ?", "answer": "5"},
]

current_question = None
players = {}

@app.route('/')
def index():
    return render_template('kbc.html')

@app.route('/mobile')
def mobile():
    return render_template('mobile.html')

@app.route('/next_question', methods=['GET'])
def next_question():
    global current_question
    if questions:
        current_question = random.choice(questions)
        return jsonify(current_question)
    return jsonify({"question": "No more questions!"})

@app.route('/submit_name', methods=['POST'])
def submit_name():
    player_name = request.json.get('name')
    if player_name:
        players[player_name] = {"score": 0}
        return jsonify({"message": f"Welcome, {player_name}!"})
    return jsonify({"message": "Name cannot be empty!"}), 400

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    answer = request.json.get('answer')
    if current_question and answer:
        correct = answer.strip().lower() == current_question["answer"].strip().lower()
        if correct:
            return jsonify({"message": "Congratulations! That's correct.", "correct": True})
        else:
            return jsonify({"message": "Sorry, that's incorrect.", "correct": False})
    return jsonify({"message": "No question available!"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.35')  