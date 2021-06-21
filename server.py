from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test', methods=['POST', 'GET'])
def test():
    if request.method == 'POST':
        data = request.get_json()
        value = data.get("string_to_cut", '')
        return {"return_string": value[2::3] } 
    else:
        return 'Something went wrong. Try again.'