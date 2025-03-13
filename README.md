 # Cross-Platform Message & Media Bot 🤖  
**Telegram + Discord Integration**  

---

## 🌟 Features  
### Telegram Bot (`tgbot.py`)  
- `/pol` + code: Retrieve saved messages  
- `/otv`: Save messages with auto-generated codes  
- `/cat`: Send random cat images  
- `/dog`: Send random dog images  

### Discord Bot (`dsbot.py`)  
- `/pol`: Get the latest saved message  
- `/otv`: Save messages with codes  
- `/cat` & `/sobak`: Send cat/dog images  
- Error handling for invalid commands  

---

## ⚙️ Configuration  
1. **Telegram Bot**:  
   - Replace `TOKENTG` in `tgbot.py` with your bot token.  

2. **Discord Bot**:  
   - Add your Discord bot token to `TOKENDISCORD` in `dsbot.py`  
   - Enable **all intents** in the [Discord Developer Portal](https://discord.com/developers/applications)  

---

## 🚀 Usage  
1. Install dependencies:  
   ```bash
   pip install telebot discord.py requests pillow
Run the bots:
python tgbot.py  # Start Telegram bot
python dsbot.py   # Start Discord bot

---

## ⚠️ Notes
file.txt is auto-created for message storage

Image folders (papka_s_kotikami, etc.) are generated automatically

EXE files may trigger antivirus false positives
