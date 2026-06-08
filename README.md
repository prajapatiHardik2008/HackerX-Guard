HackerX-Guard & Nexa Integration 🛡️🤖
HackerX-Guard is an advanced AI-powered workstation security system, now seamlessly integrated with Nexa AI Assistant. This system uses facial recognition to grant access to your Windows workstation and, upon successful verification, automatically launches your Nexa AI assistant, transitioning your security guard into your digital companion.

🚀 Features
AI Authentication: Robust facial verification using the DeepFace framework and OpenCV.

Integrated Nexa AI: Automated trigger of Nexa AI immediately following successful identity verification.

Intrusion Defense: Automated system lockdown ("Hacker X Mode") if unauthorized access or a timeout occurs.

Interactive Intelligence: Voice-controlled automation (Nexa) and interactive security alerts (gTTS).

🛠️ Prerequisites & Installation
⚠️ Note: This project is optimized for Windows OS (utilizing ctypes.windll for system interaction).

1. Clone the repositories
You will need both repositories to complete the integration:

Bash
# Clone HackerX-Guard
git clone https://github.com/prajapatiHardik2008/HackerX-Guard.git
cd HackerX-Guard

# Clone Nexa AI
git clone https://github.com/prajapatiHardik2008/Nexa.git
2. Setup Environment & Dependencies
It is best practice to maintain isolated virtual environments for each module:

Bash
# Inside HackerX-Guard folder
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt

# Inside Nexa folder
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
3. Setup Integration
In HackerX-Guard/main.py, update the path to point to your Nexa environment:

Open main.py.

Locate the python_executable variable and set it to the absolute path of your Nexa virtual environment (e.g., D:\Nexa\.venv\Scripts\python.exe).

4. Configuration
.env: Create a .env file in the HackerX-Guard root and set your hashed ADMIN_KEY.

Owner Image: Place a photo of yourself named h.jpeg in the HackerX-Guard root directory.

💻 How to Use
Start System: In the HackerX-Guard folder, run python main.py.

Authenticate: Look at the webcam to verify your identity.

Trigger Nexa: Once verified, the system will prompt: "Do you want to start Nexa right now?"

Command: Say 'yes' to launch your Nexa AI assistant automatically!

🔧 Architecture
Authentication Layer: DeepFace & OpenCV.

Security Core: Ctypes (WinAPI) & Werkzeug.

Voice Intelligence: Nexa AI (OpenAI API, SpeechRecognition).

Process Orchestration: Subprocess (Environment-isolated execution).
📄 License
MIT License.

📄 License
MIT License.
