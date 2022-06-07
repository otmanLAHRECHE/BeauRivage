import time

import PyQt5
from PyQt5.QtCore import QThread, pyqtSignal


class StartUpLoadingThread(QThread):
    _signal = pyqtSignal(int)
    _signal_result = pyqtSignal(bool)

    def __init__(self):
        super(StartUpLoadingThread, self).__init__()

    def __del__(self):
        self.terminate()
        self.wait()

    def run(self):
        for i in range(100):
            self._signal.emit(i)
            #time.sleep(0.005)
        self._signal_result.emit(True)