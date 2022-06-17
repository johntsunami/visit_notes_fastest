from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ChromeOptions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import InvalidSessionIdException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.select import Select
import winsound
from datetime import datetime
from datetime import date, timedelta

# Necessary setup for selenium
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
    "profile.default_content_setting_values.notifications": 2,
    # Change default directory for downloads
    "download.default_directory": "C:\\Users\\johnc\\Desktop\\HPDOWNLOADS",
    "download.prompt_for_download": False,  # To auto download the file
    # just click it and it will download it to this path for pdf's at least.
    "download.directory_upgrade": True,
    # It will not show PDF directly in chrome
    "plugins.always_open_pdf_externally": True,
})
driver = webdriver.Chrome(
    "C:/Users/johnc/chromedriver.exe", options=options)
actions = ActionChains(driver)


startTime = datetime.now()
today = date.today()
today = str(today)
# print("TOTAL TIME:", datetime.now() - startTime)

def sound():
    for i in range(2):
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)

def alert_sound():
    for i in range(3):
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

def perform_actions():
    """ Perform and reset actions """
    actions.perform()
    actions.reset_actions()
    for device in actions.w3c_actions.devices:
        device.clear_actions()

def find(self):

    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, self)))
    return driver.find_element(By.XPATH, self)

def load_page():
    url = driver.current_url
    driver.get(url)

def get_checked(xpath):  # don't put try statement on it because it wont go to correct one
    # sleep(.3) #1 second worked.. trying .3.  ITs needed
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    item = driver.find_element(By.XPATH, xpath)
    checked = item.get_attribute('checked')
    return checked  # returns true if checked

def press_enter():
    actions.send_keys(Keys.ENTER)
    perform_actions()

def find_allow_page_full_load(self):
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self)))
    return driver.find_element(By.XPATH, self)

def find_elements(xpath):
    WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath)))
    return driver.find_elements(By.XPATH, xpath)

def find_wait(self, wait):
    WebDriverWait(driver, wait).until(
        EC.element_to_be_clickable((By.XPATH, self)))
    return driver.find_element(By.XPATH, self)

def find_stale_element(self):
    p("Looking for stale element:", self)
    ignored_exceptions = (NoSuchElementException,
                          StaleElementReferenceException,)
    your_element = WebDriverWait(driver, 30, ignored_exceptions=ignored_exceptions)\
        .until(EC.presence_of_element_located((By.XPATH, self)))
    return driver.find_element(By.XPATH, self)

def move_to_element(xpath):
    ActionChains(driver).move_to_element(xpath)
    perform_actions()

def click_old(self, explicit_wait_seconds):
    # sleep(10)
    try:
        var = WebDriverWait(driver, explicit_wait_seconds).until(
            EC.element_to_be_clickable((By.XPATH, self)))
        # added the click here.
        ActionChains(driver).move_to_element(var).click()
        perform_actions()
        click_list.append("0")
        return driver.find_element(By.XPATH, self).click()
    except:
        try:
            sleep(1)  # 2 worked
            driver.find_element(By.XPATH, self).click()
            sleep(1)
            print('Part 1 click', self)
            click_list.append("1")
        except:
            try:
                driver.find_element(By.XPATH, self).click()
                print('Part 2 click', self)
                click_list.append("2")
            except:
                try:
                    element = find(self)
                    ActionChains(driver).move_to_element(element).click()
                    perform_actions()
                    print("part 3 click")
                    click_list.append("3")

                except Exception as e:
                    print("Find and click did not work:", self)
                    print("EXCEPTION: ", e)

def click(self):
    try:
        element = find(self)
        actions.move_to_element(element)

        actions.click(element)
        perform_actions()
        # print("first click worked")

    except:
        # print('def click not found on xplicit wait part 1', self)
        try:
            # 2 worked  #1 usually works but maybe not if internet is slow.
            sleep(2)
            driver.find_element(By.XPATH, self).click()
            sleep(1)
            # print("Sleeping on click")
        except:
            # print('def click trying to find xpath after a sleep', self)
            try:
                driver.find_element(By.XPATH, self).click()

            except:
                try:
                    element = find(self)
                    ActionChains(driver).move_to_element(element).click()
                    perform_actions()
                    print("CLICKED IT WORK")

                except Exception as e:
                    p("Find and click did not work:", self)
                    p("EXCEPTION: ", e)

def typing(xpath_to_type_in, num_of_backspaces, words_to_type):
    try:
        sleep(.2)  # was .5
        click(xpath_to_type_in)
        var = find(xpath_to_type_in)

        for i in range(num_of_backspaces):
            var.send_keys(Keys.BACKSPACE)

        var.send_keys(words_to_type)
        sleep(.5)

    except:
        p('exception typing sleep 1')
        pass
        try:
            click(xpath_to_type_in)
            sleep(1)
            # var = driver.find_element_by_xpath(xpath_to_type_in)
            var = driver.find_element(By.XPATH, xpath_to_type_in)
            var.send_keys(words_to_type)
            sleep(1)
        except:
            p('exception typing sleep 2')
            pass
            try:
                # click(xpath_to_type_in)
                sleep(2)
                p('a')
                var = find(xpath_to_type_in)
                var.send_keys(words_to_type)
                sleep(2)
            except:
                seq = driver.find_elements_by_tag_name('iframe')
                p("NUmbe of iframes:", len(seq))
                p('exception typing sleep 3: probably didnt click link before it or iframe changed. might need to inspect and search iframe to input that xpath into switch_iframe_function')
                sys.exit()

def typing_backarrow(xpath_to_type_in, num_of_right_arrows, words_to_type):
    sleep(.2)  # was .5
    click(xpath_to_type_in)
    var = find(xpath_to_type_in)

    for i in range(num_of_right_arrows):
        sleep(.1)
        var.send_keys(Keys.ARROW_RIGHT)

    for i in range(num_of_right_arrows*2):
        sleep(.1)
        var.send_keys(Keys.BACKSPACE)

    var.send_keys(words_to_type)
    sleep(.1)

def switch_to_new_window():
    p(driver.current_window_handle)
    p(driver.window_handles)

    try:
        # sleep(4)  # 2 worked but not all the time. #trying to remove this first sleep
        second_window = driver.window_handles[1]
        sleep(3)  # worked at 4
        driver.switch_to.window(second_window)
        sleep(3)  # works better slower, added this extra wait

    except:
        # p(driver.current_window_handle)
        # p('unable to switch to window after attempt 1')
        try:
            sleep(2)
            second_window = driver.window_handles[1]
            sleep(2)
            driver.switch_to.window(second_window)
            # sleep(4)
            p(driver.current_window_handle)
            p(driver.window_handles)
        except:

            pass
            try:
                # sleep(5)
                second_window = driver.window_handles[1]
                sleep(5)  # workd at 10
                driver.switch_to.window(second_window)
                sleep(5)

            except Exception as e:
                p("Switching to new 8687 window")
                p("EXCEPTION: ", e)
                p("Played sound")
                winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

