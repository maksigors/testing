from selene import by, be, have
from selene.support.shared import browser, config

def by_no_class(css_class : str) -> str:
    return f'[not(contains(@class, " {css_class} "))]'


browser.open('https://todomvc.com/examples/emberjs/')
browser.element('//*[@id="new-todo"]').type('a').press_enter()
browser.element('//*[@id="new-todo"]').type('b').press_enter()
browser.element('//*[@id="new-todo"]').type('c').press_enter()

browser.all('//*[@id="todo-list"]//*' + by_no_class('toggle')).should(have.exact_text('c'))