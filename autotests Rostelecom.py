import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import random

@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def browser_cookie():
    chrome_options = Options()
    chrome_options.add_argument("--disable-cookie") # Блокируем cookie
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_successful_login_phone(browser):

    browser.get("https://b2c.passport.rt.ru/")

    phone_input = browser.find_element(By.ID, "username")
    phone_input.send_keys("ваш номер телефона")  # Замените на ваш реальный номер

    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys("ваш пароль")  # Замените на ваш реальный пароль

    login_button = browser.find_element(By.ID, "kc-login")
    login_button.click()

    wait = WebDriverWait(browser, 10)
    wait.until(EC.url_contains("https://b2c.passport.rt.ru/account_b2c/"))

    # Проверяем, что пользователь успешно авторизовался
    assert "account_b2c" in browser.current_url
    assert "Личный кабинет" in browser.page_source  # Проверка по наличию текста на странице



def test_unsuccessful_login_wrong_password(browser):
    browser.get("https://b2c.passport.rt.ru/")

    phone_input = browser.find_element(By.ID, "username")
    phone_input.send_keys("ваш_номер_телефона")  # Замените на ваш реальный номер

    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys("неверный_пароль")  # Замените на неверный пароль

    login_button = browser.find_element(By.ID, "kc-login")
    login_button.click()

    wait = WebDriverWait(browser, 10)
    error_message = wait.until(EC.visibility_of_element_located((By.ID, "form-error-message")))

    # Проверяем, что сообщение об ошибке присутствует
    assert error_message.is_displayed()
    assert "Неверный логин или пароль" in error_message.text

    # Проверяем, что URL не изменился и пользователь остался на странице авторизации
    assert "b2c.passport.rt.ru" in browser.current_url


def test_unsuccessful_login_invalid_phone(browser):

    browser.get("https://b2c.passport.rt.ru/")

    phone_input = browser.find_element(By.ID, "username")
    phone_input.send_keys("неверный_номер_телефона")  # Замените на неверный номер

    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys("ваш_пароль")  # Замените на ваш реальный пароль

    login_button = browser.find_element(By.ID, "kc-login")
    login_button.click()

    wait = WebDriverWait(browser, 10)
    error_message = wait.until(EC.visibility_of_element_located((By.ID, "form-error-message")))

    # Проверяем, что сообщение об ошибке присутствует
    assert error_message.is_displayed()
    assert "Неверный логин или пароль" in error_message.text

    # Проверяем, что URL не изменился и пользователь остался на странице авторизации
    assert "b2c.passport.rt.ru" in browser.current_url



def test_successful_login_email(browser):

    browser.get("https://b2c.passport.rt.ru/")

    email_tab = browser.find_element(By.ID, "t-btn-tab-mail")
    email_tab.click()

    email_input = browser.find_element(By.ID, "username")
    email_input.send_keys("ваш_email")  # Замените на ваш реальный email

    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys("ваш_пароль")  # Замените на ваш реальный пароль

    login_button = browser.find_element(By.ID, "kc-login")
    login_button.click()

    wait = WebDriverWait(browser, 10)
    wait.until(EC.url_contains("https://b2c.passport.rt.ru/account_b2c/"))

    # Проверяем, что пользователь успешно авторизовался
    assert "account_b2c" in browser.current_url
    assert "Личный кабинет" in browser.page_source  # Проверка по наличию текста на странице

def test_unsuccessful_login_email_wrong_password(browser):

    browser.get("https://b2c.passport.rt.ru/")

    email_tab = browser.find_element(By.ID, "t-btn-tab-mail")
    email_tab.click()

    email_input = browser.find_element(By.ID, "username")
    email_input.send_keys("ваш_email")  # Замените на ваш реальный email

    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys("неверный_пароль")  # Замените на неверный пароль

    login_button = browser.find_element(By.ID, "kc-login")
    login_button.click()

    wait = WebDriverWait(browser, 10)
    error_message = wait.until(EC.visibility_of_element_located((By.ID, "form-error-message")))

    # Проверяем, что сообщение об ошибке присутствует
    assert error_message.is_displayed()
    assert "Неверный логин или пароль" in error_message.text

    # Проверяем, что URL не изменился и пользователь остался на странице авторизации
    assert "b2c.passport.rt.ru" in browser.current_url

