import configparser

config = configparser.RawConfigParser()
config.read("./Configuration/config.ini")


class ReadConfig:

    @staticmethod
    def get_application_url():
        url = config.get("common_info", "base_url")
        return url

    @staticmethod
    def basic_auth_user():
        user = config.get('basic_Authorization', 'user')
        return user

    @staticmethod
    def basic_auth_pwd():
        pwd = config.get('basic_Authorization', 'pwd')
        return pwd