def switch_to_old_window():
    try:
        # sleep(2)
        window_before = driver.window_handles[0]
        sleep(2)
        driver.switch_to.window(window_before)
        sleep(2)
    except:
        print("step22")
        pass
        try:
            sleep(4)
            window_before = driver.window_handles[0]
            sleep(4)
            driver.switch_to.window(window_before)
            sleep(4)
        except:
            p("Step33")
            pass
            try:
                # sleep(8)
                window_before = driver.window_handles[0]
                sleep(5)  # worked at 8
                driver.switch_to.windoww(window_before)
                sleep(5)
            except Exception as e:
                p("Switching to old98 window")
                p("EXCEPTION: ", e)
                p("Played sound")
                winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

def back(times):
    for i in range(times):
        driver.execute_script("window.history.go(-1)")
        sleep(.2)

def get_value(xpath):  # will come back 1 for one selection or another number for another one
    WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.XPATH, xpath)))
    item = driver.find_element(By.XPATH, xpath)
    return item.get_attribute('value')

def switch_iframe(xpath_to_iframe):
    seq = driver.find_elements_by_tag_name('iframe')
    p("NUmbe of iframes:", len(seq))
    iframe_xp = xpath_to_iframe
    iframe = find(iframe_xp)
    driver.switch_to.frame(iframe)
    p("USe this to close iframe and go back to original: driver.switch_to.default_content()")
    # then you have to close it

def get_all_values(xpath, printname):
    # print("loading sleep")
    # print(printname)
    data_dict = {}

    try:
        WebDriverWait(driver, .01).until(
            EC.visibility_of_element_located((By.XPATH, xpath)))
        item = driver.find_element(By.XPATH, xpath)
    except:
        data_dict[printname] = 'None'
        # print("DID NOT FIND: ", printname)
        return data_dict

    keyname = printname

    outer_html = item.get_attribute('outerHTML')
    # print(outer_html)

    if 'type="radio"' in outer_html:
        data = item.get_attribute('checked')

        # print("CHECKED1")
        # print(data)
        if data == None:
            data = 'None'

        data_dict[keyname] = data
        return data_dict

    if 'class="DrpItems10"' in outer_html:

        if 'select' in outer_html:

            try:
                select = Select(driver.find_element(
                    By.XPATH, xpath))  # does find work?
                selected_option = select.first_selected_option
                data = selected_option.text
                # print("FOUND SELECTED1", data)
                if data == None:
                    data = 'None'

                data_dict[keyname] = data
                # print("select returned dict and drpt")
                return data_dict
            except:
                print("passed dropdown")

    if 'select' in outer_html:
        # try:

        select = Select(driver.find_element(
            By.XPATH, xpath))  # does find work?
        selected_option = select.first_selected_option
        data = selected_option.text
        if data == None:
            data = 'None'
        # print("FOUND SELECTED1", data)
        data_dict[keyname] = data
        return data_dict
        # except:
        #     pass
        # print("passed dropdown22")

    data = item.get_attribute('value')
    # print("FOUND VALUE value")
    # print(data)

    if data == 'on':
        data = item.get_attribute('checked')

        # print("CHECKED2")
        print(data)
        if data == None:
            data = 'None'
        data_dict[keyname] = data
        return data_dict

    if data == '':
        pass
        # print("passing empty str")

    else:
        # print("TRYING TO APPEND IT...", keyname)
        data_dict[keyname] = data
        return data_dict

    data = item.get_attribute('checked')

    # print("CHECKEDc")
    print(data)

    data = item.text
    if data == None:
        data = 'None'

    data_dict[keyname] = data

    # print(" DONE  DONE DONE DONE DONE DONE ")
    # print("DATA_DICT: ", data_dict)

    return data_dict

def get_selected(xpath, print_name):
    try:
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, xpath)))
        select = Select(driver.find_element(
            By.XPATH, xpath))  # does find work?
        selected_option = select.first_selected_option
        selected = selected_option.text
        # print(print_name, "SELECTED ITEM:", selected)
        return selected
    except:
        try:
            stale_finder = find_stale_element(xpath)
            selected_option = stale_finder.first_selected_option
            selected = selected_option.text
        except:
            print("Trying to get value exception since get_selected failed")
            value = get_value(xpath)
            return value


###################################################################
### SPECIFIC TO HOSPICE MED PROGRAM
from login_info import *
from dictionaries import *
import sys
from time import sleep
from login_info import *


# from dateutil.parser import parse
import time
import os
from os import listdir
from os.path import isfile, join
import csv
import re
from dateutil import parser
from openpy_functions import apppend_list_of_dictionary_row,apppend_list_to_sheetname
import psycopg2


repaired = ''
idg_notes_list = []
findings = []
final_findings = []
all_data = []
click_list = []
visit_notes_list = []

def p(*args):
    running = False
    if running:
        print(*args)
        # print("Len:",len(args))
        # print("Type:",type(args))
        running = False

def add_char_every_certain_num_char_in_string(how_often_num, sentence):
    sentence2 = sentence.split()
    words_length = 0
    word_index = 0
    for word in sentence2:
        length = len(word)
        words_length += length
        word_index += 1
        # print("WORDS LENGTH:",words_length)
        if words_length > how_often_num:
            sentence2.insert(word_index, '\n')
            words_length = 0
        else:
            continue

    finished = ' '.join(sentence2)
    # print(finished)
    return finished

def add_dict(keyname, value):
    basic_dict = {}
    basic_dict[keyname] = value
    all_data.append(basic_dict)
    return
    
def get_lock_status():
    lock_status = ''
    status = find('//*[@id="ctl00_ContentPlaceHolder1_ImgProgressStatus"]')
    statusbar = status.get_attribute("title")
    print("STATUSBAR TITLE: ", statusbar)
    if 'Electronically Signed,' in statusbar:
        print("ITS LOCKED")
        lock_status = 'locked'
    else:
        lock_status = 'unlocked'

    return lock_status
# must use variable lock_status = unlock_note()
def unlock_note():
    print("------------unlocking-=-===")
    lock_status = get_lock_status()
    if lock_status == 'locked':
        print("-----------UNLOCKING NOTE------------------")
        unlock = '//*[@id="ctl00_ContentPlaceHolder1_btnUnlockNew"]'
        print("UNLOCKING")
        click(unlock)
        try:
            WebDriverWait(driver, 7).until(EC.alert_is_present(),
                                           'Timed out waiting for ' +
                                           'confirmation popup to appear.')
            alert = driver.switch_to.alert
            alert.accept()
            print("alert accepted")
        except:
            pass

    sleep(6)

    actions.send_keys(Keys.ENTER)
    perform_actions()
    # print("actions done")
    sleep(2)

    # find('//*[@id="ctl00_ContentPlaceHolder1_ImgExpandAll"]')
    click('//*[@id="ctl00_ContentPlaceHolder1_ImgExpandAll"]')
    # print("Expanded")
    sleep(6)

