from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def init_browser():
    #binary = FirefoxBinary("/usr/local/bin/geckodriver")
    #browser = webdriver.Firefox(

    driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver",log_path=None)

#)
    driver.get('https://www.carowinds.com/tickets-passes/scarowinds#')

    element = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@data-wa-section="SCarowinds Admission"]'))
    )
    element.click()

    noDays = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, '//label[contains(.,"1")]'))
    )
    noDays.click()


    noGuests = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-default ng-click-active"]'))
    )
    noGuests.click()

    admissionType = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-success ng-binding ng-click-active"]'))
    )
    admissionType.click()

    NextPage = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-primary btn-block ng-binding ng-click-active"]'))
    )
    NextPage.click()



if __name__ == '__main__':
    init_browser()