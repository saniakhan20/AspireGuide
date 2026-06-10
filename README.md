# 🎓 AspireGuide- AI-Based Career Prediction & Recommendation System

CareerML is a full-stack web application that combines **Machine Learning** with **ASP.NET MVC** and **Flask API** to provide intelligent career prediction and recommendation services based on user inputs and datasets.

The system uses a trained ML model to analyze user-related data and predict suitable career paths, helping students and learners make informed career decisions.

---

## 📌 Overview

This project integrates:

* **ASP.NET MVC** for frontend and application flow
* **Flask API** for Machine Learning model serving
* **Python ML model** for prediction logic

The application takes user inputs, sends them to the Flask API, and returns AI-powered career predictions dynamically through the web interface.

---

## 🚀 Features

* ✅ AI-based career prediction
* ✅ Machine Learning model integration
* ✅ ASP.NET MVC frontend
* ✅ Flask REST API backend
* ✅ Real-time prediction workflow
* ✅ User-friendly interface
* ✅ End-to-end ML deployment architecture

---

## 🛠️ Tech Stack

### Frontend & Backend

* **ASP.NET MVC**
* **C#**
* **HTML**
* **CSS**
* **JavaScript**

### Machine Learning

* **Python**
* **Flask**
* **Scikit-learn**
* **Pandas**
* **NumPy**

---

## 📂 Project Structure

```bash id="n82ks1"
CareerML/
│
├── Controllers/
│   └── HomeController.cs
│
├── Views/
│   └── Home/
│       └── Index.cshtml
│
├── wwwroot/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
│
├── FlaskAPI/
│   ├── app.py
│   ├── train_model.py
│   ├── requirements.txt
│
├── appsettings.json
├── Program.cs
├── Startup.cs
├── README.md
└── .gitignore
```

---

## ⚙️ How It Works

1. User enters input data through the web interface
2. ASP.NET MVC handles frontend interactions
3. Flask API receives prediction requests
4. ML model processes the input
5. Predicted career recommendation is returned to the user

---

## ▶️ Installation & Setup

### Clone Repository

```bash id="x82ls1"
git clone https://github.com/saniakhan20/CareerML.git
cd CareerML
```

---

## 🔹 Setup Flask API

Navigate to FlaskAPI:

```bash id="m92ls1"
cd FlaskAPI
```

Install dependencies:

```bash id="v82ks1"
pip install -r requirements.txt
```

Run Flask server:

```bash id="l82ks1"
python app.py
```

---

## 🔹 Run ASP.NET MVC Application

Open the project in:

* Visual Studio
* VS Code

Run:

```bash id="s82ks1"
dotnet run
```

The application will launch locally in the browser.

---

## 🧠 Machine Learning Pipeline

The project includes:

* Dataset preprocessing
* Model training
* Prediction generation
* API-based inference

The trained ML model is integrated into the Flask backend for real-time predictions.

---

## 📈 Future Improvements

* User authentication system
* Career roadmap generation
* Resume analysis integration
* AI chatbot assistance
* Deployment on cloud platforms
* Enhanced recommendation accuracy

---

## 📌 Note

Large datasets, virtual environments, and trained model files are excluded from this repository using `.gitignore`.

---

## 👩‍💻 Author

**Sania Khan**

* 💼 LinkedIn: https://www.linkedin.com/in/sania-khan-1a250a370/
* 🧠 LeetCode: https://leetcode.com/saniaakhann/

---

## ⭐ Contributing

Contributions, suggestions, and improvements are welcome!

If you found this project useful, consider giving it a ⭐ on GitHub.
