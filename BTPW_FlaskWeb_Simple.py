"""
Simplified Flask Web Application - BTPW_FlaskWeb_Demo
This version works without complex dependencies and focuses on core functionality
"""

from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime
import sqlite3
import hashlib
import os

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Database setup
DATABASE = 'blog_database.db'

def get_db_connection():
    """Get database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def hash_password(password):
    """Hash password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_user(username, password):
    """Verify user credentials"""
    conn = get_db_connection()
    user = conn.execute(
        'SELECT * FROM users WHERE username = ?', (username,)
    ).fetchone()
    conn.close()
    
    if user and user['password_hash'] == hash_password(password):
        return True
    return False

# Routes
@app.route('/')
def index():
    """Homepage with login form"""
    return render_template('index_simple.html', username=session.get('username'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Simple login without complex forms"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username and password:
            if verify_user(username, password):
                session['username'] = username
                flash('Login successful!', 'success')
                return redirect(url_for('blog_content'))
            else:
                flash('Invalid username or password', 'error')
        else:
            flash('Please fill in all fields', 'error')
    
    return render_template('index_simple.html', username=session.get('username'))

@app.route('/logout')
def logout():
    """Logout user"""
    session.pop('username', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('index'))

@app.route("/blog/content", methods=['GET', 'POST'])
def blog_content():
    """Blog page with database integration"""
    if 'username' not in session:
        flash('Please login to access the blog', 'warning')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        author = request.form.get('author')
        
        if title and content and author:
            conn = get_db_connection()
            conn.execute(
                'INSERT INTO blog_posts (title, content, author) VALUES (?, ?, ?)',
                (title, content, author)
            )
            conn.commit()
            conn.close()
            flash('Blog post created successfully!', 'success')
            return redirect(url_for('blog_content'))
        else:
            flash('Please fill in all fields', 'error')
    
    # Get all blog posts from database
    conn = get_db_connection()
    blog_posts = conn.execute(
        'SELECT * FROM blog_posts ORDER BY created_at DESC'
    ).fetchall()
    conn.close()
    
    return render_template('BlogPage_simple.html', 
                         username=session.get('username'), 
                         blog_posts=blog_posts)

@app.route("/blog/ContactUs", methods=['GET', 'POST'])
def contact_us():
    """Contact page"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('content')
        
        if name and email and subject and message:
            conn = get_db_connection()
            conn.execute(
                'INSERT INTO contact_messages (name, email, subject, message) VALUES (?, ?, ?, ?)',
                (name, email, subject, message)
            )
            conn.commit()
            conn.close()
            flash('Message sent successfully!', 'success')
            return redirect(url_for('contact_us'))
        else:
            flash('Please fill in all fields', 'error')
    
    return render_template('ContactUs_simple.html')

@app.route("/user/<username>")
def user_page(username):
    """User profile page"""
    if 'username' not in session:
        flash('Please login to view profiles', 'warning')
        return redirect(url_for('index'))
    return render_template('user.html', username=username)

@app.route("/my/secret/page")
def secret():
    """Secret page (demo)"""
    if 'username' not in session:
        flash('Please login to access secret page', 'warning')
        return redirect(url_for('index'))
    return render_template('secret.html')

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return render_template('404_simple.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500_simple.html'), 500

if __name__ == "__main__":
    print("🚀 Starting simplified Flask application...")
    print("📊 Database:", DATABASE)
    print("🌐 Server: http://127.0.0.1:5000")
    print("👤 Demo user: admin / password123")
    app.run(debug=True, host='127.0.0.1', port=5000)
