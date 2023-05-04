import unittest
from unittest.mock import MagicMock
from src.main.constants import constant
from src.main.model.Course import Course
from src.main.model.Employee import Employee
from src.main.controller.implementation.CancelCourseCmdExecutor import CancelCourseCmdExecutor
from unittest.mock import patch
from io import StringIO

class TestCancelCourseCmdExecutor(unittest.TestCase):

    def setUp(self):
        self.executor = CancelCourseCmdExecutor()
        self.course = Course("JAVA", "JAMES", "15062022", 1, 2)
        self.emp = Employee("WOO@GMAIL.COM")
        self.course._set_course_status(constant.COURSE_CANCELED)
        self.course._set_course_id("OFFERING-JAVA-JAMES")
        self.coursesDet = {
            'OFFERING-JAVA-JAMES': self.course
        }
        self.reg_id = self.course._register_employee(self.emp)

        self.regIDvsCourse = {'REG-COURSE-WOO-JAVA': self.course}

    def test_cancel_course_successfully(self):
        # Ensure that the course is cancelled and the registered employee is removed
        command_attributes = [self.reg_id]
        self.executor.executeCommand(self.coursesDet, self.regIDvsCourse, command_attributes)
        self.assertEqual(self.course._get_course_status(), constant.COURSE_CANCELED)
        all_reg_ids = [el[1] for el in self.course._get_registered_employees()]
        self.assertNotIn(self.reg_id, all_reg_ids)
        self.assertNotIn(self.reg_id, self.regIDvsCourse.keys())

    def test_cancel_course_failure_course_allocated(self):
        # Ensure that the course is not cancelled if it is already allocated
        self.course._set_course_status(constant.ALLOCATED)
        command_attributes = [self.reg_id]
        self.executor.executeCommand(self.coursesDet, self.regIDvsCourse, command_attributes)
        self.assertEqual(self.course._get_course_status(), constant.ALLOCATED)
        all_reg_ids = [el._get_reg_id() for el in self.course._get_registered_employees()]
        self.assertIn(self.reg_id, all_reg_ids)
        self.assertIn(self.reg_id, self.regIDvsCourse.keys())

    @patch('sys.stdout', new_callable=StringIO)
    def test_cancel_course_rejected_as_course_not_found(self, mock_stdout):
        # Ensure that an error message is returned if the course is not found
        command_attributes = ["12345"]
        self.executor.executeCommand(self.coursesDet, self.regIDvsCourse, command_attributes)
        expected_output = "12345 CANCEL_REJECTED\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)


