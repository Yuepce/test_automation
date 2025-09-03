import pytest
import pytest_html
from pages.cheque_page import ChequePage
from pages.home_page import HomePage
from selenium import webdriver
import time
import tests.test_home_page as test_home_page
import psycopg2
import utils.excel_utils as ExcelUtils
from selenium.webdriver.common.by import By
import os

#pytest.fixture
def browser():
    driver = webdriver.Chrome
    yield driver.quit()

@pytest.mark.TC0006
@pytest.mark.validateChequePage
def test_cheque_page(browser,request):
    data = ExcelUtils.get_data('TC0006')
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
    print("this is the test case 0006")
    cheque_page = ChequePage(browser)
    # cheque_page.click_payment_services()
    cheque_page.click_finance()
    cheque_page.click_cheque_page()
    time.sleep(5)
    assert cheque_page.verify_filter_btn().is_displayed()
    assert cheque_page.verify_clear_filter_btn().is_displayed()
    assert cheque_page.verify_update_cheque_details().is_displayed()
    # assert cheque_page.verify_import_date().is_displayed()
    # assert cheque_page.verify_account_type().is_displayed() #newly added
    # assert cheque_page.verify_id_er_member().is_displayed()
    # assert cheque_page.verify_mpf_account_no().is_displayed()
    # assert cheque_page.verify_payment_method().is_displayed()
    # # assert cheque_page.verify_app_ref_no().is_displayed()
    # assert cheque_page.verify_end_to_end_id().is_displayed()
    # assert cheque_page.verify_payment_out_ref_no().is_displayed()
    # assert cheque_page.verify_expected_payment_issue_date().is_displayed()
    # assert cheque_page.verify_dealing_date().is_displayed() #newly added
    # assert cheque_page.verify_cheque_no().is_displayed()
    # assert cheque_page.verify_tran_type().is_displayed()
    # assert cheque_page.verify_payee().is_displayed()
    # assert cheque_page.verify_payment().is_displayed()
    # assert cheque_page.verify_status().is_displayed()
    # assert cheque_page.verify_reissuance().is_displayed()
    # assert cheque_page.verify_target_currency().is_displayed()
    cheque_page.click_rows_per_page()
    time.sleep(2)
    cheque_page.hundred_rows_per_page()
    time.sleep(5)
    showing_results = cheque_page.showing_results()
    # time.sleep(5)
    for column_index, column_function in enumerate(cheque_page.sorting_column_list, start = 1):
        assert column_function(cheque_page).is_displayed()
        print(column_function(cheque_page).text, end = " ")
        column_function(cheque_page).click()
        sorted_first_value = cheque_page.find_element(By.XPATH, "//tbody/tr[1]/td[{}]".format(column_index)).text
        sorted_largest_value_on_page = cheque_page.find_element(By.XPATH, "//tbody/tr[{}]/td[{}]".format(int(showing_results),column_index)).text
        assert sorted_first_value <= sorted_largest_value_on_page, f"{column_function(cheque_page).text} Sorting Failed"
        print(f"Sorted first value {"None" if sorted_first_value == "" else sorted_first_value} <= Sorted max value on page ({showing_results}th row) {"None" if sorted_largest_value_on_page == "" else sorted_largest_value_on_page}")
    assert cheque_page.verify_action().is_displayed()
    screenshot_path = os.path.join(os.getcwd()+"\screenshots", "TC0006.png")
    request.node.driver.save_screenshot(screenshot_path)
    request.node.add_report_section(
        'test',
        'Screenshot',
        f'<img src="{screenshot_path}">')

@pytest.mark.TC0007
@pytest.mark.fetchDBValidateCheque
def test_fetch_db_validate_cheque(browser,request):
    data = ExcelUtils.get_data('TC0007')
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
    print("this is the test case 0007")
    cheque_page = ChequePage(browser)
    # cheque_page.click_payment_services()
    cheque_page.click_finance()
    cheque_page.click_cheque_page()
    time.sleep(5)
    connection = psycopg2.connect(database=data.get('Database'),user=data.get('User'),password=data.get('Password'),host=data.get('Host'),port=int(data.get('Port')))
    cursor = connection.cursor()
    cursor.execute(data.get('SQL'))
    # Fetch all rows from database
    record = cursor.fetchall()
    assert cheque_page.verify_payment_out_ref() in record[check_record]
    print("data match for Cheque Page")
    screenshot_path = os.path.join(os.getcwd()+"\screenshots", "TC0007.png")
    request.node.driver.save_screenshot(screenshot_path)
    request.node.add_report_section(
        'test',
        'Screenshot',
        f'<img src="{screenshot_path}">')

