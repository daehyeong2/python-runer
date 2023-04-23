from flask import Flask, request

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_code():
    # 요청 데이터 가져오기
    request_data = request.get_json()
    # 요청 값이 "value"인 경우에만 처리
    try : exec(request_data['code'])
    except : return "Error"
    return exec(request_data['code'])

