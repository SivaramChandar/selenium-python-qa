from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def test_google_search():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.google.com")
    search = driver.find_element(By.NAME, "q")
    search.send_keys("Selenium Python")
    search.send_keys(Keys.RETURN)
    assert "Selenium" in driver.title
    driver.quit()
