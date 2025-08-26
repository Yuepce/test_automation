from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
class PaymentViewerPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.locators = {
            "payment_viewer_page": (By.XPATH, "//span[contains(text(),'Payment Viewer')]"),
            # "payment_services_tab":(By.XPATH,"//a[text()='Payment Services']"),
            "finance_tab": (By.XPATH, "//button[@id='sl-mega-menu-toggle-Finance']//span[contains(text(),'Finance')]"),
            "filter_btn":(By.XPATH,"//button[text()='Filter']"),
            "clear_filter_btn":(By.XPATH,"//button[text()='Clear Filter']"),
            "payment_viewer":(By.XPATH,"//h3[normalize-space()='Payment Viewer']"),
            "import_date":(By.XPATH,"//*[text()='Import Date']"),
            "account_type":(By.XPATH,"//*[text()='Account Type']"), # April added
            "id_er_member":(By.XPATH,"//*[text()='MPF ID of ER / Member']"),
            "mpf_account_no":(By.XPATH,"//*[text()='MPF Account No']"),
            "payment_method":(By.XPATH,"//*[text()='Payment Method']"),
            # "app_ref_no":(By.XPATH,"//*[text()='Application Ref No']"), # April changed
            "end_to_end_id":(By.XPATH,"//*[text()='End to End ID']"),
            "payment_out_ref_no":(By.XPATH,"//*[text()='Payment Out Ref No']"),
            "expected_payment_issue_date":(By.XPATH,"//*[text()='Expected Payment Issue Date']"),
            "bank_payment_ex_date":(By.XPATH,"//*[text()='Bank Payment File Exported Date']"),
            "cheque_issue_date":(By.XPATH,"//*[text()='Cheque Issue Date']"),
            "dealing_date":(By.XPATH,"//*[text()='Dealing Date']"), # April added
            "cheque_no":(By.XPATH,"//*[text()='Cheque no / e-Payment Identifier No']"),
            "tran_type":(By.XPATH,"//*[text()='Transaction Type']"),
            "bank_cd":(By.XPATH,"//*[text()='Bank Code']"),
            "bank_acc_no":(By.XPATH,"//*[text()='Bank Account No']"),
            "swift_cd":(By.XPATH,"//*[text()='Swift Code']"),
            "payee":(By.XPATH,"//*[text()='Payee']"),
            "payment":(By.XPATH,"//*[text()='Payment in HKD']"),
            "target_currency":(By.XPATH,"//*[text()='Target Currency']"),
            "status":(By.XPATH,"//*[text()='Status']"),
            "reissuance":(By.XPATH,"//*[text()='Reissuance Indicator']"),
            "payment_send_out_date":(By.XPATH,"//*[text()='Payment Send Out Date']"),
            "reject_reason":(By.XPATH,"//*[text()='Reject Reason']"),
            "reject_reason_other":(By.XPATH,"//*[text()='Reject Reason (Other)']"),
            "returned_mail":(By.XPATH,"//*[text()='Returned Mail']"),
            "info":(By.XPATH,"//*[text()='Info']"),
            "payment_out_ref":(By.XPATH,"//tbody/tr[1]/td[7]"), # April changed
            }
    
    def click_payment_viewer_page(self):
        self.find_element(*self.locators['payment_viewer_page']).click()

    # def click_payment_services(self):
    #     self.find_element(*self.locators['payment_services_tab']).click()

    def click_finance(self):
        self.find_element(*self.locators['finance_tab']).click()

    def verify_filter_btn(self):
        filter_btn = self.find_element(*self.locators["filter_btn"])
        return filter_btn
    
    def verify_payment_out_ref(self):
        payment_out_ref = self.find_element(*self.locators["payment_out_ref"])
        return payment_out_ref.text
    
    def verify_clear_filter_btn(self):
        clear_filter_btn = self.find_element(*self.locators["clear_filter_btn"])
        return clear_filter_btn
    
    def verify_payment_viewer(self):
        payment_viewer = self.find_element(*self.locators["payment_viewer"])
        return payment_viewer
    
    def verify_import_date(self):
        import_date = self.find_element(*self.locators["import_date"])
        return import_date
    
    # April added
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
    
    def verify_end_to_end_id(self):
        end_to_end_id = self.find_element(*self.locators["end_to_end_id"])
        return end_to_end_id
    
    def verify_payment_out_ref_no(self):
        payment_out_ref_no = self.find_element(*self.locators["payment_out_ref_no"])
        return payment_out_ref_no
    
    def verify_expected_payment_issue_date(self):
        expected_payment_issue_date = self.find_element(*self.locators["expected_payment_issue_date"])
        return expected_payment_issue_date
    
    def verify_cheque_issue_date(self):
        cheque_issue_date = self.find_element(*self.locators["cheque_issue_date"])
        return cheque_issue_date
    
    # April added
    def verify_dealing_date(self):
        dealing_date = self.find_element(*self.locators["dealing_date"])
        return dealing_date
    
    def verify_bank_payment_ex_date(self):
        bank_payment_ex_date = self.find_element(*self.locators["bank_payment_ex_date"])
        return bank_payment_ex_date
    
    def verify_cheque_no(self):
        cheque_no = self.find_element(*self.locators["cheque_no"])
        return cheque_no
    
    def verify_tran_type(self):
        tran_type = self.find_element(*self.locators["tran_type"])
        return tran_type
    
    def verify_bank_cd(self):
        bank_cd = self.find_element(*self.locators["bank_cd"])
        return bank_cd
    
    def verify_bank_acc_no(self):
        bank_acc_no = self.find_element(*self.locators["bank_acc_no"])
        return bank_acc_no
    
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
    
    def verify_payment_send_out_date(self):
        payment_send_out_date = self.find_element(*self.locators["payment_send_out_date"])
        return payment_send_out_date
    
    def verify_reject_reason(self):
        reject_reason = self.find_element(*self.locators["reject_reason"])
        return reject_reason
    
    def verify_reject_reason_other(self):
        reject_reason_other = self.find_element(*self.locators["reject_reason_other"])
        return reject_reason_other
    
    def verify_returned_mail(self):
        returned_mail = self.find_element(*self.locators["returned_mail"])
        return returned_mail
    
    def verify_target_currency(self):
        target_currency = self.find_element(*self.locators["target_currency"])
        return target_currency
    
    def verify_info(self):
        info = self.find_element(*self.locators["info"])
        return info
