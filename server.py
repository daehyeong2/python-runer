import json
from flask import Flask, request, redirect
import subprocess

result = ""

app = Flask(__name__)

@app.route("/execute")
def execute_code():
    global result
    code = request.args.get('code')
    if not code:
        result = 'Empty code'
        return redirect('/')
    result = subprocess.check_output(['python', '-c', code], universal_newlines=True)
    return redirect('/')


@app.route("/")
def index():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python code runner</title>
    <style>
        body{
            margin: 0;
            background-color: bisque;
            display:flex;
            height: 100vh;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        .code-box {
            width: 200px;
            height: 100px;
            margin-bottom: 20px;
            display: block;
            border-radius: 20px;
        }
        p{
            color : gray;
        }
        form{
            display:flex;
            flex-direction: column;
            justify-content: center;
        }
        input[type="submit"]{
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h1>Python Code Runner</h1>
    <form action="/execute" method="GET">
        <input type="text" name="code" class="code-box" />
        <input type="submit" value="Execute" />
    </form>
    <p>Result: '''+result+'''</p>
</body>
</html>
'''

if __name__ == "__main__":
    app.run()
