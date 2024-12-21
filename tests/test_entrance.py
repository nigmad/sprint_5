
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import Curls
from locators import Locators
from data import Credentials


class TestEntranceViaLoginToYourAccountButton:
    def test_login_to_existing_account(self, driver):
    #Arrange
        driver.get(Curls.main_site)
        driver.find_element(*Locators.LOGIN_TO_YOUR_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL_LOGIN_PAGE).send_keys(*Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(*Credentials.password)
    #Act
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
    # Assert
        assert driver.current_url == Curls.main_site+ '/'
        driver.quit()


class TestEntranceViaMyAccountButton:
    def test_login_via_my_account_button(self, driver):
        # Arrange
        driver.get(Curls.main_site)
        driver.find_element(*Locators.MY_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL_LOGIN_PAGE).send_keys(*Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(*Credentials.password)
        # Act
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        # Assert
        assert driver.current_url == Curls.main_site + '/'
        driver.quit()



class TestEntranceViaRegFormEnterButton:
    def test_enter_via_registration_form_enter_button(self, driver):
        # Arrange
        driver.get(Curls.auth_endpoint)
        driver.find_element(*Locators.ENTER_VIA_REG_FORM).click()
        driver.find_element(*Locators.EMAIL_LOGIN_PAGE).send_keys(*Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(*Credentials.password)
        # Act
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        # Assert
        assert driver.current_url == Curls.main_site + '/'
        driver.quit()


class TestEntranceViaPasswordResetPage:
    def test_enter_via_password_reset_page(self, driver):
        # Arrange
        driver.get(Curls.password_reset_page)
        driver.find_element(*Locators.PASWORD_RESET_PAGE_ENTER_BUTTON).click()
        driver.find_element(*Locators.EMAIL_LOGIN_PAGE).send_keys(*Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(*Credentials.password)
        # Act
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        # Assert
        assert driver.current_url == Curls.main_site + '/'
        driver.quit()







