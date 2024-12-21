from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import Curls
from locators import Locators
from data import Credentials


class TestTransitionFromMyAccountToConstructor:
    def test_transition_from_my_account_to_constructor(self, driver):
    #Arrange
        driver.get(Curls.main_site)
        driver.find_element(*Locators.LOGIN_TO_YOUR_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL_LOGIN_PAGE).send_keys(*Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(*Credentials.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.MY_ACCOUNT_BUTTON).click()
    #Act
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
    # Assert
        assert driver.current_url == Curls.main_site + '/'
        driver.quit()