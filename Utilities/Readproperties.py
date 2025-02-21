import configparser

config = configparser.ConfigParser()
config.read("C:/Users/91990/PycharmProjects/pythonProject/Configurations/config.ini")


# print(config.getuserEmail())


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        baseURL = config.get('common info', 'baseURL')
        return baseURL
