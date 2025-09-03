import pytest
from pages.bto_page import BtoPage
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
    bto_page.click_rows_per_page()
    time.sleep(2)
    bto_page.hundred_rows_per_page()
    time.sleep(5)
    showing_results = bto_page.showing_results()
    for column_index, column_function in enumerate(bto_page.sorting_column_list, start = 1):
        assert column_function(bto_page).is_displayed()
        print(column_function(bto_page).text, end = " ")
        column_function(bto_page).click()
        sorted_first_value = bto_page.find_element(By.XPATH, "//tbody/tr[1]/td[{}]".format(column_index)).text
        sorted_largest_value_on_page = bto_page.find_element(By.XPATH, "//tbody/tr[{}]/td[{}]".format(int(showing_results),column_index)).text
        assert sorted_first_value <= sorted_largest_value_on_page, f"{column_function(bto_page).text} Sorting Failed"
        print(f"Sorted first value {"None" if sorted_first_value == "" else sorted_first_value} <= Sorted max value on page ({showing_results}th row) {"None" if sorted_largest_value_on_page == "" else sorted_largest_value_on_page}")
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
