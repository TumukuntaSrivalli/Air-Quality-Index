# 🌍 Air Quality Index Prediction using Machine Learning

A Machine Learning web application built with **Python**, **Streamlit**, and **Random Forest Regression** to predict **Carbon Monoxide (CO(GT))** levels using air quality sensor data from the AirQualityUCI dataset.

---

## 📖 Project Overview

Air pollution is one of the leading environmental challenges affecting human health. Carbon Monoxide (CO) is a harmful gas produced mainly from vehicle emissions and industrial activities.

This project analyzes air quality sensor data and predicts **CO(GT)** concentration using a **Random Forest Regressor**. Users can enter various environmental and gas sensor values through an interactive Streamlit interface and instantly receive a predicted CO(GT) value along with its pollution status.

---

## ✨ Features

* 🌍 Predicts **CO(GT)** concentration
* 🤖 Machine Learning using Random Forest Regression
* 📊 Interactive Streamlit web interface
* 🧹 Automatic dataset loading and preprocessing
* ⚡ Fast predictions using cached model
* 📱 Responsive and user-friendly UI

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn

---

## 📂 Dataset

**Dataset:** AirQualityUCI

The dataset contains hourly air quality measurements including:

* PT08.S1(CO)
* NMHC(GT)
* C6H6(GT)
* PT08.S2(NMHC)
* NOx(GT)
* PT08.S3(NOx)
* NO2(GT)
* PT08.S4(NO2)
* PT08.S5(O3)
* Temperature (T)
* Relative Humidity (RH)
* Absolute Humidity (AH)

**Target Variable**

* CO(GT)

---

## 📁 Project Structure

```text
Air-Quality-Prediction/
│
├── app1.py
├── AirQualityUCI.csv
├── requirements.txt
├── README.md
└── images/
```

---

## ⚙️ Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/TumukuntaSrivalli/Air-Quality-Index.git
```

### Step 2: Open in Visual Studio Code

```bash
cd Air-Quality-Prediction
code .
```

---

### Step 3: Create a Virtual Environment

**Windows**

```bash
python -m venv venv
```

---

### Step 4: Activate the Virtual Environment

**Windows (PowerShell)**

```powershell
.\venv\Scripts\Activate
```

**Windows (Command Prompt)**

```cmd
venv\Scripts\activate
```

---

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 6: Run the Streamlit Application

```bash
streamlit run app.py
```

The application will automatically open in your default web browser.

If it does not open automatically, copy and paste the local URL displayed in the terminal (typically `http://localhost:8501`) into your browser.

---

## 📊 Machine Learning Model

**Algorithm Used**

* Random Forest Regressor

### Input Features

* PT08.S1(CO)
* NMHC(GT)
* C6H6(GT)
* PT08.S2(NMHC)
* NOx(GT)
* PT08.S3(NOx)
* NO2(GT)
* PT08.S4(NO2)
* PT08.S5(O3)
* Temperature
* Relative Humidity
* Absolute Humidity

### Output

Predicted **CO(GT)** concentration.

---

## 🖥️ How to Use

1. Launch the Streamlit application.
2. Enter the air quality sensor values.
3. Click **Predict CO(GT)**.
4. View the predicted CO(GT) concentration.
5. Check whether the pollution level is **Safe** or **Unsafe**.

---

## 📦 Requirements

```text
streamlit
pandas
numpy
scikit-learn
```

---

## 🚀 Future Enhancements

* Display model evaluation metrics (R², MAE, RMSE)
* Feature importance visualization
* Air quality trend analysis
* Interactive data visualizations
* Deployment on Streamlit Community Cloud
* Real-time air quality data integration

---

## 👩‍💻 Author

**T. Srivalli**

B.Tech – Computer Science and Engineering (Data Science)

