from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By


def parse_html():
    driver = webdriver.Chrome()
    driver.get('https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273')
    titles = driver.find_elements_by_xpath("//div[@class='info-container']/div[@class='title']/a")
    images = []
    for i in range(len(titles)):
        try:
            audit = driver.find_element(By.XPATH,
                                        f"//div[@class='clearfix']/div[@class='left-col']/div[@class='image']/picture/img[@alt='{titles[i].text}']")
            images.append(audit.get_attribute('data-src'))
        except:
            images.append(None)

    dates = driver.find_elements_by_class_name('date-posted')
    city = driver.find_elements_by_xpath("//div[@class='location']/span[@class='']")
    beds_number = driver.find_elements_by_class_name('bedrooms')
    description = driver.find_elements_by_class_name('description')
    price = driver.find_elements_by_class_name('price')
    currency = [currency.text[0] for currency in price]

    data = []
    for i in range(len(images)):
        if dates[i].text[0] == '<':
            date = datetime.today().strftime('%d/%m/%Y')
        elif dates[i].text == 'Yesterday':
            date = datetime.today() - timedelta(days=1)
            date = date.strftime('%d/%m/%Y')
        else:
            date = dates[i].text
        data.append({'title': titles[i].text, 'image': images[i],
                     'date': datetime.strptime(date, "%d/%m/%Y").strftime('%d-%m-%Y'), 'city': city[i].text,
                     'beds': beds_number[i].text, 'price': price[i].text.replace('$', '').replace(',', ''),
                     'description': description[i].text, 'currency': currency[i].replace('P', '')
                     })


    return data