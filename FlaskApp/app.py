import sqlite3
from flask import Flask, render_template, request, url_for, redirect, jsonify

app = Flask(__name__)

# Function to get a database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row # This allows us to access columns by name
    return conn

@app.route('/', methods=('GET', 'POST'))
def index():
    conn = get_db_connection()

    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        
        if name and message and len(message) <= 140: # Basic validation
            conn.execute('INSERT INTO messages (name, message) VALUES (?, ?)',
                         (name, message))
            conn.commit()
            conn.close()
            return redirect(url_for('index')) # Redirect to prevent form resubmission
        elif len(message) > 140:

            return redirect(url_for('index')) # Redirect to prevent form resubmission

    # This code runs for a GET request
    messages = conn.execute('SELECT * FROM messages ORDER BY created_at DESC').fetchall()
    conn.close()
    
    return render_template(
        'index.html', 
        page_title='Guestbook Home', 
        messages=messages
    )


@app.route('/api/messages', methods=['POST'])
def add_message_api():
    data = request.get_json()
    name = data.get('name')
    message = data.get('message')

    if not name or not message:
        return jsonify({'status': 'error', 'message': 'Name and message are required.'}), 400

    conn = get_db_connection()
    conn.execute('INSERT INTO messages (name, message) VALUES (?, ?)',
                 (name, message))
    conn.commit()
    conn.close()
    
    return jsonify({'status': 'success', 'message': 'Message added!'})

# A simple health check route
@app.route('/health')
def health_check():
    return 'Server is running!', 200

@app.route('/about')
def text():
    return 'This is a simple Flask guestbook application.', 700

@app.route('/movie')
def movie():
    return 'This is my favorite movies(For tas).'
