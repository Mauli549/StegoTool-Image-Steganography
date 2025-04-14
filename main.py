import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QFileDialog, QTextEdit, QHBoxLayout, QComboBox, QCheckBox,QVBoxLayout,QHBoxLayout,QGridLayout
)
from PyQt5.QtGui import QPixmap, QMovie, QFont
from PyQt5.QtMultimedia import QSound
from PyQt5.QtCore import Qt
from stego_utils import encode_message, decode_message

class StegoTool(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StegoTool Image Steganography App")
        self.setGeometry(100, 100, 800, 500)
        self.setStyleSheet("background-color: #1e1e2f; color: white; font-size: 14px;")

        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout()

        grid_layout = QGridLayout()  # Inside main layout
        main_layout.addLayout(grid_layout)

        self.setLayout(main_layout)  # Set main layout as central layout

        # layout initialization (make sure this is present)
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # Animation (GIF) - Improved Size and Position
        self.gif_label = QLabel()
        self.gif_label.setFixedSize(1500, 300)
        self.gif_label.setAlignment(Qt.AlignCenter)

        self.movie = QMovie("resources/animation/hacker.gif")
        self.movie.setScaledSize(self.gif_label.size())
        self.gif_label.setMovie(self.movie)
        self.movie.start()

        # Animation layout (to align at bottom-right properly)
        animation_layout = QHBoxLayout()
        animation_layout.addStretch()
        animation_layout.addWidget(self.gif_label)

        # Add animation layout to grid layout
        self.layout.addLayout(animation_layout, 4, 0, 1, 3)

        # Image Preview
        self.image_label = QLabel("\n\nImage Preview")
        self.image_label.setFixedSize(300, 200)
        self.image_label.setStyleSheet("border: 2px solid gray;")
        self.image_label.setAlignment(Qt.AlignCenter)

        # Secret Message Box
        self.message_box = QTextEdit()
        self.message_box.setPlaceholderText("Enter secret message here...")
        self.message_box.setStyleSheet("background-color: #2e2e3f; color: white;")

        # Log Box
        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)
        self.log_box.setStyleSheet("background-color: black; color: lime;")

        # Language ComboBox
        self.lang_box = QComboBox()
        self.lang_box.addItems(["English", "Marathi"])

        # Theme Toggle
        self.theme_toggle = QCheckBox("Dark / Light Theme")

        # Buttons
        load_button = QPushButton("Load Image")
        load_button.clicked.connect(self.load_image)

        encode_button = QPushButton("Encode")
        encode_button.clicked.connect(self.encode)

        decode_button = QPushButton("Decode")
        decode_button.clicked.connect(self.decode)

        # Button Sound
        self.sound = QSound("resources/sounds/click.wav")

        # Layouts
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.image_label)
        top_layout.addWidget(self.message_box)

        button_layout = QHBoxLayout()
        button_layout.addWidget(load_button)
        button_layout.addWidget(encode_button)
        button_layout.addWidget(decode_button)

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.lang_box)
        bottom_layout.addWidget(self.theme_toggle)
        bottom_layout.addStretch()
        bottom_layout.addWidget(self.gif_label)

        main_layout.addLayout(top_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.log_box)
        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)

    def load_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp)")
        if file_name:
            pixmap = QPixmap(file_name).scaled(self.image_label.size(), Qt.KeepAspectRatio)
            self.image_label.setPixmap(pixmap)
            self.image_path = file_name
            self.log("[LOG] Image loaded successfully")
            self.sound.play()

    def encode(self):
        try:
            message = self.message_box.toPlainText()
            if not hasattr(self, 'image_path'):
                self.log("[ERROR] No image loaded!")
                return
            if not message.strip():
                self.log("[ERROR] No message entered!")
                return
            output_path = "resources/images/encoded_output.png"
            encode_message(self.image_path, message, output_path)
            self.log("[LOG] Message encoded and image saved at: " + output_path)
            self.sound.play()
        except Exception as e:
            self.log(f"[ERROR] Encoding failed: {e}")

    def decode(self):
        try:
            if not hasattr(self, 'image_path'):
                self.log("[ERROR] No image loaded!")
                return
            message = decode_message(self.image_path)
            self.message_box.setPlainText(message)
            self.log("[LOG] Message decoded")
            self.sound.play()
        except Exception as e:
            self.log(f"[ERROR] Decoding failed: {e}")

    def log(self, msg):
        self.log_box.append(msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StegoTool()
    window.show()
    sys.exit(app.exec_())
