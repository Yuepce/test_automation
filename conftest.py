import pytest
from selenium import webdriver
import os
from pytest_html import extras

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item,call):
#     pytest_html = item.config.pluginmanager.getplugin("html")

#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra",[])

#     #Assuming the screenshot saved
#     screenshot_path = os.path.join("screenshots","login successfully.png")
#     if os.path.exists(screenshot_path):
#         with open(screenshot_path, "rb") as image_file:
#             encoded_string = pytest_html.extras.png(image_file.read())
#             extra.append(encoded_string)
#     report.extra = extra

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if call.excinfo is not None: # Test failed
    # Get the mark
        print("Case Failed")
        markers = list(item.iter_markers())
        print(markers)
        tags = [marker.name for marker in markers if marker.name.startswith('TC')]
        print(tags)
        if tags:
            screenshot_name = f"{'_'.join(tags)}_fail.png"
            print(os.getcwd()+"\screenshots"+"\"", screenshot_name)
            screenshot_path = os.path.join(os.getcwd()+"\screenshots", screenshot_name)
            request = item._request
            request.node.driver.save_screenshot(screenshot_path)
            #add screenshot to the report
            item.user_properties.append(("screenshot",screenshot_path)) #store the screenshot path
            print("Fail Screenshot saved")
            
            # item.config.option.metadata['Screenshot'] = screenshot_path
            # item.config.hook.pytest_html_results_table_row(item=item,cell=extras.image(screenshot_path))
            request.node.add_report_section(
                'test',
                'Screenshot',
                f'<img src="{screenshot_path}">')
            
# @pytest.hookimpl(trylast=True)
# def pytest_html_results_table_row(report,cells):
#     for prop in report.user_properties:
#         if prop[0] == "Screenshot":
#             cells.append(f'<img src="{prop[1]}" alt="Screenshot" style="max-width: 200px;"/>')

            
@pytest.hookimpl(trylast=True)
def pytest_html_results_table_row(report, cells):
    if hasattr(report, "user_properties"):
        for prop in report.user_properties:
            if prop[0] == "Screenshot":
                cells.append(f'<img src="{prop[1]}" alt="Screenshot" style="max-width: 200px;"/>')

