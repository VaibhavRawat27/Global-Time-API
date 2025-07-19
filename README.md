# 🌍 GlobalTime API

GlobalTime is a simple **Flask-based API** that provides:

✅ **All official timezones of a given country**  
✅ **Current time for a specific timezone**  

This project runs **locally** and uses Python's `pytz` library (no external APIs).

---

## 🚀 Features
- Get all valid timezones for any country (e.g., India, Australia, United States).
- Get current time (with live updates) for any timezone.
- Fully local (no internet dependency except initial library installation).

---

## 📦 Installation

### 1. Clone or Download
```
git clone https://github.com/vaibhavrawat27/globaltimeapi.git
cd globaltime
```

### 2. Install Required Libraries
```
pip install flask pytz
```

### 3. Run the Flask App
```
python api.py
```

You should see:
```
 * Running on http://127.0.0.1:5000/
```

---

## 🔥 Usage

### 1. **Get All Timezones of a Country**
**Request:**
```
http://127.0.0.1:5000/globaltime?country=India
```
**Response:**
```json
{
  "country": "India",
  "timezones": ["Asia/Kolkata"]
}
```

### 2. **Get Current Time of a Specific Timezone**
**Request:**
```
http://127.0.0.1:5000/globaltime?timezone=Asia/Kolkata
```
**Response:**
```json
{
  "timezone": "Asia/Kolkata",
  "current_time": "2025-07-19 18:30:10"
}
```

---

## 🛠 Project Structure
```
globaltime/
│
├── api.py        # Main Flask application
├── LICENSE       # MIT License 
├── README.md     # Project documentation
├── api.py        # Main API Code
└── requirements.txt # All Python Library 
```

---

<!--## 📌 Future Enhancements
- Add **weather information** (temperature) for each timezone.
- Add **case-insensitive & partial country name search**.
- Deploy the API online for global access.

--- -->

## 📝 License
This project is licensed under the **MIT License** – feel free to use and modify.

---

### ✨ Author
Developed by **Vaibhav Rawat**  