def test_successful_login_login(browser):

    browser.get("https://b2c.passport.rt.ru/")

    login_tab = browser.find_element(By.ID, "t-btn-tab-login")
    login_tab.click()

    login_input = browser.find_element(By.ID, "username")
    login_input.send_keys("ваш_логин")  # Замените на ваш реальный логин

    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys("ваш_пароль")  # Замените на ваш реальный пароль

    login_button = browser.find_element(By.ID, "kc-login")
    login_button.click()

    wait = WebDriverWait(browser, 10)
    wait.until(EC.url_contains("https://b2c.passport.rt.ru/account_b2c/"))

    # Проверяем, что пользователь успешно залогинился
    assert "account_b2c" in browser.current_url
    assert "Личный кабинет" in browser.page_source  # Проверка по наличию текста на странице

def test_unsuccessful_login_invalid_login(browser):

    browser.get("https://b2c.passport.rt.ru/")

    login_tab = browser.find_element(By.ID, "t-btn-tab-login")
    login_tab.click()

    login_input = browser.find_element(By.ID, "username")
    login_input.send_keys("неверный_логин")  # Замените на неверный логин

    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys("ваш_пароль")  # Замените на ваш реальный пароль

    login_button = browser.find_element(By.ID, "kc-login")
    login_button.click()

    wait = WebDriverWait(browser, 10)
    error_message = wait.until(EC.visibility_of_element_located((By.ID, "form-error-message")))


    assert error_message.is_displayed()
    assert "Неверный логин или пароль" in error_message.text

    assert "b2c.passport.rt.ru" in browser.current_url

def test_automatic_tab_switching(browser):

    browser.get("https://b2c.passport.rt.ru/")

    input_field = browser.find_element(By.ID, "username")
    input_field.send_keys("test@example.com")
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, "t-btn-tab-mail")))
    assert "rt-tab--active" in browser.find_element(By.ID, "t-btn-tab-mail").get_attribute("class")
    input_field.clear()

    input_field.send_keys("1234567890")
    wait.until(EC.presence_of_element_located((By.ID, "t-btn-tab-phone")))
    assert "rt-tab--active" in browser.find_element(By.ID, "t-btn-tab-phone").get_attribute("class")
    input_field.clear()

    input_field.send_keys("testlogin")
    wait.until(EC.presence_of_element_located((By.ID, "t-btn-tab-login")))
    assert "rt-tab--active" in browser.find_element(By.ID, "t-btn-tab-login").get_attribute("class")
    input_field.clear()

def test_successful_login_account(browser):

    browser.get("https://b2c.passport.rt.ru/")

    account_tab = browser.find_element(By.ID, "t-btn-tab-ls")
    account_tab.click()

    login_input = browser.find_element(By.ID, "username")
    login_input.send_keys("ваш_лицевой_счет")  # Замените на ваш реальный лицевой счет

    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys("ваш_пароль")  # Замените на ваш реальный пароль

    login_button = browser.find_element(By.ID, "kc-login")
    login_button.click()

    wait = WebDriverWait(browser, 10)
    wait.until(EC.url_contains("https://b2c.passport.rt.ru/account_b2c/"))

    # Проверяем, что пользователь успешно залогинился
    assert "account_b2c" in browser.current_url
    assert "Личный кабинет" in browser.page_source  # Проверка по наличию текста на странице

def test_unsuccessful_login_account_wrong_password(browser):

    browser.get("https://b2c.passport.rt.ru/")

    account_tab = browser.find_element(By.ID, "t-btn-tab-ls")
    account_tab.click()

    login_input = browser.find_element(By.ID, "username")
    login_input.send_keys("ваш_лицевой_счет")  # Замените на ваш реальный лицевой счет

    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys("неверный_пароль")  # Замените на неверный пароль

    login_button = browser.find_element(By.ID, "kc-login")
    login_button.click()

    wait = WebDriverWait(browser, 10)
    error_message = wait.until(EC.visibility_of_element_located((By.ID, "form-error-message")))

    # Проверяем, что сообщение об ошибке присутствует
    assert error_message.is_displayed()
    assert "Неверный логин или пароль" in error_message.text

    # Проверяем, что URL не изменился и пользователь остался на странице авторизации
    assert "b2c.passport.rt.ru" in browser.current_url

