#!/usr/bin/env python3
"""
Database setup script for BTPW_FlaskWeb_Demo
This script initializes the database and creates a demo user
"""

import sqlite3
import hashlib
import os

DATABASE = 'blog_database.db'

def hash_password(password):
    """Hash password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def setup_database():
    """Initialize the database with required tables and demo data"""
    print("🚀 Setting up database...")
    
    # Remove existing database if it exists
    if os.path.exists(DATABASE):
        os.remove(DATABASE)
        print("🗑️  Removed existing database")
    
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
    
    # Insert demo user
    demo_username = 'admin'
    demo_password = 'password123'
    demo_email = 'admin@example.com'
    
    cursor.execute(
        'INSERT INTO users (username, password_hash, email) VALUES (?, ?, ?)',
        (demo_username, hash_password(demo_password), demo_email)
    )
    
    # Insert sample blog posts
    sample_posts = [
        {
            'title': 'Welcome to Flask Blog!',
            'content': 'This is your first blog post. You can create, edit, and manage your blog posts here. The blog system is built with Flask and includes user authentication, form validation, and a modern responsive design.',
            'author': 'Admin'
        },
        {
            'title': 'Getting Started with Flask',
            'content': 'Flask is a lightweight web framework for Python. It\'s perfect for building web applications, APIs, and prototypes. This demo application showcases many Flask features including routing, templates, forms, and database integration.',
            'author': 'Admin'
        },
        {
            'title': 'Modern Web Development',
            'content': 'This application demonstrates modern web development practices including responsive design, form validation, session management, and database integration. All built with Python Flask!',
            'author': 'Admin'
        }
    ]
    
    for post in sample_posts:
        cursor.execute(
            'INSERT INTO blog_posts (title, content, author) VALUES (?, ?, ?)',
            (post['title'], post['content'], post['author'])
        )
    
    conn.commit()
    conn.close()
    
    print("✅ Database setup complete!")
    print(f"📊 Created tables: users, blog_posts, contact_messages")
    print(f"👤 Demo user created: {demo_username} / {demo_password}")
    print(f"📝 Sample blog posts: {len(sample_posts)}")
    print("\n🎉 You can now run: python BTPW_FlaskWeb.py")

if __name__ == "__main__":
    setup_database()
