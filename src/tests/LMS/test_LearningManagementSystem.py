import unittest
from unittest.mock import MagicMock
from src.main.enums.CommandType import CommandType
from src.main.CmdExecutorFactory.commandExecutorFactory import CommandExecutorFactory
from src.main.LMS.LearningManagementSystem import LearningManagementSystem

class TestLearningManagementSystem(unittest.TestCase):
    
    def test_runCommand(self):
        lms = LearningManagementSystem()
        command = MagicMock()
        command._get_command_type.return_value = CommandType.ADD_COURSE_OFFERING
        command._get_command_attributes.return_value = ["Course Title", "Instructor", "2023-04-16", 10, 20]
        cmdExec = MagicMock()
        cmdExec.executeCommand = MagicMock()
        CommandExecutorFactory.create_command = MagicMock(return_value=cmdExec)
        
        lms.runCommand(command)
        
        CommandExecutorFactory.create_command.assert_called_once_with(CommandType.ADD_COURSE_OFFERING)
        cmdExec.executeCommand.assert_called_once_with(coursesDet = lms._coursesDet, regIDvsCourse = lms._regIDvsCourse, command_attributes = command._get_command_attributes())