def test_successful_login_temp_code_existing_user(browser):

    browser.get("https://b2c.passport.rt.ru/")

    get_code_button = browser.find_element(By.ID, "otp_get_code")
    get_code_button.click()

    phone_input = browser.find_element(By.ID, "phone")
    phone_input.send_keys("ваш_номер_телефона")  # Замените на ваш реальный номер

    continue_button = browser.find_element(By.ID, 'otp_send_code')
    continue_button.click()

    #  Здесь нужно перехватить код из SMS. Реальный автоматический перехват SMS может быть сложным,
    #  поэтому мы будем использовать time.sleep() + ручной ввод кода.
    #  В РЕАЛЬНЫХ АВТОТЕСТАХ НУЖНО ИСПОЛЬЗОВАТЬ ДРУГОЙ ПОДХОД (например, SMS API, мок-сервер и т.д.)
    time.sleep(30)  # Даем время получить код

    temp_code_input = browser.find_element(By.ID, "otp_code")
    temp_code_input.send_keys("временный_код")  # Замените на ваш полученный код

    continue_button_2 = browser.find_element(By.ID, 'otp_code_submit')
    continue_button_2.click()

    wait = WebDriverWait(browser, 10)
    wait.until(EC.url_contains("https://b2c.passport.rt.ru/account_b2c/"))

    # Проверяем, что пользователь успешно залогинился
    assert "account_b2c" in browser.current_url
    assert "Личный кабинет" in browser.page_source  # Проверка по наличию текста на странице


def test_successful_login_temp_code_new_user(browser):
    browser.get("https://b2c.passport.rt.ru/")

    # Нажать "получить код"
    get_code_button = browser.find_element(By.ID, "otp_get_code")
    get_code_button.click()

    phone_input = browser.find_element(By.ID, "phone")
    phone_input.send_keys("новый_номер_телефона")  # Замените на НОВЫЙ номер

    continue_button = browser.find_element(By.ID, 'otp_send_code')
    continue_button.click()

    # Здесь нужно перехватить код из SMS. Реальный автоматический перехват SMS может быть сложным,
    # поэтому мы будем использовать time.sleep() + ручной ввод кода.
    # В РЕАЛЬНЫХ АВТОТЕСТАХ НУЖНО ИСПОЛЬЗОВАТЬ ДРУГОЙ ПОДХОД (например, SMS API, мок-сервер и т.д.)
    time.sleep(30)  # Даем время получить код

    temp_code_input = browser.find_element(By.ID, "otp_code")
    temp_code_input.send_keys("временный_код")  # Замените на ваш полученный код

    continue_button_2 = browser.find_element(By.ID, 'otp_code_submit')
    continue_button_2.click()

    wait = WebDriverWait(browser, 10)
    wait.until(EC.url_contains("https://b2c.passport.rt.ru/account_b2c/"))

    # Проверяем, что пользователь успешно залогинился
    assert "account_b2c" in browser.current_url
    assert "Личный кабинет" in browser.page_source

