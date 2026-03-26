📦 Installation
1. Clone the Repository
git clone https://github.com/your-username/speech_to_command.git
cd speech_to_command
2. Install Dependencies
pip install pyttsx3
pip install SpeechRecognition
pip install wikipedia
pip install pyaudio

⚠️ Note: Installing pyaudio may require additional setup:

For Windows: Download wheel from Christoph Gohlke’s site
Then install using:
pip install path_to_whl_file
▶️ How to Run
python your_script_name.py
🧪 Usage
Run the program
Speak a command like:
"Albert Einstein wikipedia"
The assistant will:
Recognize your voice
Search Wikipedia
Speak out the result
📁 Project Structure
speech_to_command/
│── main.py
│── README.md
⚙️ Code Overview
speak(text) → Converts text to speech
takeCommand() → Listens and converts speech to text
Main loop → Detects keyword "wikipedia" and processes query
❗ Error Handling
Handles:
Unknown speech (UnknownValueError)
API issues (RequestError)
Returns fallback message if recognition fails
💡 Future Improvements
Add more commands (weather, time, apps)
GUI interface
Wake word detection (e.g., "Hey Assistant")
Multi-language support
🤝 Contributing

Pull requests are welcome! Feel free to improve features or fix bugs.

📜 License

This project is open-source and free to use.
