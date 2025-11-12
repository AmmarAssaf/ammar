
# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    result = 5 + 3
    return f'<h1>نتيجة الجمع: 5 + 3 = {result}</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
