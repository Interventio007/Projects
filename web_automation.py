import time
from selenium import webdriver
import imaplib
import smtplib
import email

url = 'https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
agent = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get(url)

email_insert = driver.find_element_by_tag_name("input")
email_insert.send_keys("") //enter email here

driver.find_element_by_class_name('CwaK9').click()
time.sleep(2)

passwd_url = driver.current_url

if passwd_url == "https://accounts.google.com/signin/v2/sl/pwd?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin&cid=1&navigationDirection=forward":
    password = driver.find_element_by_xpath("//input[@name='password']")
    password.send_keys("")    // enter password here
    driver.find_element_by_id("passwordNext").click()

time.sleep(5)

mail_url = driver.current_url

mail_id = ""                          //enter mail id here
mail_pwd = ""                         //enter password here

if mail_url == "https://mail.google.com/mail/u/0/#inbox":

    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(mail_id, mail_pwd)
    mail.select('inbox')

    type, data = mail.search(None, 'ALL')
    mail_ids = data[0]

    id_list = mail_ids.split()
    first_email_id = int(id_list[0])
    latest_email_id = int(id_list[-1])

    for i in range(latest_email_id, first_email_id, -1):
        typ, data = mail.fetch(str(i), '(RFC822)')

        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(str(response_part[1]))
                email_subject = msg['subject']
                email_from = msg['from']
                print('From : ' + email_from + '\n')
                print('Subject : ' + email_subject + '\n')

time.sleep(15)
driver.quit()
