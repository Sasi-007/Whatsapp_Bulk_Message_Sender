from selenium import webdriver
import time
import pandas as pd

df = pd.read_csv('./Book3q.csv')

phone = df['MOBILENO']

chromeDriver = "/home/johny/Desktop/chromedriver"
driver = webdriver.Chrome(chromeDriver)
#driver.get('https://web.whatsapp.com/')
counter = 0
for name,ph in enumerate(phone):
    new_ph = '+91'+str(ph)
    new_ph = str(new_ph).split('.')[0]
    if '9829047517' in new_ph:
        continue
    print(' {} sending to {} at {}'.format(counter,name,new_ph))
    driver.get('https://web.whatsapp.com/send?phone={}&source=&data=#'.format(new_ph))
    if counter == 0:
        input('Press a button')
    counter += 1
    inv = False
    mes = False
    for k in range(60):
        try:
            msg_box = driver.find_element_by_class_name('_2S1VP')
            mes = True
            if mes == True:
                break
            invalid_button = driver.find_element_by_class_name('_1WZqU')
            invalid_button.click()
            inv = True
            break
        except Exception as e:
            print(str(e))
            try:
                invalid_button = driver.find_element_by_class_name('_1WZqU')
                invalid_button.click()
                inv = True
                break
            except Exception as oo:
                print(str(oo))

            time.sleep(1)
    if inv == True:
        continue


    msg = ' नमस्कार दोस्त ! अपने दोस्तों की  तरह SSC ,RRB exams में अपना score बढ़ाएं और all  India rank improve  करें . आज ही use करें Bodhi AI app . अपना free trial  लेने के लिए नीचे दिया गया promo code डालें : "WHATSAPP" .    Download Bodhi AI at http://bit.ly/2WDBIh8'
    #for n in range(5):
    #        try:
    #                msg_box = driver.find_element_by_class_name('_2S1VP')
    #                break
    #        except Exception as e:
    #                print(str(e))

    #                # send text message
    try:
        msg_box.send_keys(msg)
    except Exception as e:
        print(str(e))
        continue
    button = driver.find_element_by_class_name('_35EW6')
    button.click()	
    time.sleep(7)
    #attach_button = driver.find_element_by_xpath('//div[@title="Attach"]')
    #time.sleep(2)
    #attach_button.click()
    #files2_button = driver.find_element_by_xpath('//input[@type="file"]')
    #files2_button.send_keys('/home/prashant/Pictures/pamphlet.png')
    #time.sleep(3)
    #upload_button = driver.find_element_by_class_name('_3hV1n')
    #upload_button.click()

    #
    print('Message successfully sent at {}'.format(new_ph))
    #time.sleep(9)

