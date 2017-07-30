# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""
def save_password():
    # optionボタンをクリック
    Option_button = drive.find_element_by_link_id('prefsButton')
    Option_button.click()

    # Export save ボタンをクリック
    Export_save_button = driver.find_element_by_link_text('Export save')
    Export_save_button.click()

    # 'w' : 書き込みモード, 'a' : 追記モード
    my_password_file = open('/Users/Polaris/CSPython/cokieClicker/password.txt', 'w')

    # 新しいパスワードをpassword_fileに書き込む
    Generated_password = driver.find_element_by_id('textareaPrompt')
    password_file.write(Generated_password)
    # password_fileを閉じる
    password_file.close()
"""

"""
def load_password():
    # optionボタンをクリック
    # ToDo : Option_buttonをクリックできるようにする
    Option_button = driver.find_element_by_id('prefsButton')
    Option_button.click()

    # Import saveボタンをクリック
    Import_save_button = driver.find_element_by_link_text('Import save')
    Import_save_button.click()

    # パスワードを保存しておいたファイル名を取得
    my_password_file = open('/Users/Polaris/CSPython/cokieClicker/password.txt')
    # 保存しておいたパスワードを取得
    my_password = my_password_file.read()

    # パスワードを入力
    my_pass_form = driver.find_element_by_link_id('textareaPrompt')
    my_pass_form.send_keys(my_password)
    my_pass_form.submit()
"""

# Choose from 'Firefox' or 'Chrome'
driver = webdriver.Chrome()

# go to cookie clicker
driver.get("http://orteil.dashnet.org/cookieclicker/")

# パスワードをロードする
#load_password()

# ウィンドウの最小化(高速化)
#driver.minimum_window()

# クッキーをひたすらクリック
while 1:
    Cookie = driver.find_element_by_id('bigCookie')
    Cookie.click()

#今んとこターミナル場でCtrl-cで終了するか、ブラウザ閉じるか
# driver.close()
