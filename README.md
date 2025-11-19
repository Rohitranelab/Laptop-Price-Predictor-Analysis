# 💻 Laptop Price Predictor

A Machine Learning–powered web application that predicts the **price of a laptop** based on its specifications such as brand, RAM, screen size, storage type, CPU, GPU, and display features.  
The app is built using **Streamlit** and a trained ML model (Scikit-Learn Pipeline).

---

## 📌 Project Aim

To develop a system that accurately predicts laptop prices based on various hardware specifications using Machine Learning and provides an easy-to-use web interface for users.

---

## 📦 Features

- Select laptop brand and type  
- Input RAM, weight, screen size  
- Choose touchscreen & IPS display  
- Select CPU, GPU, HDD, SSD  
- Calculates **PPI automatically**  
- Predicts price instantly  
- Simple and interactive UI (Streamlit)

---

## 🛠️ Technologies Used

| Component | Technology |
|----------|------------|
| Frontend | Streamlit |
| Backend ML | Scikit-Learn, XGBoost |
| Data | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Model Serialization | Pickle |

---

## 📂 Dataset Information

The dataset (`laptop_data.csv`) contains **1303 rows** and **12 columns** with laptop specifications such as:

- Company  
- TypeName  
- Inches  
- ScreenResolution  
- CPU  
- RAM  
- HDD/SSD Memory  
- GPU  
- Operating System  
- Weight  
- Price (Target variable)

---

## 🎯 Target Audience

- Students learning ML  
- Data science beginners  
- Laptop buyers  
- Tech shops & e-commerce vendors  
- Developers exploring ML deployment  

---

## 🔧 Project Structure

Laptop-Price-Predictor/
│
├── app.py # Streamlit web app
├── requirements.txt # Required Python libraries
├── laptop_data.csv # Dataset used for training
├── pipe.pkl # Trained ML model pipeline
├── df.pkl # Processed dataset for the app
└── README.md # Project documentation
