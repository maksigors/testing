from selene import by, be, have
from selene.support.shared import browser, config

#============ module 1 ======================
def test_add_tasks():
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
#end__DEF#

#============ module 2 ======================
def test_add_tasks_xpath():
    browser.open('https://todomvc.com/examples/emberjs/')
    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()

    browser.element('//*[@id="todo-list"]//li[.//text()="b"]'
                    '//*[@class="toggle"]').click()


    browser.element('//*[@id="todo-list"]//li[.//text()="a"]'
                    '//*[@class!="completed"]')
    browser.element('//*[@id="todo-list"]//li[.//text()="c"]'
                    '//*[@class!="completed"]')
    browser.element('//*[@id="todo-list"]//li[.//text()="c"]'
                    '//*[@class!="completed"]')

    browser.element('//*[@id="filters"]//a[.//text()="Completed"]').click()
    for n in range(1, 10000000):
        n = n * n
    browser.element('//*[@id="filters"]//a[.//text()="Active"]').click()
    for n in range(1, 10000000):
        n = n * n
#end__DEF#

#   =====================================
#================= M A I N ==================
#   =====================================

#test_abc_xpath()
