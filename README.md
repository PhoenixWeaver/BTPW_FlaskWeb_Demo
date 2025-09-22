# 🚀 Flask Blog Web Application

A modern, responsive Flask web application featuring a blog system with user authentication, contact forms, and dynamic content management.

## ✨ Features

- **User Authentication** - Simple login system with session management
- **Blog System** - Create, read, and manage blog posts
- **Contact Form** - Send messages with CSV data storage
- **Responsive Design** - Modern UI that works on all devices
- **Dynamic Content** - Real-time blog post creation and display
- **CSV Data Storage** - Contact messages saved to CSV file

## 🛠️ Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, Jinja2 Templates
- **Data Storage**: In-memory (blog posts), CSV (contact messages)
- **Styling**: Custom CSS with modern design patterns

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd BTPW_FlaskWeb_Demo
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python BTPW_FlaskWeb.py
```

### 4. Access the Application
Open your web browser and navigate to:
- **Homepage**: http://127.0.0.1:5000/
- **Login**: http://127.0.0.1:5000/login
- **Blog**: http://127.0.0.1:5000/blog/content
- **Contact**: http://127.0.0.1:5000/blog/ContactUs

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
- Email: bentran.phoenix@gmail.com
- GitHub: [@PhoenixWeaver](https://github.com/PhoenixWeaver)

## 🙏 Acknowledgments

- Flask community for the excellent framework
- Contributors to the learning resources
- Open source libraries and tools used

---

**Happy Coding! 🚀**
