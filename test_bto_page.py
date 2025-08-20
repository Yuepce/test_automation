import pytest
from pages.bto_page import BtoPage
from pages.home_page import HomePage
from selenium import webdriver
import time
import tests.test_home_page as test_home_page
import psycopg2
import utils.excel_utils as ExcelUtils
import os
#pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver.quit()

@pytest.mark.TC0002
@pytest.mark.validateBTO
def test_bto_page(browser,request):
    data = ExcelUtils.get_data('TC0002')
    if data:
        # Accessing the 'Description' value
        description = data.get('Test Case Description')
        print(f"Test Case Description: {description}")
    else:
        print("No data found for the specified ID.")
    request.node.driver = browser
    home_page = HomePage(browser)
    browser.get(data.get('URL'))
    home_page.click_login_btn()
    time.sleep(10)
    home_page.take_screenshot("login successfully.png")
    print("this is the test case 0002")
    bto_page = BtoPage(browser)
    bto_page.click_finance()
    # bto_page.click_payment_services()
    bto_page.click_bto_page()
    time.sleep(5)
    assert bto_page.verify_filter_btn().is_displayed()
    assert bto_page.verify_clear_filter_btn().is_displayed()
    # assert bto_page.verify_update_overseas_bank_transfer_details().is_displayed()
    assert bto_page.verify_import_date().is_displayed()
    assert bto_page.verify_account_type().is_displayed()
    assert bto_page.verify_id_er_member().is_displayed()
    assert bto_page.verify_mpf_account_no().is_displayed()
    assert bto_page.verify_payment_method().is_displayed()
    # assert bto_page.verify_app_ref_no().is_displayed()
    assert bto_page.verify_payment_out_ref_no().is_displayed()
    assert bto_page.verify_expected_payment_issue_date().is_displayed()
    assert bto_page.verify_swift_cd().is_displayed()
    assert bto_page.verify_payee().is_displayed()
    assert bto_page.verify_payment().is_displayed()
    assert bto_page.verify_status().is_displayed()
    assert bto_page.verify_dealing_date().is_displayed()
    assert bto_page.verify_reissuance().is_displayed()
    assert bto_page.verify_target_currency().is_displayed()
    assert bto_page.verify_action().is_displayed()
    screenshot_path = os.path.join(os.getcwd()+"\screenshots", "TC0002.png")
    request.node.driver.save_screenshot(screenshot_path)
    request.node.add_report_section(
        'test',
        'Screenshot',
        f'<img src="{screenshot_path}">')

@pytest.mark.TC0003
@pytest.mark.fetchDBValidateBTO
def test_fetch_db_validate_bto(browser,request):
    data = ExcelUtils.get_data('TC0003')
    if data:
        # Accessing the 'Description' value
        description = data.get('Test Case Description')
        print(f"Test Case Description: {description}")
    else:
        print("No data found for the specified ID.")
    request.node.driver = browser
    home_page = HomePage(browser)
    check_record = 0
    browser.get(data.get('URL'))
    home_page.click_login_btn()
    time.sleep(10)
    home_page.take_screenshot("login successfully.png")
    print("this is the test case 0003")
    bto_page = BtoPage(browser)
    # bto_page.click_payment_services()
    bto_page.click_finance()
    bto_page.click_bto_page()
    time.sleep(5)
    connection = psycopg2.connect(database=data.get('Database'),user=data.get('User'),password=data.get('Password'),host=data.get('Host'),port=int(data.get('Port')))
    cursor = connection.cursor()
    cursor.execute(data.get('SQL'))
    # Fetch all rows from database
    record = cursor.fetchall()
    assert bto_page.verify_payment_out_ref() in record[check_record]
    print("data match for BTO Page")
    screenshot_path = os.path.join(os.getcwd()+"\screenshots", "TC0003.png")
    request.node.driver.save_screenshot(screenshot_path)
    request.node.add_report_section(
        'test',
        'Screenshot',
        f'<img src="{screenshot_path}">')
