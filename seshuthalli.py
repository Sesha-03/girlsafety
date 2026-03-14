import speech_recognition as sr
import pywhatkit as kit
import requests
import time
import threading

# -------- GET LOCATION --------
def get_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()

        loc = data['loc'].split(',')
        lat = loc[0]
        lng = loc[1]

        return f"https://www.google.com/maps?q={lat},{lng}"

    except:
        return "Location unavailable"


# -------- SEND WHATSAPP ALERT --------
def send_whatsapp_alert():

    location = get_location()

    message = f"""
🚨 EMERGENCY ALERT 🚨
I need help!

My location:
{location}
"""

    phone_numbers = [
        "+917989475906",
        "+916304071753"
    ]

    for phone in phone_numbers:

        print(f"Sending alert to {phone}...")

        kit.sendwhatmsg_instantly(
            phone,
            message,
            wait_time=10,
            tab_close=True
        )

    print("Alert sent successfully!")


# -------- CONFIRMATION WITH TIMER --------
def confirm_alert():

    cancel_alert = {"value": False}

    def wait_for_input():
        choice = input("Emergency detected! Press N within 60 seconds to cancel: ")

        if choice.lower() == "n":
            cancel_alert["value"] = True
            print("Alert cancelled.")

    thread = threading.Thread(target=wait_for_input)
    thread.start()

    print("Waiting 60 seconds for cancellation...")

    time.sleep(60)

    if not cancel_alert["value"]:
        print("No cancellation detected. Sending alert...")
        send_whatsapp_alert()


# -------- LISTEN FOR HELP --------
def listen_for_help():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        recognizer.adjust_for_ambient_noise(source)

        print("Listening for 'help me'...")

        while True:

            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)

                print("You said:", text)

                if "help me" in text.lower():
                    confirm_alert()

            except sr.UnknownValueError:
                pass

            except sr.RequestError:
                print("Speech service error")


# -------- START --------
listen_for_help()