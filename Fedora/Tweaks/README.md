# Fedora Tweaks 🚀💻

This repository contains useful tweaks and tricks for optimizing your Fedora experience.

<br>

## Speed Up DNF Downloads ⚡

```bash
sudo nano /etc/dnf/dnf.conf
```

Paste the following content at the end of the file:
```text
max_parallel_downloads=10
fastestmirror=True
```
Save and close the file.

This configuration allows for parallel downloads and selects the fastest mirror for quicker package retrieval.

<br>

## Clean system logs ♻️
To clean system logs:
```bash
sudo journalctl --rotate
sudo journalctl --vacuum-time=1s
```

<br>

## Clean Old Kernels ♻️
To clean old kernels:
```bash
sudo dnf -y install --setopt installonly_limit=1 kernel
```

<br>


## Wine Bottles 🍷

### To install Bottles
```bash
sudo dnf -y install bottles
```

### To install supporting libraries
```bash
sudo dnf -y install mesa-dri-drivers mesa-vulkan-drivers
sudo dnf -y install wine.i686
sudo dnf -y install libgnutls.i686
sudo dnf -y install mesa-libGL.i686
sudo dnf -y install mesa-dri-drivers
sudo dnf -y install libgnutls.i686
sudo dnf -y install freetype freetype-devel
```

<br>

## Fix VLC Codecs 🎵

### To install VLC with required codecs:
```bash
sudo dnf -y install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm && sudo dnf -y install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm && sudo dnf -y install vlc
```

### To fix codecs error:
```bash
sudo dnf -y swap ffmpeg-free ffmpeg --allowerasing 
```

### Audio Issue Workaround (for 2x Playback)

If you experience audio issues when playing media at 2x speed, you can try the following workaround:

1. Open VLC Preferences:
	* Go to `Tools` > `Preferences`.
	* At the bottom left, set `Show Settings` to `All`.
	* Under `Audio`, select `Output Modules`.
2. Change Audio Output:
	* Change the Audio Output to Pulseaudio audio output.

<br>

## Enable Fractional Scaling 📏
To enable fractional scaling:
```bash
gsettings set org.gnome.mutter experimental-features "['scale-monitor-framebuffer']"
```

To disable fractional scaling:
```bash
gsettings set org.gnome.mutter experimental-features "[]"
```

To reset fractional scaling:
```bash
gsettings reset org.gnome.mutter experimental-features
```

<br>

## Increase Volume Beyond 100% 🔊
To allow volume above 100%, run:
```bash
gsettings set org.gnome.desktop.sound allow-volume-above-100-percent 'true'
```

<br>

## Remove Unwanted Bloatware ❌
To remove some pre-installed software, use:
```bash
sudo dnf -y erase yelp
sudo dnf -y erase totem
sudo dnf -y erase rhythmbox
sudo dnf -y erase gnome-tour
sudo dnf -y erase gnome-maps
sudo dnf -y erase gnome-boxes
sudo dnf -y erase mediawriter
sudo dnf -y erase simple-scan
```

<br>

## GNOME Extensions ✨
**App Indicator Support**  
Enable support for app indicators: [App Indicator](https://extensions.gnome.org/extension/615/appindicator-support)

**Desktop Icons**  
Enable desktop icons using the following extension: [Desktop Icons NG (DING)](https://extensions.gnome.org/extension/2087/desktop-icons-ng-ding)

**Clipboard History**  
Add clipboard history support: [Clipboard History](https://extensions.gnome.org/extension/4839/clipboard-history)

**Click to Close Overview**  
Enable clicking to close the overview: [Click to Close Overview](https://extensions.gnome.org/extension/3826/click-to-close-overview)

**Dash to Dock**  
Enable a dock-like application launcher: [Dash to Dock](https://extensions.gnome.org/extension/307/dash-to-dock)

**Show Desktop Button**  
Add a button to show the desktop: [Show Desktop Button](https://extensions.gnome.org/extension/1194/show-desktop-button)

<br>

# Install OBS 🖥️
To install Intel QSV Decoder for OBS:
```bash
sudo dnf -y install intel-media-driver
```

To install OBS:
```bash
sudo dnf -y install obs-studio
```

<br>

# Install Brave 🦁

```bash
curl -fsS https://dl.brave.com/install.sh | sh
```

<br>

# Install Programming Languages & Development Tools 🛠️

## Install Java JDK ☕
```bash
sudo dnf -y install java-latest-openjdk-devel.x86_64
```

To change Java Alternative:
```bash
sudo alternatives --config java
```

## Install NodeJS 🟢
```bash
sudo dnf -y install nodejs
```

## Install C++ Development Tools 🛠️
```bash
sudo dnf install @development-tools 
sudo dnf -y install cmake
```

## Install MongoDB 🍃
To install MongoDB on Fedora and resolve potential OpenSSL issues, follow these steps:

### Step 1: Remove Existing MongoDB Installations ❌  
If you've previously installed MongoDB, remove any existing packages or repositories to avoid conflicts:

```bash
sudo systemctl stop mongod
sudo dnf erase $(rpm -qa | grep mongo)
sudo rpm -e mongodb-org mongodb-mongosh
sudo rm -rf /var/log/mongodb /var/lib/mongo
sudo rm -f /etc/yum.repos.d/mongodb-org-*.repo
```

### Step 2: Add MongoDB 8.0 Repository 📦  
Create a repository file for MongoDB 8.0:

```bash
sudo nano /etc/yum.repos.d/mongodb-org-8.0.repo
```

Paste the following content into the file:
```text
[mongodb-org-8.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/9/mongodb-org/8.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://pgp.mongodb.com/server-8.0.asc
```
Save and close the file.

### Step 3: Install MongoDB with OpenSSL 3 Support 🔐
To install MongoDB with the correct OpenSSL 3 support, use the following command:

```bash
sudo dnf -y install mongodb-org mongodb-mongosh-shared-openssl3
```

### Step 4: Start MongoDB Service 🚀
After installation, start the MongoDB service:

```bash
sudo systemctl start mongod
```

### Step 5: Verify Installation ✅
Check if MongoDB is running properly:

```bash
sudo systemctl status mongod
```
This should resolve any OpenSSL-related issues and allow MongoDB to function smoothly on Fedora.