def lock_note():
    print("--------------lock_note_________________")
    lock_status = get_lock_status()
    if lock_status == "locked":
        try:
            print("Lockin it")
            lock = '//*[@id="ctl00_ContentPlaceHolder1_btnlockNew"]'
            find_wait(lock, 2)
            click(lock)
            sleep(4)
            actions.send_keys(Keys.ENTER)
            perform_actions()
        except:
            print("didn't need to lock")

    save_button = '//*[@id="ctl00_ContentPlaceHolder1_btnSave0"]'
    for i in range(2):
        click(save_button)
        sleep(.2)
    print("Pressed Save sleep4")
    sleep(4)

    repaired = 'yes'
    return repaired

def click_note(xp):
    print("--------------click note------------")
    unlock_note()
    click(xp)
    print("CLICKING NOTE")
    lock_note()
    repaired = 'yes'
    return repaired
    # sleep(30)

def type_note(xp, print_name):
    unlock_note()
    typing(xp, 8, print_name)
    lock_note()
    print("TYPED NOTE DID IT WORK ? SLEEPING 30")
    repaired = 'yes'
    return repaired
    # sleep(30)

def check_bp_range(bp):
    vs2 = bp.replace('/', "")
    diastolic = int(vs2[-2:])
    systolic = int(vs2[:-2])
    value = ''

    if systolic > 160:
        return "hypertensive"
        if systolic > 220:
            value = "hyper hyper Systolic bps " + bp

    elif systolic < 90:
        value = "hypotensive"
        if systolic < 40:
            value = "extra hypo systolic " + bp

    if diastolic > 100:
        value = "hypertensive"
        if diastolic > 180:
            value = "Very high diastolic " + bp

    elif diastolic < 50:
        value = "hypotensive"
        if diastolic < 35:
            value = "extra hypo diastolic " + bp

    return value

def click_idg():
    click('//*[@id="ctl00_TreeView1t15"]')

def click_visit_note_tab():
    click('//*[@id="ctl00_TreeView1t30"]')

