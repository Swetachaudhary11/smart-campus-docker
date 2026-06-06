from flask import Flask

app = Flask(__name__)

@app.route('/')
def attendance():
    return "Attendance Service Running"

app.run(host='0.0.0.0', port=5001)