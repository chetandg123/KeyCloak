import configparser
from selenium import webdriver
from Data.parameters import Data
from get_dir import pwd


class GetData():
    def __init__(self):
         self.p = pwd()

    def get_domain_name(self):
        config = configparser.ConfigParser()
        config.read(self.p.get_config_ini_path())
        return config['config']['domain']

    def get_username(self):
        config = configparser.ConfigParser()
        config.read(self.p.get_config_ini_path())
        return config['config']['username']

    def get_password(self):
        config = configparser.ConfigParser()
        config.read(self.p.get_config_ini_path())
        return config['config']['password']

    def get_driver(self):
        options = webdriver.ChromeOptions()
        # prefs = {'download.default_directory': self.p.get_download_dir()}
        # options.add_experimental_option('prefs', prefs)
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options, executable_path=self.p.get_driver_path())
        return self.driver

    def open_cqube_appln(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get(self.get_domain_name())
        self.driver.implicitly_wait(60)

    def login_cqube(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_id(Data.email).send_keys(self.get_username())
        self.driver.find_element_by_id(Data.passwd).send_keys(self.get_password())
        self.driver.find_element_by_id(Data.login).click()

