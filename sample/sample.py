"""

  @ 5초마다 1씩 더하는 프로그램 샘플 코드

  작성일 : 2024-01-04
  작성자 : KJW

"""

from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton
from PySide6.QtCore import QTimer, QTime

class CounterApp(QWidget):
    def __init__(self):
        super().__init__()

        self.counter = 0
        self.elapsed_time = 0
        self.is_running = False

        self.setup_ui()
        self.setup_timer()

    def setup_ui(self):
        self.layout = QVBoxLayout()

        self.label = QLabel(f"현재 값: {self.counter}\n경과 시간: 00:00")
        self.layout.addWidget(self.label)

        self.start_pause_button = QPushButton("시작")
        self.start_pause_button.clicked.connect(self.toggle_timer)
        self.layout.addWidget(self.start_pause_button)

        self.stop_button = QPushButton("멈춤")
        self.stop_button.clicked.connect(self.stop_timer)
        self.layout.addWidget(self.stop_button)

        self.setLayout(self.layout)
        self.setWindowTitle("5초마다 1씩 증가하는 프로그램")

    def setup_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_counter)
        self.time_counter = QTimer(self)
        self.time_counter.timeout.connect(self.update_elapsed_time)

    def toggle_timer(self):
        if not self.is_running:
            self.timer.start(5000)  # 5초마다 타임아웃 발생
            self.time_counter.start(1000)  # 1초마다 타임아웃 발생
            self.is_running = True
            self.start_pause_button.setText("일시정지")
        else:
            self.timer.stop()
            self.time_counter.stop()
            self.is_running = False
            self.start_pause_button.setText("시작")

    def stop_timer(self):
        self.timer.stop()
        self.time_counter.stop()
        self.is_running = False
        self.counter = 0
        self.elapsed_time = 0
        self.update_label()
        self.start_pause_button.setText("시작")

    def update_counter(self):
        self.counter += 1
        self.update_label()

    def update_elapsed_time(self):
        self.elapsed_time += 1
        self.update_label()

    def update_label(self):
        elapsed_time_str = QTime(0, 0).addSecs(self.elapsed_time).toString("mm:ss")
        self.label.setText(f"현재 값: {self.counter}\n경과 시간: {elapsed_time_str}")

if __name__ == "__main__":
    app = QApplication([])
    window = CounterApp()
    window.show()
    app.exec()