import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()
url = 'https://flight.naver.com/'
browser.get(url)

time.sleep(5) #1초대기
begin_date = browser.find_element(By.XPATH, '//button[text() = "가는 날"]')     # from selenium.webdriver.common.by import By 가 임포트 되어야 서칭이 가능하다
begin_date.click()

time.sleep(5) #1초대기
day27 = browser.find_elements(By.XPATH, '//b[text() = "27"]')     #가는날 27일 찾기
day27[0].click()                                                  #가는날 27일 클릭

time.sleep(5) #1초대기
day30 = browser.find_elements(By.XPATH, '//b[text() = "30"]')     #복귀날 30일 찾기
day30[0].click()                                                  #복귀날 30일 클릭

time.sleep(5) #1초대기
arrival = browser.find_element(By.XPATH, '//b[text() = "도착"]')   #"도착" 단어 찾기
arrival.click()                                                   #"도착" 단어 클릭

time.sleep(5) #1초대기
domestic = browser.find_element(By.XPATH, '//button[text() = "국내"]')
domestic.click()

time.sleep(5) #1초대기
jeju = browser.find_element(By.XPATH, '//i[contains(text(), "제주국제공항")]')
jeju.click()

time.sleep(5) #1초대기
search = browser.find_element(By.XPATH, '//span[contains(text(), "항공권 검색")]')
search.click()

elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="domestic_Flight__sK0eA result"]')))
print(elem.text)

browser.quit()




