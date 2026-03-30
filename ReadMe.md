# 🌿 **Serra Intelligente per Ipovedenti**

**Concorso "Cura per gli altri e per l'ambiente" - IEFP Informatica 2024**

[![ESP32-CAM Live](docs/demo.gif)](https://youtu.be/demo) [![Demo Audio](docs/web_app_screenshot.png)](https://serra-ipovedenti.web.app)

## 🔍 **Il Problema**

- **Ipovedenti**: non possono curare piante autonomamente.
- **Balcone**: luce variabile, annaffiatura difficile, maturazione pomodori invisibile.

## 🚀 **La Soluzione Completa**

ESP32-CAM → AI Colori → Firebase → Web App (Text-to-Speech) ↓ ESP32-DevKit → Sensori → 4x Relay ⚙️ (Automatico)

### 🛠️ **Componenti**

| Componente | Funzione | Costo |
| :--- | :--- | :--- |
| ESP32-CAM | Foto pomodori 1x/giorno | €8 |
| ESP32 DevKit | Sensori + 4 relay | €10 |
| DHT11, Fotores, Moisture | Controllo ambiente | €15 |
| **Totale** | **Serra completa** | **< €50** |

## 📺 **Demo Live**
1. **[Video 3min](docs/VIDEO_DEMO.mp4)**
2. **[Foto pomodori AI](pc-server/foto_pomodori/)**
3. **[Firebase Reports](https://console.firebase.google.com/project/serra-ipovedenti)**
4. **[Web App Demo](web-app/web_app.html)** ← **Apri sul telefono!**

## 🧠 **Intelligenza Artificiale (OpenCV HSV)**

🔴 Rosso > 60% → **MATURI** (raccogli!)  
🟡 30-60% → **MATURAZIONE** (aspetta)  
🟢 < 30% → **ACERBI** (crescono)

**Codice**: `analizza_pomodori.py` in `(pc-server/analizza_pomodori.py)`

## ⚙️ **Automazione Ambiente**

☀️ Luce < 800lux → LED coltivazione ON (8-20)  
💧 Umidità < 35% → Pompa 30s  
🌡️ T > 28°C → Ventola ❄️  
🔥 T < 12°C → Serpentina 20W

## 📱 **Web App Accessibile**

- ✅ **Text-to-Speech italiano**
- ✅ Caratteri grandi (1.5em)
- ✅ Alto contrasto WCAG
- ✅ Touch-friendly
- 👉 **[Provala!](web-app/web_app.html)**

## 🛠️ **Istruzioni Installazione**

### 1. **ESP32-CAM** (Foto + AI)
Arduino IDE → Copia `esp32-cam/main.ino` Strumenti → AI Thinker ESP32-CAM Upload → http://IP/stream

### 2. **ESP32 DevKit** (Sensori)
Libreria DHT Adafruit Copia `esp32-devkit/serra_devkit.ino` Upload → Serial Monitor

### 3. **PC Server** (AI + Firebase)

```bash
cd pc-server
pip install -r requirements.txt
cp ../firebase-adm.json .
python server_completo.py
