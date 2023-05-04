import zope.interface

from src.main.model.Employee import Employee
from src.main.constants import constant
from ..interface.CommandExecutorItf import CommandExecutorItf

@zope.interface.implementer(CommandExecutorItf)
class RegisterCourseCmdExecutor:
    def executeCommand(self, coursesDet, regIDvsCourse, command_attributes): # return error message if any
        try:
            courseId = command_attributes[1]
            employee = Employee(command_attributes[0])
            if (employee._get_name()==""):
                print(f"{constant.INPUT_DATA_ERROR}") 
                return

            if (coursesDet.get(courseId,False)):
                course = coursesDet.get(courseId)
                if (not (course._get_course_status() == constant.ALLOCATED) or (course._get_course_status()==constant.CANCELLED)): # 1: allocated, 2: cancelled
                    if (len(course._get_registered_employees())==int(course._get_max_employees())):
                        print(f"{constant.COURSE_FULL_ERROR}")
                    else:
                        course._set_course_status(constant.ACCEPTED)
                        self.__register_employee(employee, course, regIDvsCourse)
                else:
                    print(f"REG-COURSE-{employee._get_name()}-{course._get_course_title()} {constant.REJECTED}")

            else:   
                print(f"{constant.INPUT_DATA_ERROR}") 
                # raise SystemExit(constant.INPUT_DATA_ERROR)
        except Exception as e: 
            print(f"{constant.INPUT_DATA_ERROR}") 
            # raise SystemExit(constant.INPUT_DATA_ERROR)
    
    def __register_employee(self, employee, course, regIDvsCourse):
        regId = course._register_employee(employee)
        regIDvsCourse[regId] = course
        print(f"{regId} {course._get_course_status()}")

