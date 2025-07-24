# Student Grade

Hệ thống **tra cứu và dự đoán điểm sinh viên** gồm hai tính năng chính:

- **Tra cứu điểm sinh viên**
- **Dự đoán GPA tương lai** dựa vào dữ liệu hiện tại (Backend Node.js + Python Flask )

---

## Tính năng chính

1. **Tra cứu điểm sinh viên**: 
   - Giao diện đơn giản, dễ sử dụng
   - Tìm kiếm theo MSSV

2. **Dự đoán điểm học tập (GPA)**:
   - Người dùng nhập GPA hiện tại, tín chỉ hiện có và mục tiêu GPA
   - Hệ thống dự đoán GPA cuối khóa và cung cấp phản hồi, lời khuyên

---

## Công nghệ sử dụng

| Layer        | Công nghệ                                                                 |
|--------------|--------------------------------------------------------------------------|
| Frontend     | HTML, CSS, JavaScript                                                    |
| Backend API  | Node.js (ExpressJS)                                                      |
| ML Server    | Python (Flask, joblib, pandas, GPT4All)                                  |
| Cơ sở dữ liệu| PostgreSQL                                                               |
| ML Model     | Mô hình dự đoán GPA (`gpa_predictor_model.pkl`) và GPT4All (`.gguf`)     |

---

## Cài đặt và chạy hệ thống

### 1. Clone dự án
```bash
git clone https://github.com/Huy-Toan/student-grade.git
````

### 2. Cài đặt phần Node.js server
```bash 
cd server
npm install
npm start
````
### 3. Cài đặt và chạy Flask server (Python)
```bash 
cd flask-server
python predict_api.py
````
### Lưu ý: 
- Flask server cần model gpa_predictor_model.pkl và mô hình ngôn ngữ .gguf đặt đúng vị trí trong file model.
- Đảm bảo đã cài gpt4all và các thư viện Python cần thiết




