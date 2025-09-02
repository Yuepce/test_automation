from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.selenium_utils import take_screenshot
from selenium import webdriver
class HomePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.locators = {
            "search_box": (By.ID, "searchBox"),
            "login_btn":(By.XPATH,"//button[@type='button']"),
            "finance_tab": (By.XPATH, "//button[@id='sl-mega-menu-toggle-Finance']//span[contains(text(),'Finance')]"),
            # "payment_services_tab":(By.XPATH,"//a[text()='Payment Services']"),
            # "fund_services_tab":(By.XPATH,"//a[text()='Fund Services']"),
            "bto_page_selector":(By.XPATH,"//*[@title='Bank Transfer Overseas']"),
            "btl_page_selector":(By.XPATH,"//*[@title='Bank Transfer Local']"),
            "payment_viewer_page_selector":(By.XPATH,"//*[@title='Payment Viewer']"),
            "fund_movement_report_page_selector":(By.XPATH,"//*[@title='Fund Movement Report']"),
            "impf_home_page_title":(By.XPATH,"//*[text()='iMPF']"),
            "intermediary_change_tab":(By.XPATH,"//button[@id='sl-mega-menu-toggle-undefined']//span[contains(text(),'Intermediary')]"),
            "enquiry_platform_tab":(By.XPATH,"//button[@id='sl-mega-menu-toggle-undefined']//span[contains(text(),'Enquiry Platform')]"),
            "rebate_tab":(By.XPATH,"//button[@id='sl-mega-menu-toggle-undefined']//span[contains(text(),'Rebate')]"),
            "ealert_sunsurf_tab":(By.XPATH,"//a[text()='E-alert and SunSurf Consent Flag']"),
            "logout_btn":(By.XPATH,"//*[@id='sl-dropdown-account']/div/ul/li/button"),
            #"sign_out_account":(By.XPATH,"//div[contains(@aria-label,'Sign out')]"),
            "sign_out_account":(By.XPATH,"//img[@role='presentation']"),
            "profile_drop_down":(By.XPATH,"//*[@id='sl-dropdown-toggle-account']")
            }
   
    def enter_search(self,query):
        self.find_element(*self.locators["search_box"]).send_keys(query)
   
    def click_login_btn(self):
        self.find_element(*self.locators["login_btn"]).click()
 
    def click_logout_btn(self):
        self.find_element(*self.locators["logout_btn"]).click()
 
    def click_profile_drop_down(self):
        self.find_element(*self.locators["profile_drop_down"]).click()
 
    def click_sign_out_account(self):
        self.find_element(*self.locators["sign_out_account"]).click()
 
    def verify_login_page(self):
        login_btn = self.find_element(*self.locators["login_btn"])
        return login_btn
 
    def test_impf(self):
        impf = self.find_element(*self.locators["impf_home_page_title"])
        return impf.text
   
    def click_finance(self):
        self.find_element(*self.locators['finance_tab']).click()
 
    # def verify_payment_services_tab(self):
    #     ps_tab = self.find_element(*self.locators["payment_services_tab"])
    #     return ps_tab.text
   
    # def verify_fund_services_tab(self):
    #     fs_tab = self.find_element(*self.locators["fund_services_tab"])
    #     return fs_tab.text
   
    def verify_intermediary_change_tab(self):
        ic_tab = self.find_element(*self.locators["intermediary_change_tab"])
        return ic_tab.text
   
    def verify_enquiry_platform_tab(self):
        ep_tab = self.find_element(*self.locators["enquiry_platform_tab"])
        return ep_tab.text
   
    def verify_rebate_tab(self):
        rebate_tab = self.find_element(*self.locators["rebate_tab"])
        return rebate_tab.text
   
    # def verify_ealert_sunsurf_flag(self):
    #     ealert_flag = self.find_element(*self.locators["ealert_sunsurf_tab"])
    #     return ealert_flag.text
 
    def take_screenshot(self, filename):
        take_screenshot(self.driver, filename)
 
