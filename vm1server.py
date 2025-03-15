from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from VM1!"

if __name__ == '__main__':
    port = 8080
    app.run(debug=True, port=port, host='0.0.0.0', use_reloader=False)
