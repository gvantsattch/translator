import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from translator.ui_translator import Ui_MainWindow
from translator.app import TranslatorLogic

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resize(700, 500)

        self.logic = TranslatorLogic()
        self.languageBox.addItems(["ინგლისური", "ფრანგული"])

        self.translateButton.clicked.connect(self.translate_word)
        self.languageBox.currentIndexChanged.connect(self.clear_result)

        self.setStyleSheet("""
            QMainWindow { background-color: pink; }
            QPushButton { background-color: hotpink; color: white; }
        """)

    def translate_word(self):
        word = self.wordInput.text()
        language = self.languageBox.currentText()
        translation = self.logic.translate(word, language)
        self.resultLabel.setText(translation)

    def clear_result(self):
        self.resultLabel.setText("თარგმანი გამოჩნდება აქ")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
