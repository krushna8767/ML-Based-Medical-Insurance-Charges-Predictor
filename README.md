# 🏥 Medical Insurance Charges Prediction App

[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?logo=streamlit\&logoColor=white)]()
[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python\&logoColor=white)]()
[![Machine Learning](https://img.shields.io/badge/ML-Regression%20Model-green)]()
[![Status](https://img.shields.io/badge/Deployment-Live-success?logo=streamlit)]()

---

## 🔗 Live App

👉 **[https://your-streamlit-app-link](https://loanpredictionproject-tejasgholap.streamlit.app/)**

---

## 🧠 Project Overview

This interactive web app predicts **Medical Insurance Charges** for an individual based on their:

* **Age**
* **BMI**
* **Smoking Status**

The model is trained using a regression algorithm and saved as `best_model.pkl`.
The app uses Streamlit to provide a clean and user-friendly interface for instant predictions.

---

## 🎯 Features

✔️ Real-time prediction of estimated medical insurance cost
✔️ Simple and modern Streamlit interface
✔️ Sidebar with developer profile
✔️ Shows estimated charges in USD
✔️ Error handling if model file is missing
✔️ Lightweight and deploy-ready

---

## 🧩 Input Fields

| Feature | Description       |
| ------- | ----------------- |
| Age     | User age (18–100) |
| BMI     | Body Mass Index   |
| Smoker  | Yes / No          |

---

## 🖥️ Tech Stack Used

| Component    | Technology                                    |
| ------------ | --------------------------------------------- |
| Frontend     | Streamlit                                     |
| Backend      | Python                                        |
| ML Algorithm | Regression (custom model in `best_model.pkl`) |
| Libraries    | NumPy • Streamlit • Pickle                    |

---

## 📂 Project Structure

```
Medical-Insurance-Prediction/
│
├── streamlit_app.py        # Main Streamlit UI
├── best_model.pkl          # Trained ML regression model
├── requirements.txt        # Required dependencies
└── README.md               # Documentation
```

---

## 🏁 Run the App Locally

1️⃣ Clone the repository

```bash
git clone https://github.com/tejasgholap45/Medical-Insurance-Predictor.git
cd Medical-Insurance-Predictor
```

2️⃣ Install necessary packages

```bash
pip install -r requirements.txt
```

3️⃣ Run the Streamlit app

```bash
streamlit run streamlit_app.py
```

4️⃣ Open in browser

```
http://localhost:8501
```

---

## 📦 requirements.txt

```
streamlit
scikit-learn
numpy
pandas
pickle5

```
---

```
```
---

## 👨‍💻 Developer

**Tejas Gholap**
MCA Student | Machine Learning & AI Enthusiast

🔗 GitHub: [https://github.com/tejasgholap45](https://github.com/tejasgholap45)
🔗 LinkedIn: [https://www.linkedin.com/in/tejas-gholap-bb3417300/](https://www.linkedin.com/in/tejas-gholap-bb3417300/)

---

## 🙏 Acknowledgements

* Streamlit for the UI
* NumPy and Pickle for model handling
* Open-source ML ecosystem
