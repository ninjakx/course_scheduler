"""
    It will extract commands from the text file content and push it 
    into the command list and command type
"""

from src.main.model.Command import Command
from src.main.enums.CommandType import CommandType
from src.main.constants import constant
class CommandExtractorMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class CommandExtractor(metaclass=CommandExtractorMeta):
    def extract_command(self, input_line)->Command:
        __word = input_line.split()
        __command_type = __word[0]
        __command_attrib = __word[1:]
        _command = Command()
        if (not self.__validate_no_of_parameters(__command_type, __command_attrib)):
            return _command
        self.__set_command_type(_command, __command_type)
        self.__set_command_attributes(_command, __command_attrib)
        return _command

    def __set_command_type(self, command, command_type):
        command._set_command_type(command_type)

    def __set_command_attributes(self, command, command_attributes):
        for command_attrib in command_attributes:
            command._set_command_attributes(command_attrib)

    def __validate_no_of_parameters(self, command_type, command_attributes)->bool:
        command_type = command_type.replace('-','_')
        if (CommandType[command_type].value!=len(command_attributes)):
            print(f"{constant.INPUT_DATA_ERROR}")
            return False
        else:
            return True
