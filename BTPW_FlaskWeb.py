"""
===============================================================================
FLASK WEB APPLICATION LEARNING PROJECT - BLOG SYSTEM WITH USER AUTHENTICATION
===============================================================================
Author: Ben Tran (PhoenixWeaver)
Date: 08/15/2025
Project: BTPW_FlaskWeb_Demo
Description: A modern Flask web application featuring blog system, user 
            authentication, contact forms, and responsive UI design.
GitHub: https://github.com/PhoenixWeaver/BTPW_FlaskWeb_Demo
===============================================================================

📋 STEP-BY-STEP FIX INSTRUCTIONS
Step 1: Start Your Flask App
# In your terminal/command prompt:
cd "C:\\Users\\Admin\\Documents\\PYTHON\\BTPython\\BTPW_FlaskWeb_Demo"
python BTPW_FlaskWeb.py

Step 2: Access Your App Correctly
✅ DO THIS:
Open your web browser
Go to: http://127.0.0.1:5000 (homepage)
Or: http://127.0.0.1:5000/blog/content (blog page)
Or: http://127.0.0.1:5000/blog/ContactUs (contact page)

Step 3: Test Your App
Homepage: http://127.0.0.1:5000/
Login: http://127.0.0.1:5000/login?username=test&password=test 
User Profile: http://127.0.0.1:5000/user/test 

Visit secret page: http://127.0.0.1:5000/my/secret/page

REFERENCE:
https://www.learnpython.dev/03-intermediate-python/

=====================================================================================================================================
"""

# 1. Create a Flask app with modern configuration
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, TextAreaField, EmailField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length
from datetime import datetime
import sqlite3
import os
import hashlib
import secrets

# Initialize Flask app with modern configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', secrets.token_hex(32))
app.config['WTF_CSRF_ENABLED'] = True

# Initialize CSRF protection
csrf = CSRFProtect(app)

# Database setup
DATABASE = 'blog_database.db'

def init_db():
    """Initialize the database with required tables"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Create blog posts table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS blog_posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            email TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create contact messages table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contact_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            subject TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

# Initialize database on startup
init_db()

# WTForms for better form handling
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Login')

class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=5, max=100)])
    content = TextAreaField('Content', validators=[DataRequired(), Length(min=10, max=1000)])
    author = StringField('Author', validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField('Create Post')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired(), Length(min=5, max=100)])
    content = TextAreaField('Message', validators=[DataRequired(), Length(min=10, max=500)])
    submit = SubmitField('Send Message')

# Database helper functions
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

# 2. Create routes with modern Flask practices
@app.route('/')
def index():
    """Homepage with login form"""
    form = LoginForm()
    return render_template('index.html', form=form, username=session.get('username'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Enhanced login with form validation"""
    form = LoginForm()
    
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        if verify_user(username, password):
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('blog_content'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('index.html', form=form, username=session.get('username'))

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
    
    form = BlogPostForm()
    
    if form.validate_on_submit():
        # Save new blog post to database
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO blog_posts (title, content, author) VALUES (?, ?, ?)',
            (form.title.data, form.content.data, form.author.data)
        )
        conn.commit()
        conn.close()
        
        flash('Blog post created successfully!', 'success')
        return redirect(url_for('blog_content'))
    
    # Get all blog posts from database
    conn = get_db_connection()
    blog_posts = conn.execute(
        'SELECT * FROM blog_posts ORDER BY created_at DESC'
    ).fetchall()
    conn.close()
    
    return render_template('BlogPage.html', 
                         username=session.get('username'), 
                         blog_posts=blog_posts,
                         form=form)

@app.route("/blog/ContactUs", methods=['GET', 'POST'])
def contact_us():
    """Contact page with form validation"""
    form = ContactForm()
    
    if form.validate_on_submit():
        # Save contact message to database
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO contact_messages (name, email, subject, message) VALUES (?, ?, ?, ?)',
            (form.name.data, form.email.data, form.subject.data, form.content.data)
        )
        conn.commit()
        conn.close()
        
        flash('Message sent successfully! We will get back to you soon.', 'success')
        return redirect(url_for('contact_us'))
    
    return render_template('ContactUs.html', form=form)

@app.route("/user/<username>")
def user_page(username):
    """User profile page"""
    if 'username' not in session:
        flash('Please login to view profiles', 'warning')
        return redirect(url_for('index'))
    return render_template('user.html', username=username)

@app.route("/user")
def user_form():
    """User form page"""
    username = request.args.get('username', 'Guest')
    return render_template('user.html', username=username)

@app.route("/blog/post/<int:post_id>") 
def show_post(post_id):
    """Individual blog post page"""
    conn = get_db_connection()
    post = conn.execute(
        'SELECT * FROM blog_posts WHERE id = ?', (post_id,)
    ).fetchone()
    conn.close()
    
    if post is None:
        flash('Blog post not found', 'error')
        return redirect(url_for('blog_content'))
    
    return render_template('blog_post.html', post=post)

# Keep the old secret page route for backward compatibility
@app.route("/my/secret/page")
def secret():
    """Secret page (demo)"""
    if 'username' not in session:
        flash('Please login to access secret page', 'warning')
        return redirect(url_for('index'))
    return render_template('secret.html')

@app.route('/api/posts')
def api_posts():
    """API endpoint for blog posts"""
    conn = get_db_connection()
    posts = conn.execute(
        'SELECT * FROM blog_posts ORDER BY created_at DESC'
    ).fetchall()
    conn.close()
    
    return jsonify([dict(post) for post in posts])

@app.errorhandler(404)
def not_found(error):
    """404 error handler"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """500 error handler"""
    return render_template('500.html'), 500

############################################
# 3. returning data

#### HTML Template
print("Flask HTML Template:")

# <!doctype html>
# <title>Hello from Flask</title>
# {% if name %}
#   <h1>Hello {{ name }}!</h1>
# {% else %}
#   <h1>Hello, World!</h1>
# {% endif %}

# 4. Run the app
if __name__ == "__main__":
    print("Running flask app ...")
    # For production, set debug=False
    app.run(debug=True, host='127.0.0.1', port=5000)

# $ export FLASK_APP=my_application
# $ export FLASK_ENV=development
# $ flask run

#########


