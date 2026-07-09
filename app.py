import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# ----------------------------
# Page Config
st.set_page_config(page_title="Air Quality Predictor", layout="wide")

# Custom CSS to make inputs compact
st.markdown("""
    <style>
        div[data-baseweb="input"] > div {
            max-width: 180px;
        }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# Title
st.title("🌍 Air Quality Index Prediction")
st.write("Predict **CO(GT)** levels using air quality sensor data")

# ----------------------------
# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("AirQualityUCI.csv")
    df = df.drop(columns=['Unnamed: 15', 'Unnamed: 16'], errors='ignore')
    df = df.dropna()
    return df

data = load_data()

# ----------------------------
# Prepare ML data
X = data.drop(columns=['CO(GT)', 'Date', 'Time'], errors='ignore')
y = data['CO(GT)']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

@st.cache_resource
def train_model():
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

model = train_model()

# ----------------------------
# Input Section
st.subheader("Enter Air Quality Parameters")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Gas Sensors**")
    pt08_co = st.number_input("PT08.S1(CO)", float(X['PT08.S1(CO)'].min()), float(X['PT08.S1(CO)'].max()), float(X['PT08.S1(CO)'].mean()))
    nmhc = st.number_input("NMHC(GT)", float(X['NMHC(GT)'].min()), float(X['NMHC(GT)'].max()), float(X['NMHC(GT)'].mean()))
    c6h6 = st.number_input("C6H6(GT)", float(X['C6H6(GT)'].min()), float(X['C6H6(GT)'].max()), float(X['C6H6(GT)'].mean()))
    nox = st.number_input("NOx(GT)", float(X['NOx(GT)'].min()), float(X['NOx(GT)'].max()), float(X['NOx(GT)'].mean()))

with col2:
    st.markdown("**Sensor Array**")
    pt08_nmhc = st.number_input("PT08.S2(NMHC)", float(X['PT08.S2(NMHC)'].min()), float(X['PT08.S2(NMHC)'].max()), float(X['PT08.S2(NMHC)'].mean()))
    pt08_nox = st.number_input("PT08.S3(NOx)", float(X['PT08.S3(NOx)'].min()), float(X['PT08.S3(NOx)'].max()), float(X['PT08.S3(NOx)'].mean()))
    no2 = st.number_input("NO2(GT)", float(X['NO2(GT)'].min()), float(X['NO2(GT)'].max()), float(X['NO2(GT)'].mean()))
    pt08_no2 = st.number_input("PT08.S4(NO2)", float(X['PT08.S4(NO2)'].min()), float(X['PT08.S4(NO2)'].max()), float(X['PT08.S4(NO2)'].mean()))

with col3:
    st.markdown("**Environment**")
    pt08_o3 = st.number_input("PT08.S5(O3)", float(X['PT08.S5(O3)'].min()), float(X['PT08.S5(O3)'].max()), float(X['PT08.S5(O3)'].mean()))
    temperature = st.number_input("Temperature (°C)", float(X['T'].min()), float(X['T'].max()), float(X['T'].mean()))
    humidity = st.number_input("Humidity (RH %)", float(X['RH'].min()), float(X['RH'].max()), float(X['RH'].mean()))
    absolute_humidity = st.number_input("Absolute Humidity (AH)", float(X['AH'].min()), float(X['AH'].max()), float(X['AH'].mean()))

# ----------------------------
# Prediction
st.markdown("---")
if st.button("Predict CO(GT)"):
    user_data = {
        'PT08.S1(CO)': pt08_co,
        'NMHC(GT)': nmhc,
        'C6H6(GT)': c6h6,
        'PT08.S2(NMHC)': pt08_nmhc,
        'NOx(GT)': nox,
        'PT08.S3(NOx)': pt08_nox,
        'NO2(GT)': no2,
        'PT08.S4(NO2)': pt08_no2,
        'PT08.S5(O3)': pt08_o3,
        'T': temperature,
        'RH': humidity,
        'AH': absolute_humidity
    }

    user_df = pd.DataFrame([user_data])
    user_df = user_df[X.columns]

    prediction = model.predict(user_df)[0]

    st.subheader("Prediction Result")
    st.success(f"Predicted CO(GT): {prediction:.2f}")

    if prediction <= 2.0:
        st.info("Status: SAFE  |  Pollution Level: LOW")
    else:
        st.error("Status: UNSAFE  |  Pollution Level: HIGH")
