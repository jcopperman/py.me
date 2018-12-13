from behave import given, when, then
from framework.webapp import webapp


@given(u'I load the website')
def step_impl_load_website():
    webapp.load_website()


@when(u'I go to "{page}" page')
def step_impl_goto_page(page):
    webapp.goto_page(page)


@then(u'I see this component "{component}"')
def step_impl_verify_component(component):
    webapp.verify_component_exists(component)
