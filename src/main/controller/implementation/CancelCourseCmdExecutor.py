import zope.interface

from src.main.model.Course import Course
from src.main.model.Employee import Employee
from src.main.constants import constant
from ..interface.CommandExecutorItf import CommandExecutorItf

@zope.interface.implementer(CommandExecutorItf)
class CancelCourseCmdExecutor:
    def executeCommand(self, coursesDet, regIDvsCourse, command_attributes)->str: # return error message if any
        regId = command_attributes[0]
        course = regIDvsCourse.get(regId,None)
        if (course!=None):
            if (course._get_course_status()==constant.ALLOCATED):
                print(f"{regId} {constant.CANCEL_REJECTED}")
            else:
                self.__removeRegisteredEmployee(regId, regIDvsCourse)
                print(f"{regId} {constant.CANCEL_ACCEPTED}")
        else:
            print(f"{regId} {constant.CANCEL_REJECTED}")


    def __removeRegisteredEmployee(self, regId, regIDvsCourse):
        course = regIDvsCourse.get(regId)
        course._remove_register_employee(regId)
        del regIDvsCourse[regId]


