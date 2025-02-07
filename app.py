from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
from db import init_db, create_poll, get_polls, get_options, add_option, vote
from datetime import datetime, timedelta
import random
import string

default_expiration_date = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')

app = Flask(__name__)

def generate_random_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/')
def index():
    return render_template('index.html', default_expiration_date = default_expiration_date)

@app.route('/create_poll', methods=['POST'])
def create_poll_route():
    print("Received Form Data:", request.form)  # Debugging

    question = request.form["question"]
    expiration_date = request.form["expiration_date"]
    custom_id = request.form["custom_id"]


    if custom_id:
        id = custom_id
    else:
        id = generate_random_id()

    print("Debug:", id, question, expiration_date)  # Debug output

    if not question or not expiration_date:
        return "Error: Missing question or expiration date", 400  # Return error response


    print("debug")
    print(id, question, expiration_date)
    create_poll(id, question, expiration_date)
    return redirect(url_for(id=id))

@app.route('/<poll_id>')
def poll(poll_id):
    polls = get_polls()
    poll = [poll for poll in polls if poll[0] == poll_id][0]
    options = get_options(poll_id)
    return render_template('poll.html', poll=poll, options=options)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)