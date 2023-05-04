import unittest
from src.main.enums.CommandType import CommandType
from src.main.model.Command import Command

class TestCommand(unittest.TestCase):

    def setUp(self):
        self.command = Command()

    def test_set_command_type(self):
        self.command._set_command_type(CommandType.ADD_COURSE_OFFERING)
        self.assertEqual(self.command._get_command_type(), CommandType.ADD_COURSE_OFFERING)

    def test_set_command_attributes(self):
        self.command._set_command_attributes("JAMES")
        self.assertEqual(self.command._get_command_attributes(), ["JAMES"])
        self.command._set_command_attributes("OFFERING-JAVA-JAMES")
        self.assertEqual(self.command._get_command_attributes(), ["JAMES", "OFFERING-JAVA-JAMES"])
