from behave import given, when, then
from pages.usertable import usertable


@then(u'Verify title of loaded page')
def step_impl_verify_title():
    usertable.verify_title()

@when(u'User is added to the table')
def step_impl_add_user():
    usertable.add_user

@then(u'Then the username is unique')
def step_impl_verify_user_is_unique():
    usertable.verify_user




