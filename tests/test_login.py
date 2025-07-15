from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def test_login():
    # Set up ChromeDriver manually
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    # Optional: maximize browser and set implicit wait
    driver.maximize_window()
    driver.implicitly_wait(10)

    try:
        # Open test login page
        driver.get("https://the-internet.herokuapp.com/login")

        # Interact with login form
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button.radius").click()

        time.sleep(2)  # Wait for page to load

        # Verify successful login
        if "Secure Area" in driver.page_source:
            print("✅ Login Successful")
            return "PASS", "Login was successful."
        else:
            print("❌ Login Failed")
            return "FAIL", "Login page did not load as expected."

    except Exception as e:
        print(f"⚠️ Exception managing chrome: {e}")
        return "ERROR", f"Exception occurred: {str(e)}"

    finally:
        driver.quit()
