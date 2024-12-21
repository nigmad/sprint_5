from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import Curls
from locators import Locators
from selenium.webdriver.common.by import By


class TestConstructorTransitionToBuns:
    def test_transition_from_constructorT_to_buns(self, driver):
    #Arrange
        driver.get(Curls.main_site)
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        driver.find_element(*Locators.SOUS_BUTTON).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.SOUS_SECTION_TEXT))
    #Act
        driver.find_element(*Locators.BUNS_BUTTON).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.BUNS_SECTION_TEXT))
    # Assert
        active_tab = driver.find_element(By.CSS_SELECTOR, "[class*='tab_tab_type_current']")
        active_tab_text = active_tab.text
        assert "Булки" in active_tab_text
        driver.quit()


class TestConstructorTransitionToSous:
    def test_transition_from_constructorT_to_sous(self, driver):
    #Arrange
        driver.get(Curls.main_site)
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

    #Act
        driver.find_element(*Locators.SOUS_BUTTON).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.SOUS_SECTION_TEXT))
    # Assert
        active_tab = driver.find_element(By.CSS_SELECTOR, "[class*='tab_tab_type_current']")
        active_tab_text = active_tab.text
        assert "Соусы" in active_tab_text
        driver.quit()



class TestConstructorTransitionToFilling:
    def test_transition_from_constructorT_to_filling(self, driver):
    #Arrange
        driver.get(Curls.main_site)
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

    #Act
        driver.find_element(*Locators.FILLING_BUTTON).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.FILLING_SECTION_TEXT))
    # Assert
        active_tab = driver.find_element(By.CSS_SELECTOR, "[class*='tab_tab_type_current']")
        active_tab_text = active_tab.text
        assert "Начинки" in active_tab_text
        driver.quit()