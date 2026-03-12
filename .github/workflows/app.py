from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to CI/CD Demo App!", "status": "ok"})

@app.route('/api/health')
def health():
    return jsonify({"status": "healthy", "version": "1.0.0"})

@app.route('/api/users')
def users():
    return jsonify({
        "users": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)