from src.main.enums.CommandType import CommandType

class Command:
    def __init__(self):
       self.__command_attributes = list() # details
       self.__command_type = None

    def _get_command_attributes(self)->dict:
        return self.__command_attributes
    
    def _get_command_type(self)->CommandType:
        return self.__command_type
    
    def _set_command_type(self, command_type:CommandType):
        self.__command_type = command_type

    def _set_command_attributes(self, command_attrib:str)->list:
        self.__command_attributes.append(command_attrib)