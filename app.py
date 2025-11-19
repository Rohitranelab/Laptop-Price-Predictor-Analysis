import streamlit as st
import pickle
import pandas as pd
import numpy as np

# -----------------------
# Page Config
# -----------------------
st.set_page_config(
    page_title="Laptop Price Predictor",
    page_icon="💻",
    layout="centered",
    initial_sidebar_state="expanded"
)

# -----------------------
# Sidebar – Project Information
# -----------------------
st.sidebar.title("📘 Project Info")
st.sidebar.markdown("""
### 💻 Laptop Price Predictor
This app predicts the **market price** of a laptop based on its specifications.

#### 🔍 Features:
- Brand & Type selection  
- Hardware configuration  
- Display specifications  
- CPU/GPU options  
- Price predicted using **machine learning model**  

#### 📂 Technologies:
- Streamlit (Frontend UI)  
- Scikit-Learn (Model)  
- Pandas / NumPy  

#### 👨‍💻 Developer:
**Rohit Rane**  

""")


# -----------------------
# Page Style
# -----------------------
st.markdown("""
    <style>
        .main {
            background-color: #f7f9fc;
        }
        .title {
            text-align: center;
            font-size: 42px !important;
            color: #2B547E;
            font-weight: 700;
        }
        .subheader {
            color: #444;
            font-size: 20px;
            margin-top: -10px;
        }
        .bold-label {
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------
# Load model + dataset
# -----------------------
pipe = pickle.load(open(r"D:\Data Science\Projects\Final Project\Notebook\pipe.pkl", "rb"))
df = pickle.load(open(r"D:\Data Science\Projects\Final Project\Notebook\df.pkl", "rb"))

st.markdown("<h1 class='title'>💻 Laptop Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheader'>Select laptop specifications to estimate its market price</p>", unsafe_allow_html=True)

# -----------------------
# UI Layout
# -----------------------
st.markdown("### 🏷️ Laptop Details")

col1, col2 = st.columns(2)

with col1:
    company = st.selectbox("Brand", df["Company"].unique())
    laptop_type = st.selectbox("Type", df["TypeName"].unique())
    ram = st.selectbox("RAM (GB)", [2,4,6,8,12,16,24,32,64])
    weight = st.number_input("Weight of Laptop (kg)", min_value=0.5, max_value=5.0, value=1.5)

with col2:
    touchscreen = st.selectbox("Touchscreen", ["No", "Yes"])
    ips = st.selectbox("IPS Display", ["No", "Yes"])
    screen_size = st.slider("Screen Size (inches)", 10.0, 18.0, 13.0)
    resolution = st.selectbox(
        "Screen Resolution",
        ['1920x1080','1366x768','1600x900','3840x2160',
         '3200x1800','2880x1800','2560x1600','2560x1440','2304x1440']
    )

st.markdown("---")

st.markdown("### ⚙️ Hardware Specifications")
col3, col4 = st.columns(2)

with col3:
    cpu = st.selectbox("CPU Brand", df["Cpu brand"].unique())
    hdd = st.selectbox("HDD (GB)", [0,128,256,512,1024,2048])

with col4:
    ssd = st.selectbox("SSD (GB)", [0,8,128,256,512,1024])
    gpu = st.selectbox("GPU Brand", df["Gpu brand"].unique())

os = st.selectbox("Operating System", df["os"].unique())

# -----------------------
# Prediction Logic
# -----------------------
st.markdown("---")
if st.button("🔍 Predict Price", use_container_width=True):

    touchscreen_val = 1 if touchscreen == "Yes" else 0
    ips_val = 1 if ips == "Yes" else 0

    X_res = int(resolution.split("x")[0])
    Y_res = int(resolution.split("x")[1])
    ppi = ((X_res**2 + Y_res**2) ** 0.5) / screen_size

    query = pd.DataFrame([{
        "Company": company,
        "TypeName": laptop_type,
        "Ram": ram,
        "Weight": weight,
        "Touchscreen": touchscreen_val,
        "IPS": ips_val,
        "PPI": ppi,
        "Cpu brand": cpu,
        "HDD": hdd,
        "SSD": ssd,
        "Gpu brand": gpu,
        "os": os
    }])

    predicted_log_price = pipe.predict(query)[0]
    predicted_price = np.exp(predicted_log_price)

    st.success(f"💰 **Predicted Price: ₹{int(predicted_price):,}**")
