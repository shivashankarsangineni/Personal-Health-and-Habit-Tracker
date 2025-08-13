from flask import Flask, render_template, request, redirect, session
from database import get_db_connection
import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Home/Dashboard
@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect('/login')
    conn = get_db_connection()
    habits = conn.execute('SELECT * FROM habits WHERE user_id = ? ORDER BY date DESC LIMIT 7', 
                          (session['user_id'],)).fetchall()
    conn.close()
    return render_template('index.html', habits=habits)

# Register
@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        conn = get_db_connection()
        conn.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', 
                     (name, email, password))
        conn.commit()
        conn.close()
        return redirect('/login')
    return render_template('register.html')

# Login
@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE email = ? AND password = ?', 
                            (email, password)).fetchone()
        conn.close()
        if user:
            session['user_id'] = user['id']
            return redirect('/')
    return render_template('login.html')

# Add Habit
@app.route('/add', methods=('GET', 'POST'))
def add_habit():
    if request.method == 'POST':
        exercise = request.form['exercise']
        sleep = request.form['sleep']
        water = request.form['water']
        calories = request.form['calories']
        today = datetime.date.today()
        conn = get_db_connection()
        conn.execute('INSERT INTO habits (user_id, date, exercise_minutes, sleep_hours, water_litres, calories) VALUES (?, ?, ?, ?, ?, ?)', 
                     (session['user_id'], today, exercise, sleep, water, calories))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('add_habit.html')

if __name__ == '__main__':
    app.run(debug=True)
