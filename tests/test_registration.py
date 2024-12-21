from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import Curls
from locators import Locators
from helper import generate_registration_data

class TestRegistrationWithNewCredentials:

    def test_success_registration(self, driver):
        # Arrange
        driver.get(Curls.auth_endpoint)
        name, email, password = generate_registration_data()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        # Act
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_FORM))
        # Assert
        assert driver.current_url == Curls.login_page
        driver.quit()



class TestRegistrationIncorrectPasswordFailed:

    def test_incorrect_password_registration(self, driver):
        # Arrange
        driver.get(Curls.auth_endpoint)
        driver.find_element(*Locators.NAME).send_keys("name")
        driver.find_element(*Locators.EMAIL).send_keys("abc@email.com")
        driver.find_element(*Locators.PASSWORD).send_keys("1")

        # Act
        driver.find_element(*Locators.REG_BUTTON).click()

        # Assert:
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.ERROR_MESSAGE))
        assert driver.current_url == Curls.auth_endpoint
        driver.quit()






