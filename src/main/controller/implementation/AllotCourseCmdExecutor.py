import zope.interface
from ..interface.CommandExecutorItf import CommandExecutorItf
from src.main.constants import constant
@zope.interface.implementer(CommandExecutorItf)
class AllotCourseCmdExecutor:
    def executeCommand(self, coursesDet, regIDvsCourse, command_attributes)->str: # return error message if any
        courseID = command_attributes[0]
        course = coursesDet.get(courseID, None)
        if (course!=None):
            numOfRegisteredEmployees = len(course._get_registered_employees())
            if (numOfRegisteredEmployees<int(course._get_min_employees())):
                course._set_course_status(constant.COURSE_CANCELED)
                self.__get_allot_status(course)
            else:
                course._set_course_status(constant.ALLOCATED)
                self.__get_allot_status(course)
        else:
            print(f"{constant.INPUT_DATA_ERROR}") 

    def __get_allot_status(self, course):
        status = None
        if (course._get_course_status()==constant.COURSE_CANCELED):
            status = constant.COURSE_CANCELED
        else:
            status = constant.CONFIRMED
        # find employees registered for this course
        for regEmp in course._get_registered_employees():
            emp = regEmp._get_employee()
            reg_id = regEmp._get_reg_id()
            print(f"{reg_id} {emp._get_email()} {course._get_course_id()} {course._get_course_title()} {course._get_instructor()} {course._get_date()} {status}")
