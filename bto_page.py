from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
class BtoPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.locators = {
            "bto_page": (By.XPATH, "//span[contains(text(),'Bank Transfer Overseas')]"),
            # "payment_services_tab":(By.XPATH,"//a[text()='Payment Services']"),
            "finance_tab": (By.XPATH, "//button[@id='sl-mega-menu-toggle-Finance']//span[contains(text(),'Finance')]"),
            "filter_btn":(By.XPATH,"//button[text()='Filter']"),
            "clear_filter_btn":(By.XPATH,"//button[text()='Clear Filter']"),
            # "update_overseas_bank_transfer_details":(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[15]/div[1]/span[1]/button[1]/span[1]"),
            "import_date":(By.XPATH,"//*[text()='Import Date']"),
            "account_type":(By.XPATH,"//*[text()='Account Type']"),
            "id_er_member":(By.XPATH,"//*[text()='MPF ID of ER / Member']"),
            "mpf_account_no":(By.XPATH,"//*[text()='MPF Account No']"),
            "payment_method":(By.XPATH,"//*[text()='Payment Method']"),
            # "app_ref_no":(By.XPATH,"//*[text()='Application Ref No']"),
            "payment_out_ref_no":(By.XPATH,"//*[text()='Payment Out Ref No']"),
            "expected_payment_issue_date":(By.XPATH,"//*[text()='Expected Payment Issue Date']"),
            "dealing_date":(By.XPATH,"//*[text()='Dealing Date']"),
            "swift_cd":(By.XPATH,"//*[text()='Swift Code']"),
            "payee":(By.XPATH,"//*[text()='Payee']"),
            "payment":(By.XPATH,"//*[text()='Payment in HKD']"),
            "status":(By.XPATH,"//*[text()='Status']"),
            "reissuance":(By.XPATH,"//*[text()='Reissuance Indicator']"),
            "target_currency":(By.XPATH,"//*[text()='Target Currency']"),
            "action":(By.XPATH,"//*[text()='Actions']"),
            "payment_out_ref":(By.CSS_SELECTOR,"tbody tr:nth-child(1) td:nth-child(6) div:nth-child(1)")
            }
    
    def click_bto_page(self):
        self.find_element(*self.locators['bto_page']).click()

    def click_finance(self):
        self.find_element(*self.locators['finance_tab']).click()

    # def click_payment_services(self):
    #     self.find_element(*self.locators['payment_services_tab']).click()

    def verify_filter_btn(self):
        filter_btn = self.find_element(*self.locators["filter_btn"])
        return filter_btn
    
    def verify_payment_out_ref(self):
        payment_out_ref = self.find_element(*self.locators["payment_out_ref"])
        return payment_out_ref.text
    
    def verify_clear_filter_btn(self):
        clear_filter_btn = self.find_element(*self.locators["clear_filter_btn"])
        return clear_filter_btn
    
    # def verify_update_overseas_bank_transfer_details(self):
    #     update_overseas_bank_transfer_details = self.find_element(*self.locators["update_overseas_bank_transfer_details"])
    #     return update_overseas_bank_transfer_details
    
    def verify_import_date(self):
        import_date = self.find_element(*self.locators["import_date"])
        return import_date
    
    def verify_account_type(self):
        account_type = self.find_element(*self.locators["account_type"])
        return account_type

    def verify_id_er_member(self):
        id_er_member = self.find_element(*self.locators["id_er_member"])
        return id_er_member
    
    def verify_mpf_account_no(self):
        mpf_account_no = self.find_element(*self.locators["mpf_account_no"])
        return mpf_account_no
    
    def verify_payment_method(self):
        payment_method = self.find_element(*self.locators["payment_method"])
        return payment_method
    
    # def verify_app_ref_no(self):
    #     app_ref_no = self.find_element(*self.locators["app_ref_no"])
    #     return app_ref_no
    
    def verify_payment_out_ref_no(self):
        payment_out_ref_no = self.find_element(*self.locators["payment_out_ref_no"])
        return payment_out_ref_no
    
    def verify_expected_payment_issue_date(self):
        expected_payment_issue_date = self.find_element(*self.locators["expected_payment_issue_date"])
        return expected_payment_issue_date
    
    def verify_dealing_date(self):
        dealing_date = self.find_element(*self.locators["dealing_date"])
        return dealing_date
    
    def verify_swift_cd(self):
        swift_cd = self.find_element(*self.locators["swift_cd"])
        return swift_cd
    
    def verify_payee(self):
        payee = self.find_element(*self.locators["payee"])
        return payee
    
    def verify_payment(self):
        payment = self.find_element(*self.locators["payment"])
        return payment
    
    def verify_status(self):
        status = self.find_element(*self.locators["status"])
        return status
    
    def verify_reissuance(self):
        reissuance = self.find_element(*self.locators["reissuance"])
        return reissuance
    
    def verify_target_currency(self):
        target_currency = self.find_element(*self.locators["target_currency"])
        return target_currency
    
    def verify_action(self):
        action = self.find_element(*self.locators["action"])
        return action
    
