from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import Curls
from locators import Locators
from data import Credentials


class TestTransitionViaMyAccountButton:
    def test_transition_via_my_account_button(self, driver):
    #Arrange
        driver.get(Curls.main_site)
        driver.find_element(*Locators.LOGIN_TO_YOUR_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL_LOGIN_PAGE).send_keys(*Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(*Credentials.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.MY_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.PROFILE))
    #Act
        driver.find_element(*Locators.EXIT_BUTTON).click()
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
    # Assert
        assert driver.current_url == Curls.login_page
        driver.quit()