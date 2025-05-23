import joblib
from flask import Flask, request, jsonify, render_template
# request : 요청객체, A가 B를 호출할 때 보내는 정보를 담고 있음
from konlpy.tag import Okt # 자바가 깔려있어야 돌아감 -> 주의

app = Flask(__name__)

okt = Okt()

def tw_tokenzier(text): # 일반적으로 tw_tokenzier 오류 많이 남
    tokenzier_ko = okt.morphs(text)
    return tokenzier_ko

try:
    model = joblib.load("머신러닝/lr_v1.pkl")
    vec = joblib.load("머신러닝/tfidf_vect.pkl")
except Exception as e:
    print(f"모델 로드 중 오류 발생: {str(e)}")
    raise

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"]) # 이 url로 나게에 전달
def predict():
    # 1. 웹개발 (프론트, 백앤드에서 정보를 예쁘게 처리했다 해도 방어막 만들어야 함)
    data = request.get_json() # form으로 요청하는 정보를 바꿔줌
    if not data or "text" not in data:
        return jsonify({"error" : "텍스트가 올바르지 않거나 제공되지 않습니다."}), 400 # 400 에러
    text = data["text"]
    if not text.strip():
        return jsonify({"error" : "텍스트가 올바르지 않거나 제공되지 않습니다."}), 400 # text가 비어있을 때
    # 2. 웹개발 X
    # vec를 transform 하고
    # lr을 사용해서 예측하고
    # 긍정/부정으로 변경해서
    text_tfidf = vec.transform([text])
    predict = model.predict(text_tfidf)[0]
    return jsonify({"emotion" : str(predict)})

# 내가 쓰면 뜨고 남이 import하면 안 뜸
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
# debug=True : ?
# host="0.0.0.0" : Running on http://10.125.121.171:5001 이거 백앤드 주려고