import unittest
from src.main.model.Course import Course
from src.main.model.Employee import Employee

class TestCourse(unittest.TestCase):

    def setUp(self):
        self.course = Course("JAVA", "JAMES", "15062022", 1, 2)
        self.employee = Employee("ALICE@GMAIL.COM")
        self.reg_id = f"REG-COURSE-{self.employee._get_name()}-{self.course._get_course_title()}"

    def test_register_employee(self):
        self.assertEqual(len(self.course._get_registered_employees()), 0)
        self.course._register_employee(self.employee)
        self.assertEqual(len(self.course._get_registered_employees()), 1)
        self.assertEqual(self.course._get_registered_employees()[0]._get_employee()._get_name(), "ALICE")
        self.assertEqual(self.course._get_registered_employees()[0]._get_reg_id(), self.reg_id)

    def test_remove_register_employee(self):
        self.course._register_employee(self.employee)
        self.assertEqual(len(self.course._get_registered_employees()), 1)
        self.course._remove_register_employee(self.reg_id)
        self.assertEqual(len(self.course._get_registered_employees()), 0)

    def test_match_course(self):
        course1 = Course("JAVA", "JAMES", "15062022", 1, 2)
        course2 = Course("PYTHON", "LILY", "15072022", 1, 2)
        self.assertTrue(self.course._match_course(course1))
        self.assertFalse(self.course._match_course(course2))
