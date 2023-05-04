import zope.interface

from src.main.model.Course import Course

from ..interface.CommandExecutorItf import CommandExecutorItf
from src.main.constants import constant
@zope.interface.implementer(CommandExecutorItf)
class AddCourseCmdExecutor:

    def executeCommand(self, coursesDet, regIDvsCourse, command_attributes)->Course: 
        course = self.__add_course_offering(command_attributes) 
        if (course==None):
            # SystemExit(constant.INPUT_DATA_ERROR)
            print(f"{constant.INPUT_DATA_ERROR}") 
            return None
        self.__course_offering(coursesDet, course) 
        return course

    def __add_course_offering(self, commandAttribs):
        try: # we already handled the input parameters size error in the command extractor so it won't fail
            course_title = commandAttribs[0]
            instructor = commandAttribs[1]
            date = commandAttribs[2]
            min_employees = commandAttribs[3]
            max_employees = commandAttribs[4]
            offering = Course(course_title, instructor, date, min_employees, max_employees)
            offering._set_course_id("OFFERING-"+course_title+"-"+instructor)
            return offering
        except:
            return None
        
    def __course_offering(self, coursesDet , course):
        coursesDet[course._get_course_id()] = course
        print(course._get_course_id())
        