def test_successful_password_recovery_phone(browser):

    browser.get("https://b2c.passport.rt.ru/")

    forgot_password_link = browser.find_element(By.ID, "forgot-password")
    forgot_password_link.click()

    phone_input = browser.find_element(By.ID, "phone")
    phone_input.send_keys("ваш_номер_телефона")  # Замените на ваш реальный номер

    captcha_input = browser.find_element(By.ID, 'captcha')
    #  Тут нужно ввести капчу, автоматизировать сложно. Пока пропускаем
    #  В РЕАЛЬНЫХ АВТОТЕСТАХ НУЖНО ИСПОЛЬЗОВАТЬ ДРУГОЙ ПОДХОД (например, обходить капчу, выключать ее, использовать мок-сервер и т.д.)
    time.sleep(5) #Даем время ввести капчу

    continue_button = browser.find_element(By.ID, 'reset-by-phone')
    continue_button.click()


    #  Здесь нужно перехватить код из SMS. Реальный автоматический перехват SMS может быть сложным,
    #  поэтому мы будем использовать time.sleep() + ручной ввод кода.
    #  В РЕАЛЬНЫХ АВТОТЕСТАХ НУЖНО ИСПОЛЬЗОВАТЬ ДРУГОЙ ПОДХОД (например, SMS API, мок-сервер и т.д.)
    time.sleep(30)  # Даем время получить код

    sms_code_input = browser.find_element(By.ID, "code")
    sms_code_input.send_keys("временный_код")  # Замените на ваш полученный код

    continue_button_2 = browser.find_element(By.ID, 'reset-by-code')
    continue_button_2.click()


    new_password_input = browser.find_element(By.ID, "password-new")
    new_password_input.send_keys("новый_пароль") # Замените на желаемый новый пароль

    confirm_password_input = browser.find_element(By.ID, "password-confirm")
    confirm_password_input.send_keys("новый_пароль") # Замените на желаемый новый пароль

    save_password_button = browser.find_element(By.ID, "reset-password-submit")
    save_password_button.click()

    wait = WebDriverWait(browser, 10)
    wait.until(EC.url_contains("https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?session"))

    assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?session" in browser.current_url


def test_unsuccessful_password_recovery_phone_wrong_sms_code(browser):

    browser.get("https://b2c.passport.rt.ru/")

    forgot_password_link = browser.find_element(By.ID, "forgot-password")
    forgot_password_link.click()

    phone_input = browser.find_element(By.ID, "phone")
    phone_input.send_keys("ваш_номер_телефона")  # Замените на ваш реальный номер

    captcha_input = browser.find_element(By.ID, 'captcha')
    #  Тут нужно ввести капчу, автоматизировать сложно. Пока пропускаем
    #  В РЕАЛЬНЫХ АВТОТЕСТАХ НУЖНО ИСПОЛЬЗОВАТЬ ДРУГОЙ ПОДХОД (например, обходить капчу, выключать ее, использовать мок-сервер и т.д.)
    time.sleep(5)  # Даем время ввести капчу


    continue_button = browser.find_element(By.ID, 'reset-by-phone')
    continue_button.click()


    sms_code_input = browser.find_element(By.ID, "code")
    sms_code_input.send_keys("неверный_код")  # Замените на неверный код

    continue_button_2 = browser.find_element(By.ID, 'reset-by-code')
    continue_button_2.click()


    wait = WebDriverWait(browser, 10)
    error_message = wait.until(EC.visibility_of_element_located((By.ID, "form-error-message")))

    # Проверяем, что сообщение об ошибке присутствует
    assert error_message.is_displayed()
    assert "Неверный код из SMS" in error_message.text

    # Проверяем, что URL не изменился и пользователь остался на странице ввода кода
    assert "reset-by-code" in browser.current_url

