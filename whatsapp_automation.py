from selenium import webdriver
import time
from datetime import datetime
import datetime as dt


class whatsapp_Login():

    def __init__(self):
        self.webpage()

    def webpage(self):

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
        self.driver.quit()
        # # time_to_wait_secs = ""
        # try:
        #     time_to_wait_secs = ((int(diff_in_time[0:2]) * 3600) + (int(diff_in_time[3:5]) * 60) + (int(diff_in_time[6:8])))
        # except ValueError:
        #     diff_in_time = "0" + diff_in_time
        #     print(diff_in_time)
        #     time_to_wait_secs = ((int(diff_in_time[0:2]) * 3600) + (int(diff_in_time[3:5]) * 60) + (int(diff_in_time[6:8])))
        #
        # print(time_to_wait_secs)
        #
        # time.sleep(time_to_wait_secs - 10)
        #
        # self.driver.quit()
        #
        # search_chat = self.driver.find_element_by_tag_name("input")
        # search_chat.send_keys(user_req_contact)
        # time.sleep(5)
        # self.driver.find_element_by_class_name("_2wP_Y").click()
        # time.sleep(5)
        # self.driver.find_element_by_class_name("_1Plpp").click()
        # text_input_selector = self.driver.find_element_by_class_name("_1Plpp")
        # text_input_selector.send_keys(user_input)
        # self.driver.find_element_by_class_name("_35EW6").click()
        #
        # time.sleep(30)
        # self.driver.quit()


if __name__ == '__main__':

    start = whatsapp_Login()
