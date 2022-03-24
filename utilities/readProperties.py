import configparser

config = configparser.RawConfigParser()
config.read("./configurations/config.ini")


class ReadConfig:
    @staticmethod
    def get_url():
        url = config.get("common info", "baseUrl")
        return url

    @staticmethod
    def get_user_email():
        user_email = config.get("common info", "user_email")
        return user_email

    @staticmethod
    def get_password():
        password = config.get("common info", "password")
        return password
