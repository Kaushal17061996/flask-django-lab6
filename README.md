# Flask and Django Web Application Lab

## Overview

This project demonstrates basic web development using two Python frameworks: **Flask** and **Django**.
The goal of this lab is to understand routing, templates, and simple form handling in Flask, and to create a minimal web application using Django.

---

# Part 1 – Flask Application

## Features Implemented

* Basic Flask web application
* Home route displaying a welcome message
* Dynamic route that greets the user by name
* HTML template using **Jinja2**
* A form that accepts user input and displays a personalized greeting

## Flask File Structure

```
flask_app/
│
├── app.py
└── templates/
      ├── hello.html
      └── form.html
```

## How to Run the Flask Application

1. Navigate to the Flask project directory

```
cd flask_app
```

2. Create and activate virtual environment (optional)

```
python -m venv venv
venv\Scripts\activate
```

3. Install Flask

```
pip install flask
```

4. Run the Flask application

```
python app.py
```

5. Open the browser and go to:

```
http://127.0.0.1:5000
```

### Example Routes

Home Page:

```
http://127.0.0.1:5000
```

Dynamic Greeting:

```
http://127.0.0.1:5000/hello/YourName
```

Form Page:

```
http://127.0.0.1:5000/form
```

---

# Part 2 – Django Application

## Features Implemented

* Django project creation
* Django application creation
* Template rendering
* Basic homepage displaying a message
* URL routing using Django views

## Django File Structure

```
django_app/
│
├── manage.py
├── mysite/
│     ├── settings.py
│     ├── urls.py
│
├── core/
│     ├── views.py
│
└── templates/
      └── home.html
```

## How to Run the Django Application

1. Navigate to the Django project directory

```
cd django_app
```

2. Create virtual environment (optional)

```
python -m venv venv
venv\Scripts\activate
```

3. Install Django

```
pip install django
```

4. Run the development server

```
python manage.py runserver
```

5. Open the browser and visit:

```
http://127.0.0.1:8000
```

You should see the message:

```
Hello from Django!
```

---

# Screenshots

The following screenshots were captured and submitted on Blackboard:

1. Flask form page working
2. Flask dynamic greeting page
3. Django welcome page
4. Django admin interface (if implemented)

---

# Summary

This lab helped demonstrate the differences between **Flask** and **Django** frameworks.

Flask is a **lightweight framework** where developers manually configure routes, templates, and forms. Django is a **full-featured framework** that provides built-in tools such as URL routing, admin panels, and project structure.

Through this lab we learned how to:

* Build simple web applications
* Use templates for dynamic content
* Handle user input through forms
* Run applications locally using Flask and Django
