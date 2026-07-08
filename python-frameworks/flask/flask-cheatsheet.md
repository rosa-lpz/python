# Flask Cheat Sheet

## Installation

```bash
pip install flask
```

## Basic Application

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
```

## Run the Application

```bash
python app.py
```

## Routes

```python
@app.route("/")
def home():
    return "Home Page"

@app.route("/about")
def about():
    return "About Page"
```

## Dynamic Routes

```python
@app.route("/user/<name>")
def user(name):
    return f"Hello, {name}"

@app.route("/post/<int:id>")
def post(id):
    return f"Post {id}"
```

## HTTP Methods

```python
from flask import request

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "Form Submitted"
    return "Login Form"
```

## Request Data

```python
request.args.get("name")      # Query parameter
request.form["username"]      # Form data
request.json                  # JSON data
```

## Returning JSON

```python
from flask import jsonify

@app.route("/api")
def api():
    return jsonify({
        "message": "Success",
        "status": 200
    })
```

## HTML Templates

```python
from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")
```

**templates/index.html**

```html
<h1>{{ title }}</h1>
<p>{{ message }}</p>
```

Pass data:

```python
return render_template(
    "index.html",
    title="Welcome",
    message="Hello Flask"
)
```

## Forms

```html
<form method="POST">
    <input type="text" name="username">
    <button type="submit">Submit</button>
</form>
```

```python
username = request.form["username"]
```

## Redirect

```python
from flask import redirect, url_for

return redirect(url_for("home"))
```

## URL Generation

```python
url_for("home")
url_for("user", name="Alice")
```

## Sessions

```python
from flask import session

app.secret_key = "secret"

session["user"] = "Alice"

user = session.get("user")
```

## Error Handling

```python
@app.errorhandler(404)
def not_found(error):
    return "Page Not Found", 404
```

## Static Files

Folder structure:

```text
project/
│── app.py
│── static/
│   ├── style.css
│   └── logo.png
│── templates/
    └── index.html
```

Use in HTML:

```html
<link rel="stylesheet"
href="{{ url_for('static', filename='style.css') }}">
```

## Jinja Template Syntax

Variable:

```html
{{ name }}
```

If statement:

```html
{% if user %}
  Welcome
{% endif %}
```

Loop:

```html
{% for item in items %}
  {{ item }}
{% endfor %}
```

## REST API Example

```python
@app.route("/users", methods=["GET"])
def users():
    return jsonify([
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ])
```

## Project Structure

```text
project/
│── app.py
│── templates/
│── static/
│── requirements.txt
```

## Common Flask Imports

```python
from flask import (
    Flask,
    request,
    jsonify,
    render_template,
    redirect,
    url_for,
    session
)
```

## Useful Commands

```bash
pip install flask
pip freeze > requirements.txt
python app.py
```

## Common HTTP Status Codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | OK                    |
| 201  | Created               |
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 403  | Forbidden             |
| 404  | Not Found             |
| 500  | Internal Server Error |
