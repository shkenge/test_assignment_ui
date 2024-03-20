import pytest
from selenium import webdriver
import logging

logging.basicConfig(level=logging.INFO)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        screenshot_path = f"screenshot_{item.name}.png"
        item.funcargs['browser'].save_screenshot(screenshot_path)
        logging.info(f"Screenshot captured: {screenshot_path}")

@pytest.fixture(scope="function")
def browser(request):
    logging.info("\nStart browser for test.")
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    logging.info("\nQuit browser.")
    browser.quit()
