from flask import Flask, request, jsonify
import io
import sys

app = Flask(__name__)


@app.route('/run', methods=['POST'])
def run_code():
    code = request.json['code']
    sys.stdout = io.StringIO()
    try:
        exec(code)
    except Exception as e:
        print(str(e))
    output = sys.stdout.getvalue()
    sys.stdout = sys.__stdout__
    return jsonify({'output': output})


if __name__ == '__main__':
    app.run(debug=True)
