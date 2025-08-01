# 🕒 Digital Clock using Python and Tkinter

This is a simple **Digital Clock** GUI application built using Python's `tkinter` library. It displays the current system time and updates every second.

## 📸 Preview

![Digital Clock Screenshot](screenshot.png) <!-- Optional: Add a screenshot of your app -->

---

## 💡 Features

- Real-time clock display (HH:MM:SS AM/PM)
- Stylish digital font with cyan-on-black theme
- Simple and lightweight GUI
- Updates every second automatically

---

## 📦 Requirements

- Python 3.x  
- Tkinter (usually comes pre-installed with Python)

---

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/digital-clock.git
   cd digital-clock
   
Run the Python file:

bash
Copy
Edit
python digital_clock.py
🛠️ Code Overview
strftime() is used to fetch current time.

after(1000, time) is used to update the time every second.

GUI window is created with Tk(), and styled with background and font colors.

📁 File Structure
bash
Copy
Edit
digital-clock/
├── digital_clock.py   # Main Python script
└── README.md          # Project README

📌 Future Improvements (Optional)
Add date display

Allow format switching (12/24-hour)

Add theme customization

