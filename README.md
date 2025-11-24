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

- `app.py` - Streamlit web app
- `requirements.txt` - Required Python libraries
- `laptop_data.csv` - Dataset used for training
- `pipe.pkl` - Trained ML model pipeline
- `Laptop_Price_Prediction.ipynb` - Jupyter Notebook for EDA and model development
- `df.pkl` - Processed dataset for the app
- `README.md` - Project documentation

---

## 🧠 Machine Learning Workflow

### ✔ 1. Data Cleaning
- Extracting numeric values (RAM, memory, weight)
- Handling missing and inconsistent data

### ✔ 2. Feature Engineering  
- Encoding brand/type features  
- Extracting CPU and GPU brand  
- Converting touchscreen & IPS to binary  
- Calculating **PPI = √(X² + Y²) / Screen Size**

### ✔ 3. Model Training  
- Regression model using Scikit-Learn  
- Log transformation on price to improve accuracy  
- Evaluation with metrics (RMSE, MAE)

### ✔ 4. Deployment  
- Saving trained pipeline as `pipe.pkl`  
- Building Streamlit app (`app.py`)  
- Real-time user prediction

---

## 📦 Installation & Setup

### **1. Clone the Repository**
```bash
git clone https://github.com/Rohitranelab/Laptop-Price-Predictor.git
cd Laptop-Price-Predictor
```
### **2. Install Required Libraries**
```bash
pip install -r requirements.txt
```

### **3. Run the Streamlit App**
```bash
streamlit run app.py
```


## 🧪 Example Prediction Flow

- User selects:
- Brand: Dell
- RAM: 8GB
- CPU: Intel i5
- GPU: Nvidia
- IPS: Yes
- Touchscreen: No
- Screen Size: 15.6
- Resolution: 1920x1080

**👉 Model predicts something like:**
₹55,000 – ₹65,000 (approx.)

## 💡 Use Cases

- 💰 Laptop price estimator tool
- 🛒 E-commerce laptop pricing support
- 🏬 Shop pricing automation
- 🎓 ML learning project for students
- 🖥️ Laptop comparison applications
