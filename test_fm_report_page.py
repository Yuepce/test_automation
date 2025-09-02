import pytest
from pages.fm_report_page import FMReportPage
from pages.home_page import HomePage
from selenium import webdriver
import time
import tests.test_home_page as test_home_page
import psycopg2
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.base_page import BasePage
import utils.excel_utils as ExcelUtils
import os

# April added:
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import calendar

#pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver.quit()

@pytest.mark.TC0010
@pytest.mark.validateFundReport
def test_fm_report_page(browser,request):
    data = ExcelUtils.get_data('TC0010')
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
    print("this is the test case 0010")
    fm_report_page = FMReportPage(browser)
    # fm_report_page.click_fund_services()
    fm_report_page.click_finance()
    fm_report_page.click_fm_report_page()
    time.sleep(5)
    assert fm_report_page.verify_from_date_picker().is_displayed()
    assert fm_report_page.verify_to_date_picker().is_displayed()
    assert fm_report_page.verify_disabled_export_btn().is_displayed()
    screenshot_path = os.path.join(os.getcwd()+"screenshots", "TC0010.png")
    request.node.driver.save_screenshot(screenshot_path)
    request.node.add_report_section(
        'test',
        'Screenshot',
        f'<img src="{screenshot_path}">')
    

@pytest.mark.TC0011
@pytest.mark.check3monthsValidation
def test_check_three_months_validation(browser,request):
    data = ExcelUtils.get_data('TC0011')
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
    fm_report_page = FMReportPage(browser)
    # fm_report_page.click_fund_services()
    fm_report_page.click_finance()
    fm_report_page.click_fm_report_page()
    time.sleep(5)

    # current_date = datetime.now()
    # three_months_ago = current_date - relativedelta(months=3)
    # year = three_months_ago.year
    # month = three_months_ago.strftime("%b")
    # day = three_months_ago.day

    # 提取年月日
    target_date = datetime.now()
    # test data： target_date = datetime(2025, 1, 30)
    three_months_ago = target_date - relativedelta(months=3)
    year_text = str(three_months_ago.year)
    month_text = three_months_ago.strftime("%b")  # 获取月份缩写，比如 'Jun'
    day_text = str(three_months_ago.day)

    fm_report_page.click_from_date_picker()
    fm_report_page.click_date_picker_day_to_month_to_year()
    fm_report_page.click_date_picker_day_to_month_to_year()

    # # Test
    # year_field = browser.find_element(By.XPATH, "//td[normalize-space()='2025']")
    # year_field.click()
    # month_field = browser.find_element(By.XPATH, "//td[normalize-space()='Jun']")
    # month_field.click()
    # # day_field = browser.find_element(By.XPATH, "//td[normalize-space()='2']")
    # day_field = browser.find_element(By.XPATH, "//td[@class='current-month-cell '][normalize-space()='2']")
    # day_field.click()

    # Original
    # year_field = browser.find_element(By.XPATH, "//td[normalize-space()='{}']".format(year))
    # year_field.click()
    # month_field = browser.find_element(By.XPATH, "//td[normalize-space()='{}']".format(month))
    # month_field.click()
    # day_field = browser.find_element(By.XPATH, "(//td[normalize-space()='{}'])[last()]".format(day))
    # day_field.click()

   # 点击年份
    year_xpath = f"//td[normalize-space()='{year_text}']"
    year_element = browser.find_element(By.XPATH, year_xpath)
    year_element.click()

    # 点击月份
    month_xpath = f"//td[normalize-space()='{month_text}']"
    month_element = browser.find_element(By.XPATH, month_xpath)
    month_element.click()

    # 点击日期
    # 这里假设你之前用的class 'current-month-cell '，可以这样写
    day_xpath = f"//td[contains(@class, 'current-month-cell') and normalize-space()='{day_text}']"
    day_element = browser.find_element(By.XPATH, day_xpath)
    day_element.click()

    fm_report_page.click_to_date_picker()
    fm_report_page.click_today_btn()
    fm_report_page.click_export_btn()
    assert fm_report_page.verify_three_months_error_one().is_displayed()
  # assert fm_report_page.verify_three_months_error_two().is_displayed()
    screenshot_path = os.path.join(os.getcwd()+"screenshots", "TC0011.png")
    request.node.driver.save_screenshot(screenshot_path)
    request.node.add_report_section(
        'test',
        'Screenshot',
        f'<img src="{screenshot_path}">')

@pytest.mark.TC0012
@pytest.mark.exportFundMovementReport
def test_export_fund_movement_report(browser, request):
    data = ExcelUtils.get_data('TC0012')
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
    fm_report_page = FMReportPage(browser)
    # fm_report_page.click_fund_services()
    fm_report_page.click_finance()
    fm_report_page.click_fm_report_page()
    time.sleep(5)

    # current_date = datetime.now()
    # three_months_ago = current_date - relativedelta(months=3)
    # one_day_closer = three_months_ago + timedelta(days=1)

     # 提取年月日
    target_date = datetime.now()
    # test data： target_date = datetime(2025, 1, 30)
    three_months_ago = target_date - relativedelta(months=3)
    one_day_closer = three_months_ago + timedelta(days=1)
    
    year_text = str(one_day_closer.year)
    month_text = one_day_closer.strftime("%b")  # 获取月份缩写，比如 'Jun'
    day_text = str(one_day_closer.day)

    # year = one_day_closer.year
    # month = one_day_closer.strftime("%B")
    # day = one_day_closer.day

    fm_report_page.click_from_date_picker()
    fm_report_page.click_date_picker_day_to_month_to_year()
    fm_report_page.click_date_picker_day_to_month_to_year()

    # year_field = browser.find_element(By.XPATH, "//td[normalize-space()='{}']".format(year))
    # year_field.click()
    # month_field = browser.find_element(By.XPATH, "//td[normalize-space()='{}']".format(month))
    # month_field.click()
    # # day_field = browser.find_element(By.XPATH, "//td[normalize-space()='{}']".format(day))
    # day_field = browser.find_element(By.XPATH, "(//td[normalize-space()='{}'])[last()]".format(day))
    # day_field.click()

    # 点击年份
    year_xpath = f"//td[normalize-space()='{year_text}']"
    year_element = browser.find_element(By.XPATH, year_xpath)
    year_element.click()

    # 点击月份
    month_xpath = f"//td[normalize-space()='{month_text}']"
    month_element = browser.find_element(By.XPATH, month_xpath)
    month_element.click()

    # 点击日期
    # 这里假设你之前用的class 'current-month-cell '，可以这样写
    day_xpath = f"//td[contains(@class, 'current-month-cell') and normalize-space()='{day_text}']"
    day_element = browser.find_element(By.XPATH, day_xpath)
    day_element.click()
    
    fm_report_page.click_to_date_picker()
    fm_report_page.click_today_btn() 
    fm_report_page.click_export_btn()
    time.sleep(5)
    assert fm_report_page.verify_successful_pop_up().is_displayed()
    screenshot_path = os.path.join(os.getcwd()+"screenshots", "TC0012.png")
    request.node.driver.save_screenshot(screenshot_path)
    request.node.add_report_section(
        'test',
        'Screenshot',
        f'<img src="{screenshot_path}">')
    
