# Alexa Virtual Assistant

A voice-controlled Windows assistant. Say **"Alexa"** to wake it, then speak commands to open apps, read the news, search Google/YouTube, find local files, or chat with AI.

## What it does

- Wake word: **"Alexa"** — say **"stop"** to exit
- Open apps: WhatsApp, DeepSeek, Google, Brave, Calculator, Clock, YouTube
- Read the news aloud (NewsAPI)
- Google & YouTube search by voice
- Find files across D:/E:/F: drives
- AI chat via Groq (Llama 3.3 70B)
- Power controls: screen off, sleep, lock, restart, shutdown

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/alexa-virtual-assistant.git
cd alexa-virtual-assistant

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

If `PyAudio` fails to install (common on Windows):

```bash
pip install pipwin
pipwin install pyaudio
```

**Add your API keys** — copy `api_example.py` → `api.py`, then paste keys from:
- [Groq](https://console.groq.com/keys)
- [NewsAPI](https://newsapi.org/register)

## Usage

```bash
python main.py
```

Say **"Alexa"** to activate, then speak a command:

```
open whatsapp
tell me the news
search in google for python tutorials
search in youtube for lo-fi beats
search in my files for resume
ask ai what is quantum computing
laptop shutdown
```

## Notes

- **Windows only** — relies on `ctypes.windll`, `os.startfile`, and Windows `shutdown`
- Power commands have a **10-second delay** before executing
- File search covers **D:/E:/F:** by default — edit the `disks` list in `file_search.py` to change
- Brave path in `system_control.py` is hardcoded to a Desktop shortcut — edit if needed

## License

MIT — see [LICENSE](LICENSE).