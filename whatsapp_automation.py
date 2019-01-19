from selenium import webdriver
import time
from datetime import datetime
import datetime as dt
from PyQt5 import QtWidgets
import sys


class whatsapp_Login(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initial_info()

    def initial_info(self):

        self.First_warning_window = QtWidgets.QWidget()
        self.resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.width = (self.resolution.width() // 2) - 200
        self.height = (self.resolution.height() // 2) - 75
        self.First_warning_window.setGeometry(self.width, self.height, 400, 150)

        self.info_text = QtWidgets.QLabel(self.First_warning_window)
        self.info_text.setText(
            "Please authenticate your Whatsapp login by: \n\n Whatsapp -> Whatsapp Web -> scan Qr Code \n\n Or \n\n Whatsapp -> Whatsapp Web -> + symbol -> Scan Qr code")

        self.ok_first_window_button = QtWidgets.QPushButton("Ok", self.First_warning_window)
        self.ok_first_window_button.move(335, 115)
        self.ok_first_window_button.clicked.connect(self.get_name)

        self.First_warning_window.setFixedSize(400, 150)

        self.First_warning_window.show()

    def webpage(self):

        self.First_warning_window.close()
        self.login_check = False

        url = 'https://web.whatsapp.com/'
        agent = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')
        self.driver.get(url)

        time.sleep(15)

        self.curr_url = self.driver.current_url

        element_check = self.driver.find_element_by_class_name("MZIyP")

        if element_check:
            self.login_check = True

        if self.curr_url == "https://web.whatsapp.com" and self.login_check == False:
            self.login_fail()

        elif self.login_check:
            self.login_successful()

    def get_name(self):

        self.First_warning_window.close()

        self.name_window = QtWidgets.QWidget()
        self.width = (self.resolution.width() // 2) - 150
        self.height = (self.resolution.height() // 2) - 50
        self.name_window.setGeometry(self.width, self.height, 325, 125)

        self.name_label = QtWidgets.QLabel(self.name_window)
        self.name_label.setText("Enter the contact you want to send to:")

        self.name_entry = QtWidgets.QLineEdit(self.name_window)

        self.name_ok_button = QtWidgets.QPushButton("Ok", self.name_window)

        self.name_label.move(25, 25)
        self.name_entry.move(25, 60)
        self.name_entry.resize(250, 25)
        self.name_ok_button.move(260, 95)

        self.name_ok_button.clicked.connect(self.get_text)

        self.name_window.show()

    def get_text(self):

        self.name_window.close()

        self.text_window = QtWidgets.QWidget()
        self.width = (self.resolution.width() // 2) - 150
        self.height = (self.resolution.height() // 2) - 50
        self.text_window.setGeometry(self.width, self.height, 350, 175)

        self.text_label = QtWidgets.QLabel(self.text_window)
        self.text_label.setText("Enter the text you want to send to the contact:")

        self.text_entry = QtWidgets.QTextEdit(self.text_window)

        self.text_ok = QtWidgets.QPushButton("Ok", self.text_window)
        self.text_ok.clicked.connect(self.get_time)

        self.text_label.move(25, 25)
        self.text_entry.move(25, 50)
        self.text_entry.resize(300, 85)
        self.text_ok.move(290, 140)

        self.text_window.show()

    def get_time(self):

        self.text_window.close()

        self.time_window = QtWidgets.QWidget()
        self.width = (self.resolution.width() // 2) - 150
        self.height = (self.resolution.height() // 2) - 50
        self.time_window.setGeometry(self.width, self.height, 325, 125)

        self.time_label = QtWidgets.QLabel(self.time_window)
        self.time_label.setText("Enter time in HH:MM:SS:")

        self.time_entry = QtWidgets.QLineEdit(self.time_window)

        self.time_ok_button = QtWidgets.QPushButton("Ok", self.time_window)
        
        self.time_label.move(25, 25)
        self.time_entry.move(25, 60)
        self.time_entry.resize(250, 25)
        self.time_ok_button.move(260, 95)

        self.time_ok_button.clicked.connect(self.get_text)

        self.time_window.show()

    def login_fail(self):

        print("Please Scan the Qr Code")
        self.driver.quit()

    def login_successful(self):

        user_req_contact = input("Enter the contact to send:\n")
        user_input = input("The text you want to send: \n")
        user_input_time = input("Enter time in HH:MM:SS: \n")
        current_time = datetime.now()
        curr_time_hour = current_time.hour
        curr_time_min = current_time.minute
        curr_time_sec = current_time.second
        current_time_proper = str(curr_time_hour) + ":" + str(curr_time_min) + ":" + str(curr_time_sec)
        user_input_time_striped = dt.datetime.strptime(user_input_time, '%H:%M:%S')
        current_time_proper_striped = dt.datetime.strptime(current_time_proper, '%H:%M:%S')
        print(user_input_time_striped)
        print(current_time_proper_striped)
        diff_in_time = (user_input_time_striped - current_time_proper_striped)
        diff_in_time = str(diff_in_time)
        print(diff_in_time)
        # self.driver.quit()

        try:
            time_to_wait_secs = (
                    (int(diff_in_time[0:2]) * 3600) + (int(diff_in_time[3:5]) * 60) + (int(diff_in_time[6:8])))
        except ValueError:
            diff_in_time = "0" + diff_in_time
            print(diff_in_time)
            time_to_wait_secs = (
                    (int(diff_in_time[0:2]) * 3600) + (int(diff_in_time[3:5]) * 60) + (int(diff_in_time[6:8])))

        print(time_to_wait_secs)

        time.sleep(time_to_wait_secs - 5)

        search_chat = self.driver.find_element_by_tag_name("input")
        search_chat.send_keys(user_req_contact)
        time.sleep(5)
        self.driver.find_element_by_class_name("_2EXPL").click()
        time.sleep(5)
        self.driver.find_element_by_class_name("_1Plpp").click()
        text_input_selector = self.driver.find_element_by_class_name("_1Plpp")
        text_input_selector.send_keys(user_input)
        self.driver.find_element_by_class_name("_35EW6").click()

        time.sleep(30)
        self.driver.quit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    start = whatsapp_Login()
    sys.exit(app.exec_())
