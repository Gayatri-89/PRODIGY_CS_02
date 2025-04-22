# PRODIGY_CS_02
Image Encryption Tool using Python (Pixel Inversion)
# PRODIGY_CS_2 - Image Encryption Tool 🔐🖼️

This is my **second task** as part of the **Cybersecurity Internship** at **Prodigy InfoTech**.

## 📌 Task Description:
Develop an image encryption and decryption tool using **Python** by manipulating pixel values. This script applies a simple pixel inversion method where each RGB component is inverted to encrypt and decrypt the image.

## 🛠️ Features:
- Image encryption using pixel inversion
- Decryption by reapplying the same process
- Handles transparency (RGBA)
- Built using Python and PIL (Pillow)

## 📷 How It Works:
- Encryption: `RGB = (255 - R, 255 - G, 255 - B)`
- Decryption: The same inversion logic restores the original

## 🚀 How to Run:
1. Install Pillow:  
   ```bash
   pip install Pillow
