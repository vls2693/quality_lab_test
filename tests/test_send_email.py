import time
from steps.main_page_steps import MainPageSteps
from constants.constants import *
import pytest


def test_send_email(browser, link=MAIN_PAGE, login=LOGIN, password=PASSWORD):
    # открываем браузер
    main_page = MainPageSteps(browser, url=link)
    main_page.open_browser_step()
    # авторизуемся валидными логином и паролем
    main_page.authorization_step(user_name=login, user_password=password)
    # отправляем письмо
    main_page.send_email_step(addressee=ADDRESSEE, text=MAIL_TEXT)
    time.sleep(1)
