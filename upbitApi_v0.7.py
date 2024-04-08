import sys
import time

import requests

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtGui import *


form_class = uic.loadUiType("ui/up.ui")[0]

# 시그널 클래스 -> 업비트서버에 요청을 넣어서 코인 정보를 가져오는 일을 하는 클래스
class UpbitCall(QThread):
    # 시그널 함수 선언(정의)
    coinDataSent = pyqtSignal(float, float, float, float, float, float, float, float)

    def run(self):
        while True:     # 무한루프

            url = "https://api.upbit.com/v1/ticker"
            param = {"markets":"KRW-BTC"}
            # "https://api.upbit.com/v1/ticker?markets=KRW-BTC"
            response = requests.get(url, params=param)
            result = response.json()

            trade_price = result[0]["trade_price"]  # 비트코인의 현재가격
            high_price = result[0]["high_price"]  # 최고가
            low_price = result[0]["low_price"]  # 최고가
            prev_closing_price = result[0]["prev_closing_price"]  # 전일종가
            trade_volume = result[0]["trade_volume"]  # 최근 거래량
            acc_trade_volume_24h = result[0]["acc_trade_volume_24h"]  # 24시간 누적 거래량
            acc_trade_price_24h = result[0]["acc_trade_price_24h"]  # 24시간 누적 거래대금
            signed_change_rate = result[0]["signed_change_rate"]  # 부호가 있는 변화율

            self.coinDataSent.emit(
                float(trade_price),
                float(high_price),
                float(low_price),
                float(prev_closing_price),
                float(trade_volume),
                float(acc_trade_volume_24h),
                float(acc_trade_price_24h),
                float(signed_change_rate)
            )
            # 업비트 api 호출 딜레이 2초
            time.sleep(2)

class MainWindow(QMainWindow, form_class):  # 슬롯 클래스
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # ui 불러오기
        self.setWindowTitle("비트코인 정보 프로그램 v0.7")

        self.ubc = UpbitCall()  # 시그널 클래스로 객체 선언
        self.ubc.coinDataSent.connect(self.fillCoinData)
        self.ubc.start()  # 시그널 클래스 run() 실행
        self.setWindowIcon(QIcon("icon/bci.png"))



    def fillCoinData(self, trade_price, high_price, low_price, prev_closing_price,
                     trade_volume, acc_trade_volume_24h, acc_price_volume_24h, signed_change_rate):
        self.trade_price.setText(f"{trade_price:,.0f}원")
        self.high_price.setText(f"{high_price:,.0f}원")
        self.low_price.setText(f"{low_price:,.0f}원")
        self.prev_closing_price.setText(f"{prev_closing_price:,.0f}원")
        self.trade_volume.setText(f"{trade_volume:,.3f}개")
        self.acc_trade_volume_24h.setText(f"{acc_trade_volume_24h:,.3f}개")
        self.acc_price_volume_24h.setText(f"{acc_price_volume_24h:,.0f}원")
        self.signed_change_rate.setText(f"{signed_change_rate:.2f}%")
        self.update_style()

    def update_style(self):   # 변화율이 +이면 빨간색, -이면 파란색으로 표시
        if "-" in self.signed_change_rate.text():

            self.signed_change_rate.setStyleSheet("background-color:blue;color:white;")
            self.trade_price.setStyleSheet("color:blue;")
        else:
            self.signed_change_rate.setStyleSheet("background-color:red;color:white;")
            self.trade_price.setStyleSheet("color:red;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())








