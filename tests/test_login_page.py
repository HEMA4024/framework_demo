from src.login_page import LoginPage


def test_login_with_valid_credentials(driver_init):
    lp = LoginPage(driver_init)
    lp.login("steve_jobs@gmail.com", "steve123")
    result = lp.is_user_logged_in()
    assert result, "Invalid user"
    print("user logged in successfully")
    lp.logout()


def test_login_with_invalid_credentials(driver_init):
    lp = LoginPage(driver_init)
    lp.login("abc@gmail.com", "abc123")
    result = lp.is_user_logged_in()
    assert result, "Invalid user"
    print("user logged in successfully")
    lp.logout()


def test_login_invalid_email_with_valid_password(driver_init):
    lp=LoginPage(driver_init)
    lp.login(" ","abc123")
    result=lp.is_user_logged_in()
    assert result, "Invalid username"
    print("user logged in successfully")
    lp.logout()


def test_login_with_invalid_email_valid_password(driver_init):
    lp=LoginPage(driver_init)
    lp.login(" "," ")
    result=lp.is_user_logged_in()
    assert result, "Invalid credential"
    print("user logged in successfully")
    lp.logout()

# test login with blank email and some password
# test login with blank email and password