def parse_assessments(list_of_dicts):
    add_to_write_list = ['visit_date','visit_type', 'date_of_qa', 'primary_dx','primary_disease','discipline','staff_assigned',  'temp','pulse','resp','bp','weight','mac','o2_sat','ambulation','toileting','trasfer','dressing','feeding','bathing']
    parse_findings = []
    write_list = []
    problem_list = []
    text_list = []
    print("checking for blank rows")


    def append_blank_row(*row_values):
        
        # convert list of dict to one dict
        result_dict = {}
        for d in list_of_dicts:
            # print(d)
            result_dict.update(d)

        count_num = 0
        row_len = len(row_values)
        for row in row_values:

            for key, value in result_dict.items():
                if row == key:

                    if value == 'None':
                        count_num += 1
                        # print("added")
                        # print("count_num:", count_num)
                        if count_num == row_len:
                            parse_findings.append("No selection on:" + row)
    append_blank_row('covid_screen_yes', 'covid_screen_no')
    append_blank_row('pt_report_pos_no','pt_report_pos_yes')
    append_blank_row('pain_controlled_yes', 'pain_controlled_no', 'pain_controlled_n/a')
    append_blank_row('pt_anxiety_none', 'pt_anxiety_mild', 'pt_anxiety_mod', 'pt_anxiety_sev')
    append_blank_row('depression_none', 'depression_mild', 'depression_mod', 'depression_sev')
    append_blank_row('agitation_none', 'agitation_mild', 'agitation_mod', 'agitation_sev')
    append_blank_row('confusion_none', 'confusion_mild', 'confusion_mod', 'confusion_sev')
    append_blank_row('speech_impair_none', 'speech_impair_mild', 'speech_impair_mod', 'speech_impair_sev')
    append_blank_row('other_neuro_none','other_neuro_mild','other_neuro_mod','other_neuro_sev')
    append_blank_row('arrhythmia_none', 'arrhythmia_mild', 'arrhythmia_mod', 'arrhythmia_sev')
    append_blank_row('edema_none', 'edema_mild', 'edema_mod', 'edema_sev')
    append_blank_row('chest_pain_none', 'chest_pain_mild', 'chest_pain_mod', 'chest_pain_sev')
    append_blank_row('cardio_other_none', 'cardio_other_mild', 'cardio_other_mod', 'cardio_other_sev')
    append_blank_row('infection_none', 'infection_mild', 'infection_mod', 'infection_sev')
    append_blank_row('nausea_none', 'nausea_mild', 'nausea_mod', 'nausea_sev')
    append_blank_row('vomiting_none', 'vomiting_mild', 'vomiting_mod', 'vomiting_sev')
    append_blank_row('constipation_none', 'constipation_mild', 'constipation_mod', 'constipation_sev')
    append_blank_row('diarrhea_none', 'diarrhea_mild', 'diarrhea_mod', 'diarrhea_sev')
    append_blank_row('gastro_other_none', 'gastro_other_mild', 'gastro_other_mod', 'gastro_other_sev')
    append_blank_row('percent_intake_none', 'percent_intake_mild', 'percent_intake_mod', 'percent_intake_sev')
    append_blank_row('nutrition_other_none', 'nutrition_other_mild', 'nutrition_other_mod', 'nutrition_other_sev')
    append_blank_row('blood_sugar_none', 'blood_sugar_mild', 'blood_sugar_mod', 'blood_sugar_sev')
    append_blank_row('endocrine_other_none', 'endocrine_other_mild', 'endocrine_other_mod', 'endocrine_other_sev')
    append_blank_row('urinary_problem_none', 'urinary_problem_mild', 'urinary_problem_mod', 'urinary_problem_sev')
    append_blank_row('urinary_other_symptom_none', 'urinary_other_symptom_mild', 'urinary_other_symptom_mod', 'urinary_other_symptom_sev')
    append_blank_row('insomnia_none', 'insomnia_mild', 'insomnia_mod', 'insomnia_sev')
    append_blank_row('somnolence_none', 'somnolence_mild', 'somnolence_mod', 'somnolence_sev')
    append_blank_row('sleep_other_none', 'sleep_other_mild', 'sleep_other_mod', 'sleep_other_sev')
    append_blank_row('muskulo_weakness_none', 'muskulo_weakness_mild', 'muskulo_weakness_mod', 'muskulo_weakness_sev')
    append_blank_row('muskulo_contracture_none', 'muskulo_contracture_mild', 'muskulo_contracture_mod', 'muskulo_contracture_sev')
    append_blank_row('muskulo_other_none', 'muskulo_other_mild', 'muskulo_other_mod', 'muskulo_other_sev')
    append_blank_row('rash_none', 'rash_mild', 'rash_mod', 'rash_sev')
    append_blank_row('wound_none', 'wound_mild', 'wound_mod', 'wound_sev')
    append_blank_row('ulcer_none', 'ulcer_mild', 'ulcer_mod', 'ulcer_sev')
    append_blank_row('other_skin_none', 'other_skin_mild', 'other_skin_mod', 'other_skin_sev')
    append_blank_row('any_fall_yes','any_fall_no')
    append_blank_row('change_in_safety_yes','change_in_safety_no')
    append_blank_row('update_family_yes','update_family_no')
    append_blank_row('update_cm_yes','update_cm_no')
    append_blank_row('comfort_pack_yes','comfort_pack_no')
    append_blank_row('dme_inspected_yes','dme_inspected_faulty')
    append_blank_row('check_foley_yes','check_foley_no','check_foley_n/a')
    append_blank_row('check_gi_tube_no','check_gi_tube_yes','check_gi_tube_n/a')
    append_blank_row('confirmed_sched_yes','confirmed_sched_no')
    append_blank_row('bp_sit','bp_lying','bp_standing')
    append_blank_row('mac_left','mac_right')

    


    for dictionary in list_of_dicts:
        for key, val in dictionary.items():

            for word in add_to_write_list:
                if key == word:
                    write_list.append(val)

            def append_if_wrong(key_name, correct_value):

                if key == key_name:
                    # print(key_name, val)
                    if val == correct_value:
                        pass
                    else:
                        parse_findings.append(key + " not selected.")
            append_if_wrong('form_type', '--Select One--')
            append_if_wrong('covid_screened_yes', 'true')
            append_if_wrong('pt_report_pos_no', 'true')
            append_if_wrong('covid_followed', 'true')
            append_if_wrong('utilized_ppe', 'true')
            append_if_wrong('physical_comfort', 'true')
            append_if_wrong('emotional_support','true')
            append_if_wrong('safety_instructions', 'true')
            append_if_wrong('environmental_needs', 'true')
            append_if_wrong('knowledge_related_needs','true')
            
        
            #### IF ANY ARE UNSELECTED IT NOTIFIES
            if key == 'form_type':
                pass

            else: 
                if val == '--Select One--':
                    parse_findings.append(key + " unselected")
            

            def if_true_add_problem_list():
                true_list = ['','increased_respiratory_distress','increased_fatigue','decreased_food_fluid_intake','decreased_bowel_bladder_function','decreased_loc','friction_problem','probably_inadequate_nutrition','very_poor_nutrition','slightly_limited_mobility','very_limited_mobility','completely_immobile','chairfast','bedfast','sensory_slightly_limited','sensory_very_limited','sensory_completely_limited','wound_skin_impairment_yes','skin_turgor_poor','skin_mottling','skin_jaundice','skin_diaphoretic','skin_cool','left_hemiparesis','right_hemiparesis','hemiparesis','left_hemiplegia','right_hemiplegia','hemiplegias','quadriplegia','paraplegia','contractures','prostheses','amputation','muscle_spasms','joint_swelling','muscle_weakness','rom_loss','muscle_rigidity','lack_of_sleep','excessive_sleep','sleep_insomnia','sleep_overly_drowsy','pacemaker','skin_cyanotic' ,'skin_pale','pitted_level_1','pitted_level_2','pitted_level_3','pitted_level_4','pitted_level_4_plus','edema_yes','cardiac_related_pain_yes','femoral_absent','femoral_brady','femoral_tachy','femoral_weak','femoral_regular','radial_absent','radial_brady','radial_tachy','radial_weak','radial_irregular','pedal_absent','pedal_tachy','pedal_pulse_irrigular','apical_tachy','apical_weak','apical_irreg','hypertension','hypotension','balance_impaired','hard_hearing','blind','limited_six_words','slurred_speech','aphasia','depression_hx','schizo_hx','ocd_hx','bipolar_hx','disoriented','coma','min_responsive','lethargic','tremors','sundowning','combative','seizure','depressed','agitated','restless','angry','anxious','confused','pt_uncomfortable_yes','lose_taste_yes','language_comm_needs','check_foley_yes','dme_inspected_faulty','comfort_pack_need','update_cm_no','update_family_no','change_in_safety_yes','pt_report_pos_yes','lose_taste','addit_concerns','pain_controlled_no','pain_controlled_n/a','artificially_fed_peg','artificially_fed_ng','artificially_fed_jtube','artificially_fed_pump','artificially_fed_tpn','artificially_fed_specify','ambu_max_assist','non_ambulatory','bedbound','non_ambu_max_assist','any_fall_yes']
                if val == 'true':
                
                    for item in true_list:
                        if key == item:
                            problem_list.append(key)

            if_true_add_problem_list()

            def print_txt_other():
                if 'txt' in key:
                  
                    if val == '':
                        pass
                    else:
                        print("KEY",key,val)
                        text_list.append(key + val)

                elif 'obs' in key:
                    if val == '':
                        pass
                    else:

                        text_list.append(key + val)
            print_txt_other()

            def parse_vitals():
                vital_list = ['temp','pulse','resp','bp','mac']
            
                if key in vital_list:
                    if val == '':
                        parse_findings.append('key' + 'is blank')
                    else:
                        pass

                try:
                    if key == 'bp':
                    
                        bp = val
                        bp = bp.split("/")
                        print(bp)
                        bp[0] = int(bp[0])
                        print(bp[0])
                        print("here")
                        if bp[0] >= 140:  # 140/90 up hyper  90/60
                            blood_pressure = "hypertensive"
                            print("hyper bp")
                            problem_list.append("pt bp hyper" + val)
                        elif bp[0] <= 90:
                            blood_pressure = "hypotensive"
                            print('hypo bp')
                            problem_list.append("pt bp hypo" + val)
                        elif bp[0] < 140 and bp[0] > 90:
                            blood_pressure = "normal"

                            print('normal bp')
                        else:
                            print("BP NOT FOUND")
                    
                    if key == 'temp':
                        temp = float(val)

                        if temp < 96.5:
                            print('low temp')
                            problem_list.append('low temp '+ val)

                        elif temp > 99:
                            print('high temp')
                            problem_list.append('high temp '+ val)

                        else:
                            print('temp ok')
                    
                    if key == 'pulse':
                        pulse = int(val)

                        if pulse < 55:
                            problem_list.append("Bradycardia pulse " + val)

                        elif pulse > 105:
                            problem_list.append("Tachycardia pulse " + val)
                    if key == 'resp':
                        
                        resp = int(val)

                        if resp < 10:
                            problem_list.append("pt has bradypnea "+ val)
                        elif resp > 22:
                            problem_list.append("pt has tachypnea "+ val)

                except:
                    print("missing vital maybe? it passed it")


    if len(problem_list) > 1: 
        list_to_string_newline = """{}""".format("\n".join(problem_list[0:]))
        write_list.append(list_to_string_newline)
    elif len(problem_list) == 1:
        shorter_str = shorten_str_newlines(problem_list[0])
        write_list.append(shorter_str)
    else:
        write_list.append(str(text_list))



    if len(text_list) > 1: 
        list_to_string_newline = """{}""".format("\n".join(text_list[0:]))
        write_list.append(list_to_string_newline)
    elif len(text_list) == 1:
        shorter_str = shorten_str_newlines(text_list[0])
      
        write_list.append(shorter_str)
    else:
        write_list.append(str(text_list))

    
    if len(parse_findings) > 1: 
        list_to_string_newline = """{}""".format("\n".join(parse_findings[0:]))
        write_list.append(list_to_string_newline)
    elif len(parse_findings) == 1:
        shorter_str = shorten_str_newlines(parse_findings[0])
       
        write_list.append(shorter_str)
    else:
        write_list.append(str(parse_findings))


  

    print("")
    print("write_list: ", write_list)
    print("")
    print("parse_findings", parse_findings)
    print("")
    print("problem_list",problem_list)
    print("")
    print('text_list',text_list)         
    return write_list

