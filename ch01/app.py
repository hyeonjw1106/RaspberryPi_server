from flask import Flask

app = Flask(__name__)

@app.route('/<action>')
def greet(action):
    if action == "hi":
        return "hi flask world"
    elif action == "bye":
        return "bye flask world"
    else:
        return f"unknown action: {action}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

