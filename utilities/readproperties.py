import configparser

config = configparser.RawConfigParser()
config.read("./Configuration/config.ini")


class ReadConfig:

    @staticmethod
    def get_application_url():
        url = config.get("common_info", "base_url")
        return url

    @staticmethod
    def basic_auth_valid_user():
        user = config.get('basic_Authorization', 'valid_user')
        return user

    @staticmethod
    def basic_auth_valid_pwd():
        pwd = config.get('basic_Authorization', 'valid_pwd')
        return pwd

    @staticmethod
    def basic_auth_invalid_user():
        user = config.get('basic_Authorization', 'invalid_user')
        return user

    @staticmethod
    def basic_auth_invalid_pwd():
        pwd = config.get('basic_Authorization', 'invalid_pwd')
        return pwd

    @staticmethod
    def no_of_clicks_add_element():
        clicks = config.get('Add Element', 'no_of_clicks')
        return int(clicks)
