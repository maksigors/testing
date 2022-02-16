from selene import by, be, have
from selene.support.shared import browser, config

def test_todo_complete_css():
    browser.open('https://todomvc.com/examples/emberjs/')
    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()

    browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

    browser.element('#todo-list>li:nth-of-type(2) .toggle') \
        .click()
    browser.element('#todo-list>li.completed') \
        .should(have.exact_text('b'))
    browser.all('#todo-list>li:not(.completed)') \
        .should(have.exact_texts('a','c'))