def parse_nurse_visit(list_of_dicts):
    add_to_write_list = ['visit_date','visit_type', 'date_of_qa', 'staff_assigned', 'discipline', 'temp','pulse','resp','bp','weight','mac','ambulation','toileting','trasfer','dressing','feeding','bathing']
    parse_findings = []
    write_list = []
    problem_list = []
    text_list = []
    print("checking for blank rows")
    def append_blank_row(*row_values):
        
        # convert list of dict to one dict
        result_dict = {}
        for d in list_of_dicts:
            # print(d)
            result_dict.update(d)

        count_num = 0
        row_len = len(row_values)
        for row in row_values:

            for key, value in result_dict.items():
                if row == key:

                    if value == 'None':
                        count_num += 1
                        # print("added")
                        # print("count_num:", count_num)
                        if count_num == row_len:
                            parse_findings.append("No selection on:" + row)
    append_blank_row('covid_screen_yes', 'covid_screen_no')
    append_blank_row('pt_report_pos_no','pt_report_pos_yes')
    append_blank_row('pain_controlled_yes', 'pain_controlled_no', 'pain_controlled_n/a')
    append_blank_row('pt_anxiety_none', 'pt_anxiety_mild', 'pt_anxiety_mod', 'pt_anxiety_sev')
    append_blank_row('depression_none', 'depression_mild', 'depression_mod', 'depression_sev')
    append_blank_row('agitation_none', 'agitation_mild', 'agitation_mod', 'agitation_sev')
    append_blank_row('confusion_none', 'confusion_mild', 'confusion_mod', 'confusion_sev')
    append_blank_row('speech_impair_none', 'speech_impair_mild', 'speech_impair_mod', 'speech_impair_sev')
    append_blank_row('other_neuro_none','other_neuro_mild','other_neuro_mod','other_neuro_sev')
    append_blank_row('arrhythmia_none', 'arrhythmia_mild', 'arrhythmia_mod', 'arrhythmia_sev')
    append_blank_row('edema_none', 'edema_mild', 'edema_mod', 'edema_sev')
    append_blank_row('chest_pain_none', 'chest_pain_mild', 'chest_pain_mod', 'chest_pain_sev')
    append_blank_row('cardio_other_none', 'cardio_other_mild', 'cardio_other_mod', 'cardio_other_sev')
    append_blank_row('infection_none', 'infection_mild', 'infection_mod', 'infection_sev')
    append_blank_row('nausea_none', 'nausea_mild', 'nausea_mod', 'nausea_sev')
    append_blank_row('vomiting_none', 'vomiting_mild', 'vomiting_mod', 'vomiting_sev')
    append_blank_row('constipation_none', 'constipation_mild', 'constipation_mod', 'constipation_sev')
    append_blank_row('diarrhea_none', 'diarrhea_mild', 'diarrhea_mod', 'diarrhea_sev')
    append_blank_row('gastro_other_none', 'gastro_other_mild', 'gastro_other_mod', 'gastro_other_sev')
    append_blank_row('percent_intake_none', 'percent_intake_mild', 'percent_intake_mod', 'percent_intake_sev')
    append_blank_row('nutrition_other_none', 'nutrition_other_mild', 'nutrition_other_mod', 'nutrition_other_sev')
    append_blank_row('blood_sugar_none', 'blood_sugar_mild', 'blood_sugar_mod', 'blood_sugar_sev')
    append_blank_row('endocrine_other_none', 'endocrine_other_mild', 'endocrine_other_mod', 'endocrine_other_sev')
    append_blank_row('urinary_problem_none', 'urinary_problem_mild', 'urinary_problem_mod', 'urinary_problem_sev')
    append_blank_row('urinary_other_symptom_none', 'urinary_other_symptom_mild', 'urinary_other_symptom_mod', 'urinary_other_symptom_sev')
    append_blank_row('insomnia_none', 'insomnia_mild', 'insomnia_mod', 'insomnia_sev')
    append_blank_row('somnolence_none', 'somnolence_mild', 'somnolence_mod', 'somnolence_sev')
    append_blank_row('sleep_other_none', 'sleep_other_mild', 'sleep_other_mod', 'sleep_other_sev')
    append_blank_row('muskulo_weakness_none', 'muskulo_weakness_mild', 'muskulo_weakness_mod', 'muskulo_weakness_sev')
    append_blank_row('muskulo_contracture_none', 'muskulo_contracture_mild', 'muskulo_contracture_mod', 'muskulo_contracture_sev')
    append_blank_row('muskulo_other_none', 'muskulo_other_mild', 'muskulo_other_mod', 'muskulo_other_sev')
    append_blank_row('rash_none', 'rash_mild', 'rash_mod', 'rash_sev')
    append_blank_row('wound_none', 'wound_mild', 'wound_mod', 'wound_sev')
    append_blank_row('ulcer_none', 'ulcer_mild', 'ulcer_mod', 'ulcer_sev')
    append_blank_row('other_skin_none', 'other_skin_mild', 'other_skin_mod', 'other_skin_sev')
    append_blank_row('any_fall_yes','any_fall_no')
    append_blank_row('change_in_safety_yes','change_in_safety_no')
    append_blank_row('update_family_yes','update_family_no')
    append_blank_row('update_cm_yes','update_cm_no')
    append_blank_row('comfort_pack_yes','comfort_pack_no')
    append_blank_row('dme_inspected_yes','dme_inspected_faulty')
    append_blank_row('check_foley_yes','check_foley_no','check_foley_n/a')
    append_blank_row('check_gi_tube_no','check_gi_tube_yes','check_gi_tube_n/a')
    append_blank_row('confirmed_sched_yes','confirmed_sched_no')
    append_blank_row('bp_sit','bp_lying','bp_standing')
    append_blank_row('mac_left','mac_right')

    


    for dictionary in list_of_dicts:
        for key, val in dictionary.items():

            for word in add_to_write_list:
                if key == word:
                    write_list.append(val)

            def append_if_wrong(key_name, correct_value):

                if key == key_name:
                    # print(key_name, val)
                    if val == correct_value:
                        pass
                    else:
                        parse_findings.append(key + " not selected.")
            append_if_wrong('form_type', '--Select One--')
            append_if_wrong('covid_screened_yes', 'true')
            append_if_wrong('pt_report_pos_no', 'true')
            append_if_wrong('covid_followed', 'true')
            append_if_wrong('utilized_ppe', 'true')
            append_if_wrong('physical_comfort', 'true')
            append_if_wrong('emotional_support','true')
            append_if_wrong('safety_instructions', 'true')
            append_if_wrong('environmental_needs', 'true')
            append_if_wrong('knowledge_related_needs','true')
            
            

       
            #### IF ANY ARE UNSELECTED IT NOTIFIES
            if key == 'form_type':
                pass

            else: 
                if val == '--Select One--':
                    parse_findings.append(key + " unselected")
            

            def if_true_add_problem_list():
                true_list = ['language_comm_needs','check_foley_yes','dme_inspected_faulty','comfort_pack_need','update_cm_no','update_family_no','change_in_safety_yes','pt_report_pos_yes','lose_taste','addit_concerns','pain_controlled_no','pain_controlled_n/a','artificially_fed_peg','artificially_fed_ng','artificially_fed_jtube','artificially_fed_pump','artificially_fed_tpn','artificially_fed_specify','ambu_max_assist','non_ambulatory','bedbound','non_ambu_max_assist','any_fall_yes']
                if val == 'true':

                    if 'mild' in key:
                        problem_list.append(key)

                    elif 'mod' in key:
                        problem_list.append(key)

                    elif 'sev' in key:
                        problem_list.append(key)

                
                    for item in true_list:
                        if key == item:
                            problem_list.append(key)

            if_true_add_problem_list()

            def print_txt_other():
                if 'txt' in key:
                  
                    if val == '':
                        pass
                    else:
                        print("KEY",key,val)
                        text_list.append(key + val)

                elif 'obs' in key:
                    if val == '':
                        pass
                    else:

                        text_list.append(key + val)
            print_txt_other()

            def parse_vitals():
                vital_list = ['temp','pulse','resp','bp','mac']
            
                if key in vital_list:
                    if val == '':
                        parse_findings.append('key' + 'is blank')
                    else:
                        pass

                try:
                    if key == 'bp':
                    
                        bp = val
                        bp = bp.split("/")
                        print(bp)
                        bp[0] = int(bp[0])
                        print(bp[0])
                        print("here")
                        if bp[0] >= 140:  # 140/90 up hyper  90/60
                            blood_pressure = "hypertensive"
                            print("hyper bp")
                            problem_list.append("pt bp hyper" + val)
                        elif bp[0] <= 90:
                            blood_pressure = "hypotensive"
                            print('hypo bp')
                            problem_list.append("pt bp hypo" + val)
                        elif bp[0] < 140 and bp[0] > 90:
                            blood_pressure = "normal"

                            print('normal bp')
                        else:
                            print("BP NOT FOUND")
                    
                    if key == 'temp':
                        temp = float(val)

                        if temp < 96.5:
                            print('low temp')
                            problem_list.append('low temp '+ val)

                        elif temp > 99:
                            print('high temp')
                            problem_list.append('high temp '+ val)

                        else:
                            print('temp ok')
                    
                    if key == 'pulse':
                        pulse = int(val)

                        if pulse < 55:
                            problem_list.append("Bradycardia pulse " + val)

                        elif pulse > 105:
                            problem_list.append("Tachycardia pulse " + val)
                    if key == 'resp':
                        
                        resp = int(val)

                        if resp < 10:
                            problem_list.append("pt has bradypnea "+ val)
                        elif resp > 22:
                            problem_list.append("pt has tachypnea "+ val)

                except:
                    print("missing vital maybe? it passed it")


    if len(problem_list) > 1: 
        list_to_string_newline = """{}""".format("\n".join(problem_list[0:]))
        write_list.append(list_to_string_newline)
    
    elif len(problem_list) == 1:
        shorter_str = shorten_str_newlines(text_list[0])
        write_list.append(shorter_str)
    else:
        write_list.append(str(problem_list))

    if len(text_list) > 1: 
        list_to_string_newline = """{}""".format("\n".join(text_list[0:]))
        write_list.append(list_to_string_newline)
    elif len(text_list) == 1:
        shorter_str = shorten_str_newlines(text_list[0])
        write_list.append(shorter_str)
    else:
        write_list.append(str(text_list))

    
    if len(parse_findings) > 1: 
        list_to_string_newline = """{}""".format("\n".join(parse_findings[0:]))
        write_list.append(list_to_string_newline)
    elif len(parse_findings) == 1:
        shorter_str = shorten_str_newlines(parse_findings[0])
        write_list.append(shorter_str)
    else:
        write_list.append(str(parse_findings))


  

    print("")
    print("write_list: ", write_list)
    print("")
    print("parse_findings", parse_findings)
    print("")
    print("problem_list",problem_list)
    print("")
    print('text_list',text_list)         
    return write_list

