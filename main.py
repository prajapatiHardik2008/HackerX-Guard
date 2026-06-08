from asyncio import subprocess
import time
from werkzeug.security import check_password_hash
from gtts import gTTS
import pygame 
import ctypes
import cv2
from deepface import DeepFace
import os
from dotenv import load_dotenv
import msvcrt
import sys
import subprocess
load_dotenv() 
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'   
def input_with_timeout(prompt, timeout=10):
    print(prompt, end="", flush=True)
    start_time = time.time()
    user_input = ""
    
    while True:
        # Check karo agar 10 seconds poore ho gaye hain
        if time.time() - start_time > timeout:
            print("\n⏰ Time out! 10 seecons for input has passed.")
            return None # Timer khatam, toh None return karega

        # Check karo agar user ne koi key press ki hai
        if msvcrt.kbhit():
            char = msvcrt.getche().decode('utf-8')
            if char == '\r': # '\r' matlab Enter key
                print() # New line ke liye
                return user_input
            elif char == '\b': # Backspace handle karne ke liye
                if len(user_input) > 0:
                    user_input = user_input[:-1]
                    # Screen par se aakhri char mitane ke liye
                    sys.stdout.write(' \b')
                    sys.stdout.flush()
            else:
                user_input += char
                
        time.sleep(0.1) # CPU par load kam karne ke liye chota sa break


def speak(Text):
    tts = gTTS(Text)
    tts.save('text.mp3')

# Initialize pygame mixer
    pygame.mixer.init()

    # Load your audio file

    pygame.mixer.music.load("text.mp3")  # Replace with your file path

    # Play the audio
    pygame.mixer.music.play()

    # print("Playing music... Press Enter to stop.")
    # input()  # Keeps the program running until you press Enter
    # Stop the music
    while pygame.mixer.music.get_busy():
      time.sleep(0.1)
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    os.remove("text.mp3")

def capture_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("captured_image.jpg", frame)
    cap.release()

def verify_and_lock(owner_img, test_img):
    print("🔄 Verifying identity... Please wait.")
    
    # Check agar files exist karti hain
    if not os.path.exists(owner_img) or not os.path.exists(test_img):
        print("❌ Error: missing file(s). Please check the paths and try again.")
        return

    try:
        # DeepFace se dono images ko compare kar rahe hain
        # Enforce_detection=False rakha hai taaki agar photo clear na ho toh crash na kare
        result = DeepFace.verify(
            img1_path=owner_img, 
            img2_path=test_img, 
            enforce_detection=False
        )
        
        # Result check kar rahe hain
        if result["verified"]:
            return True 
        else:
            return False
            # Windows ko lock karne ka command
            # ctypes.windll.user32.LockWorkStation()
            
    except Exception as e:

        print(f"❌ Something went wrong: {e}")
        return "Something went wrong. Please check the error message above."


# Run the test
if __name__ == "__main__":
    # Apni do files ka naam yahan likho
    while True:
        speak("Please look at the camera for identity verification.")
        capture_image()
        if not os.path.exists("captured_image.jpg"):
            continue
        OWNER_IMAGE = "h.jpeg"
        TEST_IMAGE = "captured_image.jpg"
        #capture_image()  # Capture a new image from webcam
        res = verify_and_lock(OWNER_IMAGE, TEST_IMAGE)
        if res:
            print("✅ Identity verified! , wELCOME BACK H-24 HOW IT'S GOING ? ")
            os.remove("captured_image.jpg")  # Clean up the captured image
            speak("Identity verified! , wELCOME BACK H-24 HOW IT'S GOING ? , do you want to start Nexa right now ? yes/no")
            user_response = input_with_timeout("Your response (yes/no): ", timeout=10)
            if user_response and user_response.lower() == "yes":
                python_executable = r"D:\Nexa\.venv\Scripts\python.exe" # past here your nexa python executable path
            script_path = r"D:\Nexa\main.py" # past here your nexa script path
            try:

                subprocess.Popen([python_executable, script_path])
                print("🚀 Nexa is starting...")
            except Exception as e:
                print(f"❌ Error starting Nexa: {e}")  
        elif res == False:
            print("❌ Identity verification failed. Access denied.")
            os.remove("captured_image.jpg")  # Clean up the captured image  
            speak("Identity verification failed. Access denied , you are not the owner of this system , please try with Access Key or contact the owner of this system")
            speak("Please enter the access key immediately or the system will be locked.")
            Userkey = input_with_timeout("Enter Access Key: ", timeout=10)  # User se access key input le rahe hain with a timeout
            if Userkey is None:
                print("⏰ No input received. Locking the system for security reasons.")
                speak("No input received. Hacker X mode activated! My owner is not here right now, but Hacker X will be watching you.")
                time.sleep(5)  # Wait for a few seconds before locking
                ctypes.windll.user32.LockWorkStation()  # Lock the workstation after failed attempts
                time.sleep(10)  # Wait for a few seconds before locking
                continue
            adminkey = os.getenv("ADMIN_KEY")# Get the admin key from environment variable
            isvalid = check_password_hash(adminkey,Userkey)
            if isvalid: 
                print("✅ Access Key verified!")
                speak("Access Key verified! , Wellcome Guest , you can use this system but please do not try to access the owner's data or files , have a nice day !")
            else:
                print("❌ Invalid Access Key. Access denied.")
                speak("Invalid Access Key. Access denied , system will be locked for security reasons")
                time.sleep(5)  # Wait for a few seconds before locking
                ctypes.windll.user32.LockWorkStation()  # Lock the workstation after failed attempts
        else:
            print(f"❌ Error: {res}")
            os.remove("captured_image.jpg")  # Clean up the captured image
        time.sleep(10)  # Wait for 1 hour before next verification

        
