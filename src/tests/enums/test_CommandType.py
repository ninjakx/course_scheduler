import unittest
from aenum import NoAlias
from src.main.enums.CommandType import CommandType

class TestCommandType(unittest.TestCase):
    def test_command_type_values(self):
        self.assertEqual(CommandType.ADD_COURSE_OFFERING.value, 5)
        self.assertEqual(CommandType.REGISTER.value, 2)
        self.assertEqual(CommandType.ALLOT.value, 1)
        self.assertEqual(CommandType.CANCEL.value, 1)
        
    def test_command_type_name(self):
        self.assertEqual(CommandType.ADD_COURSE_OFFERING.name, "ADD_COURSE_OFFERING")
        self.assertEqual(CommandType.REGISTER.name, "REGISTER")
        self.assertEqual(CommandType.ALLOT.name, "ALLOT")
        self.assertEqual(CommandType.CANCEL.name, "CANCEL")

if __name__ == '__main__':
    unittest.main()