def parse_sw_list(list_of_dicts):
    add_to_write_list = ['visit_date', 'visit_type','date_of_qa', 'staff_assigned', 'discipline']
    parse_findings = []
    write_list = []
    problem_list = []
    text_list = []
    print("checking for blank rows")
    def append_blank_row(*row_values):
        
        # convert list of dict to one dict
        result_dict = {}
        for d in list_of_dicts:
            # print(d)
            result_dict.update(d)

        count_num = 0
        row_len = len(row_values)
        for row in row_values:

            for key, value in result_dict.items():
                if row == key:

                    if value == 'None':
                        count_num += 1
                        # print("added")
                        # print("count_num:", count_num)
                        if count_num == row_len:
                            parse_findings.append("No selection on:" + row)
    append_blank_row('covid_screen_yes', 'covid_screen_no')
    append_blank_row('pt_report_pos_no','pt_report_pos_yes')
    append_blank_row('pain_controlled_yes', 'pain_controlled_no', 'pain_controlled_n/a')
    append_blank_row('pt_anxiety_none', 'pt_anxiety_mild', 'pt_anxiety_mod', 'pt_anxiety_sev')

  
    


    for dictionary in list_of_dicts:
        for key, val in dictionary.items():

            for word in add_to_write_list:
                if key == word:
                    write_list.append(val)

            def append_if_wrong(key_name, correct_value):

                if key == key_name:
                    # print(key_name, val)
                    if val == correct_value:
                        pass
                    else:
                        parse_findings.append(key + " not selected.")
            append_if_wrong('form_type', '--Select One--')
            append_if_wrong('covid_screened_yes', 'true')
            append_if_wrong('pt_report_pos_no', 'true')
            append_if_wrong('covid_followed', 'true')
            append_if_wrong('utilized_ppe', 'true')
            append_if_wrong('physical_comfort', 'true')
            append_if_wrong('emotional_support','true')
            append_if_wrong('safety_instructions', 'true')
            append_if_wrong('environmental_needs', 'true')
            append_if_wrong('knowledge_related_needs','true')
            
            

       
            #### IF ANY ARE UNSELECTED IT NOTIFIES
            if key == 'form_type':
                pass

            else: 
                if val == '--Select One--':
                    parse_findings.append(key + " unselected")
            

            def if_true_add_problem_list():
                true_list = ['language_comm_needs','pt_report_pos_yes','pain_controlled_no','pain_controlled_n/a']
                if val == 'true':

                    if 'mild' in key:
                        problem_list.append(key)

                    elif 'mod' in key:
                        problem_list.append(key)

                    elif 'sev' in key:
                        problem_list.append(key)

                
                    for item in true_list:
                        if key == item:
                            problem_list.append(key)

            if_true_add_problem_list()

            def print_txt_other():
                if 'txt' in key:
                  
                    if val == '':
                        pass
                    else:
                        if val != 'None':
                            print("KEY",key,val)
                            text_list.append(key + val)
                        else:
                            pass

                elif 'obs' in key:
                    if val == '':
                        pass
                    else:

                        text_list.append(key + val)
            print_txt_other()

        
    if len(problem_list) > 1: 
        list_to_string_newline = """{}""".format("\n".join(problem_list[0:]))

        write_list.append(list_to_string_newline)
    elif len(parse_findings) == 1:
        shorter_str = shorten_str_newlines(problem_list[0])
        write_list.append(shorter_str)
    else:
        write_list.append(str(problem_list))


    if len(text_list) > 1: 
        list_to_string_newline = """{}""".format("\n".join(text_list[0:]))
        write_list.append(list_to_string_newline)
    elif len(text_list) == 1:
        shorter_str = shorten_str_newlines(text_list[0])
        write_list.append(shorter_str)
    else:
        write_list.append(str(text_list))

    
    if len(parse_findings) > 1: 
        list_to_string_newline = """{}""".format("\n".join(parse_findings[0:]))
        write_list.append(list_to_string_newline)
    elif len(parse_findings) == 1:
        shorter_str = shorten_str_newlines(parse_findings[0])
        write_list.append(shorter_str)
    else:
        write_list.append(str(parse_findings))


    print("")
    print("write_list: ", write_list)
    print("")
    print("parse_findings", parse_findings)
    print("")
    print("problem_list",problem_list)
    print("")
    print('text_list',text_list)         
    return write_list

