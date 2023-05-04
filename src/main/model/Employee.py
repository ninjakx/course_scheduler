import re

from src.main.constants import constant

class Employee:
    def __init__(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        self.__email = email
        self.__name = ""
        if (re.fullmatch(regex, email)):
            self.__name = email.split("@")[0]

    def _get_name(self)->str:
        # if self.__name=="":
        #     return constant.INPUT_DATA_ERROR
        return self.__name
    
    def _get_email(self):
        return self.__email
