# StegoTool-Image-Steganography

📘 Project Documentation
Project Title: StegoTool – Image Steganography App
Version: 1.0
Author: Mauli Gaming 

1. 🔍 Project Overview
StegoTool is a modern, 3D-styled GUI-based application built using Python and PyQt5. It allows users to hide secret text messages inside image files using steganography techniques. The project supports bilingual UI (English + Marathi), dark/light themes, animations, sound effects, and more for an engaging user experience.

2. ⚙️ Technologies Used
Python 3.x
PyQt5 –GUI Design
Pillow (PIL) – Image Processing
base64 – Text Encoding/Decoding
QMovie – For GIF Animation
os, sys, io, datetime – Utility modules

3. 🧰 Features
Hide secret text inside an image
Decode hidden message from a stego image
GUI in English and Marathi
3D-style interface and buttons
Dark & Light theme toggle
Animated GIF integration
Sound effects on actions
Real-time logging panel
Error handling with pop-ups
Save/export stego image file

4. 📁 Folder Structure
css
Copy code
StegoTool/
├── main.py
├── stego_utils.py
├── resources/
│   ├── icons/
│   ├── sounds/
│   ├── gifs/
│   └── style.qss
├── output/
├── README.md
└── requirements.txt

6. 🚀 How to Run the App
 bash
  Copy code:
            pip install -r requirements.txt
            python main.py

8. 📖 Step-by-Step Usage
To Hide Text into Image:
Open the application.
Click on “Choose Image” and select any .png or .jpg image.
Enter the secret message in the “Text Box”.
Click “Hide Message”.
Save the image by clicking “Save Stego Image”.
Confirmation and log message will appear.
To Decode Hidden Text:
Click on “Open Stego Image”.
Select the image with hidden data.
Click “Decode Message”.
The hidden message will be shown in the text area.

7. 🌟 Advantages (Pros)
✅ User-friendly interface with modern design
✅ Supports both Marathi and English
✅ Secure way to hide messages in images
✅ Portable and lightweight
✅ Dark/light theme customization
✅ No internet required – works offline
✅ Includes sounds, logs, and error messages for better feedback

8. ⚠️ Limitations (Cons)
❌ Can only hide plain text (no audio/video support yet)
❌ Limited to PNG and JPG images
❌ No encryption – message is visible after extraction
❌ Not suitable for high-security environments
❌ GIF animations are only decorative, not functional

9. 🧩 Future Scope
Add support to hide audio, video, or PDF inside media
Encrypt data before embedding
Add drag & drop functionality
Introduce password protection
Web-based version using Flask or Django

10. ✅ Conclusion
StegoTool is an excellent beginner-friendly tool for understanding image steganography. With a rich GUI experience and interactive features, it makes the concept fun and practical. It’s great for students, ethical hacking learners, and cybersecurity enthusiasts.
