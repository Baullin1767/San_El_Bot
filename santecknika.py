from time import sleep
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc 

def parse_santexnic(url, sale=3):
    driver = uc.Chrome()
    driver.maximize_window()
    driver.get(url)
    sleep(30)

    #придумать как считать количество пройденных элементов (не комплектов) для
    #указания индекса для count_rows()

    #print(driver.find_element(By.XPATH, f'/html/body/div[5]/main/div[2]/div/form/main/div/div[2]/div[2]/div[1]/div[1]/div/a/div[1]').text)
    #print(driver.find_element(By.XPATH, f'/html/body/div[5]/main/div[2]/div/form/main/div/div[2]/div[2]/div[2]/div[1]/div/a/div[1]').text)
    #print(driver.find_element(By.XPATH, f'/html/body/div[5]/main/div[2]/div/form/main/div/div[2]/div[2]/div[3]/div[1]/div/a/div[1]').text)

    #print(driver.find_element(By.XPATH, f'/html/body/div[5]/main/div[2]/div/form/main/div/div[{start}]/div[2]/div[{element}]/div[1]/div/a/div[1]').text)
    #print(driver.find_element(By.XPATH, f'/html/body/div[5]/main/div[2]/div/form/main/div/div[3]/div[2]/div[2]/div[1]/div/a/div[1]').text)
    #print(driver.find_element(By.XPATH, f'/html/body/div[5]/main/div[2]/div/form/main/div/div[3]/div[2]/div[3]/div[1]/div/a/div[1]').text)

    number_of_element, result_price = 1, 0
    test_names, test_prices = [], []

    while True:
        try:
            name = driver.find_element(By.XPATH,
                                       f'/html/body/div[5]/main/div[2]/div/form/main/div/div[{number_of_element}]/div/div[1]/div/div/a/div[1]').text
            #                                    f'/html/body/div[5]/main/div/div/form/main/div[2]/div[1]/div[3]/div[2]/div[1]/div/a/div[1]
            #                                     '/html/body/div[5]/main/div[2]/div/form/main/div/div[2]/div[2]/div[1]/div[3]/div[1]/span
            price = driver.find_element(By.XPATH,
                                        f'/html/body/div[5]/main/div[2]/div/form/main/div/div[{number_of_element}]/div/div[3]/div[1]/div').text
            print(name, price)
            # if name in names:
            # names.append(str(count) + '. ' + name)
            # count += 1
            # else:
            test_names.append(name)
            if '\n' in price:
                two_elements = price.split('\n')
                price = int(two_elements[1].replace('₽', '').replace(' ', '')) - int(
                    two_elements[0].replace('—', '').replace('₽', '').replace(' ', ''))
                result_price += price
            else:
                result_price += int(price.replace('₽', '').replace(' ', ''))
            test_prices.append(price)
            number_of_element += 1
        except:
            break

    def count_rows():
        number = 1
        count = 0
        statement = 1
        was_element:bool = False
        while True:
            try:
                #                                      '/html/body/div[5]/main/div[2]/div/form/main/div/div[2]/div[1]/div[1]/div/div/div
                #                                      '/html/body/div[5]/main/div[2]/div/form/main/div/div[3]/div[1]/div[1]/div/div/div
                group = driver.find_element(By.XPATH, f'/html/body/div[5]/main/div[2]/div/form/main/div/div[{number}]/div[1]/div[1]/div/div/div')
                if statement:
                    start = number
                    statement = 0
                was_element = True
                number += 1
                count += 1
            except:
                if was_element:
                    break
                else:
                    number += 1
            print(number, was_element)
            if not was_element and (number + 1 > len(test_names) or number + 1 > len(test_prices)):
                start = 1
                default_parse = True
                break
            else:
                default_parse = False

        return (count + 1, start, default_parse)

    new_names, new_prices = [], []

    def parse_row(row):
        element = 1
        new_res_price = 0
        while True:
            try:

                #добавить поиск имени по start аналогично

                new_price = driver.find_element(By.XPATH, f'/html/body/div[5]/main/div[2]/div/form/main/div/div[{row}]/div[2]/div[{element}]/div[3]/div[1]/span').text
                #new_name = driver.find_element(By.XPATH, f'/html/body/div[5]/main/div[2]/div/form/main/div/div[{start}]/div[2]/div[{element}]/div[1]/div/a/div[1]').text
                #                                        '/html/body/div[5]/main/div[2]/div/form/main/div/div[2]/div[3]/div[2]/div[1]/div/a/div[1]
                #                                        '/html/body/div[5]/main/div[2]/div/form/main/div/div[2]/div[3]/div[3]/div[1]/div/a/div[1]
                #
                #                                        '/html/body/div[5]/main/div[2]/div/form/main/div/div[3]/div[3]/div[1]/div[1]/div/a/div[1]
                #                                        '/html/body/div[5]/main/div[2]/div/form/main/div/div[3]/div[3]/div[2]/div[1]/div/a/div[1]
                #                                        '/html/body/div[5]/main/div[2]/div/form/main/div/div[3]/div[3]/div[3]/div[1]/div/a/div[1]
                print(new_price)
                #print(new_name)
                new_res_price += int(new_price.replace('₽', '').replace(' ', ''))
                new_prices.append(new_price)
                #prices.append(new_price)
                element += 1
            except:
                break


    def parse_in_group(start):
        element = 1
        while True:
            print(start, element)
            try:
                new_name = driver.find_element(By.XPATH, f'/html/body/div[5]/main/div[2]/div/form/main/div/div[{start}]/div[2]/div[{element}]/div[1]/div/a/div[1]').text
                print(new_name)
                new_names.append(new_name)
                element += 1
            except:
                break



    #res_price = str(int(result_price - ((result_price * sale) / 100))) + '₽'
    price_from_website1 = driver.find_element(By.XPATH, '/html/body/div[5]/main/div[2]/div/form/aside/div/div/div/div[1]/div[2]/div/div[1]/span').text.replace(' ','').replace('₽', '')
    price_from_website2 = driver.find_element(By.XPATH, '/html/body/div[5]/main/div[2]/div/form/aside/div/div/div/div[1]/div[3]/div/div[1]/span').text.replace(' ','').replace('₽', '')
    if int(price_from_website1) > int(price_from_website2):
        price_from_website = price_from_website1
    else:
        price_from_website = price_from_website2

    price_from_website = int(int(price_from_website) - ((int(price_from_website) * int(sale)) / 100))

    count = count_rows()
    start = count[1]
    state = count[2]
    old_start = count[1]
    rows = count_rows()[0]
    print('r:',rows, 's',start)

    if rows and not state:
        for row in range(1, rows+1):
            parse_row(row)

        for i in range(start, start + rows):
            print(f'start point: {start}')
            parse_in_group(start)
            start += 1

        current_row = start - 1
        print('current row', current_row)

        #print(price_from_website)

        print(new_names, new_prices)

        number_of_element, count, result_price = 1, 1, 0
        names, prices = [], []

        print('old start =', old_start)

        if rows != old_start:
            for i in range(1, old_start):
                name = driver.find_element(By.XPATH,
                                           f'/html/body/div[5]/main/div[2]/div/form/main/div/div[{number_of_element}]/div/div[1]/div/div/a/div[1]').text

                #                                    f'/html/body/div[5]/main/div/div/form/main/div[2]/div[1]/div[3]/div[2]/div[1]/div/a/div[1]
                #                                     '/html/body/div[5]/main/div[2]/div/form/main/div/div[2]/div[2]/div[1]/div[3]/div[1]/span
                price = driver.find_element(By.XPATH,
                                            f'/html/body/div[5]/main/div[2]/div/form/main/div/div[{number_of_element}]/div/div[3]/div[1]/div').text
                print(name, price)
                # if name in names:
                # names.append(str(count) + '. ' + name)
                # count += 1
                # else:
                names.append(name)
                if '\n' in price:
                    two_elements = price.split('\n')
                    price = int(two_elements[1].replace('₽', '').replace(' ', '')) - int(
                        two_elements[0].replace('—', '').replace('₽', '').replace(' ', ''))
                    result_price += price
                else:
                    result_price += int(price.replace('₽', '').replace(' ', ''))
                prices.append(price)
                number_of_element += 1

            number_of_element = current_row
        else:
            number_of_element = old_start


        while True:
            try:
                name = driver.find_element(By.XPATH,
                                           f'/html/body/div[5]/main/div[2]/div/form/main/div/div[{number_of_element}]/div/div[1]/div/div/a/div[1]').text
                #                                    f'/html/body/div[5]/main/div/div/form/main/div[2]/div[1]/div[3]/div[2]/div[1]/div/a/div[1]
                #                                     '/html/body/div[5]/main/div[2]/div/form/main/div/div[2]/div[2]/div[1]/div[3]/div[1]/span
                price = driver.find_element(By.XPATH,
                                            f'/html/body/div[5]/main/div[2]/div/form/main/div/div[{number_of_element}]/div/div[3]/div[1]/div').text
                print(name, price)
                # if name in names:
                # names.append(str(count) + '. ' + name)
                # count += 1
                # else:
                names.append(name)
                if '\n' in price:
                    two_elements = price.split('\n')
                    price = int(two_elements[1].replace('₽', '').replace(' ', '')) - int(
                        two_elements[0].replace('—', '').replace('₽', '').replace(' ', ''))
                    result_price += price
                else:
                    result_price += int(price.replace('₽', '').replace(' ', ''))
                prices.append(price)
                number_of_element += 1
            except:
                break

        print(result_price)

        names.extend(new_names)
        prices.extend(new_prices)
    else:
        print('else')
        result_price = 0
        names, prices = [], []

        number_of_element = 1

        while True:
            try:
                name = driver.find_element(By.XPATH,
                                           f'/html/body/div[5]/main/div[2]/div/form/main/div/div[{number_of_element}]/div/div[1]/div/div/a/div[1]').text
                #                                    f'/html/body/div[5]/main/div/div/form/main/div[2]/div[1]/div[3]/div[2]/div[1]/div/a/div[1]
                #                                     '/html/body/div[5]/main/div[2]/div/form/main/div/div[2]/div[2]/div[1]/div[3]/div[1]/span
                price = driver.find_element(By.XPATH,
                                            f'/html/body/div[5]/main/div[2]/div/form/main/div/div[{number_of_element}]/div/div[3]/div[1]/div').text
                print(name, price)
                # if name in names:
                # names.append(str(count) + '. ' + name)
                # count += 1
                # else:
                names.append(name)
                if '\n' in price:
                    two_elements = price.split('\n')
                    price = int(two_elements[1].replace('₽', '').replace(' ', '')) - int(
                        two_elements[0].replace('—', '').replace('₽', '').replace(' ', ''))
                    result_price += price
                else:
                    result_price += int(price.replace('₽', '').replace(' ', ''))
                prices.append(price)
                number_of_element += 1
            except:
                break

    return (names, prices, price_from_website)

