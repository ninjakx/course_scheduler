
from collections import OrderedDict
from src.main.CmdExecutorFactory.commandExecutorFactory import CommandExecutorFactory
from src.main.constants import constant

class LearningManagementSystem:
    # For allocation we want to keep track of offering courses via courseDet
    # Registered user taken the course will be kept in the map 
    # this will help in keeping the registered course taken by the employee and also fetch the details
    _regIDvsCourse = dict()
    _coursesDet = OrderedDict()

    def runCommand(self, command):
        cmdExec = CommandExecutorFactory().create_command(command._get_command_type())
        try:
            cmdExec.executeCommand(coursesDet = self._coursesDet, regIDvsCourse = self._regIDvsCourse, command_attributes = command._get_command_attributes())
        except Exception as e:
            print(constant.INPUT_DATA_ERROR)
        
        