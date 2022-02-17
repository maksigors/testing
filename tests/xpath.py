from selene import by, be, have
from selene.support.shared import browser, config

def by_no_class(css_class : str) -> str:
    return f'[not(contains(@class, "{css_class}"))]'

def by_class(css_class : str) -> str:
    return f'[contains(@class, "{css_class}")]'

def filter_by_class(css_class : str) -> str:
    return f'[contains(concat(" ", normalize-space(@class), " "), " {css_class} ")]'

browser.open('https://todomvc.com/examples/emberjs/')
browser.element('//*[@id="new-todo"]').type('a').press_enter()
browser.element('//*[@id="new-todo"]').type('b').press_enter()
browser.element('//*[@id="new-todo"]').type('c').press_enter()

browser.element('//*[@id="todo-list "]//li[.//text()="b"]//*' + filter_by_class('toggle')) \
    .click()


browser.all('//*[@id="new-todo"]//*' + by_no_class("toggle")).should(have.exact_text('a'))
browser.all('//*[@id="new-todo"]//*' + by_no_class("toggle")).should(have.exact_text('c'))
browser.all('//*[@id="new-todo"]//li' + by_class('toggle')).should(have.exact_text('b'))