const express = require('express');
const router = express.Router();
const axios = require('axios'); 

// Route xử lý POST từ client
router.post('/', async (req, res) => {
    const {
        currentGPA, desiredGPA,
        currentCredits, totalCredits,
        remaining2CreditCourses, remaining3CreditCourses
    } = req.body;

    try {
        // Gửi dữ liệu sang Flask server
        const response = await axios.post('http://localhost:5000/predict', {
            current_credits: parseInt(currentCredits),
            total_credits: parseInt(totalCredits),
            current_gpa: parseFloat(currentGPA),
            target_gpa: parseFloat(desiredGPA),
            num_2_credit: parseInt(remaining2CreditCourses),
            num_3_credit: parseInt(remaining3CreditCourses)
        });

        const { predicted_final_gpa, feedback } = response.data;

        // Gửi kết quả lại về client
        res.json({
            predictedGPA: predicted_final_gpa,
            message: feedback
        });

    } catch (error) {
        console.error("Lỗi gọi Flask:", error.message);
        res.status(500).json({ error: "Lỗi khi dự đoán GPA từ server Python" });
    }
});


module.exports = router;
