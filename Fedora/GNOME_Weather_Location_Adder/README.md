# 🖥️ GNOME Weather Location Adder

This repository contains a bash script for manually adding locations to the GNOME Weather app, especially useful when the app's search does not return results for certain cities.

## ⚙️ Description

GNOME Weather might sometimes fail to find specific cities or locations. This script allows you to manually add locations to GNOME Weather using OpenStreetMap's Nominatim service for location search. The script supports both system installations and Flatpak installations of GNOME Weather.

## 📋 Prerequisites

- **GNOME Weather** installed on Fedora (either system or Flatpak).

- **curl** for making HTTP requests. Typically installed by default.

## 🚀 Usage
Clone the repository:
```bash
git clone https://github.com/patricnilackshan/gnome-weather-location-adder.git
cd gnome-weather-location-adder
```

Make the script executable:
```bash
chmod +x AddLocationToGnomeWeather.sh
```

Run the script and follow the prompts to input the location:
```bash
./AddLocationToGnomeWeather.sh
```

## 💡 Notes
Ensure GNOME Weather is closed before running the script to avoid conflicts.
If using Flatpak, ensure the flatpak command is available on your system.


## 🛠️ Script Details
The script performs the following steps:

**Check GNOME Weather Installation**: Detect if GNOME Weather is installed either as a system app or a Flatpak.

**Determine Locale**: Uses your system's locale settings for localization.

**Search for Location**: Uses OpenStreetMap’s Nominatim service to find the location details.

**Confirm Location**: Prompts for confirmation before adding the location.

**Add Location**: Updates GNOME Weather’s location settings with the new location.

<br>

### © PATRIC NILACKSHAN (pnilackshan@gmail.com)

<img align="right" src="https://visitor-badge.laobi.icu/badge?page_id=patricnilackshan.gnome-weather-location-adder" />
