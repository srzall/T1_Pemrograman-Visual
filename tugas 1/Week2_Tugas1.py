# Samsul Rizal
# F1D02310025
# Kelas D

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QLineEdit, QComboBox, QVBoxLayout,
    QHBoxLayout, QMessageBox
)
from PySide6.QtCore import Qt

class FormBiodata(QWidget):

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Form Biodata Mahasiswa")
        self.setFixedSize(400, 580)
        self.setStyleSheet("background-color: white; font-family: Arial;")

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(25, 25, 25, 25)
        main_layout.setSpacing(8) 

        input_style = "padding: 8px; border: 1px solid #82c390; border-radius: 4px; background-color: #f9fff9;"
        
        main_layout.addWidget(QLabel("Nama Lengkap:"))
        self.input_nama = QLineEdit()
        self.input_nama.setStyleSheet(input_style)
        main_layout.addWidget(self.input_nama)

        main_layout.addSpacing(5) 

        main_layout.addWidget(QLabel("NIM:"))
        self.input_nim = QLineEdit()
        self.input_nim.setStyleSheet(input_style)
        main_layout.addWidget(self.input_nim)

        main_layout.addSpacing(5)

        main_layout.addWidget(QLabel("Kelas:"))
        self.input_kelas = QLineEdit()
        self.input_kelas.setStyleSheet(input_style)
        main_layout.addWidget(self.input_kelas)

        main_layout.addSpacing(5)

        main_layout.addWidget(QLabel("Jenis Kelamin:"))
        self.combo_jk = QComboBox()
        self.combo_jk.addItems(["Laki-laki", "Perempuan"])
        self.combo_jk.setStyleSheet(
            "QComboBox { padding: 8px; border: 1px solid #ccc; border-radius: 4px; background-color: white; }"
            "QComboBox QAbstractItemView { background-color: white; border: 1px solid #ccc; }"
        )
        main_layout.addWidget(self.combo_jk)

        main_layout.addSpacing(15)

        btn_layout = QHBoxLayout()
        
        self.btn_tampilkan = QPushButton("Tampilkan")
        self.btn_tampilkan.setFixedSize(90, 35) 
        self.btn_tampilkan.setStyleSheet(
            "background-color: #3498db; color: white; border: none; border-radius: 4px; font-weight: bold;"
        )
        self.btn_tampilkan.clicked.connect(self.tampilkan)

        self.btn_reset = QPushButton("Reset")
        self.btn_reset.setFixedSize(90, 35) 
        self.btn_reset.setStyleSheet(
            "background-color: #95a5a6; color: white; border: none; border-radius: 4px; font-weight: bold;"
        )
        self.btn_reset.clicked.connect(self.reset)

        btn_layout.addWidget(self.btn_tampilkan)
        btn_layout.addWidget(self.btn_reset)
        btn_layout.addStretch() 

        main_layout.addLayout(btn_layout)
        main_layout.addSpacing(15)

        self.label_hasil = QLabel("")
        self.label_hasil.setWordWrap(True)
        self.label_hasil.hide() 
        
        main_layout.addWidget(self.label_hasil)
        main_layout.addStretch() 

        self.setLayout(main_layout)

    def tampilkan(self):
        nama = self.input_nama.text().strip()
        nim = self.input_nim.text().strip()
        kelas = self.input_kelas.text().strip()
        jk = self.combo_jk.currentText()

        if not nama or not nim or not kelas:
            QMessageBox.warning(self, "Error", "Semua field inputan harus diisi!")
            return

        self.label_hasil.setText(
            f"<b style='font-size:13px;'>DATA BIODATA</b><br><br>" f"Nama: {nama}<br>" f"NIM: {nim}<br>" f"Kelas: {kelas}<br>" f"Jenis Kelamin: {jk}"
        )
        
        self.label_hasil.setStyleSheet(
            "padding: 15px; background-color: #d4edda; color: #155724; "
            "border-left: 5px solid #28a745; border-radius: 3px;"
        )
        self.label_hasil.show()

    def reset(self):
        self.input_nama.clear()
        self.input_nim.clear()
        self.input_kelas.clear()
        self.combo_jk.setCurrentIndex(0)
        self.label_hasil.clear()
        self.label_hasil.hide() 

if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    window = FormBiodata()
    window.show()
    sys.exit(app.exec())