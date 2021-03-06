import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Nothing said about cross-browser comapatability in requirements to this task!!!
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Enter language: ru, en, es...")


@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption('language')
    options = Options()

    # TODO: input options must be validated
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})

    browser = webdriver.Chrome(options=options)
    yield browser

    browser.quit()
