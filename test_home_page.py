import pytest
from pages.home_page import HomePage
from selenium import webdriver
import time
import unittest
import utils.excel_utils as ExcelUtils
import os
 
#pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver.quit()
 
@pytest.mark.TC0001
@pytest.mark.login
def test_login(browser, request):
    data = ExcelUtils.get_data('TC0001')
   
    if data:
        # Accessing the 'Description' value
        description = data.get('Test Case Description')
        print(f"Test Case Description: {description}")
    else:
        print("No data found for the specified ID.")
    request.node.driver = browser
    home_page = HomePage(browser)
    browser.get(data.get('URL'))
    print("this is the test  case 0001")
    # assert False
    home_page.click_login_btn()
    time.sleep(10)
   
    impf_title = home_page.test_impf()
    home_page.click_finance()
    # ps_tab = home_page.verify_payment_services_tab()
    # fs_tab = home_page.verify_fund_services_tab()
    ic_tab = home_page.verify_intermediary_change_tab()
    ep_tab = home_page.verify_enquiry_platform_tab()
    rebate_tab = home_page.verify_rebate_tab()
    # ealert_flag = home_page.verify_ealert_sunsurf_flag()
    print("[CP: Get iMPF Page Title: ]"+ impf_title)
    assert impf_title == "iMPF"
    assert ic_tab == "Intermediary"
    assert ep_tab == "Enquiry Platform"
    assert rebate_tab == "Rebate"
    # assert ps_tab == "Payment Services"
    # assert fs_tab == "Fund Services"
    # assert ealert_flag == "E-alert and SunSurf Consent Flag"
    screenshot_path = os.path.join(os.getcwd()+"\screenshots", "TC0001.png")
    request.node.driver.save_screenshot(screenshot_path)
    request.node.add_report_section(
        'test',
        'Screenshot',
        f'<img src="{screenshot_path}">')
   
 
@pytest.mark.TC0013
@pytest.mark.logout  
def test_logout(browser, request):
    data = ExcelUtils.get_data('TC0013')
    if data:
        # Accessing the 'Description' value
        description = data.get('Test Case Description')
        print(f"Test Case Description: {description}")
    else:
        print("No data found for the specified ID.")
    request.node.driver = browser
    home_page = HomePage(browser)
    browser.get(data.get('URL'))
    print("this is the test  case 0013")
    home_page.click_login_btn()
    time.sleep(10)
    home_page.click_profile_drop_down()
    home_page.click_logout_btn()
    home_page.click_sign_out_account()
    time.sleep(2)
    screenshot_path = os.path.join(os.getcwd()+"\screenshots", "TC0013.png")
    request.node.driver.save_screenshot(screenshot_path)
    request.node.add_report_section(
        'test',
        'Screenshot',
        f'<img src="{screenshot_path}">')
    assert home_page.verify_login_page().is_displayed()