def test_unsuccessful_password_recovery_phone_invalid_password(browser):
    browser.get("https://b2c.passport.rt.ru/")

    forgot_password_link = browser.find_element(By.ID, "forgot-password")
    forgot_password_link.click()

    phone_input = browser.find_element(By.ID, "phone")
    phone_input.send_keys("ваш_номер_телефона")  # Замените на ваш реальный номер

    captcha_input = browser.find_element(By.ID, 'captcha')
    # Тут нужно ввести капчу, автоматизировать сложно. Пока пропускаем
    #  В РЕАЛЬНЫХ АВТОТЕСТАХ НУЖНО ИСПОЛЬЗОВАТЬ ДРУГОЙ ПОДХОД (например, обходить капчу, выключать ее, использовать мок-сервер и т.д.)
    time.sleep(5) #Даем время ввести капчу

    continue_button = browser.find_element(By.ID, 'reset-by-phone')
    continue_button.click()

    # Здесь нужно перехватить код из SMS. Реальный автоматический перехват SMS может быть сложным,
    # поэтому мы будем использовать time.sleep() + ручной ввод кода.
    #  В РЕАЛЬНЫХ АВТОТЕСТАХ НУЖНО ИСПОЛЬЗОВАТЬ ДРУГОЙ ПОДХОД (например, SMS API, мок-сервер и т.д.)
    time.sleep(30)  # Даем время получить код

    sms_code_input = browser.find_element(By.ID, "code")
    sms_code_input.send_keys("временный_код")  # Замените на ваш полученный код

    continue_button_2 = browser.find_element(By.ID, 'reset-by-code')
    continue_button_2.click()

    new_password_input = browser.find_element(By.ID, "password-new")
    new_password_input.send_keys("неверный_пароль") # Замените на невалидный пароль

    confirm_password_input = browser.find_element(By.ID, "password-confirm")
    confirm_password_input.send_keys("неверный_пароль")

    save_password_button = browser.find_element(By.ID, "reset-password-submit")
    save_password_button.click()

    # Ожидаем, что система не перенаправит пользователя и отобразит сообщение об ошибке
    wait = WebDriverWait(browser, 10)
    error_message = wait.until(EC.visibility_of_element_located((By.ID, "password-error-message")))

    # Проверяем, что сообщение об ошибке присутствует
    assert error_message.is_displayed()
    assert "Длина пароля должна быть не менее 8 символов" in error_message.text or "Пароль должен содержать только латинские буквы и цифры" in error_message.text

    # Проверяем, что URL не изменился и пользователь остался на странице ввода нового пароля
    assert "reset-password" in browser.current_url


def test_successful_password_recovery_email(browser):

    browser.get("https://b2c.passport.rt.ru/")

    forgot_password_link = browser.find_element(By.ID, "forgot-password")
    forgot_password_link.click()

    email_tab = browser.find_element(By.ID, "reset-by-email")
    email_tab.click()

    email_input = browser.find_element(By.ID, "email")
    email_input.send_keys("ваш_email")  # Замените на ваш реальный email

    captcha_input = browser.find_element(By.ID, 'captcha')

    # Тут нужно ввести капчу, автоматизировать сложно. Пока пропускаем
    time.sleep(5)  # Даем время ввести капчу

    continue_button = browser.find_element(By.ID, 'reset-by-email')
    continue_button.click()

    # Здесь нужно перехватить код из email.
    time.sleep(30)  # Даем время получить код

    email_code_input = browser.find_element(By.ID, "code")
    email_code_input.send_keys("временный_код")  # Замените на ваш полученный код

    continue_button_2 = browser.find_element(By.ID, 'reset-by-code')
    continue_button_2.click()

    new_password_input = browser.find_element(By.ID, "password-new")
    new_password_input.send_keys("новый_пароль")  # Замените на желаемый новый пароль

    confirm_password_input = browser.find_element(By.ID, "password-confirm")
    confirm_password_input.send_keys("новый_пароль")  # Замените на желаемый новый пароль

    save_password_button = browser.find_element(By.ID, "reset-password-submit")
    save_password_button.click()

    wait = WebDriverWait(browser, 10)
    wait.until(EC.url_contains("https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?session"))

    assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?session" in browser.current_url


def generate_random_phone_number():
    return '79' + str(random.randint(100000000, 999999999))


