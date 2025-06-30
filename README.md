# AgriBot Rover – Hack the Hills 2025 🌽🚜

Autonomous all-terrain robot designed to transport agricultural waste (like corn stalks and husks) from hillside farms to roadside collection points. Developed as a submission for the **AgriSpark Hackathon 2025 – "Hack the Hills"**, this project aims to reduce labor, time, and risk for farmers working in mountainous areas.

---

## 📌 Problem Statement

Farmers in hilly regions face difficulties transporting post-harvest corn waste from the fields down to roads where trucks can access. It’s labor-intensive, time-consuming, and dangerous – especially during the rainy season.

---

## 💡 Our Solution: AgriBot Rover

An autonomous wheeled robot designed to:
- Traverse uneven, sloped terrain
- Carry 10–15 kg of agricultural waste per trip
- Automatically return to base for the next load
- Use GPS, IMU, and obstacle sensors for navigation
- Be monitored and controlled via a simple web dashboard

---

## 🔧 System Components

- **Microcontroller:** ESP32 or Raspberry Pi
- **Locomotion:** 4WD DC gear motors + off-road wheels
- **Sensors:** Ultrasonic, IMU, GPS
- **Power Supply:** LiPo battery or solar hybrid
- **Communication:** Wi-Fi or LoRa (optional)
- **Software:** Python + Web dashboard (Flask/Streamlit)

---

## 📽️ Demo Video

👉 [Link to video here]()

---

## 📊 Impact

| Metric | Before (manual) | After (AgriBot) |
|--------|------------------|------------------|
| Time per trip | ~40 mins | ~10 mins |
| Labor required | 2–3 people | 0 (autonomous) |
| Safety | Medium risk | Low risk |
| Energy usage | Human | Renewable battery |

---

## 🚀 Getting Started (Prototype Simulation)

```bash
git clone https://github.com/your-username/agribot-rover-hackthehills2025.git
cd agribot-rover
