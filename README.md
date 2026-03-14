# Voice-Activated Emergency Alert System 🚨

## Overview

The **Voice-Activated Emergency Alert System** is a Python-based safety application that listens for a distress phrase such as **"help me"** and automatically sends emergency alerts to predefined contacts through **WhatsApp**.

When the phrase is detected, the system starts a **60-second confirmation timer**. If the alert is not cancelled during that time, it sends a message with the user's **current location link**.

This project demonstrates the integration of **speech recognition, APIs, and automation** to build a simple personal safety tool.

---

## Features

* 🎤 **Voice Detection** – Continuously listens for the phrase **"help me"**
* ⏱ **Safety Timer** – Allows cancellation within 60 seconds to prevent false alerts
* 📍 **Automatic Location Sharing** – Sends a Google Maps location link
* 💬 **WhatsApp Emergency Alert** – Notifies emergency contacts instantly
* ⚡ **Real-time Monitoring** – Runs continuously until stopped

---

## Technologies Used

* Python
* SpeechRecognition
* PyAudio
* PyWhatKit
* Requests API
* Threading

---

## How It Works

1. The program continuously listens through the microphone.
2. When the phrase **"help me"** is detected:

   * A 60-second countdown begins.
3. The user can cancel the alert by pressing **N** during this time.
4. If not cancelled:

   * The system retrieves the user's approximate location using an IP-based API.
   * A **Google Maps link** is generated.
5. The program sends a **WhatsApp alert message** with the location to emergency contacts.

---

## Installation

### 1. Install Python

Download Python from:
https://www.python.org/downloads/

---

### 2. Install Required Libraries

Run the following commands in terminal:

```
pip install SpeechRecognition
pip install pywhatkit
pip install requests
pip install pyaudio
```

For Windows (if PyAudio fails):

```
pip install pipwin
pipwin install pyaudio
```

---

### 3. Login to WhatsApp Web

Open:

https://web.whatsapp.com

Scan the QR code and keep the browser logged in.

---

## Usage

Run the program:

```
python seshuthalli.py
```

The system will display:

```
Listening for 'help me'...
```

If the phrase **"help me"** is detected:

* The emergency confirmation process starts.

To stop the program:

```
Ctrl + C
```

---

## Example Alert Message

```
🚨 EMERGENCY ALERT 🚨
I need help!

My location:
https://www.google.com/maps?q=latitude,longitude
```

---

## Future Improvements

* Mobile app integration
* GPS-based location instead of IP location
* SMS and phone call alerts
* Panic button support
* Multiple emergency phrases

---

## Author

**Sesha Katnam**

Computer Science student interested in building real-world problem solving applications using software and automation.

---

## License

This project is open source and available for learning and educational purposes.