def shorten_str_newlines(sentence):  #30 is good for excel
    sentence2 = sentence.split()
    words_length = 0
    word_index = 0
    for word in sentence2:
        length = len(word)
        words_length += length
        word_index += 1
        # print("WORDS LENGTH:",words_length)
        if words_length > 45:
            sentence2.insert(word_index, '\n')  
            words_length = 0 
        else:
            continue
    
    finished = ' '.join(sentence2) 
    # print(finished)
    return finished

def expand_assessment_tab():
    expand_assessment_xp = "//a[@id='ctl00_TreeView1n7']"
    click(expand_assessment_xp)

def click_nursing():
    nursing_xp = "//*[text()='Nursing']"
    click(nursing_xp)

def open_comprehensive_assessment():
    print("opening comprehensive")
    open_comprehensive_xp = "(//*[text()='Comprehensive']/preceding-sibling::td)[1]"
    open_comp_for_pt_german = '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[10]/td[1]/input'
    try:
        click(open_comprehensive_xp)
        expand_all_ass_tabs = "//*[@id='ctl00_ContentPlaceHolder1_ImgExpandAll']"
        click(expand_all_ass_tabs)
    except:
        click(open_comp_for_pt_german)
        click(expand_all_ass_tabs)

def expand_once_comp_opened():  # second one in case first one didn't work
    expand_all_ass_tabs = "//*[@id='ctl00_ContentPlaceHolder1_ImgExpandAll']"
    click(expand_all_ass_tabs)

def search_pt():
    search_pt = "//input[@name='ctl00$TopSearch$txtSearch']"
    typing(search_pt, 0, pt_name)
    sleep(1)
    actions.send_keys(Keys.ENTER)
    # print("pressed Enter")
    perform_actions()

############### MAIN FLOW #################


def login_hospice():
    p("_---------------------LOGIN_HOSPICE----------------------")
    driver.get("https://hospicemd.com/")
    driver.maximize_window()

    login = """//input[@name="LoginIdtxtbox"]"""

    typing(login, 0, login_name)

    pw = """//input[@name="Passwordtxtbox"]"""
    typing(pw, 0, password)
    login = """//input[@name="loginbut"]"""
    click(login)
    search_pt()

def find_soc():
    expand_assessment_xp = "//a[@id='ctl00_TreeView1n7']"
    click(expand_assessment_xp)

    nursing_xp = "//*[text()='Nursing']"
    click(nursing_xp)

    print("opening comprehensive")
    open_comprehensive_xp = "(//*[text()='Comprehensive']/preceding-sibling::td)[2]"
    click(open_comprehensive_xp)

    soc = find(open_comprehensive_xp)
    soc = soc.text
    print("SOC:", soc)
    add_dict('soc', soc)
    return soc

def find_dx():
    dx_dict = {}
    print("opening comprehensive to get dx")
    open_comprehensive_xp = "(//*[text()='Comprehensive']/preceding-sibling::td)[1]"
    open_comp_for_pt_german = '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[10]/td[1]/input'
    try:
        click(open_comprehensive_xp)
        expand_all_ass_tabs = "//*[@id='ctl00_ContentPlaceHolder1_ImgExpandAll']"
        click(expand_all_ass_tabs)

    except:
        click(open_comp_for_pt_german)
        click(expand_all_ass_tabs)

    expand_all_ass_tabs = "//*[@id='ctl00_ContentPlaceHolder1_ImgExpandAll']"
    click(expand_all_ass_tabs)
    dx = get_selected(
        '//*[@id="ctl00_ContentPlaceHolder1_DrpPDDisease0"]', 'Diagnosis')
    add_dict('dx', dx)
    return dx

