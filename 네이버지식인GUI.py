import sys
from PySide6.QtWidgets import QApplication, QWidget
from naver_kin import Ui_Form

class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # self.객체이름.clicked.connect(self.실행할메서드이름)
        self.start_btn.clicked.connect(self.start)
        self.reset_btn.clicked.connect(self.reset)
        self.save_btn.clicked.connect(self.save)
        self.quit_btn.clicked.connect(self.quit)

    def start(self):
        print("시작")
    def reset(self):
        print("리셋")
    def save(self):
        print("저장")
    def quit(self):
        print("종료")

app = QApplication()
window = MainWindow()
window.show()
sys.exit(app.exec_())