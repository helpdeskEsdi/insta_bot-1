from login import open_login, login_cookies
from profiles import go_profile

if __name__ == "__main__":
    driver = open_login()
    login_cookies(driver, cookies_file="cookies.json", use_json=True)
    go_profile(driver)
