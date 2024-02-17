import random

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://forms.yandex.ru/cloud/657ada9e84227c84c114f76b/"
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)


try:
    driver.get(url=URL)
    time.sleep(3)
    # FIRST PAGE
    # push to button 'Далее' on first page
    driver.find_element(By.XPATH,'//*[@id="root"]/div/main/form/div/div[3]/button').click()

    #SECOND PAGE
    # push to button on 'Республика Татарстан' on second page
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/form/div/div[1]/div/div[1]/label[8]').click()
    # writing name of build on second page
    driver.find_element(By.XPATH, '//*[@id="suggest-1"]').send_keys('КАЗ им. С.П. Горбунова филиал АО Туполев')

    # choise random gender on second page
    list_gender = ['мужской', 'женский']
    random_gender = random.choice(list_gender)
    driver.find_element(By.XPATH, f"//p[contains(text(), '{random_gender}')]").click()

    # choise random age on second page
    list_age = ['18-23', '24-29', '30-35']
    random_age = random.choice(list_age)
    driver.find_element(By.XPATH, f"//p[contains(text(), '{random_age}')]").click()

    # choise random study on second page
    list_study = ['среднее', 'среднее профессиональное', 'неоконченное высшее', 'высшее']
    random_study = random.choice(list_study)
    driver.find_element(By.XPATH, f"//p[contains(text(), '{random_study}')]").click()

    # choise random exp on second page
    list_exp = ['меньше 1 года', '1-3 года', '3-5 лет', '5-10 лет', 'более 10 лет']
    random_exp = random.choice(list_exp)
    driver.find_element(By.XPATH, f"//p[contains(text(), '{random_exp}')]").click()

    # choise job title on second page
    list_job_title = ['руководитель высшего звена (директор, зам. директора)', 'руководитель среднего звена (начальник цеха/отдела и т.п.)', 'руководитель низшего звена (начальник бюро, мастер и т.п.)', 'инженерно-технический работник', 'основной производственный рабочий', 'вспомогательный производственный рабочий', 'иное']
    random_job_title = random.choice(list_job_title)
    driver.find_element(By.XPATH, f"//p[contains(text(), '{random_job_title}')]").click()

    # choise hobby on second page
    list_hobby = ['провожу время с друзьями и семьей', 'читаю новости в интернете', 'играю в компьютерные игры',
                  'смотрю телевизор, видео в интернете', 'читаю книги',
                  'есть хобби (рисование, рыбалка, коллекционирование, рукоделие и т.п.)',
                  'занимаюсь саморазвитием (посещаю тренинги и т.п.)', 'занимаюсь спортом',
                  'хожу в кино или театры']
    i_random = random.randint(1,3)
    random_hobby = random.sample(list_hobby, i_random)
    for value_text in random_hobby:
        driver.find_element(By.XPATH, f"//p[contains(text(), '{value_text}')]").click()

    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/form/div/div[10]/button[2]').click()

    #THIRD PAGE
    time.sleep(3)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()