import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QTimer, QTime

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.start_button = QPushButton("start", self)
        self.stop_button = QPushButton("stop", self)
        self.reset_button = QPushButton("reset", self)
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Will's Stopwatch")
        self.setGeometry(450, 350, 300, 300)
        
        main_layout = QVBoxLayout(self)
        button_layout = QHBoxLayout(self)

        main_layout.addWidget(self.time_label)
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.reset_button)
        button_layout.addWidget(self.stop_button)
        main_layout.addLayout(button_layout)

        self.time_label.setText("00:00:00.00")
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 50px;")

        self.start_button.clicked.connect(self.press_start_button)
        self.stop_button.clicked.connect(self.press_stop_button)
        self.reset_button.clicked.connect(self.press_reset_button)        
        self.timer.timeout.connect(self.update_display)

    def press_stop_button(self):
        self.timer.stop()

    def press_start_button(self):
        self.timer.start(10)

    def press_reset_button(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText("00:00:00.00")

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10

        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())