from flask import Flask, jsonify, send_from_directory
import requests

app = Flask(__name__)

# -----------------------------
# API Endpoints
# -----------------------------

@app.route('/api/user')
def fetch_user():
    """Fetch a single user"""
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(url)
    response.raise_for_status()
    return jsonify(response.json())


@app.route('/api/posts')
def fetch_posts():
    """Fetch all posts"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    response.raise_for_status()
    return jsonify(response.json())


# -----------------------------
# HTML Routes
# -----------------------------

@app.route('/')
def serve_home():
    return send_from_directory('.', 'index.html')

@app.route('/user')
def serve_user_page():
    return send_from_directory('.', 'user.html')

@app.route('/posts')
def serve_posts_page():
    return send_from_directory('.', 'posts.html')


# -----------------------------
# Run Server
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)
