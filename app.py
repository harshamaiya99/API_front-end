from flask import Flask, jsonify, send_from_directory
import requests

app = Flask(__name__)

# Example GET route that calls your real API
@app.route('/api/data')
def fetch_api_data():

    url = "https://jsonplaceholder.typicode.com/users/1"

    response = requests.get(url)
    response.raise_for_status()
    return jsonify(response.json())

# Serve the HTML file
@app.route('/')
def serve_html():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)