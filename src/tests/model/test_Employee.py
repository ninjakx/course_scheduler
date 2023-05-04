import unittest
from src.main.model.Employee import Employee

class TestEmployee(unittest.TestCase):

    def test_get_name(self):
        # Test case when valid email is given
        employee1 = Employee("LILY@GMAIL.COM")
        self.assertEqual(employee1._get_name(), "LILY")

        # Test case when invalid email is given
        employee2 = Employee("invalid-email")
        self.assertEqual(employee2._get_name(), "")

    def test_get_email(self):
        employee = Employee("LILY@GMAIL.COM")
        self.assertEqual(employee._get_email(), "LILY@GMAIL.COM")

if __name__ == '__main__':
    unittest.main()
