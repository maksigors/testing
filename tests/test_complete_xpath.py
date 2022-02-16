from selene import by, be, have
from selene.support.shared import browser, config

def test_add_tasks_xpath():
    browser.open('https://todomvc.com/examples/emberjs/')
    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()

    # browser.element('//*[@id="todo-list"]//li[.//text()="b"]'
    #                 '//*[@class="toggle"]').click()
    browser.element('//*[@id="todo-list"]//li[.//text()="b"]'
                    '//*[contains(concat(" ", normalize-space(@class), " "), " toggle ")]') \
        .click()

    browser.all('#todo-list li:not(.completed)').should(have.exact_texts('a','c'))
    browser.all('#todo-list li.completed').should(have.exact_text('b'))

    browser.element('//*[@id="filters"]//a[.//text()="Completed"]').click()
    browser.element('//*[@id="filters"]//a[.//text()="Active"]').click()