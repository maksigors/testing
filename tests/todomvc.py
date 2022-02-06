from selene import by, be, have
from selene.support.shared import browser, config
#config.browser_name: str = 'firefox'
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
    browser.element('#new-todo').should(be.visible).type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()

    browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

    browser.all('#todo-list>li').element_by(have.exact_text('b')) \
        .element('.toggle').click()

    browser.all('#todo-list>li').filtered_by(have.css_class('completed')) \
        .should(have.exact_texts('b'))
    browser.all('#todo-list>li').filtered_by(have.no.css_class('completed'))\
        .should(have.exact_texts('a', 'c'))
def test_abc_xpath():
    browser.open('https://todomvc.com/examples/emberjs/')
    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()

#============ main ======================

test_abc()
