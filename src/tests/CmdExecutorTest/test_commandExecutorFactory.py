import unittest
from src.main.CmdExecutorFactory.commandExecutorFactory import CommandExecutorFactory
from src.main.controller.implementation.AddCourseCmdExecutor import AddCourseCmdExecutor
from src.main.controller.implementation.RegisterCourseCmdExecutor import RegisterCourseCmdExecutor
from src.main.controller.implementation.AllotCourseCmdExecutor import AllotCourseCmdExecutor
from src.main.controller.implementation.CancelCourseCmdExecutor import CancelCourseCmdExecutor

class TestCommandExecutorFactory(unittest.TestCase):

    def setUp(self):
        self.factory = CommandExecutorFactory()

    def test_create_command_with_valid_command_name(self):
        add_command = self.factory.create_command("ADD_COURSE_OFFERING")
        self.assertIsInstance(add_command, AddCourseCmdExecutor)
        register_command = self.factory.create_command("REGISTER")
        self.assertIsInstance(register_command, RegisterCourseCmdExecutor)
        allot_command = self.factory.create_command("ALLOT")
        self.assertIsInstance(allot_command, AllotCourseCmdExecutor)
        cancel_command = self.factory.create_command("CANCEL")
        self.assertIsInstance(cancel_command, CancelCourseCmdExecutor)

    def test_create_command_with_invalid_command_name(self):
        invalid_command = self.factory.create_command("invalid-command")
        self.assertIsNone(invalid_command)
