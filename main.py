import sys
from itertools import cycle
from PySide6.QtWidgets import QApplication, QMainWindow
from window.mainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.xorCheckBox.clicked.connect(self.onXorCheckBoxClicked)
        self.ui.rawPacketTextEdit.textChanged.connect(self.onRawPacketTextEditTextChanged)
        self.ui.xorKeyTextEdit.textChanged.connect(self.onRawPacketTextEditTextChanged)

    def onXorCheckBoxClicked(self):
        self.ui.xorKeyTextEdit.setEnabled(self.ui.xorCheckBox.isChecked())
        self.onRawPacketTextEditTextChanged()

    def clearPacketInfoTextEdits(self):
        # self.ui.magicStartTextEdit.setStyleSheet("")
        # self.ui.magicEndTextEdit.setStyleSheet("")
        self.ui.magicStartTextEdit.setPlainText("")
        self.ui.cmdIdHexTextEdit.setPlainText("")
        self.ui.cmdIdDecTextEdit.setPlainText("")
        self.ui.metadataLengthHexTextEdit.setPlainText("")
        self.ui.metadataLengthDecTextEdit.setPlainText("")
        self.ui.bodyLengthHexTextEdit.setPlainText("")
        self.ui.bodyLengthDecTextEdit.setPlainText("")
        self.ui.metadataTextEdit.setPlainText("")
        self.ui.bodyTextEdit.setPlainText("")
        self.ui.magicEndTextEdit.setPlainText("")

    def onRawPacketTextEditTextChanged(self):
        def xorHex(data: str, key: str) -> str:
            return bytes(v ^ k for (v, k) in zip(bytes.fromhex(data), cycle(bytes.fromhex(key)))).hex()

        def hexToDec(c: str) -> int:
            try:
                return int(c, 16)
            except ValueError:
                pass

        def myToString(c) -> str:
            return str(c) if c is not None else ""

        self.clearPacketInfoTextEdits()
        raw = self.ui.rawPacketTextEdit.toPlainText() if not self.ui.xorCheckBox.isChecked()\
            else xorHex(self.ui.rawPacketTextEdit.toPlainText(), self.ui.xorKeyTextEdit.toPlainText())
        try:
            self.ui.magicStartTextEdit.setPlainText(
                magic_start := raw[0:4])
            self.ui.cmdIdHexTextEdit.setPlainText(
                cmdid_hex := raw[4:8])
            self.ui.cmdIdDecTextEdit.setPlainText(myToString(
                cmdid := hexToDec(cmdid_hex)))
            self.ui.metadataLengthHexTextEdit.setPlainText(
                metadata_length_hex := raw[8:12])
            self.ui.metadataLengthDecTextEdit.setPlainText(myToString(
                metadata_length := hexToDec(metadata_length_hex)))
            self.ui.bodyLengthHexTextEdit.setPlainText(
                body_length_hex := raw[12:20])
            self.ui.bodyLengthDecTextEdit.setPlainText(myToString(
                body_length := hexToDec(body_length_hex)))
            self.ui.metadataTextEdit.setPlainText(
                metadata := raw[20:(p_metadata_end := 20 + metadata_length * 2)])
            self.ui.bodyTextEdit.setPlainText(
                body := raw[p_metadata_end:(p_body_end := p_metadata_end + body_length * 2)])
            self.ui.magicEndTextEdit.setPlainText(
                magic_end := raw[p_body_end:(p_magic_end_end := p_body_end + 4)])
        except TypeError:
            pass

        magic_dict = {
            self.ui.magicStartTextEdit: "4567",
            self.ui.magicEndTextEdit: "89ab"
        }
        for textedit, value in magic_dict.items():
            textedit.setStyleSheet("background:palegreen" if (text := textedit.toPlainText()).lower() == value
                                   else "" if text == "" else "background:salmon")


if __name__ == '__main__':

    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
