# API Front-End (Flask + jsonplaceholder)

A tiny example project demonstrating a minimal Flask app that serves a few static HTML pages and exposes simple proxy API endpoints which fetch data from https://jsonplaceholder.typicode.com.

This project is intended as a learning/demo app showing how to:

- Serve static HTML files from Flask
- Create simple API routes that fetch remote JSON and return it to the client
- Use client-side JavaScript (fetch) to call local API routes and display results

## Repository structure

- `app.py` - Flask application. Serves HTML pages and provides two API routes:
  - `/api/user` - fetches user data from jsonplaceholder (`/users/1`)
  - `/api/posts` - fetches posts data from jsonplaceholder (`/posts`)
- `index.html` - Home page with links to the user and posts pages
- `user.html` - Simple page that fetches and displays a single user (via `/api/user`)
- `posts.html` - Simple page that fetches and displays posts (via `/api/posts`)

## Quick start

Requirements:

- Python 3.8+
- `pip` (or `py -m pip` on Windows)

Recommended: create and activate a virtual environment.

On Windows (PowerShell):

```powershell
py -3 -m venv .venv; .\.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
```

If there is no `requirements.txt`, install Flask and requests directly:

```powershell
py -m pip install Flask requests
```

Run the app:

```powershell
py app.py
```

By default Flask runs in debug mode in this project. Open your browser at http://127.0.0.1:5000/ and click through the pages.

## Endpoints

- GET / -> serves `index.html`
- GET /user -> serves `user.html`
- GET /posts -> serves `posts.html`
- GET /api/user -> returns JSON from `https://jsonplaceholder.typicode.com/users/1`
- GET /api/posts -> returns JSON from `https://jsonplaceholder.typicode.com/posts`

Example: in `posts.html` the following client JS fetches the first five posts:

```js
const res = await fetch('/api/posts');
const data = await res.json();
document.getElementById('data').textContent = JSON.stringify(data.slice(0, 5), null, 2);
```

## Files overview

- `app.py` (Flask server)
  - Uses `requests` to perform server-side API calls then returns the JSON via `jsonify`.
  - Serves the HTML files using `send_from_directory('.', '<file>')` so the files can live in the project root for simplicity.

- `index.html`
  - Simple navigation to the user and posts pages.

- `user.html`
  - Button which calls `/api/user` and displays the JSON response inside a `<pre>` element.

- `posts.html`
  - Button which calls `/api/posts` and displays the first five entries.

## Notes and next steps

- This is intentionally minimal and safe for demos. Consider these improvements if you want to expand the project:
  - Add `requirements.txt` (e.g., `Flask\nrequests`).
  - Use Flask's `static/` and `templates/` conventions for larger projects.
  - Add basic error handling and user-friendly UI for network errors.
  - Add unit tests for the Flask routes.

## Troubleshooting

- If you get network errors, ensure your machine can reach `https://jsonplaceholder.typicode.com`.
- If Flask fails to start because port 5000 is in use, run with `py -m flask run --port 5001` or change the `app.run` call.

## License

This project is provided as-is for learning and demonstration purposes.
