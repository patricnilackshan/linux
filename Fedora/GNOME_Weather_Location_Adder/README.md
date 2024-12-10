# 🌦️ GNOME Weather Location Adder

Manually add locations to the GNOME Weather app when the app's search does not return results for specific cities.

---

## ⚙️ Description

This script uses OpenStreetMap's Nominatim service to find and add custom locations to GNOME Weather. Supports both system installations and Flatpak installations.

---

## 📋 Requirements

- **GNOME Weather** installed on Fedora (system or Flatpak).
- **curl** (typically pre-installed).

---

## 🚀 Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/patricnilackshan/linux.git
    cd Fedora/GNOME_Weather_Location_Adder
    ```

2. **Make the script executable**:
    ```bash
    chmod +x AddLocationToGnomeWeather.sh
    ```

3. **Run the script and follow the prompts**:
    ```bash
    ./AddLocationToGnomeWeather.sh
    ```

---

## 💡 Notes

- Ensure GNOME Weather is closed before running the script to avoid conflicts.
- For Flatpak installations, ensure the `flatpak` command is available.
