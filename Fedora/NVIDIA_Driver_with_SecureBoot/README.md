# 🖥️ Fedora + NVIDIA + Secure Boot Fix 🚀

Step-by-step guide to installing and signing NVIDIA drivers on Fedora with Secure Boot enabled.

---

## 🎯 Requirements

- Fedora OS (Secure Boot enabled)
- NVIDIA GPU

---

## 📋 Preconditions

1. Ensure Secure Boot is **ON** in BIOS setup mode.
2. Remove older NVIDIA installations.
3. Optionally disable 'quiet' boot for easier debugging:
    ```bash
    sudo grubby --update-kernel=ALL --remove-args='quiet'
    ```

---

## 🚀 Steps to Fix

1. **Check your graphics adapter**:
    ```bash
    lspci | grep -E "VGA|3D"
    ```

2. **Verify Secure Boot state**:
    ```bash
    mokutil --sb-state
    ```

3. **Update system**:
    ```bash
    sudo dnf update -y && sudo dnf upgrade -y
    ```

4. **Install required tools**:
    ```bash
    sudo dnf install -y kmodtool akmods mokutil openssl
    ```

5. **Generate and import certificates**:
    ```bash
    sudo kmodgenca -a
    sudo mokutil --import /etc/pki/akmods/certs/public_key.der
    ```
    👉 Note: Enter a password when prompted. This password will be used in the next step.

6. **Reboot to enroll certificate**:
    Reboot the system to enroll the certificate:
    ```bash
    systemctl reboot
    ```
    During boot, MOK Manager will ask if you want to enroll the key. Choose "Enroll MOK" -> "Continue" and enter the password created in Step 5.
    <img src="https://raw.githubusercontent.com/patricnilackshan/linux/refs/heads/main/Fedora/NVIDIA_Driver_with_SecureBoot/images/mok_management.png" width="800">

7. **Install NVIDIA drivers**:
    ```bash
    sudo dnf install -y akmod-nvidia xorg-x11-drv-nvidia-cuda
    ```

8. **Reboot again**:
    ```bash
    systemctl reboot
    ```

---

## 🎉 Congratulations! NVIDIA drivers should now work with Secure Boot enabled.