def test_successful_registration_new_phone(browser):

    browser.get("https://b2c.passport.rt.ru/")

    register_link = browser.find_element(By.ID, "kc-register")
    register_link.click()

    first_name_input = browser.find_element(By.NAME, "firstName")
    first_name_input.send_keys("Тест")

    last_name_input = browser.find_element(By.NAME, "lastName")
    last_name_input.send_keys("Тестов")

    region_select = browser.find_element(By.XPATH, "//div[@class='rt-select__arrow rt-select__arrow--no-label']")
    region_select.click()
    time.sleep(1)
    region_option = browser.find_element(By.XPATH, "//div[@class='rt-select__list-item' and contains(text(),'Москва')]")
    region_option.click()

    phone_input = browser.find_element(By.ID, "address")
    new_phone_number = generate_random_phone_number()  # Генерируем новый номер телефона
    phone_input.send_keys(new_phone_number)  # Замените на НОВЫЙ номер

    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys("TestPassword123")  # Замените на желаемый новый пароль

    password_confirm_input = browser.find_element(By.ID, "password-confirm")
    password_confirm_input.send_keys("TestPassword123")  # Замените на желаемый новый пароль

    register_button = browser.find_element(By.NAME, "register")
    register_button.click()

    # Даем время получить код
    time.sleep(30)

    sms_code_input = browser.find_element(By.ID, "code")
    sms_code_input.send_keys("временный_код")  # Замените на ваш полученный код

    confirm_button = browser.find_element(By.NAME, "confirm")
    confirm_button.click()

    wait = WebDriverWait(browser, 10)
    wait.until(EC.url_contains("https://b2c.passport.rt.ru/account_b2c/"))

    assert "account_b2c" in browser.current_url
    assert "Личный кабинет" in browser.page_source

def test_unsuccessful_registration_existing_email(browser):

    browser.get("https://b2c.passport.rt.ru/")

    register_link = browser.find_element(By.ID, "kc-register")
    register_link.click()

    first_name_input = browser.find_element(By.NAME, "firstName")
    first_name_input.send_keys("Тест")

    last_name_input = browser.find_element(By.NAME, "lastName")
    last_name_input.send_keys("Тестов")

    region_select = browser.find_element(By.XPATH, "//div[@class='rt-select__arrow rt-select__arrow--no-label']")
    region_select.click()
    time.sleep(1)
    region_option = browser.find_element(By.XPATH, "//div[@class='rt-select__list-item' and contains(text(),'Москва')]")
    region_option.click()

    email_input = browser.find_element(By.ID, "address")
    email_input.send_keys("ваш_email")  # Замените на ваш реальный email

    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys("TestPassword123") # Замените на желаемый новый пароль

    password_confirm_input = browser.find_element(By.ID, "password-confirm")
    password_confirm_input.send_keys("TestPassword123")

    register_button = browser.find_element(By.NAME, "register")
    register_button.click()

    wait = WebDriverWait(browser, 10)
    error_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "card-modal__title")))

    assert error_message.is_displayed()
    assert "Учетная запись с указанным email уже существует" in error_message.text

    # Проверяем, что URL не изменился и пользователь остался на странице регистрации
    assert "register" in browser.current_url


def test_cookie_check_authorization(browser_cookie):
    # Открываем страницу авторизации с заблокированными файлами cookie
    browser_cookie.get("https://b2c.passport.rt.ru/")

    # Проверяем, что отображается всплывающее окно с файлами cookie
    wait = WebDriverWait(browser_cookie, 10)
    cookie_popup = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "card-modal")))

    # Проверяем, что pop-up присутствует и содержит нужный текст
    assert cookie_popup.is_displayed()

    title = cookie_popup.find_element(By.CLASS_NAME, "card-modal__title")
    assert "Для корректной работы сайта необходимо включить поддержку cookie" == title.text

    hint = cookie_popup.find_element(By.CLASS_NAME, "card-modal__hint")
    assert "В вашем браузере отключено использование cookie, пожалуйста, включите их или воспользуйтесь другим браузером." == hint.text

    repeat_button = cookie_popup.find_element(By.CLASS_NAME, "rt-btn--orange")
    assert repeat_button.is_displayed()

    cookie_button = cookie_popup.find_element(By.CLASS_NAME, "rt-btn--gray")
    assert cookie_button.is_displayed()

def test_user_agreement(browser):

    browser.get("https://b2c.passport.rt.ru/")

    user_arg = browser.find_element(By.ID, "rt-auth-agreement-link")
    #
    assert user_arg.is_displayed() and user_arg.is_enabled(), "Кнопка неактивна"
    user_arg.click()
    assert "Публичная оферта о заключении Пользовательского соглашения на использование Сервиса «Ростелеком ID»" in user_arg.text
