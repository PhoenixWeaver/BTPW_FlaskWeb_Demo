# 🚀 Flask Blog Web Application

A modern, responsive Flask web application featuring a blog system with user authentication, contact forms, and dynamic content management. **Recently updated with modern Flask practices, database integration, and enhanced security features!**

## ✨ Features

### 🔐 **Authentication & Security**
- **Secure Login System** - Session-based authentication with password hashing
- **CSRF Protection** - Built-in CSRF protection for form security
- **Input Validation** - Comprehensive form validation with WTForms
- **Session Management** - Secure user sessions with automatic logout

### 📝 **Blog System**
- **Database Integration** - SQLite database for persistent data storage
- **Create & Manage Posts** - Full CRUD operations for blog posts
- **Real-time Updates** - Dynamic content creation and display
- **Author Management** - Track post authors and creation dates

### 📧 **Contact System**
- **Modern Contact Form** - Professional contact form with validation
- **Database Storage** - Contact messages stored in SQLite database
- **Email Validation** - Proper email format validation
- **Success Notifications** - Flash messages for user feedback

### 🎨 **Modern UI/UX**
- **Responsive Design** - Mobile-first design that works on all devices
- **Modern Navigation** - Clean navigation bar with user status
- **Flash Messages** - Animated success/error notifications
- **Professional Styling** - Modern CSS with gradients and animations

## 🛠️ Technologies Used

- **Backend**: Python Flask 3.0.0
- **Database**: SQLite with SQLAlchemy-style queries
- **Forms**: Flask-WTF with WTForms validation
- **Security**: CSRF protection, password hashing, session management
- **Frontend**: HTML5, CSS3, Jinja2 Templates, Font Awesome icons
- **Styling**: Modern CSS with gradients, animations, and responsive design

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/PhoenixWeaver/BTPW_FlaskWeb_Demo.git
cd BTPW_FlaskWeb_Demo
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup Database
```bash
python setup_database.py
```

### 4. Run the Application
```bash
python BTPW_FlaskWeb.py
```

### 5. Access the Application
Open your web browser and navigate to:
- **Homepage**: http://127.0.0.1:5000/
- **Blog**: http://127.0.0.1:5000/blog/content
- **Contact**: http://127.0.0.1:5000/blog/ContactUs

### 🔑 Demo Credentials
- **Username**: `admin`
- **Password**: `password123`

## 📖 Usage Guide

### Login System
- Use any username and password to login
- Login redirects to the blog page
- Session persists during the application run

### Blog Features
- **View Posts**: See all existing blog posts
- **Create Posts**: Add new blog posts with title, author, and content
- **Real-time Updates**: New posts appear immediately

### Contact Form
- Fill out the contact form with your details
- Messages are saved to `contact_messages.csv`
- Form includes validation for required fields

## 📁 Project Structure

```
BTPW_FlaskWeb_Demo/
├── BTPW_FlaskWeb.py          # Main Flask application
├── requirements.txt          # Python dependencies
├── README.md                # Project documentation
├── .gitignore              # Git ignore rules
├── start_flask_app.bat     # Windows batch file to start app
├── templates/              # HTML templates
│   ├── index.html          # Homepage
│   ├── BlogPage.html       # Blog interface
│   ├── ContactUs.html      # Contact form
│   ├── user.html           # User profile page
│   └── secret.html         # Secret page
├── static/                 # Static files
│   ├── style.css           # Main stylesheet
│   └── favicon.png         # Website icon
└── contact_messages.csv    # Contact form data (generated)
```

## 🔧 Configuration

### Environment Variables
The application runs in debug mode by default. For production:
```python
app.run(debug=False, host='0.0.0.0', port=5000)
```

### Data Storage
- **Blog Posts**: Stored in memory (resets on restart)
- **Contact Messages**: Saved to CSV file with timestamps

## 🎯 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Homepage with login form |
| GET | `/login` | User authentication |
| GET | `/blog/content` | Blog page with posts and creation form |
| GET | `/blog/ContactUs` | Contact form page |
| POST | `/contact/submit` | Submit contact form |
| GET | `/user/<username>` | User profile page |
| GET | `/my/secret/page` | Secret page (demo) |

## 🎨 Customization

### Styling
Edit `static/style.css` to customize the appearance:
- Color schemes
- Layout dimensions
- Typography
- Responsive breakpoints

### Templates
Modify HTML templates in the `templates/` directory:
- Add new pages
- Customize existing layouts
- Implement new features

## 🔒 Security Notes

⚠️ **This is a demo application with basic security. For production use:**

- Implement proper password hashing
- Use POST method for sensitive data
- Add input validation and sanitization
- Implement CSRF protection
- Use environment variables for configuration
- Add proper error handling

## 🚀 Deployment

### Local Development
```bash
python BTPW_FlaskWeb.py
```

### Production Deployment
1. Set `debug=False` in the application
2. Use a production WSGI server (Gunicorn, uWSGI)
3. Set up a reverse proxy (Nginx)
4. Configure environment variables
5. Set up SSL certificates

## 📚 Learning Resources

This project includes a comprehensive learning guide: `BenTran_PhoenixWeaver_LEARNING_GUIDE.md`

Topics covered:
- Flask framework fundamentals
- Web routing and URL handling
- Template rendering with Jinja2
- Form handling and data processing
- HTML5 and CSS3 concepts
- Web development best practices

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Ben Tran (PhoenixWeaver)**
- GitHub: [@PhoenixWeaver](https://github.com/PhoenixWeaver)

## 🙏 Acknowledgments

- Flask community for the excellent framework
- Contributors to the learning resources
- Open source libraries and tools used

---

**Happy Coding! 🚀**
