from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.chrome.options import Options
import time
from twilio.rest import Client


def send_program_start_message():
    message = client.messages \
        .create(
        body="Program started.",
        from_='your twilio number here',
        to='your own number here'
    )
    print(message.sid)
    print(message.status)


def send_time_available_message():
    message = client.messages \
        .create(
        body="Free appointment available.",
        from_='your twilio number here',
        to='your own number here'
    )
    print(message.sid)
    print(message.status)


is_time_available = False

account_sid = "your twilio SID here"
auth_token = "your twilio TOKEN here"
client = Client(account_sid, auth_token)
send_program_start_message()

while not is_time_available:

    chrome_driver_path = "chromedriver.exe full address here. For example: C:\ProgramFiles\Development\chromedriver"
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

    driver.get("https://ir-appointment.visametric.com/de")

    time.sleep(5)

    schengen_button = driver.find_element(by=By.NAME, value="schengenBtn")
    print(schengen_button)
    schengen_button.click()
    time.sleep(5)

    survey_start = driver.find_element(by=By.NAME, value="surveyStart")
    print(survey_start)
    survey_start.click()
    time.sleep(1)

    nationality_radio = driver.find_element(by=By.NAME, value="nationality")
    print(nationality_radio)
    nationality_radio.click()
    time.sleep(1)

    submit_button = driver.find_element(by=By.ID, value="btnSubmit")
    print(submit_button)
    submit_button.click()
    time.sleep(5)

    city_dropdown = Select(driver.find_element(by=By.ID, value="city"))
    print(city_dropdown)
    city_dropdown.select_by_visible_text("TEHERAN")
    time.sleep(1)

    office_dropdown = Select(driver.find_element(by=By.ID, value="office"))
    print(office_dropdown)
    office_dropdown.select_by_visible_text("TEHERAN")
    time.sleep(1)

    office_type_dropdown = Select(driver.find_element(by=By.ID, value="officetype"))
    print(office_type_dropdown)
    office_type_dropdown.select_by_visible_text("NORMAL")
    time.sleep(1)

    totalPerson_dropdown = Select(driver.find_element(by=By.ID, value="totalPerson"))
    print(totalPerson_dropdown)
    totalPerson_dropdown.select_by_value("2")
    time.sleep(1)

    try:
        print("checking...")
        check_atm_radio = driver.find_element(by=By.ID, value="atm")
        print(check_atm_radio)
        check_atm_radio.click()
        time.sleep(1)
        print("time available.")
        send_time_available_message()
        time.sleep(200)
        send_time_available_message()
        time.sleep(200)
        send_time_available_message()
        time.sleep(200)
        send_time_available_message()
        time.sleep(200)
        send_time_available_message()
        time.sleep(200)

        is_time_available = True
    except ElementNotInteractableException:
        print("time not available.")

    driver.close()
    time.sleep(300)
