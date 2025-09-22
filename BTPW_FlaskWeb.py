####### Ben Tran #######
### Date: 08/15/2025 ###
# Web Frameworks #

"""
📋 STEP-BY-STEP FIX INSTRUCTIONS
Step 1: Start Your Flask App
# In your terminal/command prompt:
cd "C:/Users/Admin/Documents/PYTHON/BTPython/BT_FlaskWeb_Template"
python BTFlaskWeb.py

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

# 1. Create a Flask app
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
app = Flask(__name__)

# Simple in-memory storage for blog posts and current user
blog_posts = []
current_user = None

# 2. Create routes
@app.route('/')
def index():
    global current_user
    return render_template('index.html', username=current_user)

@app.route('/login')
def login():
    global current_user
    username = request.args.get('username')
    password = request.args.get('password')
    
# In-memory data storage (NOT production-ready!)
# This is a simple way to store data in memory for learning purposes
# In a real application, you'd use a database like SQLite, PostgreSQL, etc.
# >>> PhonenixWeaver/BTPW_GoHTTP_Server

    if username and password:
        current_user = username
        return redirect(url_for('blog_content'))
    return redirect(url_for('index'))

@app.route("/blog/content")
def blog_content():
    global current_user, blog_posts
    
    # Check if there's a new post being submitted
    name = request.args.get('name')
    title = request.args.get('title')
    content = request.args.get('content')
    
    recent_post = None
    if name and title and content:
        # Create new blog post
        new_post = {
            'name': name,
            'title': title,
            'content': content,
            'date': datetime.now().strftime('%B %d, %Y at %I:%M %p')
        }
        blog_posts.insert(0, new_post)  # Add to beginning of list
        recent_post = new_post
    
    return render_template('BlogPage.html', 
                         username=current_user, 
                         blog_posts=blog_posts[1:] if recent_post else blog_posts,
                         recent_post=recent_post)

@app.route("/blog/ContactUs")
def contact_us():
    return render_template('ContactUs.html') 

@app.route("/user/<username>")
def user_page(username):
    return render_template('user.html', username=username)

@app.route("/user")
def user_form():
    username = request.args.get('username', 'Guest')
    return render_template('user.html', username=username)

@app.route("/blog/post/<int:post_id>") 
def show_post(post_id):
    return render_template('blog_post.html', post_id=post_id)

# Keep the old secret page route for backward compatibility
@app.route("/my/secret/page")
def secret():
    return render_template('secret.html')

# Handle contact form submissions
@app.route("/contact/submit", methods=['POST'])
def submit_contact():
    # Get form data
    name = request.form.get('name')
    email = request.form.get('email') 
    subject = request.form.get('subject')
    message = request.form.get('content')
    
    # Simple validation
    if name and email and subject and message:
        # Save contact message to CSV file
        import csv
        import os
        from datetime import datetime

        # Create CSV file if it doesn't exist
        csv_file = 'contact_messages.csv'
        file_exists = os.path.exists(csv_file)

        try:
            with open(csv_file, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                
                # Write header if file is new
                if not file_exists:
                    writer.writerow(['Date', 'Time', 'Name', 'Email', 'Subject', 'Message'])
                
                # Write message data
                current_time = datetime.now()
                writer.writerow([
                    current_time.strftime('%Y-%m-%d'),
                    current_time.strftime('%H:%M:%S'),
                    name,
                    email,
                    subject,
                    message
                ])
            
            print(f"✅ Contact message saved to: {csv_file}")
            print(f"📧 From: {name} ({email})")
            print(f"🎯 Subject: {subject}")
            
        except Exception as e:
            print(f"❌ Error saving contact message: {e}")
        
        # Redirect back to contact page with success message
        return redirect(url_for('contact_us', success='true'))
    else:
        # Redirect back with error message
        return redirect(url_for('contact_us', error='true'))

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


