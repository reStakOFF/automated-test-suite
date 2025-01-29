from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import unittest
import time
import HtmlTestRunner
import os

class TestAutorization(unittest.TestCase):
    def setUp(self):
        # Инициализируем драйвер (Chrome)
        chrome_options = Options()
        
        prefs = {
            "profile.managed_default_content_settings.images": 2,  # Отключение изображений
            "profile.managed_default_content_settings.stylesheet": 2,  # Отключение CSS
            #"profile.managed_default_content_settings.javascript": 2,  # Отключение JavaScript
        }
        chrome_options.add_experimental_option("prefs",prefs)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(5) # Неявное ожидание элементов.
        self.driver.get("https://small-games.info/")
        
    def test_autorization(self):
        driver = self.driver
        #Поиск поля для ввода логина и ввод значения 
        username_field = driver.find_element(By.NAME, "login").send_keys("aleks98")
        #Поиск поля для ввода пароля и ввод значения
        password_field = driver.find_element(By.NAME, "pass").send_keys("aleks98")
        #Поиск кнопки отправки формы и клик по ней
        button_send_form = driver.find_element(By.NAME, "btnOk").click()
        #Ждем некоторое время для загрузки страницы после авторизации
        time.sleep(3)
        
        #Проверяем, что авторизация прошла успешно
        #Проверяем наличие элемента, который отображается только после авторизации
        try:
            succes_element = driver.find_element(By.LINK_TEXT, "aleks98 [3|41]")
            self.assertTrue(succes_element.is_displayed())
            print("Autorization succes!")
        except Exception as e:
            print(f"Authorization error: {e}")
            self.fail("Authorization failed")
            
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    # Запуск теста с генерацией HTML-отчета
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="reports",  # Папка для сохранения отчета
            report_name="authorization_test_report",  # Имя отчета
            open_in_browser=True  # Открыть отчет в браузере после завершения
        )
    )