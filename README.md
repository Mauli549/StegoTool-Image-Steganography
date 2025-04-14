# StegoTool: Image Steganography App

📄 Project Documentation
Project Title: StegoTool – Image Steganography Application
Version: 1.0
Author: Mauli Gaming Takshil

🔎 1. Introduction
StegoTool is a powerful and visually engaging steganography tool that enables users to hide and retrieve secret messages within image files. Designed using Python and PyQt5, it blends modern UI features with core information security principles. The application is user-friendly, bilingual (English and Marathi), and equipped with animations, sound effects, themes, and error handling – making it an excellent educational and practical tool.

💡 2. Objective
The primary objective of this project is to provide a secure and simple method to hide textual data inside images, using steganography, and demonstrate how digital files can carry hidden information without visibly altering the media.

🛠️ 3. Tools & Technologies Used
Component	Description
Python 3	Core programming language
PyQt5	GUI development framework
Pillow (PIL)	Image processing library
base64	For encoding and decoding text data
QMovie	GIF animation handler
os, sys, io	File and system utilities
🎨 4. Key Features
🔐 Text Encoding in Image

🔓 Text Decoding from Image

🌐 Bilingual UI (English + Marathi)

💠 3D-style modern interface

🌗 Light/Dark Theme Switch

🎞️ GIF Animation Integration

🔊 Sound Feedback on Actions

📜 Live Logging Panel

⚠️ Pop-up Error Handling

💾 Save/Export Stego Images

📁 5. Project Structure
bash
Copy code
StegoTool/
│
├── main.py                # Main application logic
├── stego_utils.py         # Encoding and decoding logic
├── resources/             # Assets folder
│   ├── icons/             # Button icons
│   ├── gifs/              # Animation files
│   ├── sounds/            # Sound effects
│   └── style.qss          # Theme stylesheet
├── output/                # Generated stego images
├── requirements.txt       # Required Python libraries
└── README.md              # Project information

![image alt]()
📌 6. Installation & Execution
🧾 Requirements:
bash
  Copy code:
               pip install -r requirements.txt
▶️ To Run:
        bash
            Copy code :
                python main.py

📘 7. How to Use
➕ To Hide a Message:
Launch the application.

Click on “Choose Image” and select an image.

Type your secret message.

Click “Hide Message”.

Save the new stego image.

➖ To Reveal a Hidden Message:
Click on “Open Stego Image”.

Select an image with hidden text.

Click “Decode Message”.

The hidden text will appear in the textbox.

✅ 8. Advantages
Simple, beginner-friendly interface

Secure way to embed text in images

Works offline, no internet needed

Stylish GUI with themes and animations

Dual-language support enhances accessibility

Saves stego image for later decoding

❌ 9. Limitations
Only supports hiding plain text
Does not support audio, video, or file embedding
Hidden message can be extracted by anyone (no encryption)
PNG/JPG only – limited format compatibility
Not suitable for high-level secure communications

🔮 10. Future Enhancements
Add support for hiding audio, video, or file attachments
Implement encryption + password protection
Add drag and drop image support
Build a web version using Flask or Django
Cloud-based stego-image storage & sharing

📌 11. Conclusion
StegoTool is a visually rich, educational, and practical tool that simplifies the process of learning and using image-based steganography. With support for bilingual UI, interactive design, and core functionality, it stands as a strong base for further development in the field of cybersecurity and digital communication.

