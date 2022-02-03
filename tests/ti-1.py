from selene import by, be, have
from selene.support.shared import browser

def test_search():
    browser.config.browser_name = 'firefox'
    browser.config.base_url = 'https://google.com'
    browser.config.timeout = 2
    browser.open('https://google.com/ncr')
    browser.element(by.name('q')).should(be.blank)\
        .type('python selene').press_enter()
    browser.all('#search .g').should(have.size_greater_than_or_equal(6))\
        .first.should(have.text('Concise API for Selenium'))\
        .element('.r>a').click()
    browser.should(have.title_containing('yashaka/selene'))

def test_abc():
    browser.open('https://todomvc.com/examples/emberjs/')
    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()

    browser.all('#todo-list>li').element_by(have.exact_text('b')) \
        .element('.toggle').click()
    browser.all('#filters a').element_by(have.exact_text('Completed')) \
        .click()
    browser.all('#filters a').element_by(have.exact_text('Active')) \
        .click()

#============ main ======================

test_abc()