def check_missing_visits(start_date):
    print("CHECKING MISSING VISITS")
    reports = click('//*[@id="ctl00_HyperLink1"]')
    missing_visits = click('//*[@id="ctl00_ContentPlaceHolder1_MVisits"]')
    sleep(1)

    from_ = typing_backarrow(
        '//*[@id="ctl00_ContentPlaceHolder1_txtfrom"]', 20, start_date)
    sleep(1)
    submit = click('//*[@id="ctl00_ContentPlaceHolder1_btnSearch"]')
    start_date_rows = '/html/body/form/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/div/table/tbody/tr/td/div/div[1]/div/div[*]/table/tbody/tr/td[2]/span'
    try:
        start_dates = find_elements(start_date_rows)
    except:
        print("No missing visits found")
        return  # because if their are none it will skip function

    rows_num = len(start_dates)

    names_num = 2
    iterate_num = 1
    expand_num = 1  # this one goes up +3 each time since element isn't read on every number
    for i in range(rows_num):
        expander = f'/html/body/form/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/div/table/tbody/tr/td/div/div[1]/div/div[{expand_num}]/table/tbody/tr/td[15]/img'
        click(expander)
        expand_num += 3
        sleep(.3)

    # FIND NAME

    ### TRYING TO SEE IF I CAN PRINT NAMES AND DATES ##
    all_rows = find_elements(
        '/html/body/form/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/div/table/tbody/tr/td/div/div[1]/div/div')
    for row in all_rows:
        row_text = row.text

        potential_date_row = row_text[:3]
        # print("potential_date_row",potential_date_row)

        try:
            potential_date_row = int(potential_date_row)
            dates = row_text
            # print("DATES:",dates)
        except:
            pass

        if pt_name in row_text:
            findings.append("Missing Visit Notes" + dates[4:-13])
            print("FOUND MISSING NOTES AND ADDED TO FINDING")

def gather_nurse_assessment_data():
    
    print("-------------Gather comp baseline -------------")
    search_pt()
    expand_assessment_tab()
    click_nursing()

    # GO TO COMP or recert if there is recert

       # PICK MOST RECENT RECERT IF THERE IS ONE>
    try:
        assessment = click(
            '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[2]/td[1]/input')
        expand_once_comp_opened()
    except:
        findings.append("No Nurse Assessment Found")
        print("No assessment found")

    nurse_assessment_list = []
    nurse_assessment_list.insert(1, {'visit_type': "Assessment"})
    nurse_assessment_list.insert(2, {'date_of_qa': today})

    current_url = driver.current_url
    driver.get(current_url)
    print("got current url", current_url)

    for key, value in assessment_xp_dict.items():
        assessment_dict = get_all_values(value, key)
        nurse_assessment_list.append(assessment_dict)

    assessment_list = parse_assessments(nurse_assessment_list)

    print("Assessment_list",assessment_list)

    heading = ['VISIT TYPE','Date of Visit','Person','Discipline','Temp','Pulse','Resp','BP','Weight','MAC','Ambulation','Toileting','Bathing or baseline','Text Info','Findings','Assessessment Baseline','Assessment Text','Assessment Findings']
    apppend_list_to_sheetname(heading,pt_name)
    apppend_list_to_sheetname(assessment_list,pt_name)
    

    return nurse_assessment_list


def add_value_list(listname):
    print("LIST IS HERE +++++++++++++")
    print(listname)
    for i in range(10):   # THIS IS NEEDED TO PUT THE FINDINGS IN THE S COLUMN ON SHEET
            listname.insert(-1, 'none')

def gather_visit_notes_data():
    open_visit_notes = click('//*[@id="ctl00_TreeView1t30"]')

    visit_notes_page_one = find_elements(
        '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[*]/td[1]/input')
    # num_notes = len(visit_notes_page_one)
    num_notes = 2
    # visit_notes_list = []
    for visit_notes in visit_notes_page_one:
        print("num_notes", num_notes)

        visit_note = click(
            f'//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[{num_notes}]/td[1]/input')
        num_notes += 1

        expand_all = click('//*[@id="ctl00_ContentPlaceHolder1_ImgExpandAll"]')

        current_url = driver.current_url
        driver.get(current_url)

        print("got current url", current_url)

        discipline = get_selected(
            '//*[@id="ctl00_ContentPlaceHolder1_DropDiscipline"]', 'discipline')
        print('discipline: ', discipline)

        visit_list = []
        visit_list.insert(1, {'visit_type': "Visit"})  # THIS WAS FORWARD ONE
        visit_list.insert(2, {'date_of_qa': str(today)})  # THIS WAS FORWARD ONE

        if discipline == 'BSW' or discipline == 'MSW' or discipline == 'SW':
            print("Gathering info for bsw")
            
            for key, value in visit_dict_sw.items():
                assessment_dict = get_all_values(value, key)

                visit_list.append(assessment_dict)
  
            write_list = parse_sw_list(visit_list)

            add_value_list(write_list)

            
        elif discipline == 'LVN':
            print("Gathering LVN info")
            
            for key, value in visit_dict_lvn.items():
                assessment_dict = get_all_values(value, key)
                visit_list.append(assessment_dict)
                
            write_list =parse_nurse_visit(visit_list)
   

        elif discipline == 'RN':
            print("Gathering info RN")
         
            for key, value in visit_dict_rn.items():
                assessment_dict = get_all_values(value, key)
                visit_list.append(assessment_dict)

            write_list =parse_nurse_visit(visit_list)
        
        
        elif discipline == 'SC':  ## NEED TO MODIFY THIS PARSING>
            print("Gathering SC INFO")

            for key, value in visit_dict_sw.items():
                assessment_dict = get_all_values(value, key)
                visit_list.append(assessment_dict)
            write_list = parse_sw_list(visit_list)

            
            add_value_list(write_list)  # alligns the columns
            
        else:
            print("ERROR NO DISCIPLINE NOTED:")
            

        print("visit_list",visit_list)

    



        apppend_list_to_sheetname(write_list,pt_name)
        
        visit_notes_list.append(visit_list)
        print("Reopening visit notes to gather info.")
        click('//*[@id="ctl00_TreeView1t30"]')

    return visit_notes_list

def get_idg_data():
    idg = click('//*[@id="ctl00_TreeView1t15"]')
    idgs = find_elements(
        '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[*]/td[1]/input')
    num_notes = 2
    # visit_notes_list = []
    for idg in idgs:
        if num_notes <= 5:  # limiting it to first 3 idg
            idg_note = click(
                f'//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[{num_notes}]/td[1]/input')
            num_notes += 1

            expand_idg_discussion = click(
                '//*[@id="ctl00_ContentPlaceHolder1_ImgPnlComment"]')
            current_url = driver.current_url
            driver.get(current_url)
            print("got current url", current_url)

            # sleep(10)
            idg_list = [] 
            idg_list.insert(1, {'visit_type': "IDG"})  # THIS WAS FORWARD ONE
            idg_list.insert(2, {'date_of_qa': str(today)})

            for key, value in idg_notes_xp_dict.items():
                idg_dict = get_all_values(value, key)
                idg_list.append(idg_dict)
                
            idg_notes_list.append(idg_list)

            print("Reopening idg notes to gather info.")
            click('//*[@id="ctl00_TreeView1t15"]')
    for idg in idg_notes_list:
        apppend_list_of_dictionary_row(idg,pt_name)
    return idg_notes_list







