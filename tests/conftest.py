import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options

from tests.config import USE_SELENOID, DEFAULT_BROWSER_NAME, DEFAULT_BROWSER_VERSION, DEFAULT_SELENOID_URL
from utils import attach
from dotenv import load_dotenv
import os


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Укажите браузер: chrome или firefox"
    )
    parser.addoption(
        "--browser_version",
        action="store",
        default="128.0",
        help="Укажите версию браузера"  # chrome 128.0, 127.0, firefox 124.0, 125.0
    )
    parser.addoption(
        "--selenoid_url",
        action="store",
        default="selenoid.autotests.cloud",
        help="URL Selenoid"
    )


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function")
def setup_browser(request):
    # Определяем, используется ли Selenoid
    print(f" Selenoid: {USE_SELENOID}")
    video_url = ""

    if USE_SELENOID:
        browser_name = request.config.getoption('--browser_name')
        browser_version = request.config.getoption('--browser_version')
        selenoid_url = request.config.getoption('--selenoid_url')
        print(f"Установленные параметры: {selenoid_url}: {browser_name}:{browser_version}")
        browser_name = browser_name if browser_name != "" else DEFAULT_BROWSER_NAME
        browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
        selenoid_url = selenoid_url if selenoid_url != "" else DEFAULT_SELENOID_URL

        options = FirefoxOptions() if browser_name.lower() == "firefox" else Options()

        selenoid_capabilities = {
            "browserName": browser_name,
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableLog": True,
                "enableVNC": True,
                "enableVideo": True,
                "screenResolution": "1280x1080"
            },
            "goog:loggingPrefs": {"browser": "ALL"},
            "pageLoadStrategy": "eager"
        }

        if browser_name.lower() == "firefox":
            selenoid_capabilities["moz:firefoxOptions"] = {
                "log": {"level": "trace"},
                "prefs": {
                    "devtools.console.stdout.content": True,
                    "browser.console.showInPanel": True,
                    "dom.ipc.processCount": 8
                }
            }

        options.capabilities.update(selenoid_capabilities)

        selenoid_login = os.getenv("SELENOID_LOGIN")
        selenoid_pass = os.getenv("SELENOID_PASS")

        print(options.to_capabilities())
        driver = webdriver.Remote(
            command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
            options=options
        )

        video_url = selenoid_url
    else:
        print(f"Браузер: {DEFAULT_BROWSER_NAME}")
        options = FirefoxOptions() if DEFAULT_BROWSER_NAME.lower() == "firefox" else Options()
        options.page_load_strategy = 'eager'
        if DEFAULT_BROWSER_NAME.lower() == "firefox":
            options.set_preference("devtools.console.stdout.content", True)
            options.set_preference("browser.console.showInPanel", True)
        driver = webdriver.Firefox(options=options) if DEFAULT_BROWSER_NAME.lower() == "firefox" else webdriver.Chrome(
            options=options)
    browser.config.driver = driver
    browser.config.window_width = 1280
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'
    print(f"Установленный размер окна: {browser.config.window_width}x{browser.config.window_height}")
    yield browser
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser, video_url)
    driver.quit()