# 🖥️ Fedora + NVIDIA + Secure Boot Fix 🚀

This guide provides a step-by-step approach for installing and signing the NVIDIA driver on Fedora systems with Secure Boot enabled. 

## ⚙️ Requirements

- Fedora OS (with Secure Boot enabled)
- Compatible NVIDIA GPU

---

## 📋 Preconditions

1. This method is tested for **Fedora 39/40** and **latest NVIDIA drivers**.
2. Secure Boot must be **ON** in setup mode in BIOS.
3. Remove all older NVIDIA installations.
4. Optionally, disable 'quiet' boot for easier debugging:
    ```bash
    sudo grubby --update-kernel=ALL --remove-args='quiet'
    ```

## 🚀 Steps to Fix

### 1. **Check Your Graphics Adapter**

Ensure your system detects the NVIDIA graphics adapter:
```bash
lspci | grep -E "VGA|3D"
```

### 2. Check Secure Boot State
Verify if Secure Boot is enabled:
```bash
mokutil --sb-state
```

### 3. Update Your System
Update your packages and system:
```bash
sudo dnf update -y
sudo dnf upgrade -y
```

### 4. Install Required Packages
Install the necessary tools for signing the NVIDIA driver kernel modules:
```bash
sudo dnf install -y kmodtool akmods mokutil openssl
```

### 5. Generate and Import Kernel Signing Certificates
Generate the certificate required to sign kernel modules:
```bash
sudo kmodgenca -a
```

Import the key and set a password for it:
```bash
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```
Note: Enter a password when prompted. This password will be used in the next step.

### 6. Reboot to Enroll the Certificate
Reboot the system to enroll the certificate:
```bash
systemctl reboot
```
During boot, MOK Manager will ask if you want to enroll the key. Choose "Enroll MOK" -> "Continue" and enter the password created in step 5.
<img src="https://raw.githubusercontent.com/patricnilackshan/fedora-nvidia-secure-boot-fix/refs/heads/main/images/mok_management.png" width="800">


### 7. Install NVIDIA Drivers
Once the system reboots, install the NVIDIA drivers and CUDA support:
```bash
sudo dnf install -y akmod-nvidia
sudo dnf install -y xorg-x11-drv-nvidia-cuda
```

### 8. Reboot Again
Reboot the system to finalize the driver installation:
```bash
systemctl reboot
```
<br>

### © PATRIC NILACKSHAN (pnilackshan@gmail.com)

<img align="right" src="https://visitor-badge.laobi.icu/badge?page_id=patricnilackshan.fedora-nvidia-secure-boot-fix" />
