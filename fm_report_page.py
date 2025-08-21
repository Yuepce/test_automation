from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
class FMReportPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.locators = {
            # "fund_services_tab":(By.XPATH,"//a[text()='Fund Services']"),
            "finance_tab": (By.XPATH, "//button[@id='sl-mega-menu-toggle-Finance']//span[contains(text(),'Finance')]"),
            "fund_movement_report_page_selector":(By.XPATH,"//span[contains(text(),'Fund Movement Report')]"),
            "fund_movement_report":(By.XPATH,"///h3[normalize-space()='Fund Movement Report']"),
            "from_date_picker":(By.XPATH,"//button[@aria-controls='relStartDate']"),
            "to_date_picker":(By.XPATH,"//button[@aria-controls='relEndDate']//span[@class='sl-icon sl-icon-calendar sl-icon_non-interactive']"),
            "disabled_export_btn":(By.XPATH,"//span[@class='sl-icon sl-icon-download sl-icon_non-interactive']/parent::*/parent::button[text()='Export']"),
            "today_btn":(By.XPATH,"//div[contains(@class,'react-datepicker__today-button')]"),
            "export_btn":(By.XPATH,"//button[text()='Export']"),
            "three_months_error_one":(By.XPATH,"//div[@class='notification-component']"),
            # "three_months_error_two":(By.XPATH,"//p[text()='Only 3 months is allowed'][2]"),
            "successful_pop_up":(By.XPATH,"//h2[text()='Fund Movement File generation is Completed. File is  exported to Downloads folder.']")
            }
    
    
    def click_fm_report_page(self):
        self.find_element(*self.locators['fund_movement_report_page_selector']).click()

    def click_finance(self):
        self.find_element(*self.locators['finance_tab']).click()
        
    # def click_fund_services(self):
    #     self.find_element(*self.locators['fund_services_tab']).click()

    def verify_from_date_picker(self):
        from_date_picker = self.find_element(*self.locators["from_date_picker"])
        return from_date_picker
    
    def verify_to_date_picker(self):
        to_date_picker = self.find_element(*self.locators["to_date_picker"])
        return to_date_picker
    
    def verify_disabled_export_btn(self):
        disabled_export_btn = self.find_element(*self.locators["disabled_export_btn"])
        return disabled_export_btn
    
    def click_from_date_picker(self):
        self.find_element(*self.locators['from_date_picker']).click()

    def click_to_date_picker(self):
        self.find_element(*self.locators['to_date_picker']).click()

    def click_today_btn(self):
        self.find_element(*self.locators['today_btn']).click()

    def click_export_btn(self):
        self.find_element(*self.locators['export_btn']).click()

    def verify_three_months_error_one(self):
        three_months_error_one = self.find_element(*self.locators["three_months_error_one"])
        return three_months_error_one.text
    
    def verify_three_months_error_two(self):
        three_months_error_two = self.find_element(*self.locators["three_months_error_two"])
        return three_months_error_two
    
    def verify_successful_pop_up(self):
        successful_pop_up = self.find_element(*self.locators["successful_pop_up"])
        return successful_pop_up

    
    
