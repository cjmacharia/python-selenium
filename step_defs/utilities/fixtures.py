import pytest

from pageobjects.LoginPage import LoginPage


@pytest.fixture(autouse=True, params=[{'email': "standard_user", 'password': "secret_sauce"}])
def standard_login(init_driver, request):
    login_page = LoginPage(init_driver)
    login_page.enter_email(request.param['email'])
    login_page.enter_password(request.param['password'])
    login_page.click_login()


