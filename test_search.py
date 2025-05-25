from selene import browser, have
import pytest

@pytest.fixture
def browser_window_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()

def test_search_duckduckgo(browser_window_size):
    browser.open('https://duckduckgo.com/')
    browser.element('[name=q]').type('qa.guru')
    browser.element('[class="iconButton_icon__K7FBb iconButton_size-20__Ql3lL"]').click()
    browser.element('html').should(have.text('qa.guru'))

def test_bad_search_duckduckgo(browser_window_size):
    browser.open('https://duckduckgo.com/')
    browser.element('[name=q]').type('qa.guru')
    browser.element('[class="iconButton_icon__K7FBb iconButton_size-20__Ql3lL"]').click()
    browser.element('html').should(have.text('hbd21hb12uhbdubudbf7tb23'))