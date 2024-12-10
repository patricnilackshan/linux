# 📋➡️📱 Clip to QR 

Clip2QR is a simple Python script that converts text from your clipboard into a QR code, making it easy to transfer text from your computer to your phone.

---

## 🎯 Requirements

- `Python 3.x`
- `qrcode`
- `pyperclip`

---

## 🚀 Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/patricnilackshan/linux.git
    cd Fedora/Clip_2_QR
    ```

2. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Make the script executable**:
    ```bash
    chmod +x clip2qr.py
    ```

4. **Add an alias to your `~/.bashrc` for easier access**:

    - Open the file with:
    ```bash
    nano ~/.bashrc
    ```

    - Add this line at the end of the file:
    ```bash
    alias clip2qr='/path/to/bin/python /path/to/clip2qr.py'
    ```
    *(Replace `/path/to/bin/python` and `/path/to/clip2qr.py` with actual paths)*

    - Save and close the file.
    - Apply the changes:
    ```bash
    source ~/.bashrc
    ```

---

## 🖥️ Usage

1. Copy any text to your clipboard.
2. Open a terminal and type `clip2qr`.
3. A window will appear displaying the generated QR code.

