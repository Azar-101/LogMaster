# KeyCapture

**KeyCapture** is a basic Python tool that records and logs keystrokes. It uses the `pynput` library to capture each key pressed and saves the data to a log file. The tool is intended for educational purposes only, and it is crucial to obtain explicit user consent and follow ethical guidelines when using or implementing keyloggers.

## Features
- Records all key presses, including special keys (Shift, Ctrl, etc.).
- Saves the logged keystrokes to a text file (`keylog.txt`).
- Stops logging when the **Escape** key is pressed.

## Requirements
- Python 3.x
- `pynput` library

### Installation:
1. Install the required library:
   ```bash
   pip install pynput
   ```
###Run the Python script:

```bash

python keylogger.py
```
The keystrokes will be saved to a file named keylog.txt in the same directory.

###Ethical Considerations
Keyloggers can be highly invasive and unethical if used without explicit permission. Always ensure you have obtained proper consent before using or sharing this tool. This project is for educational purposes only.

###License
This project is open-source and available under the MIT License.

