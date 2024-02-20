from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time
import random




def initial_test():
    try:
        URL = "https://forms.yandex.ru/cloud/657ada9e84227c84c114f76b/"
        options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        #options.add_argument('--remote-allow-origins=*')
        options.add_argument("user-data-dir=C:\\Users\\\ZayatsAS\\AppData\\Local\\Google\\Chrome\\User Data")
        options.add_argument("profile-directory=Default")
        driver = webdriver.Chrome(options=options)
        driver.get(url=URL)
        time.sleep(4)
        # FIRST PAGE
        # push to button 'Далее' on first page
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/form/div/div[3]/button').click()

        # SECOND PAGE
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
        list_study = ['среднее профессиональное', 'неоконченное высшее', 'высшее']
        random_study = random.choice(list_study)
        driver.find_element(By.XPATH, f"//p[contains(text(), '{random_study}')]").click()

        # choise random exp on second page
        list_exp = ['менее 1 года', '1-3 года', '3-5 лет', '5-10 лет', 'более 10 лет']
        random_exp = random.choice(list_exp)
        driver.find_element(By.XPATH, f"//p[contains(text(), '{random_exp}')]").click()

        # choise job title on second page
        list_job_title = ['инженерно-технический работник', 'основной производственный рабочий',
                          'вспомогательный производственный рабочий', 'иное']
        random_job_title = random.choice(list_job_title)
        driver.find_element(By.XPATH, f"//p[contains(text(), '{random_job_title}')]").click()

        # choise hobby on second page
        list_hobby = ['провожу время с друзьями и семьей', 'читаю новости в интернете', 'играю в компьютерные игры',
                      'смотрю телевизор, видео в интернете', 'читаю книги',
                      'есть хобби (рисование, рыбалка, коллекционирование, рукоделие и т.п.)',
                      'занимаюсь саморазвитием (посещаю тренинги и т.п.)', 'занимаюсь спортом',
                      'хожу в кино или театры']
        count_hobby_random = random.randint(1, 3)
        random_hobby = random.sample(list_hobby, count_hobby_random)
        for value_text in random_hobby:
            driver.find_element(By.XPATH, f"//p[contains(text(), '{value_text}')]").click()

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/form/div/div[10]/button[2]').click()
        time.sleep(3)

        # THIRD PAGE
        # choise random value on trade union on third page
        list_answer_trade_union = ['Да', 'Нет']
        random_answer_trade_union = random.choice(list_answer_trade_union)
        driver.find_element(By.XPATH, f"//p[contains(text(), '{random_answer_trade_union}')]").click()
        time.sleep(3)

        # choise yes or not in input trade union
        if random_answer_trade_union == 'Да':
            # choise role in trade union
            list_role_trade_union = ['рядовой член профсоюза',
                                     'профсоюзный активист (участник и/или организатор мероприятий)']
            random_role_trade_union = random.choice(list_role_trade_union)
            driver.find_element(By.XPATH, f"//p[contains(text(), '{random_role_trade_union}')]").click()

            # choise why member
            list_why_member = ['по убеждению', 'по традиции (семейные, трудовые)', 'из чувства солидарности',
                               'в расчете на материальную помощь',
                               'в расчете на защиту трудовых прав', 'для получения социальных льгот',
                               'для участия в профсоюзных мероприятиях',
                               'для развития и личностного роста', 'как все', 'не знаю']
            count_why_member = random.randint(1, 5)
            random_why_member = random.sample(list_why_member, count_why_member)
            for count_i_reason in random_why_member:
                driver.find_element(By.XPATH, f"//p[contains(text(), '{count_i_reason}')]").click()

            # choise why not member
            list_why_not_member = ['ничего не знают о работе профсоюза',
                                   'не знают, что на предприятии есть первичная профсоюзная организация',
                                   'препятствия со стороны руководства предприятия',
                                   'неуверенность в том, что профсоюз сможет защитить права работников',
                                   'низкий авторитет профсоюза',
                                   'уверенность работников в самостоятельной защите прав',
                                   'отсутствие системной работы по вовлечению в профсоюз',
                                   'нежелание платить профсоюзные взносы',
                                   'использование устаревших и несовременных подходов в деятельности профсоюза',
                                   'непонимание значения и пользы профсоюза',
                                   'иное']
            count_why_not_member_random = random.randint(1, 5)
            random_why_not_member = random.sample(list_why_not_member, count_why_not_member_random)
            for count_i_reason in random_why_not_member:
                driver.find_element(By.XPATH, f"//p[contains(text(), '{count_i_reason}')]").click()

            #
            list_prioritet_not = [
                'регулирование социально-трудовых отношений на основе коллективного договора и соглашений',
                'представление интересов членов профсоюза на различных уровнях',
                'решение вопросов достойной заработной платы работников',
                'оказание правовой помощи и юридической защиты членов профсоюза',
                'контроль за соблюдением требований охраны труда, улучшением условий труда',
                'организация культурно-массовых и спортивных мероприятий',
                'содействие в оздоровлении, санаторно-курортном лечении членов профсоюза',
                'привлечение в профсоюз новых членов']
            count_prioritet_not_random = random.randint(1, 5)
            random_prioritet_not = random.sample(list_prioritet_not, count_prioritet_not_random)
            for count_i_reason in random_prioritet_not:
                driver.find_element(By.XPATH, f"//p[contains(text(), '{count_i_reason}')]").click()

        elif random_answer_trade_union == 'Нет':
            list_reason_not = ['ничего не знаю о профсоюзах', 'не предлагали вступить',
                               'препятствия со стороны руководства предприятия',
                               'отсутствие пользы и выгоды от профсоюза',
                               'нет пересечений видов деятельности с моими интересами',
                               'низкое качество работы профсоюзного комитета и штатных работников ППОО (при наличии)',
                               'недостаточная организация культурно-массовой и спортивной работы',
                               'недостаточная информационная деятельность',
                               'использование устаревших и несовременных подходов в деятельности профсоюза',
                               'пассивная позиция в решении вопросов с руководством предприятия',
                               'высокий размер профсоюзного взноса']
            count_reason_not_random = random.randint(1, 5)
            random_reason_not = random.sample(list_reason_not, count_reason_not_random)
            for count_i_reason in random_reason_not:
                driver.find_element(By.XPATH, f"//p[contains(text(), '{count_i_reason}')]").click()

            # choise reason for joining on third page
            list_reason_for_joing = ['Ходатайство о повышении зп', 'Плавающий график работы',
                                     'Новые мероприятия на предприятии',
                                     'Улучшение взаимоотношений между руководством и простыми рабочими',
                                     'Условия труда']
            random_reason_for_joing = random.choice(list_reason_for_joing)
            driver.find_element(By.XPATH, '//*[@id="answer_long_text_30903456"]').send_keys(
                f'{random_reason_for_joing}')

            # choise reason for reluctance on third page
            list_reason_for_reluctance = ['ничего не знают о работе профсоюза',
                                          'не знают, что на предприятии есть первичная профсоюзная организация',
                                          'препятствия со стороны руководства предприятия',
                                          'неуверенность в том, что профсоюз сможет защитить права работников',
                                          'низкий авторитет профсоюза',
                                          'уверенность работников в самостоятельной защите прав',
                                          'отсутствие системной работы по вовлечению в профсоюз',
                                          'нежелание платить профсоюзные взносы',
                                          'использование устаревших и несовременных подходов в деятельности профсоюза',
                                          'непонимание значения и пользы профсоюза',
                                          'иное']
            count_reason_for_reluctance_random = random.randint(1, 5)
            random_reason_for_reluctance = random.sample(list_reason_for_reluctance, count_reason_for_reluctance_random)
            for count_i_reason in random_reason_for_reluctance:
                driver.find_element(By.XPATH, f"//p[contains(text(), '{count_i_reason}')]").click()

            # choise reason for prioritet
            list_prioritet = [
                'регулирование социально-трудовых отношений на основе коллективного договора и соглашений',
                'представление интересов членов профсоюза на различных уровнях',
                'решение вопросов достойной заработной платы работников',
                'оказание правовой помощи и юридической защиты членов профсоюза',
                'контроль за соблюдением требований охраны труда, улучшением условий труда',
                'организация культурно-массовых и спортивных мероприятий',
                'содействие в оздоровлении, санаторно-курортном лечении членов профсоюза',
                'привлечение в профсоюз новых членов']
            count_prioritet_random = random.randint(1, 5)
            random_prioritet = random.sample(list_prioritet, count_prioritet_random)
            for count_i_reason in random_prioritet:
                driver.find_element(By.XPATH, f"//p[contains(text(), '{count_i_reason}')]").click()

        # FOURTH PAGE
        # push to button from third page to fourth page
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/form/div/div[7]/button[2]').click()

        # choise satisfied or not on fourth page
        list_satisfied = ['удовлетворен(-а)', 'удовлетворен(-а), но не полностью', 'не удовлетворен(-а)']
        random_satisfied = random.choice(list_satisfied)
        driver.find_element(By.XPATH, f"//p[contains(text(), '{random_satisfied}')]").click()

        # choise sources on fourth page
        list_sources = ['личный контакт', 'печатные издания', 'информационные стенды',
                        'телевидение, радио на предприятии',
                        'сайты профсоюза и его организаций', 'социальные сети и мессенджеры',
                        'корпоративные ресурсы (почта, локальный инфопортал предприятия и т.д.)']
        count_sources_random = random.randint(1, 5)
        random_sources = random.sample(list_sources, count_sources_random)
        for count_i_reason in random_sources:
            driver.find_element(By.XPATH, f"//p[contains(text(), '{count_i_reason}')]").click()

        # push to button from fourth to fifth page
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/form/div/div[4]/button[2]').click()

        # FIFTH PAGE
        # choice of assessment
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/form/div/div[1]/div/div[1]/div/button').click()
        action = ActionChains(driver)
        random_assessment = random.randint(1, 10)
        for i in range(random_assessment):
            action.send_keys(Keys.ARROW_DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        # push to button to final page
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/form/div/div[3]/button[2]').click()
        time.sleep(3)
        driver.close()
        driver.quit()
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    a = 1
    while a <= 10:
        initial_test()