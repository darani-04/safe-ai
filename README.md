# 🚀 SafeRoute AI – Intelligent Safety Navigation System

## 📌 Overview

SafeRoute AI is an intelligent web-based safety navigation system designed to help users identify and choose safer travel routes based on real-world data. The system analyzes multiple environmental and situational factors such as crowd density, street lighting conditions, and crime reports to enhance user safety during navigation.

Unlike traditional navigation systems that focus only on the shortest path, SafeRoute AI prioritizes user safety by integrating data-driven insights into route selection.

---

## 🎯 Objectives

* Enhance personal safety during travel
* Identify and suggest safer routes
* Utilize multi-source data for accurate safety analysis
* Apply intelligent decision-making in navigation systems

---

## 🧠 Key Features

* 🔐 User Authentication System
* 🗺️ Smart Route Safety Analysis
* 📊 Crowd Density Evaluation
* 💡 Street Lighting Condition Assessment
* 🚨 Crime Data Analysis
* ⚠️ Risk Level Prediction
* 📍 Interactive Map Visualization using Leaflet.js

---

## 🛠️ Tech Stack

### Frontend:

* HTML5
* CSS3
* JavaScript
* Leaflet.js (for map visualization and route display)

### Backend:

* Python (Flask Framework)

### Data Handling:

* CSV datasets (Crowd Density, Street Light, Crime Reports)

---

## 🗺️ Map Integration

The system uses **Leaflet.js** to:

* Display interactive maps
* Visualize routes dynamically
* Highlight safer paths based on computed safety scores

---

## ⚙️ System Architecture

User → Frontend (UI) → Flask API → Backend Logic → Dataset Processing → Response → UI

---

## 🔄 How It Works

1. User enters source and destination
2. The system gathers data from:

   * Crowd Density Dataset
   * Street Light Dataset
   * Crime Report Dataset
3. Backend processes and combines all data sources
4. Safety score and risk level are calculated
5. Leaflet.js displays the safest route on the map

---

## ▶️ Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/darani-04/safe-ai
```

2. Navigate to the project folder:

```bash
cd SafeRoute
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

5. Open in browser:

```
http://127.0.0.1:5001/
```

---

## 🌐 Live Demo

👉 **Live Project:**
https://safe-ai-5fjq.onrender.com/

---

## 📂 Project Structure

```
SafeRoute/
│── app.py
│── requirements.txt
│── crowddata.csv
│── lightingdata.csv
│── crimedata.csv
│── templates/
│── static/
```

---

## 🔐 Security Note

Sensitive data such as API keys, credentials, or environment variables are not included in this repository. It is recommended to use `.env` files for secure handling of such information.

---

## 🚀 Deployment

This project is deployed using:

* Render (Backend & Hosting)

---

## 📈 Future Enhancements

* Integration with real-time GPS tracking
* Machine Learning-based safety prediction
* Live traffic and crime data integration
* Mobile application development

---

## 🏆 Achievements

* 🥇 First Place – Project Expo, Arifa Institute of Technology, Nagapattinam
* 🥉 Third Place – ML & Web Development Project Expo

---

## 👤 Author

**Darani A**
Aspiring Full Stack Developer | AI Enthusiast

---

## 📄 License

This project is developed for educational and research purposes.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
