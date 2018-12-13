# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, uuid


class Tmp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.way2automation.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_tmp(self):

        username = uuid.uuid4;

        driver = self.driver
        driver.get(self.base_url + "/angularjs-protractor/webtables/")
        driver.find_element_by_xpath("//button[@type='add']").click()
        driver.find_element_by_name("FirstName").clear()
        driver.find_element_by_name("FirstName").send_keys("FName1")
        driver.find_element_by_name("LastName").clear()
        driver.find_element_by_name("LastName").send_keys("LName1")
        driver.find_element_by_name("UserName").clear()
        driver.find_element_by_name("UserName").send_keys(str(username))
        driver.find_element_by_name("Password").clear()
        driver.find_element_by_name("Password").send_keys("Pass1234")
        driver.find_element_by_name("optionsRadios").click()
        Select(driver.find_element_by_name("RoleId")).select_by_visible_text("Admin")
        driver.find_element_by_name("Email").clear()
        driver.find_element_by_name("Email").send_keys("admin@mail.com")
        driver.find_element_by_name("Mobilephone").clear()
        driver.find_element_by_name("Mobilephone").send_keys("0825555")
        driver.find_element_by_css_selector("button.btn.btn-success").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
