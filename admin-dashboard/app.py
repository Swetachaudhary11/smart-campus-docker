from flask import Flask

app = Flask(__name__)

@app.route('/')
def admin():
    return "Admin Dashboard Running"

app.run(host='0.0.0.0', port=5003)