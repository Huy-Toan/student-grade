from flask import Flask, request, jsonify
import joblib
import pandas as pd
from gpt4all import GPT4All

app = Flask(__name__)

gpa_model = joblib.load("gpa_predictor_model.pkl")

# Tải model sử dụng file .gguf
gpt_model = GPT4All("models/mistral-7b-instruct-v0.1.Q3_K_L.gguf")

def generate_feedback(current_gpa, target_gpa, predicted_gpa):
    prompt = f"""
Tôi là một sinh viên đại học. GPA hiện tại của tôi là {current_gpa}, mục tiêu là {target_gpa}, và hệ thống dự đoán tôi có thể đạt {predicted_gpa}.
Hãy viết một đoạn phản hồi ngắn (1-3 câu) bằng tiếng Việt để đưa ra lời khuyên hoặc khuyến khích phù hợp.
"""
    with gpt_model:
        response = gpt_model.generate(prompt, max_tokens=100, temp=0.7, top_k=40, top_p=0.9)
        return response.strip()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        print("Nhận dữ liệu:", data)

        input_df = pd.DataFrame([{
            "current_credits": data["current_credits"],
            "total_credits": data["total_credits"],
            "current_gpa": data["current_gpa"],
            "target_gpa": data["target_gpa"],
            "num_2_credit": data["num_2_credit"],
            "num_3_credit": data["num_3_credit"]
        }])

        predicted = gpa_model.predict(input_df)[0]
        final_gpa = round(predicted, 2)

        # Tạo phản hồi bằng mô hình GPT
        feedback = generate_feedback(data["current_gpa"], data["target_gpa"], final_gpa)
        
        print(feedback)

        return jsonify({
            "predicted_final_gpa": final_gpa,
            "feedback": feedback
        })

    except Exception as e:
        print("Lỗi:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
