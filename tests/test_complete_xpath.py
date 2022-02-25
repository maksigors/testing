from selene import by, be, have
from selene.support.shared import browser, config
from selen.libs.helpers import xpath as xp

def test_add_tasks_xpath():
    browser.open('https://todomvc.com/examples/emberjs/')
    browser.element('//*[@id="new-todo"]').type('a').press_enter()
    browser.element('//*[@id="new-todo"]').type('b').press_enter()
    browser.element('//*[@id="new-todo"]').type('c').press_enter()

    browser.element('//*[@id="todo-list"]//li[.//text()="b"]'
                    '//*' + xp.by_class('toggle')).click()

    browser.all('//*[@id="new-todo"]//*' + xp.by_no_class("completed")).should(have.exact_text('a'))
    browser.all('//*[@id="new-todo"]//*' + xp.by_no_class("completed")).should(have.exact_text('c'))
    browser.all('//*[@id="new-todo"]//li' + xp.by_class('completed')).should(have.exact_text('b'))

