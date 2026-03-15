# Samsul Rizal
# F1D02310025
# kelas D 

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QLineEdit, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PySide6.QtCore import Qt

class KonversiSuhuApp(QWidget):

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):

        self.setWindowTitle("Konversi Suhu")
        self.setFixedSize(400, 380)

        layout = QVBoxLayout()
        layout.setSpacing(15)

        # Judul
        judul = QLabel("KONVERSI SUHU")
        judul.setAlignment(Qt.AlignmentFlag.AlignCenter)
        judul.setStyleSheet(
            "font-size: 16px; font-weight: bold; padding: 12px; "
            "background: #3498db; color: white; border-radius: 5px;"
        )

        lbl_input = QLabel("Masukkan Suhu (Celsius):")
        lbl_input.setStyleSheet("font-size: 13px;")

        self.input_suhu = QLineEdit()
        self.input_suhu.setPlaceholderText("Contoh: 100")
        self.input_suhu.setStyleSheet(
            "padding: 10px; font-size: 14px; border: 1px solid #27ae60; "
            "background: #eafaf1; border-radius: 4px;"
        )

        btn_layout = QHBoxLayout()

        self.btn_fahrenheit = QPushButton("Fahrenheit")
        self.btn_kelvin = QPushButton("Kelvin")
        self.btn_reamur = QPushButton("Reamur")

        btn_style = "padding: 10px; font-weight: bold; background: #3498db; color: white; border: none; border-radius: 5px;"

        for btn in [self.btn_fahrenheit, self.btn_kelvin, self.btn_reamur]:
            btn.setStyleSheet(btn_style)
            btn_layout.addWidget(btn)

        self.btn_fahrenheit.clicked.connect(self.hitung_fahrenheit)
        self.btn_kelvin.clicked.connect(self.hitung_kelvin)
        self.btn_reamur.clicked.connect(self.hitung_reamur)

        self.label_hasil = QLabel("<b>Hasil Konversi:</b><br><br>-")
        self.label_hasil.setTextFormat(Qt.TextFormat.RichText)
        self.label_hasil.setStyleSheet(
            "padding: 15px; background: #d6eaf8; color: #154360; border-radius: 5px; font-size: 13px;"
        )

        layout.addWidget(judul)
        layout.addWidget(lbl_input)
        layout.addWidget(self.input_suhu)
        layout.addLayout(btn_layout)
        layout.addWidget(self.label_hasil)
        layout.addStretch()

        self.setLayout(layout)

    def get_celsius(self):
        teks = self.input_suhu.text().strip()
        
        if not teks:
            QMessageBox.warning(self, "Error", "Input suhu tidak boleh kosong!")
            return None
            
        try:
            celsius = float(teks)
            return celsius
        except ValueError:
            QMessageBox.warning(self, "Error", "Input harus berupa angka!")
            return None

    def tampil_hasil(self, hasil_teks):
        self.label_hasil.setText(f"<b>Hasil Konversi:</b><br><br>{hasil_teks}")

    def hitung_fahrenheit(self):
        celsius = self.get_celsius()
        if celsius is not None:
            fahrenheit = (celsius * 9/5) + 32
            self.tampil_hasil(f"{celsius:g} Celsius = {fahrenheit:.2f} Fahrenheit")

    def hitung_kelvin(self):
        celsius = self.get_celsius()
        if celsius is not None:
            kelvin = celsius + 273.15
            self.tampil_hasil(f"{celsius:g} Celsius = {kelvin:.2f} Kelvin")

    def hitung_reamur(self):
        celsius = self.get_celsius()
        if celsius is not None:
            reamur = celsius * 4/5
            self.tampil_hasil(f"{celsius:g} Celsius = {reamur:.2f} Reamur")


app = QApplication(sys.argv)
window = KonversiSuhuApp()
window.show()
sys.exit(app.exec())