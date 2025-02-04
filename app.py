from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
from db import init_db

app = Flask(__name__)



if __name__ == '__main__':
    app.run(debug=True)