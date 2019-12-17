




import selenium
from selenium import webdriver
from selenium.webdriver.common import keys
import time
import re
from pyfiglet import Figlet
from selenium.webdriver.support.ui import Select


options = webdriver.ChromeOptions()
#options.add_argument("--start-maximized")
options.add_argument('--headless')
#options.add_argument('--disable-dev-shm-usage')


dr = webdriver.Chrome(executable_path = '/usr/bin/chromedriver' , chrome_options= options)

f = Figlet(font='slant')
print(f.renderText('BY : DEEPLOGIX'))


dr.get('https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
try:
    email = input('Please Enter your Email : ')
    password = input('Please Enter your Password : ')
    dr.find_element_by_id('identifierId').send_keys(email)
    time.sleep(2)
    dr.find_element_by_id('identifierNext').click()
    time.sleep(2)
    dr.find_element_by_css_selector('input[type*="password"]').send_keys(password)
    dr.find_element_by_id('passwordNext').click()
    print('Login Successful.....')
except Exception as e:
    print('Login Failed! , Please Try Again...')
time.sleep(2)
print("Processing....")
while True:
    try:
        for link in dr.find_elements_by_tag_name('tr[class*="zA zE"]'):
            link.click()
            a = dr.find_element_by_id(':1').text
            if re.search('Amount of travellers: 1',a) or re.search('Amount of travellers: 2',a) or re.search('Amount of travellers: 3',a) or re.search('Amount of travellers: 4',a):
                try:
                    time.sleep(4)
    #                     temp_url = dr.current_url
                    acc_button =  dr.find_element_by_link_text('ACCEPT')
                    time.sleep(2)
                    acc_button.click()
                    print('Congratulations!! PROPOSAL ACCEPTED---------------------------------------------------------------')
                    time.sleep(4)
                    print(dr.current_url)
                    time.sleep(5)
                    dr.switch_to_window(dr.window_handles[1])
                    dr.find_element_by_link_text('Go to bookings').click()
                    time.sleep(2)    
                    dr.find_element_by_link_text('Planned bookings (1)').click()
                    time.sleep(2)
                    for tr1 in dr.find_elements_by_tag_name('tr[class*="trhover"]'):
                        tr1.click()
                        time.sleep(2)
                        sel = Select(dr.find_element_by_css_selector('select[name*="userdriver_id"]'))
                        time.sleep(2)
                        sel.select_by_index(1)
                        time.sleep(2)
                        btn = dr.find_element_by_tag_name('input[id*="btnSubmit"]')
                        btn.click()
                        time.sleep(2)
                        dr.close()
                        break
                    dr.switch_to_window(dr.window_handles[0])
                except Exception as e:
                    print("Exception",e)
                    dr.switch_to_window(dr.window_handles[0])
                    pass
            else:
                try:
                    time.sleep(4)
                    dec_button = dr.find_element_by_link_text('DECLINE')
                    time.sleep(2)
                    dec_button.click()
                    print('PROPOSAL DECLINED-----------------------------------------------------------------------------------')
                    time.sleep(3)
                    dr.switch_to_window(dr.window_handles[1])
                    dr.close()
                    dr.switch_to_window(dr.window_handles[0])
                except Exception as e:
                    print("Exception",e)
                    dr.switch_to_window(dr.window_handles[0])
                    pass

            dr.back()
            time.sleep(3)
        dr.refresh()
    
    except Exception as e:
        print('Something Went Wrong! , Please Try again')
        print("Exception",e)
        pass








