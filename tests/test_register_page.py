from src.registration_page import RegistrationPage


def test_register_with_valid_credentials(driver_init):
    lp = RegistrationPage(driver_init)
    lp.register("nemu","nimi","nimu1@gmail.com","neni123")
    result = lp.is_user_register()
    assert result, "Invalid user"
    print("user register in successfully")
    lp.logout()
