
import pytest
from faker import Faker
from pageObjects.Login_Page import Login_Page_Class
from pageObjects.Registration_Page import Registration_Page_Class


@pytest.mark.usefixtures("browser_setup") # new
class Test001:
    driver = None # new
    def test_Credkart_URL_001(self):
        self.driver.get("https://automation.credence.in")
        if self.driver.title == "CredKart":
            self.driver.save_screenshot(".\\Screenshots\\CredKart_Home_Page_pass.png")
        else :
            self.driver.save_screenshot(".\\Screenshots\\CredKart_Home_Page_fail.png")
            assert False




    def test_Credkart_login_002(self):
        self.driver.get("https://automation.credence.in/login")
        self.lp = Login_Page_Class(self.driver)  #object create kara hai.

        # email=self.driver.find_element(By.ID,"email")
        # email.send_keys("CredenceTest_5005@credence.in")

        self.lp.enter_email("CredenceTest_5005@credence.in")

        # password= self.driver.find_element(By.ID, "password")
        # password.send_keys("Password@123")

        self.lp.enter_password("Password@123")

        # login_button=self.driver.find_element(By.CLASS_NAME,"btn-primary")
        # login_button.click()

        self.lp.click_submit()


        # try:
        #     WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[@role='button']")))
        #     self.driver.save_screenshot(".\\Screenshots\\Login_success_screenshot.png")
        #
        #     self.driver.find_element(By.XPATH, "//a[@role='button']").click()
        #
        #     self.driver.find_element(By.XPATH, "/html/body/header/nav/div/div[2]/ul[2]/li[3]/ul/li/a").click()
        #     print("Login Success")
        # except:
        #     self.driver.save_screenshot(".\\Screenshots\\Login_failure_screenshot.png")
        #     print("Login Failure")
        #     assert False

        if self.lp.verify_menu()=="Pass":
            self.lp.click_menu()
            self.lp.click_logout()
            self.driver.save_screenshot(".\\Screenshots\\Login_pass_screenshot.png")

        else:
            self.driver.save_screenshot(".\\Screenshots\\Login_failure_screenshot.png")
            assert False






    def test_Credkart_Registration_003(self):
        self.driver.get("https://automation.credence.in/register")

        name_data = Faker().name()
        print(f"name_data-->{name_data}")

        email_data = Faker().email()
        print(f"email_data-->{email_data}")

        self.rp=Registration_Page_Class(self.driver)
        self.lp= Login_Page_Class(self.driver)

        # Enter Name
        # self.driver.find_element(By.ID, "name").send_keys(name_data)
        self.rp.enter_name(name_data)

        # Enter Email
        # self.driver.find_element(By.ID, "email").send_keys(email_data)
        self.lp.enter_email(email_data)

        # Enter Password
        # self.driver.find_element(By.ID, "password").send_keys("Password@123")
        self.lp.enter_password("Password@123")

        # Enter Confirm Password
        # self.driver.find_element(By.ID, "password-confirm").send_keys("Password@123")
        self.rp.enter_confirm_password("Password@123")

        # Click Register Button
        # self.driver.find_element(By.CLASS_NAME, "btn-primary").click()
        self.lp.click_submit()



        if  self.lp.verify_menu()=="Pass":
            self.lp.click_menu()
            self.lp.click_logout()
            self.driver.save_screenshot(".\\Screenshots\\Registration_pass_screenshot.png")

        else:
            self.driver.save_screenshot(".\\Screenshots\\Registration_failure_screenshot.png")
            assert False




# pytest -v -s -n auto --html=HTMLReports/my_report.html --browser chrome