from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response
import sqlite3
from db import init_db, create_poll, get_polls, get_options, add_option, vote, remove_expired_polls
from datetime import datetime, timedelta
import random
import string
from apscheduler.schedulers.background import BackgroundScheduler

default_expiration_date = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')

app = Flask(__name__)

def generate_random_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/')
def index():
    return render_template('index.html', default_expiration_date = default_expiration_date)

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/create_poll', methods=['POST'])
def create_poll_route():


    question = request.form["question"]
    expiration_date = request.form["expiration_date"]
    custom_id = request.form["custom_id"]


    if custom_id:
        id = custom_id
    else:
        id = generate_random_id()

    if not expiration_date:
        return render_template('error.html', message="Error: Missing expiration date", url="/"), 400

    if not question:    
        return render_template('error.html', message="Error: Missing question text", url="/"), 400
    
    if expiration_date < datetime.now().strftime('%Y-%m-%d'):
        return render_template('error.html', message="Error: Expiration date must be in the future", url="/"), 400
    

    create_poll(id, question, expiration_date)
    return redirect(url_for('poll', poll_id=id))

@app.route('/<poll_id>')
def poll(poll_id):
    polls = get_polls()
    print(polls)
    poll = next((poll for poll in polls if poll[0] == poll_id), None)
    print(poll)
    if poll is None:
        return "Error: Poll not found", 404  
    options = get_options(poll_id)
    options.sort(key=lambda option: option[3], reverse=True)  # Sort options by votes in descending order
    return render_template('poll.html', poll=poll, options=options)

@app.route('/vote/<poll_id>/<option_id>', methods=['POST'])
def vote_route(poll_id, option_id):
    vote_cookie = request.cookies.get(f'voted_{poll_id}_{option_id}')
    if vote_cookie:
        return jsonify({"message": "You can only vote once per option."}), 400
    
    vote(poll_id, option_id)
    response = make_response(jsonify({"message": "Vote successful."}))
    response.set_cookie(f'voted_{poll_id}_{option_id}', 'true', max_age=60*60*24*365) 
    return response

@app.route('/add_option/<poll_id>', methods=['POST'])
def add_option_route(poll_id):
    option = request.form["option"]
    if not option:
        return render_template('error.html', message="Error: Missing option text", url=f"/{poll_id}"), 400
    add_option(poll_id, option)
    return redirect(url_for('poll', poll_id=poll_id))

@app.route('/health')
def health_check():
    return "OK", 200

scheduler = BackgroundScheduler()
scheduler.add_job(remove_expired_polls, 'interval', days=1)
scheduler.start()

if __name__ == '__main__':
    init_db()
    remove_expired_polls()  # Check for expired polls on startup
    app.run(debug=True, host='0.0.0.0', port=8737)