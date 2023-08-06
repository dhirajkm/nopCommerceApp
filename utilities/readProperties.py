import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig:
        @staticmethod
        def getApplicationURL():
            url = config.get('common info','baseUrl')
            return url

        @staticmethod
        def getUseremail():
            userEmail = config.get('common info','username')
            return userEmail

        @staticmethod
        def getUserpassword():
            userPassword = config.get('common info', 'password')
            return userPassword



