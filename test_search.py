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

def test_search_google_emptystate(browser_window_size):
    browser.open('https://www.google.com/')
    browser.element('[name="q"]').type('ФЫАДТОЫФРА!?№АР!*№А(РВФАТГЗШУПВЫАТ*?("№ПАРТзГЩРТBDSAIHBDSNJGN#@(GNUDSFMD"kje9pw7ghf2nfdw').press_enter()
    browser.element('html').should(have.text('Нет результатов для'))