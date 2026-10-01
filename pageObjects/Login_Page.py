

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Login_Page_Class:
    text_email_id="email"
    text_Password_id="password"
    login_button_class_name="btn-primary"
    link_menu_xpath="//a[@role='button']"
    link_logout_xpath="//a[normalize-space()='Logout']"


    def __init__(self,driver):
       self.driver = driver


    def enter_email(self,email):
       self.driver.find_element(By.ID,self.text_email_id).send_keys(email)

    def enter_password(self,password):
       self.driver.find_element(By.ID,self.text_Password_id).send_keys(password)

    def click_submit(self):
        self.driver.find_element(By.CLASS_NAME,self.login_button_class_name).click()

    def click_menu(self):
        self.driver.find_element(By.XPATH,self.link_menu_xpath).click()

    def click_logout(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.link_logout_xpath)
            )
        ).click()

    def verify_menu(self):
        try:
            WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[@role='button']")))
            return "Pass"
        except:
            return "Fail"



