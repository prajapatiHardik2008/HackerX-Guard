# HackerX-Guard


HackerX-Guard 🛡️👀

An AI-powered local authentication and security system that uses facial recognition to grant access to your Windows workstation. If an unauthorized face is detected, it triggers audio warnings, demands an encrypted access key within a specific timeout, and automatically locks down the system if verification fails ("Hacker X Mode").

## 🚀 Features

*   **AI Facial Recognition:** Uses the `DeepFace` framework and OpenCV to capture and verify the user's identity against an owner image.
*   **Voice Assistant Integration:** Uses Google Text-to-Speech (`gTTS`) and `pygame` to provide interactive voice prompts and security alerts.
*   **Secure Access Key:** Fallback option using hashed passwords (`werkzeug.security`) if face verification fails.
*   **Timed Input:** Uses custom Windows-native input loop with a 10-second countdown before auto-locking.
*   **Automated Workstation Lock:** Instantly locks Windows using `ctypes` if an unauthorized intrusion or timeout occurs.

---

## 🛠️ Prerequisites & Installation

> ⚠️ **Note:** This project is designed specifically for **Windows OS** because it utilizes `msvcrt` for key-handling and `ctypes.windll` for locking the workstation.

### 1. Clone the repository
```bash
git clone https://github.com/prajapatiHardik2008/HackerX-Guard.git
cd HackerX-Guard

```

### 2. Install Dependencies

Make sure you have Python installed, then install the required libraries:

```bash
pip install opencv-python deepface gtts pygame python-dotenv werkzeug

```

### 3. Setup Environment Variables

Create a `.env` file in the root directory of the project and add your hashed admin key:

```env
ADMIN_KEY=your_werkzeug_pbkdf2_hashed_password_here

```

### 4. Add Owner Image

Place a photo of your face in the root directory and name it `h.jpeg` (or change the `OWNER_IMAGE` variable in the script to match your image file name).

---

## 💻 How to Use

Simply run the main python script:

```bash
python main.py

```

1. The script will ask you to look at the webcam.
2. If it recognizes you, it will welcome you back.
3. If it doesn't recognize the face, it will ask for a backup Access Key.
4. If the wrong key is entered or the 10-second timer expires, **Hacker X mode activates** and locks your Windows machine immediately.

---

## 🔧 Technologies Used

* **Python 3.x**
* **DeepFace** & **OpenCV** (Computer Vision & Face Verification)
* **gTTS** & **Pygame Mixer** (Audio & Speech Synthesis)
* **Werkzeug** (Secure Password Hashing)
* **Ctypes** (Windows API Integration)

---

## 📄 License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).

---
